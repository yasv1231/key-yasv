#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的实时摄像头检测脚本
"""

import cv2
from ultralytics import YOLO
import time

def main():
    print("🎥 启动实时摄像头检测...")
    print("💡 按 'q' 键退出程序")
    
    # 加载模型
    print("📥 加载YOLO模型...")
    model = YOLO('yolov8n.pt')
    print("✅ 模型加载完成")
    
    # 打开摄像头
    print("📹 打开摄像头...")
    cap = cv2.VideoCapture(0)  # 0表示默认摄像头
    
    if not cap.isOpened():
        print("❌ 无法打开摄像头")
        return
    
    print("✅ 摄像头已打开")
    print("🚀 开始实时检测...")
    
    # 用于计算FPS
    start_time = time.time()
    frame_count = 0
    
    while True:
        # 读取摄像头画面
        ret, frame = cap.read()
        if not ret:
            print("❌ 无法读取摄像头画面")
            break
        
        # 进行目标检测
        results = model(frame, verbose=False)
        
        # 绘制检测结果
        annotated_frame = results[0].plot()
        
        # 计算FPS
        frame_count += 1
        if frame_count % 30 == 0:  # 每30帧计算一次FPS
            current_time = time.time()
            fps = frame_count / (current_time - start_time)
            print(f"📊 当前FPS: {fps:.1f}")
        
        # 显示结果
        cv2.imshow('YOLO Real-time Detection', annotated_frame)
        
        # 按'q'键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # 清理资源
    cap.release()
    cv2.destroyAllWindows()
    print("👋 程序结束")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 程序被用户中断")
    except Exception as e:
        print(f"❌ 程序出错: {e}")
