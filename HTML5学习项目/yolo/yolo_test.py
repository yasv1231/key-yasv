#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YOLO目标检测测试脚本
使用Ultralytics YOLOv8进行目标检测
"""

import cv2
import numpy as np
from ultralytics import YOLO
import matplotlib.pyplot as plt
from PIL import Image
import os

def test_yolo_detection():
    """测试YOLO目标检测功能"""
    print("🚀 开始YOLO目标检测测试...")
    
    try:
        # 加载预训练的YOLOv8模型
        print("📥 加载YOLOv8模型...")
        try:
            model = YOLO('yolov8n.pt')  # 使用nano版本，速度最快
        except Exception as e:
            print(f"⚠️  模型下载失败: {e}")
            print("🔄 尝试使用在线模型...")
            model = YOLO('yolov8n.pt', verbose=False)
        
        # 创建一个测试图像（包含一些基本形状来模拟目标）
        print("🎨 创建测试图像...")
        test_image = create_test_image()
        
        # 保存测试图像
        test_image_path = 'test_image.jpg'
        cv2.imwrite(test_image_path, test_image)
        print(f"💾 测试图像已保存: {test_image_path}")
        
        # 进行目标检测
        print("🔍 开始目标检测...")
        results = model(test_image_path)
        
        # 显示检测结果
        print("📊 检测结果:")
        for r in results:
            boxes = r.boxes
            if boxes is not None:
                print(f"   检测到 {len(boxes)} 个目标")
                for i, box in enumerate(boxes):
                    # 获取边界框坐标
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                    # 获取置信度
                    conf = box.conf[0].cpu().numpy()
                    # 获取类别ID
                    cls = int(box.cls[0].cpu().numpy())
                    # 获取类别名称
                    class_name = model.names[cls]
                    
                    print(f"   目标 {i+1}: {class_name} (置信度: {conf:.2f})")
                    print(f"     位置: ({x1:.0f}, {y1:.0f}) 到 ({x2:.0f}, {y2:.0f})")
            else:
                print("   未检测到任何目标")
        
        # 保存带标注的结果图像
        annotated_image = results[0].plot()
        result_path = 'yolo_detection_result.jpg'
        cv2.imwrite(result_path, annotated_image)
        print(f"🖼️  检测结果图像已保存: {result_path}")
        
        # 显示图像（如果在支持的环境中）
        try:
            plt.figure(figsize=(12, 6))
            
            # 原始图像
            plt.subplot(1, 2, 1)
            plt.imshow(cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB))
            plt.title('原始测试图像')
            plt.axis('off')
            
            # 检测结果
            plt.subplot(1, 2, 2)
            plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
            plt.title('YOLO检测结果')
            plt.axis('off')
            
            plt.tight_layout()
            plt.savefig('yolo_comparison.png', dpi=150, bbox_inches='tight')
            print("📈 对比图已保存: yolo_comparison.png")
            
        except Exception as e:
            print(f"⚠️  无法显示图像: {e}")
        
        print("✅ YOLO测试完成！")
        return True
        
    except Exception as e:
        print(f"❌ YOLO测试失败: {e}")
        return False

def create_test_image():
    """创建一个包含基本形状的测试图像"""
    # 创建白色背景
    img = np.ones((480, 640, 3), dtype=np.uint8) * 255
    
    # 绘制一些基本形状来模拟目标
    # 矩形（模拟汽车）
    cv2.rectangle(img, (100, 200), (200, 300), (0, 0, 255), -1)
    
    # 圆形（模拟人）
    cv2.circle(img, (400, 150), 50, (0, 255, 0), -1)
    
    # 椭圆（模拟其他物体）
    cv2.ellipse(img, (500, 350), (80, 40), 0, 0, 360, (255, 0, 0), -1)
    
    # 添加一些文字
    cv2.putText(img, 'YOLO Test Image', (200, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    
    return img

def test_webcam_detection():
    """测试实时摄像头检测（可选）"""
    print("\n🎥 测试实时摄像头检测...")
    print("按 'q' 键退出摄像头检测")
    
    try:
        # 加载模型
        model = YOLO('yolov8n.pt')
        
        # 打开摄像头
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ 无法打开摄像头")
            return False
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # 进行检测
            results = model(frame)
            
            # 绘制结果
            annotated_frame = results[0].plot()
            
            # 显示结果
            cv2.imshow('YOLO Real-time Detection', annotated_frame)
            
            # 按 'q' 退出
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
        print("✅ 摄像头检测测试完成")
        return True
        
    except Exception as e:
        print(f"❌ 摄像头检测失败: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("🎯 YOLO目标检测测试程序")
    print("=" * 50)
    
    # 基本检测测试
    success = test_yolo_detection()
    
    if success:
        print("\n" + "=" * 50)
        print("🎉 所有测试完成！")
        print("生成的文件:")
        print("  - test_image.jpg (测试图像)")
        print("  - yolo_detection_result.jpg (检测结果)")
        print("  - yolo_comparison.png (对比图)")
        print("=" * 50)
        
        # 询问是否进行摄像头测试
        try:
            choice = input("\n是否进行实时摄像头检测测试？(y/n): ").lower()
            if choice == 'y':
                test_webcam_detection()
        except KeyboardInterrupt:
            print("\n👋 程序已退出")
    else:
        print("\n❌ 测试失败，请检查依赖安装")
