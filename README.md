# publaynet - 5000
这里是一个识别论文PDF结构与结构类型的项目，可识别类别包括文本，标题，列表，表格，图像。
## 训练方法
采用yolov9c模型在kaggle平台上进行训练。
## 所用数据集
所用为pulaynet数据集，可见https://github.com/ibm-aur-nlp/publaynet  
完整数据集下载可到https://developer.ibm.com/exchanges/data/all/publaynet/  
本项目随机选取了其中5000个文件进行训练以及验证。
## 模型预测
可以使用以下命令依靠项目中的best.pt文件进行模型识别：
```
yolo predict model='.pt文件位置' source='需要识别的论文图片位置'
```
也可以用以下代码进行识别并获取数据形式的识别结果：
```
from ultralytics import YOLO
model = YOLO('.pt文件位置')
results = model('需要识别的论文图片位置')
```
## 识别结果示例
![4](https://github.com/M31Vy/python_projects/assets/61035763/69c01c6f-c9cc-4713-977b-4556231079cd)
