# fruit
这里是一个识别水果种类的项目，可识别类别包括苹果、香蕉、橘子。  
## 训练方法
采用yolov9c模型在kaggle平台上进行训练。
## 所用数据集
所使用数据集为：https://www.kaggle.com/datasets/mbkinaci/fruit-images-for-object-detection
数据量为240个图像。
## 训练结果
| **Class** | **Images** | **Instances** | **Box(P** | **R** | **mAP50** | **mAP50-95)** |
|-----------|------------|---------------|-----------|-------|-----------|---------------|
| all    | 239    | 464       | 0.925 | 0.927 | 0.97  | 0.766     |
| apple  | 239    | 155       | 0.893 | 0.973 | 0.981 | 0.818     |
| banana | 239    | 169       | 0.939 | 0.814 | 0.934 | 0.651     |
| orange | 239    | 140       | 0.944 | 0.993 | 0.994 | 0.829     |
## 模型预测
可以使用以下命令依靠best.pt文件进行模型识别：
```
yolo predict model='.pt文件位置' source='需要识别的图片位置'
```
也可以用以下代码进行识别并获取数据形式的识别结果：
```
from ultralytics import YOLO
model = YOLO('.pt文件位置')
results = model('需要识别的图片位置')
```
## 识别结果示例
![2024 8 23](https://github.com/user-attachments/assets/7bbe26bc-d203-4a50-a513-6077177dcb47)
