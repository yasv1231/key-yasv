#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YOLO模型下载和测试脚本
专门下载yolov8n.pt模型并进行目标检测测试
"""

import cv2
import numpy as np
from ultralytics import YOLO
import matplotlib.pyplot as plt
from PIL import Image
import os
import time

def load_yolo_model():
    """加载YOLOv8n模型"""
    print("📥 加载YOLOv8n模型...")
    
    # 检查模型文件是否存在
    model_path = 'yolov8n.pt'
    if os.path.exists(model_path):
        file_size = os.path.getsize(model_path) / (1024 * 1024)  # MB
        print(f"✅ 找到模型文件: {model_path} ({file_size:.1f} MB)")
    else:
        print("❌ 模型文件不存在，请先运行 download_model_manual.py 下载模型")
        return None
    
    try:
        # 加载模型，设置weights_only=False以兼容PyTorch 2.6+
        import torch
        torch.serialization.add_safe_globals(['ultralytics.nn.tasks.DetectionModel'])
        model = YOLO(model_path)
        print("✅ YOLOv8n模型加载成功！")
        return model
        
    except Exception as e:
        print(f"❌ 模型加载失败: {e}")
        print("🔄 尝试使用兼容模式加载...")
        try:
            # 尝试使用兼容模式
            import torch
            torch.serialization.add_safe_globals([
                'ultralytics.nn.tasks.DetectionModel',
                'ultralytics.nn.modules.conv.Conv',
                'ultralytics.nn.modules.block.C2f',
                'ultralytics.nn.modules.block.SPPF',
                'ultralytics.nn.modules.head.Detect'
            ])
            model = YOLO(model_path)
            print("✅ YOLOv8n模型加载成功！(兼容模式)")
            return model
        except Exception as e2:
            print(f"❌ 兼容模式也失败: {e2}")
            return None

def create_test_image():
    """创建一个包含多种形状的测试图像"""
    print("🎨 创建测试图像...")
    
    # 创建白色背景
    img = np.ones((480, 640, 3), dtype=np.uint8) * 255
    
    # 绘制多个形状来模拟不同的目标
    # 矩形（模拟汽车/卡车）
    cv2.rectangle(img, (50, 200), (200, 350), (0, 0, 255), -1)
    cv2.rectangle(img, (60, 210), (190, 340), (255, 255, 255), -1)
    
    # 圆形（模拟人）
    cv2.circle(img, (400, 150), 60, (0, 255, 0), -1)
    cv2.circle(img, (400, 150), 40, (255, 255, 255), -1)
    
    # 椭圆（模拟其他物体）
    cv2.ellipse(img, (500, 350), (100, 50), 0, 0, 360, (255, 0, 0), -1)
    cv2.ellipse(img, (500, 350), (80, 40), 0, 0, 360, (255, 255, 255), -1)
    
    # 三角形（模拟其他形状）
    pts = np.array([[300, 300], [250, 400], [350, 400]], np.int32)
    cv2.fillPoly(img, [pts], (128, 0, 128))
    
    # 添加文字
    cv2.putText(img, 'YOLO Detection Test', (150, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2)
    cv2.putText(img, 'Multiple Objects', (200, 80), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
    
    return img

def test_yolo_detection_with_model(model):
    """使用下载的模型进行目标检测测试"""
    print("🔍 开始目标检测测试...")
    
    try:
        # 创建测试图像
        test_image = create_test_image()
        
        # 保存测试图像
        test_image_path = 'yolo_test_image.jpg'
        cv2.imwrite(test_image_path, test_image)
        print(f"💾 测试图像已保存: {test_image_path}")
        
        # 进行目标检测
        print("🔍 正在进行目标检测...")
        start_time = time.time()
        results = model(test_image_path)
        detection_time = time.time() - start_time
        
        print(f"⏱️  检测耗时: {detection_time:.2f} 秒")
        
        # 分析检测结果
        print("📊 检测结果分析:")
        for i, r in enumerate(results):
            boxes = r.boxes
            if boxes is not None and len(boxes) > 0:
                print(f"   检测到 {len(boxes)} 个目标:")
                
                for j, box in enumerate(boxes):
                    # 获取边界框坐标
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                    # 获取置信度
                    conf = box.conf[0].cpu().numpy()
                    # 获取类别ID
                    cls = int(box.cls[0].cpu().numpy())
                    # 获取类别名称
                    class_name = model.names[cls]
                    
                    print(f"     目标 {j+1}: {class_name}")
                    print(f"       置信度: {conf:.3f}")
                    print(f"       位置: ({x1:.0f}, {y1:.0f}) -> ({x2:.0f}, {y2:.0f})")
                    print(f"       尺寸: {x2-x1:.0f} x {y2-y1:.0f} 像素")
            else:
                print("   未检测到任何目标")
        
        # 保存带标注的结果图像
        annotated_image = results[0].plot()
        result_path = 'yolo_detection_result.jpg'
        cv2.imwrite(result_path, annotated_image)
        print(f"🖼️  检测结果图像已保存: {result_path}")
        
        # 创建对比图
        create_comparison_image(test_image, annotated_image)
        
        return True
        
    except Exception as e:
        print(f"❌ 目标检测失败: {e}")
        return False

def create_comparison_image(original, annotated):
    """创建原始图像和检测结果的对比图"""
    try:
        plt.figure(figsize=(15, 6))
        
        # 原始图像
        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
        plt.title('原始测试图像', fontsize=14, fontweight='bold')
        plt.axis('off')
        
        # 检测结果
        plt.subplot(1, 2, 2)
        plt.imshow(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))
        plt.title('YOLO检测结果', fontsize=14, fontweight='bold')
        plt.axis('off')
        
        plt.tight_layout()
        plt.savefig('yolo_comparison.png', dpi=150, bbox_inches='tight')
        plt.close()
        
        print("📈 对比图已保存: yolo_comparison.png")
        
    except Exception as e:
        print(f"⚠️  创建对比图失败: {e}")

def test_model_info(model):
    """显示模型信息"""
    print("\n📋 模型信息:")
    print("=" * 40)
    
    try:
        # 获取模型信息
        model_info = model.info()
        print(f"模型类型: YOLOv8n")
        print(f"模型大小: 约 6.2 MB")
        print(f"支持类别数: {len(model.names)}")
        
        print("\n支持的检测类别:")
        for i, name in model.names.items():
            print(f"  {i}: {name}")
        
    except Exception as e:
        print(f"⚠️  获取模型信息失败: {e}")

def main():
    """主函数"""
    print("=" * 60)
    print("🎯 YOLOv8n 模型下载和测试程序")
    print("=" * 60)
    
    # 步骤1: 加载模型
    model = load_yolo_model()
    if model is None:
        print("❌ 模型加载失败，程序退出")
        return False
    
    # 步骤2: 显示模型信息
    test_model_info(model)
    
    # 步骤3: 进行目标检测测试
    success = test_yolo_detection_with_model(model)
    
    if success:
        print("\n" + "=" * 60)
        print("🎉 YOLO测试完成！")
        print("=" * 60)
        print("📁 生成的文件:")
        files = [
            'yolov8n.pt',
            'yolo_test_image.jpg', 
            'yolo_detection_result.jpg',
            'yolo_comparison.png'
        ]
        
        for file in files:
            if os.path.exists(file):
                size = os.path.getsize(file) / 1024  # KB
                print(f"  ✅ {file} ({size:.1f} KB)")
            else:
                print(f"  ❌ {file} (未找到)")
        
        print("\n💡 使用说明:")
        print("  - yolov8n.pt: 下载的YOLO模型文件")
        print("  - yolo_test_image.jpg: 原始测试图像")
        print("  - yolo_detection_result.jpg: 带检测框的结果图像")
        print("  - yolo_comparison.png: 原始图像与检测结果的对比图")
        
        return True
    else:
        print("\n❌ 测试失败")
        return False

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 程序被用户中断")
    except Exception as e:
        print(f"\n❌ 程序运行出错: {e}")
