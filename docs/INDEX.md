# RPA Framework 文档索引

> 在贡献文档前，请先阅读项目根目录下的 [CONTRIBUTING.md](../CONTRIBUTING.md) 文件。

## 项目结构

rpa_framework/
├── docs/               # 文档目录
│   ├── INDEX.md       # 文档索引
│   ├── HISTORY.md     # 开发历史
│   ├── api/           # API文档
│   │   └── core/      # 核心API文档
│   │       ├── base_bot.md            # 基础机器人API
│   │       ├── base_action.md         # 动作基类API
│   │       ├── ocr_actions.md         # OCR动作API
│   │       ├── screenshot_helper.md    # 截图工具API
│   │       ├── ocr_helper.md          # OCR工具API
│   │       ├── app_helper.md          # 应用管理API
│   │       ├── network_monitor.md     # 网络监控API
│   ├── design/        # 设计文档
│   │   ├── architecture.md    # 架构设计
│   │   ├── actions.md         # 动作系统设计
│   │   └── flow_schema.md     # 流程定义格式
│   └── requirements/  # 需求文档
│       └── overview.md        # 需求概述
├── rpa/              # 核心代码
│   ├── core/         # 核心功能模块
│   │   ├── actions/             # 动作实现
│   │   │   ├── __init__.py     # 动作注册
│   │   │   ├── base_action.py  # 动作基类
│   │   │   ├── ui_actions.py   # UI动作(UIAutomator2实现)
│   │   │   ├── ocr_actions.py  # OCR动作
│   │   │   ├── data_actions.py # 数据动作
│   │   │   ├── flow_actions.py # 流程控制动作
│   │   │   └── app_actions.py  # 应用动作
│   │   ├── network_monitor.py  # 网络监控
│   │   └── base_bot.py        # RPA基础类
│   ├── utils/        # 工具模块
│   │   ├── logger.py           # 日志工具
│   │   ├── ocr_helper.py      # OCR工具类
│   │   ├── screenshot.py      # 截图工具类(UIAutomator2实现)
│   │   └── app_helper.py      # 应用管理工具类
│   └── assets/       # 内置资源文件
├── flows/            # 流程配置文件
├── tests/            # 测试用例
│   └── flows/         # 流程测试用例
│       ├── ui_actions_test.yaml     # UI动作测试
│       ├── ocr_actions_test.yaml    # OCR动作测试
│       ├── data_actions_test.yaml   # 数据动作测试
│       ├── app_actions_test.yaml    # 应用动作测试
│       └── flow_actions_test.yaml   # 流程控制动作测试
├── debug/            # 调试输出目录
├── logs/             # 日志输出目录
├── CONTRIBUTING.md   # 贡献指南
├── README.md         # 项目说明
└── requirements.txt  # Python依赖

## 文档索引

### 设计文档
- [架构设计](design/architecture.md) - 系统整体架构设计
- [动作系统设计](design/actions.md) - RPA动作系统详细设计
- [流程定义格式](design/flow_schema.md) - YAML流程定义说明

### API文档
- [BaseBot API](api/core/base_bot.md) - RPA基础机器人类API
- [BaseAction API](api/core/base_action.md) - 动作基类API
- [OCR动作 API](api/core/ocr_actions.md) - OCR相关动作API
- [截图工具 API](api/core/screenshot_helper.md) - 截图相关API
- [OCR工具 API](api/core/ocr_helper.md) - OCR工具API
- [应用管理 API](api/core/app_helper.md) - 应用管理API
- [网络监控 API](api/core/network_monitor.md) - 网络监控API

### 需求文档
- [需求概述](requirements/overview.md) - 项目需求概览

### 测试文档
- UI动作测试 (tests/flows/ui_actions_test.yaml)
  - 区域点击
  - 滑动操作
  - 节点查找与点击
- OCR动作测试 (tests/flows/ocr_actions_test.yaml)
  - 文字识别
  - 文字验证
  - 智能点击
- 数据动作测试 (tests/flows/data_actions_test.yaml)
  - 变量操作
  - 数据导出
  - 列表处理
- 应用动作测试 (tests/flows/app_actions_test.yaml)
  - 应用安装
  - 应用启动
  - 状态检查
- 流程控制测试 (tests/flows/flow_actions_test.yaml)
  - 循环控制
  - 条件判断
  - 变量操作

### 其他文档
- [开发历史](HISTORY.md) - 版本更新记录