import os
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

from llama_index.core import SimpleDirectoryReader, KnowledgeGraphIndex
from llama_index.core.graph_stores import SimpleGraphStore
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
from llama_index.core import StorageContext

from pyvis.network import Network
import networkx as nx

import streamlit as st
from streamlit.components import v1 as components
import uuid

api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key
else:
    print("Please set the OPENAI_API_KEY environment variable.")



col1, col2 = st.sidebar.columns(2)

buttongraph = col1.button("加载文件", key="graph_create")
buttonClean = col2.button("删除文件", key="delete")

if "upload_key" not in st.session_state:
    st.session_state.upload_key = str(uuid.uuid4())

# 导入.txt文件
uploaded_files = st.sidebar.file_uploader("Choose a TXT files", type=["txt"], 
                                          accept_multiple_files=True, key=st.session_state.upload_key)

if buttonClean:
    for file in os.listdir("data"):
        os.remove(os.path.join("data", file))
    st.session_state.upload_key = str(uuid.uuid4())  # 创建一个新的文件上传器
    st.rerun()  # 立即刷新 Streamlit 应用



@st.cache_data
def initialize():
    llm = OpenAI(temperature=0, model="gpt-4o-mini")
    chunk_size = 512

    graph_store = SimpleGraphStore()
    storage_context = StorageContext.from_defaults(graph_store=graph_store)
    return llm, chunk_size, storage_context

@st.cache_data
def graph(html_graph):
    with st.expander("查看图结构"):
        # 在 Streamlit 页面上显示 HTML
        components.html(html_graph, width=800, height=600, scrolling=True)

@st.cache_data
def load(uploaded_files):
    global Settings
    with st.sidebar:
        message = st.empty()  # 在侧边栏创建一个空的插槽
    if uploaded_files:        
        for uploaded_file in uploaded_files:
            if uploaded_file is not None:
                temp_file = os.path.join("./data", uploaded_file.name)
                # 将上传的文件保存到临时文件中
                with open(temp_file, "wb") as f:
                    f.write(uploaded_file.getvalue())

        uploaded_file_names = [uploaded_file.name for uploaded_file in uploaded_files if uploaded_file is not None]
        # 获取 data 文件夹中的所有文件名
        data_file_names = os.listdir("./data")
        # 找出只在 data 文件夹中存在的文件
        extra_files = set(data_file_names) - set(uploaded_file_names)
        # 删除这些文件
        for file_name in extra_files:
            os.remove(os.path.join("./data", file_name))

        Settings.llm, Settings.chunk_size, storage_context = initialize()

        # 使用 SimpleDirectoryReader 加载临时文件
        documents = SimpleDirectoryReader("data").load_data()

        # NOTE: can take a while!
        index = KnowledgeGraphIndex.from_documents(
            documents,
            max_triplets_per_chunk=2,
            storage_context=storage_context,
            include_embeddings=True,
        )

        query_engine = index.as_query_engine(
            include_text=True,
            response_mode="tree_summarize",
            embedding_mode="hybrid",
            similarity_top_k=5,
        )

        g = index.get_networkx_graph()
        net = Network(notebook=False, cdn_resources="in_line", directed=True)
        net.from_nx(g)
        html_graph = net.generate_html().encode('utf-8')

        graph(html_graph)

        return query_engine

    else:
        message.text("Please upload files first.")

if buttongraph:
    load(uploaded_files)



# 这里的对话框源代码(streamlit/lib/)streamlit/elements/widgets/chat.py第355行：
# position = "inline" -> position = "bottom"
prompt_text = st.chat_input("请输入您的问题")

if prompt_text:
    query_engine = load(uploaded_files)

    with st.chat_message(name="user", avatar="user"):
        st.write(prompt_text)

    with st.chat_message(name="assistant", avatar="assistant"):
        with st.spinner("Thinking..."):
            response = query_engine.query(prompt_text)
            st.write(response.response)
            with st.expander("查看详细信息"):
                st.write("metadata")
                st.json(response.metadata,expanded=False)
                st.write("source_nodes")
                st.json(response.source_nodes,expanded=False)