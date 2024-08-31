# publaynet - 5000
这里是一个识别论文PDF结构与结构类型的项目，可识别类别包括文本，标题，列表，表格，图像。
## 训练方法
采用yolov9c模型在kaggle平台上进行训练。
## 所用数据集
所用为pulaynet数据集，可见https://github.com/ibm-aur-nlp/publaynet  
完整数据集下载可到https://developer.ibm.com/exchanges/data/all/publaynet/  
本项目随机选取了其中5000个文件进行训练以及验证，其中4000用作训练，1000个用作验证。
## 训练结果
| **Class** | **Images** | **Instances** | **Box(P** | **R** | **mAP50** | **mAP50-95)** |
|-----------|------------|---------------|-----------|-------|-----------|---------------|
| all       | 1000       | 9775          | 0.961     | 0.939 | 0.972     | 0.906         |
| text      | 1000       | 7008          | 0.963     | 0.941 | 0.982     | 0.935         |
| title     | 1000       | 1918          | 0.959     | 0.952 | 0.975     | 0.792         |
| list      | 1000       | 245           | 0.933     | 0.853 | 0.932     | 0.892         |
| table     | 1000       | 282           | 0.98      | 0.972 | 0.989     | 0.959         |
| figure    | 1000       | 322           | 0.972     | 0.978 | 0.98      | 0.949         |
## 模型预测
**模型位置：./output/runs/detect/train/weights/best.pt**

可以使用以下命令依靠上述的best.pt文件进行模型识别：
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
