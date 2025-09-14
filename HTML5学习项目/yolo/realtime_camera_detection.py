#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实时摄像头目标检测脚本
使用电脑摄像头进行实时YOLO目标检测
"""

import cv2
import numpy as np
from ultralytics import YOLO
import time
import os

class RealTimeDetector:
    def __init__(self, model_path='yolov8n.pt'):
        """初始化实时检测器"""
        self.model_path = model_path
        self.model = None
        self.cap = None
        self.fps = 0
        self.frame_count = 0
        self.start_time = time.time()
        
    def load_model(self):
        """加载YOLO模型"""
        print("📥 加载YOLO模型...")
        try:
            if not os.path.exists(self.model_path):
                print(f"❌ 模型文件不存在: {self.model_path}")
                return False
            
            self.model = YOLO(self.model_path)
            print("✅ 模型加载成功！")
            return True
        except Exception as e:
            print(f"❌ 模型加载失败: {e}")
            return False
    
    def init_camera(self, camera_index=0):
        """初始化摄像头"""
        print("📹 初始化摄像头...")
        try:
            self.cap = cv2.VideoCapture(camera_index)
            if not self.cap.isOpened():
                print(f"❌ 无法打开摄像头 {camera_index}")
                return False
            
            # 设置摄像头参数
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.cap.set(cv2.CAP_PROP_FPS, 30)
            
            print("✅ 摄像头初始化成功！")
            return True
        except Exception as e:
            print(f"❌ 摄像头初始化失败: {e}")
            return False
    
    def calculate_fps(self):
        """计算FPS"""
        self.frame_count += 1
        current_time = time.time()
        if current_time - self.start_time >= 1.0:  # 每秒更新一次FPS
            self.fps = self.frame_count / (current_time - self.start_time)
            self.frame_count = 0
            self.start_time = current_time
    
    def draw_info(self, frame):
        """在图像上绘制信息"""
        # 绘制FPS
        cv2.putText(frame, f'FPS: {self.fps:.1f}', (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # 绘制说明文字
        cv2.putText(frame, 'Press Q to quit, SPACE to pause', (10, frame.shape[0] - 20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        return frame
    
    def run_detection(self):
        """运行实时检测"""
        print("🚀 开始实时检测...")
        print("💡 操作说明:")
        print("   - 按 'Q' 键退出")
        print("   - 按 'SPACE' 键暂停/继续")
        print("   - 按 'S' 键保存当前帧")
        print("   - 按 'R' 键重置FPS计数")
        
        paused = False
        saved_count = 0
        
        while True:
            if not paused:
                ret, frame = self.cap.read()
                if not ret:
                    print("❌ 无法读取摄像头画面")
                    break
                
                # 进行目标检测
                results = self.model(frame, verbose=False)
                
                # 绘制检测结果
                annotated_frame = results[0].plot()
                
                # 计算并显示FPS
                self.calculate_fps()
                
                # 绘制信息
                annotated_frame = self.draw_info(annotated_frame)
                
                # 显示结果
                cv2.imshow('YOLO Real-time Detection', annotated_frame)
            
            # 处理按键
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('q') or key == ord('Q'):
                print("👋 用户退出")
                break
            elif key == ord(' '):  # 空格键暂停/继续
                paused = not paused
                status = "暂停" if paused else "继续"
                print(f"⏸️  检测{status}")
            elif key == ord('s') or key == ord('S'):  # 保存当前帧
                if not paused:
                    saved_count += 1
                    filename = f'captured_frame_{saved_count}.jpg'
                    cv2.imwrite(filename, annotated_frame)
                    print(f"💾 已保存: {filename}")
            elif key == ord('r') or key == ord('R'):  # 重置FPS
                self.fps = 0
                self.frame_count = 0
                self.start_time = time.time()
                print("🔄 FPS计数已重置")
    
    def cleanup(self):
        """清理资源"""
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
        print("🧹 资源清理完成")

def test_camera_availability():
    """测试摄像头可用性"""
    print("🔍 检测可用摄像头...")
    available_cameras = []
    
    for i in range(5):  # 检查前5个摄像头索引
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                available_cameras.append(i)
                print(f"✅ 摄像头 {i}: 可用")
            cap.release()
        else:
            print(f"❌ 摄像头 {i}: 不可用")
    
    return available_cameras

def main():
    """主函数"""
    print("=" * 60)
    print("🎥 YOLO实时摄像头目标检测")
    print("=" * 60)
    
    # 检测可用摄像头
    cameras = test_camera_availability()
    if not cameras:
        print("❌ 没有找到可用的摄像头")
        return False
    
    # 创建检测器
    detector = RealTimeDetector()
    
    # 加载模型
    if not detector.load_model():
        return False
    
    # 初始化摄像头（使用第一个可用的摄像头）
    camera_index = cameras[0]
    if len(cameras) > 1:
        print(f"📹 找到多个摄像头，使用摄像头 {camera_index}")
    
    if not detector.init_camera(camera_index):
        return False
    
    try:
        # 运行检测
        detector.run_detection()
    except KeyboardInterrupt:
        print("\n👋 程序被用户中断")
    except Exception as e:
        print(f"❌ 程序运行出错: {e}")
    finally:
        # 清理资源
        detector.cleanup()
    
    return True

if __name__ == "__main__":
    main()
