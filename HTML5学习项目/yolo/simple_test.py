#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化的YOLO测试脚本
测试基本功能而不需要下载模型
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

def test_opencv():
    """测试OpenCV基本功能"""
    print("🔧 测试OpenCV基本功能...")
    
    try:
        # 创建一个测试图像
        img = np.ones((300, 400, 3), dtype=np.uint8) * 255
        
        # 绘制一些形状
        cv2.rectangle(img, (50, 50), (150, 150), (0, 0, 255), -1)
        cv2.circle(img, (300, 100), 50, (0, 255, 0), -1)
        cv2.putText(img, 'OpenCV Test', (100, 250), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        
        # 保存图像
        cv2.imwrite('opencv_test.jpg', img)
        print("✅ OpenCV测试成功！图像已保存为 opencv_test.jpg")
        
        # 显示图像信息
        print(f"📊 图像尺寸: {img.shape}")
        print(f"📊 图像类型: {img.dtype}")
        
        return True
        
    except Exception as e:
        print(f"❌ OpenCV测试失败: {e}")
        return False

def test_ultralytics_import():
    """测试Ultralytics导入"""
    print("🔧 测试Ultralytics导入...")
    
    try:
        from ultralytics import YOLO
        print("✅ Ultralytics导入成功！")
        
        # 测试YOLO类
        print("🔧 测试YOLO类...")
        # 不实际加载模型，只测试类是否可用
        print("✅ YOLO类可用！")
        
        return True
        
    except Exception as e:
        print(f"❌ Ultralytics测试失败: {e}")
        return False

def test_matplotlib():
    """测试Matplotlib功能"""
    print("🔧 测试Matplotlib功能...")
    
    try:
        # 创建测试数据
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        
        # 创建图表
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Matplotlib Test')
        plt.legend()
        plt.grid(True)
        
        # 保存图表
        plt.savefig('matplotlib_test.png', dpi=150, bbox_inches='tight')
        plt.close()
        
        print("✅ Matplotlib测试成功！图表已保存为 matplotlib_test.png")
        return True
        
    except Exception as e:
        print(f"❌ Matplotlib测试失败: {e}")
        return False

def test_pil():
    """测试PIL功能"""
    print("🔧 测试PIL功能...")
    
    try:
        # 创建测试图像
        img = Image.new('RGB', (200, 200), color='red')
        
        # 保存图像
        img.save('pil_test.jpg')
        
        # 读取图像信息
        img_info = {
            'size': img.size,
            'mode': img.mode,
            'format': img.format
        }
        
        print("✅ PIL测试成功！图像已保存为 pil_test.jpg")
        print(f"📊 图像信息: {img_info}")
        
        return True
        
    except Exception as e:
        print(f"❌ PIL测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("=" * 50)
    print("🧪 YOLO环境基础测试")
    print("=" * 50)
    
    tests = [
        ("OpenCV", test_opencv),
        ("Ultralytics", test_ultralytics_import),
        ("Matplotlib", test_matplotlib),
        ("PIL", test_pil)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        print(f"\n🔍 运行 {test_name} 测试...")
        results[test_name] = test_func()
    
    print("\n" + "=" * 50)
    print("📊 测试结果汇总:")
    print("=" * 50)
    
    for test_name, result in results.items():
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{test_name}: {status}")
    
    all_passed = all(results.values())
    
    if all_passed:
        print("\n🎉 所有基础测试通过！")
        print("💡 现在可以尝试运行完整的YOLO测试")
        print("💡 运行命令: python yolo_test.py")
    else:
        print("\n⚠️  部分测试失败，请检查依赖安装")
    
    print("\n📁 生成的文件:")
    test_files = ['opencv_test.jpg', 'matplotlib_test.png', 'pil_test.jpg']
    for file in test_files:
        if os.path.exists(file):
            print(f"  - {file}")
    
    return all_passed

if __name__ == "__main__":
    main()
