from typing import Dict, Any, List
from .base_action import BaseAction
import json
import yaml
from pathlib import Path

class AppendToListAction(BaseAction):
    """向列表添加数据"""
    
    def execute(self, params: Dict[str, Any]) -> bool:
        list_name = params['list']
        data = params['data']
        
        try:
            # 获取当前列表
            current_list = self.bot.get_variable(list_name)
            if not isinstance(current_list, list):
                current_list = []
            
            # 解析数据中的变量引用
            resolved_data = {}
            for key, value in data.items():
                if isinstance(value, str) and "${" in value:
                    resolved_data[key] = self.bot._resolve_variable(value)
                else:
                    resolved_data[key] = value
            
            # 添加数据
            current_list.append(resolved_data)
            
            # 更新变量
            self.bot.set_variable(list_name, current_list)
            
            self.logger.info(f"向列表 {list_name} 添加数据: {resolved_data}")
            return True
            
        except Exception as e:
            self.logger.error(f"添加数据失败: {str(e)}")
            return False

class ExportDataAction(BaseAction):
    """导出数据到文件"""
    
    def execute(self, params: Dict[str, Any]) -> bool:
        data = self.bot.get_variable(params['data'])
        format_type = params.get('format', 'json')
        filename = params['filename']
        
        try:
            # 确保输出目录存在
            output_path = Path(filename)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 根据格式类型导出数据
            if format_type == 'json':
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                    
            elif format_type == 'yaml':
                with open(output_path, 'w', encoding='utf-8') as f:
                    yaml.dump(data, f, allow_unicode=True)
                    
            elif format_type == 'csv':
                import csv
                if not isinstance(data, list):
                    raise ValueError("CSV格式只支持列表数据")
                    
                # 获取所有可能的字段
                fields = set()
                for item in data:
                    if isinstance(item, dict):
                        fields.update(item.keys())
                fields = sorted(list(fields))
                
                with open(output_path, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(data)
                    
            else:
                raise ValueError(f"不支持的导出格式: {format_type}")
                
            self.logger.info(f"已导出 {len(data) if isinstance(data, list) else 1} 条记录到: {filename}")
            
            # 如果是调试模式,同时保存一份到调试目录
            if self.bot.debug:
                debug_path = self.bot.debug_dir / f"{self.bot.current_step_index:03d}_导出数据" / output_path.name
                debug_path.parent.mkdir(parents=True, exist_ok=True)
                
                if format_type == 'json':
                    with open(debug_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                elif format_type == 'yaml':
                    with open(debug_path, 'w', encoding='utf-8') as f:
                        yaml.dump(data, f, allow_unicode=True)
                elif format_type == 'csv':
                    with open(debug_path, 'w', encoding='utf-8', newline='') as f:
                        writer = csv.DictWriter(f, fieldnames=fields)
                        writer.writeheader()
                        writer.writerows(data)
                        
                self.logger.debug(f"调试数据已保存到: {debug_path}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"导出数据失败: {str(e)}")
            return False

class SetVariableAction(BaseAction):
    """设置变量值"""
    
    def execute(self, params: Dict[str, Any]) -> bool:
        try:
            name = params['name']
            value = params['value']
            
            # 如果值是变量引用,解析它
            if isinstance(value, str) and "${" in value:
                value = self.bot._resolve_variable(value)
                
            # 设置变量
            self.bot.set_variable(name, value)
            
            self.logger.debug(f"设置变量 {name} = {value}")
            return True
            
        except Exception as e:
            self.logger.error(f"设置变量失败: {str(e)}")
            return False

class GetVariableAction(BaseAction):
    """获取变量值"""
    
    def execute(self, params: Dict[str, Any]) -> Any:
        try:
            name = params['name']
            default = params.get('default')
            
            # 获取变量值
            value = self.bot.get_variable(name, default)
            
            self.logger.debug(f"获取变量 {name} = {value}")
            return value
            
        except Exception as e:
            self.logger.error(f"获取变量失败: {str(e)}")
            return None 