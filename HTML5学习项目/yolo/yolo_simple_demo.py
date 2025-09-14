#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化的YOLO演示脚本
解决PyTorch兼容性问题
"""

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

# 设置环境变量解决PyTorch兼容性问题
os.environ['TORCH_LOAD_WEIGHTS_ONLY'] = 'False'

def load_yolo_model():
    """加载YOLO模型"""
    print("📥 加载YOLOv8n模型...")
    
    # 检查模型文件
    model_path = 'yolov8n.pt'
    if not os.path.exists(model_path):
        print("❌ 模型文件不存在，请先运行 download_model_manual.py")
        return None
    
    file_size = os.path.getsize(model_path) / (1024 * 1024)
    print(f"✅ 找到模型文件: {model_path} ({file_size:.1f} MB)")
    
    try:
        from ultralytics import YOLO
        model = YOLO(model_path)
        print("✅ 模型加载成功！")
        return model
    except Exception as e:
        print(f"❌ 模型加载失败: {e}")
        return None

def create_test_image():
    """创建测试图像"""
    print("🎨 创建测试图像...")
    
    # 创建白色背景
    img = np.ones((480, 640, 3), dtype=np.uint8) * 255
    
    # 绘制多个形状
    # 矩形
    cv2.rectangle(img, (50, 200), (200, 350), (0, 0, 255), -1)
    cv2.rectangle(img, (60, 210), (190, 340), (255, 255, 255), -1)
    
    # 圆形
    cv2.circle(img, (400, 150), 60, (0, 255, 0), -1)
    cv2.circle(img, (400, 150), 40, (255, 255, 255), -1)
    
    # 椭圆
    cv2.ellipse(img, (500, 350), (100, 50), 0, 0, 360, (255, 0, 0), -1)
    cv2.ellipse(img, (500, 350), (80, 40), 0, 0, 360, (255, 255, 255), -1)
    
    # 添加文字
    cv2.putText(img, 'YOLO Test Image', (150, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2)
    
    return img

def run_detection(model):
    """运行目标检测"""
    print("🔍 开始目标检测...")
    
    # 创建测试图像
    test_image = create_test_image()
    test_path = 'test_image.jpg'
    cv2.imwrite(test_path, test_image)
    print(f"💾 测试图像已保存: {test_path}")
    
    try:
        # 进行检测
        start_time = time.time()
        results = model(test_path)
        detection_time = time.time() - start_time
        
        print(f"⏱️  检测耗时: {detection_time:.2f} 秒")
        
        # 分析结果
        for r in results:
            boxes = r.boxes
            if boxes is not None and len(boxes) > 0:
                print(f"📊 检测到 {len(boxes)} 个目标:")
                for i, box in enumerate(boxes):
                    conf = box.conf[0].cpu().numpy()
                    cls = int(box.cls[0].cpu().numpy())
                    class_name = model.names[cls]
                    print(f"   {i+1}. {class_name} (置信度: {conf:.3f})")
            else:
                print("📊 未检测到目标")
        
        # 保存结果
        annotated = results[0].plot()
        result_path = 'detection_result.jpg'
        cv2.imwrite(result_path, annotated)
        print(f"🖼️  结果图像已保存: {result_path}")
        
        # 创建对比图
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB))
        plt.title('原始图像')
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.imshow(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))
        plt.title('检测结果')
        plt.axis('off')
        
        plt.tight_layout()
        plt.savefig('comparison.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("📈 对比图已保存: comparison.png")
        
        return True
        
    except Exception as e:
        print(f"❌ 检测失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("🎯 YOLO简化演示")
    print("=" * 50)
    
    # 加载模型
    model = load_yolo_model()
    if model is None:
        return False
    
    # 显示模型信息
    print(f"\n📋 模型信息:")
    print(f"   支持类别数: {len(model.names)}")
    print(f"   主要类别: person, car, truck, bus, bicycle, motorcycle")
    
    # 运行检测
    success = run_detection(model)
    
    if success:
        print("\n🎉 YOLO演示完成！")
        print("📁 生成的文件:")
        files = ['test_image.jpg', 'detection_result.jpg', 'comparison.png']
        for file in files:
            if os.path.exists(file):
                size = os.path.getsize(file) / 1024
                print(f"   ✅ {file} ({size:.1f} KB)")
    else:
        print("\n❌ 演示失败")
    
    return success

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 程序被中断")
    except Exception as e:
        print(f"\n❌ 程序出错: {e}")
