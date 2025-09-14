# YOLO目标检测项目

这是一个基于Ultralytics YOLOv8的目标检测测试项目。

## 🚀 功能特性

- **目标检测**: 使用YOLOv8进行实时目标检测
- **图像处理**: 支持图像和视频的目标检测
- **实时检测**: 支持摄像头实时检测
- **结果可视化**: 自动生成检测结果图像和对比图

## 📋 环境要求

- Python 3.8+
- CUDA支持（可选，用于GPU加速）

## 🛠️ 安装步骤

### 1. 安装Python依赖

```bash
pip install -r requirements.txt
```

### 2. 验证安装

```bash
python yolo_test.py
```

## 📁 项目结构

```
yolo/
├── requirements.txt      # Python依赖包
├── yolo_test.py         # 主测试脚本
└── README.md           # 项目说明文档
```

## 🎯 使用方法

### 基本测试

运行测试脚本进行基本功能测试：

```bash
python yolo_test.py
```

这将：
1. 加载YOLOv8模型
2. 创建测试图像
3. 进行目标检测
4. 生成结果图像

### 实时摄像头检测

在基本测试完成后，程序会询问是否进行实时摄像头检测。

## 📊 输出文件

运行测试后会生成以下文件：

- `test_image.jpg` - 原始测试图像
- `yolo_detection_result.jpg` - 带检测框的结果图像
- `yolo_comparison.png` - 原始图像与检测结果的对比图

## 🔧 自定义使用

### 检测自己的图像

```python
from ultralytics import YOLO

# 加载模型
model = YOLO('yolov8n.pt')

# 检测图像
results = model('your_image.jpg')

# 显示结果
results[0].show()
```

### 检测视频

```python
# 检测视频文件
results = model('your_video.mp4')

# 保存结果
results[0].save('output_video.mp4')
```

## 🎨 支持的模型

- `yolov8n.pt` - Nano版本（最快，精度较低）
- `yolov8s.pt` - Small版本（平衡速度和精度）
- `yolov8m.pt` - Medium版本（较高精度）
- `yolov8l.pt` - Large版本（高精度）
- `yolov8x.pt` - Extra Large版本（最高精度）

## 🐛 常见问题

### 1. 模型下载失败

如果模型下载失败，可以手动下载模型文件到项目目录。

### 2. 摄像头无法打开

确保摄像头没有被其他程序占用，或者检查摄像头权限设置。

### 3. 内存不足

如果遇到内存问题，可以：
- 使用更小的模型（如yolov8n.pt）
- 减小输入图像尺寸
- 使用CPU而不是GPU

## 📚 更多资源

- [Ultralytics官方文档](https://docs.ultralytics.com/)
- [YOLOv8 GitHub仓库](https://github.com/ultralytics/ultralytics)
- [OpenCV文档](https://docs.opencv.org/)

## 📄 许可证

本项目仅供学习和测试使用。
