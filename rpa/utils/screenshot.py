from typing import List, Optional, Tuple
import os
from PIL import Image
from loguru import logger
import uiautomator2 as u2
import io

class ScreenshotHelper:
    def __init__(self, device_id: str):
        """
        初始化截图助手
        
        Args:
            device_id: 设备ID
        """
        self.device_id = device_id
        self.logger = logger
        self.scale = 0.5  # 内部缩放比例
        self.quality = 50  # JPEG质量
        # 初始化UIAutomator2连接
        self.ui_device = u2.connect(device_id)

    def take_screenshot(self, 
                       save_path: str,
                       region: Optional[List[int]] = None,
                       filename_prefix: str = "screenshot") -> str:
        """
        获取屏幕截图，支持区域截图
        
        Args:
            save_path: 保存目录
            region: 截图区域 [x1, y1, x2, y2]，None表示全屏
            filename_prefix: 文件名前缀
            
        Returns:
            截图文件的完整路径
        """
        try:
            # 确保保存目录存在
            os.makedirs(save_path, exist_ok=True)
            
            # 生成文件名
            import time
            filename = f"{filename_prefix}.jpg"  # 使用jpg格式
            full_path = os.path.join(save_path, filename)
            
            # 使用UIAutomator2截图
            screenshot_data = self.ui_device.screenshot(format='pillow')
            
            # 如果指定了区域，先裁剪
            if region:
                x1, y1, x2, y2 = region
                screenshot_data = screenshot_data.crop((x1, y1, x2, y2))
            
            # 缩放图片
            original_size = screenshot_data.size
            new_size = tuple(int(dim * self.scale) for dim in original_size)
            screenshot_data = screenshot_data.resize(new_size, Image.Resampling.LANCZOS)
            
            # 转换为灰度图
            screenshot_data = screenshot_data.convert('L')
            
            # 保存为JPEG格式
            screenshot_data.save(full_path, 'JPEG', quality=self.quality, optimize=True)
            
            return full_path
            
        except Exception as e:
            self.logger.error(f"截图失败: {str(e)}")
            raise

    def get_scale_factor(self) -> float:
        """获取当前缩放比例"""
        return self.scale

    def get_real_coordinates(self, x: int, y: int) -> Tuple[int, int]:
        """将缩放后的坐标转换为实际坐标
        
        Args:
            x: 缩放图片上的x坐标
            y: 缩放图片上的y坐标
            
        Returns:
            实际屏幕上的坐标(x, y)
        """
        # 只考虑缩放因子，不考虑区域偏移
        return (int(x / self.scale), int(y / self.scale))