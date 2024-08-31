import streamlit as st
import torch

from http import HTTPStatus
import dashscope
from dashscope.api_entities.dashscope_response import Role

import requests
import time
import hashlib
import os

# 创建一个下拉选择框
model_choice = st.sidebar.selectbox("选择模型", ["阿里巴巴qwen-max", "天工2.0"], key="model_choice")

max_length = st.sidebar.slider("max_length", 0, 32768, 8192, step=1)
top_p = st.sidebar.slider("top_p", 0.0, 1.0, 0.8, step=0.01)
temperature = st.sidebar.slider("temperature", 0.0, 1.0, 0.6, step=0.01)

# 添加一个按钮
buttonClean = st.sidebar.button("清理历史记录", key="clean")

def clean_session():
    st.session_state.history = []
    st.session_state.past_key_values = None
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    st.rerun()

if buttonClean:
    clean_session()

if "history" not in st.session_state:
    st.session_state.history = []

with st.chat_message("assistant"):
            st.write("Please ask me.")

prompt_text = st.chat_input("请输入您的问题")

if model_choice == "阿里巴巴qwen-max":
    if prompt_text:
        message = st.session_state.history

        for text in message:
            with st.chat_message(text["role"]):
                st.write(text["content"])

        with st.chat_message(name="user", avatar="user"):
            st.write(prompt_text)

        message.append({"role": Role.USER, "content": prompt_text})

        with st.chat_message(name="assistant", avatar="assistant"):
            with st.spinner("Thinking..."):

                dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

                response = dashscope.Generation.call(
                    dashscope.Generation.Models.qwen_max,
                    messages=message,
                    result_format='message',
                )

                placeholder = st.empty()
                all_response = ''
                if response.status_code == HTTPStatus.OK:
                    for item in response.output.choices:
                        all_response += item.message.content
                        placeholder.markdown(all_response)
                    placeholder.markdown(all_response)
                    message.append({"role": response.output.choices[0]['message']['role'],
                                    "content": response.output.choices[0]['message']['content']})
                else:
                    print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                        response.request_id, response.status_code,
                        response.code, response.message
                    ))

        st.session_state.history = message

elif model_choice == "天工2.0":
     if prompt_text:

        with st.chat_message(name="user", avatar="user"):
            st.write(prompt_text)

        url = 'https://sky-api.singularity-ai.com/saas/api/v4/generate'
        app_key = os.getenv('SKY_API_KEY')
        app_secret = os.getenv('SKY_API_SECRET')
        timestamp = str(int(time.time()))
        sign_content = app_key + app_secret + timestamp
        sign_result = hashlib.md5(sign_content.encode('utf-8')).hexdigest()

        headers={
        "app_key": app_key,
        "timestamp": timestamp,
        "sign": sign_result,
        "Content-Type": "application/json",
        "stream": "true"
        }

        data = {
            "messages": [
                {
                    "role": "user",
                    "content": prompt_text
                }
            ],
            "model": "SkyChat-MegaVerse"
        }

        response = requests.post(url, headers=headers, json=data, stream=True)

        # 处理响应流
        for line in response.iter_lines():
            if line:
                # 处理接收到的数据
                print(line.decode('utf-8'))
