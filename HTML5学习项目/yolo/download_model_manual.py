#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
手动下载YOLOv8n模型的脚本
提供多种下载方式
"""

import os
import requests
import urllib.request
from pathlib import Path

def download_with_requests():
    """使用requests库下载模型"""
    print("🔧 尝试使用requests库下载...")
    
    url = "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt"
    
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open('yolov8n.pt', 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        progress = (downloaded / total_size) * 100
                        print(f"\r📥 下载进度: {progress:.1f}%", end='', flush=True)
        
        print(f"\n✅ 下载完成！文件大小: {downloaded / (1024*1024):.1f} MB")
        return True
        
    except Exception as e:
        print(f"\n❌ requests下载失败: {e}")
        return False

def download_with_urllib():
    """使用urllib下载模型"""
    print("🔧 尝试使用urllib下载...")
    
    url = "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt"
    
    try:
        def show_progress(block_num, block_size, total_size):
            downloaded = block_num * block_size
            if total_size > 0:
                progress = (downloaded / total_size) * 100
                print(f"\r📥 下载进度: {progress:.1f}%", end='', flush=True)
        
        urllib.request.urlretrieve(url, 'yolov8n.pt', show_progress)
        print(f"\n✅ 下载完成！")
        return True
        
    except Exception as e:
        print(f"\n❌ urllib下载失败: {e}")
        return False

def check_model_exists():
    """检查模型文件是否已存在"""
    if os.path.exists('yolov8n.pt'):
        size = os.path.getsize('yolov8n.pt') / (1024 * 1024)
        print(f"✅ 模型文件已存在: yolov8n.pt ({size:.1f} MB)")
        return True
    return False

def provide_manual_download_info():
    """提供手动下载信息"""
    print("\n" + "=" * 60)
    print("📋 手动下载YOLOv8n模型的方法:")
    print("=" * 60)
    
    print("\n🌐 方法1: 浏览器下载")
    print("   1. 打开浏览器访问:")
    print("      https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt")
    print("   2. 下载文件到当前目录")
    print("   3. 确保文件名为: yolov8n.pt")
    
    print("\n🔧 方法2: 使用wget (如果已安装)")
    print("   wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt")
    
    print("\n🔧 方法3: 使用curl (如果已安装)")
    print("   curl -L -o yolov8n.pt https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt")
    
    print("\n📱 方法4: 使用手机热点")
    print("   如果网络连接有问题，可以尝试使用手机热点")
    
    print("\n💡 下载完成后，运行以下命令测试:")
    print("   python yolo_download_test.py")

def main():
    """主函数"""
    print("=" * 60)
    print("📥 YOLOv8n模型下载工具")
    print("=" * 60)
    
    # 检查模型是否已存在
    if check_model_exists():
        print("🎉 模型已存在，可以直接使用！")
        return True
    
    print("🔍 开始尝试下载YOLOv8n模型...")
    
    # 尝试不同的下载方法
    methods = [
        ("requests", download_with_requests),
        ("urllib", download_with_urllib)
    ]
    
    for method_name, method_func in methods:
        print(f"\n🔄 尝试方法: {method_name}")
        if method_func():
            print(f"✅ {method_name}下载成功！")
            return True
        else:
            print(f"❌ {method_name}下载失败")
    
    # 所有自动下载方法都失败，提供手动下载信息
    provide_manual_download_info()
    return False

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 下载被用户中断")
    except Exception as e:
        print(f"\n❌ 程序运行出错: {e}")
