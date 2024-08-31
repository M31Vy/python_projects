# RAG - Knowledge Graph Index
这里是一个对文本段通过知识图谱(KG)进行检索增强生成(RAG)的项目，支持多个文本文件参与检索生成。
## 采用方案
采用的是LlamaIndex里的Knowledge Graph Index方法借助Openai的大模型生成知识图谱并进行检索，再通过Streamlit编写的网页呈现出来。
## 使用方法
安装好LlamaIndex和Streamlit库，然后用streamlit run main.py运行chat文件夹里的main.py文件，在左侧侧边栏中选择RAG，将出现如下界面：
![rag](https://github.com/user-attachments/assets/e23cfd2a-cc23-46ba-a3ed-d6f1e9f5460e)
其中红色框为文件上传功能，上传的文件应为TXT文本文件，支持上传多个文本文件。  
蓝色框为加载文件，上传完所有文件后再点击这个按钮，程序将对上传的文件进行知识图谱(KG)的生成，这会花费一段时间，生成结束后将在右侧主页面出现如图的“查看图结构”按钮，可以点开查看生成的知识图谱，图可以通过鼠标滑轮放大及缩小。  
生成图结构后便可通过下方的对话框进行询问与对话了。  
紫色框里则是删除文件功能，不再需要这些上传的文件以及生成的知识图谱时便可通过这个按钮对它们进行清空，此时便可重新上传文件。
## 使用示例
![image](https://github.com/user-attachments/assets/84560788-b036-4e90-b189-04f6a7d6da52)
点击下方的“查看详细信息”还可以查看生成这个答案的相关的metadata以及nodes
![image](https://github.com/user-attachments/assets/d83b0e88-d1e6-471e-a612-af33a7afad5b)
