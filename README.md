# 医疗疾病数据分析大屏可视化系统

## 项目简介

本项目是一个基于Python和Vue.js的医疗疾病数据分析可视化系统，集成了数据分析、机器学习预测、报告生成和AI智能对话等功能。系统采用深蓝色科技风格UI设计，提供直观的数据可视化展示和智能的医疗咨询服务。

## 核心功能

### 1. 数据可视化大屏
- 实时展示医疗数据统计信息
- 疾病分布地图可视化
- 多维度数据图表展示（饼图、柱状图、折线图等）
- 动态数据更新和交互

### 2. 疾病预测分析
- 基于机器学习的疾病预测模型
- 支持多种算法（随机森林、SVM、神经网络等）
- 预测结果可视化展示
- 模型性能评估指标

### 3. 数据管理
- 医疗数据表格展示
- 数据筛选和排序功能
- 数据导入导出
- 数据统计分析

### 4. 报告生成
- 自动生成数据分析报告
- 支持多种报告格式
- 可定制报告模板
- 报告下载和打印

### 5. AI医疗助手
- **多对话管理**：支持创建、切换、重命名、删除多个对话
- **智能问答**：基于DeepSeek大模型的医疗咨询服务
- **快速咨询**：提供常见医疗问题快速入口
- **Markdown支持**：AI回复支持富文本格式显示
- **数据持久化**：对话历史自动保存，支持30天内查看

## 技术栈

### 后端技术
- **Python 3.12**
- **Flask**: Web框架
- **Flask-SocketIO**: WebSocket通信
- **SQLAlchemy**: ORM数据库操作
- **Pandas**: 数据处理和分析
- **Scikit-learn**: 机器学习算法
- **OpenAI SDK**: 集成DeepSeek API
- **NumPy**: 数值计算

### 前端技术
- **Vue.js 2.x**: 前端框架
- **Vue Router**: 路由管理
- **Element UI**: UI组件库
- **ECharts**: 数据可视化图表
- **Socket.IO Client**: WebSocket客户端
- **Marked**: Markdown解析
- **Axios**: HTTP请求

### 数据库
- **MySQL 5.7+ / 8.0+**：作为病例数据和爬虫数据的主存储（`medicalinfo` 数据库）
- **SQLite (`data/data.db`)**：历史示例 / 轻量级测试（可选，不再作为主数据源）

## 项目结构

```
基于python医疗疾病数据分析大屏可视化系统/
│
├── app.py                       # Flask 主应用入口（REST API、数据管理、报告生成等）
├── websocket_chat.py            # WebSocket 服务（AI 医疗助手，对接 DeepSeek）
├── requirements.txt             # Python 依赖包
├── .env                         # 环境配置文件（DeepSeek & 数据库等）
├── medicalinfo.sql              # MySQL 初始化脚本（病例数据表结构和示例数据）
├── .env.example                # 团队共享的环境变量模板
│
├── spiders/                     # 爬虫与定时任务模块
│   ├── spiderMain.py            # 爬虫主程序（按疾病爬取病例）
│   ├── spiderDetail.py          # 详情页解析
│   ├── data_sync_manager.py     # CSV -> MySQL 数据同步
│   ├── model_trainer.py         # 定时训练 / 评估模型
│   ├── start_scheduler.py       # 定时任务统一入口（APScheduler）
│   └── ...
│
├── utils/                       # 工具模块
│   ├── __init__.py
│   ├── db_config.py             # 统一数据库配置（从 .env 读取 DB_*）
│   ├── query.py                 # 通用 MySQL 查询封装
│   └── ...
│
├── machine/                     # 机器学习 / AI 模块
│   ├── __init__.py
│   ├── tree.py                  # BERT 模型与相似病例检索（MedicalAI）
│   └── ...
│
└── front-end-template-1-master/  # Vue前端项目
    ├── package.json              # 前端依赖配置
    ├── vue.config.js            # Vue配置
    │
    ├── public/                  # 静态资源
    │   └── index.html
    │
    └── src/                     # 源代码
        ├── main.js              # 入口文件
        ├── App.vue              # 根组件
        │
        ├── router/              # 路由配置
        │   └── index.js
        │
        ├── views/               # 页面组件
        │   ├── Index.vue        # 首页大屏
        │   ├── Pred.vue         # 疾病预测
        │   ├── TableData.vue    # 数据管理
        │   ├── Report.vue       # 报告生成
        │   └── AiChat.vue       # AI医疗助手
        │
        ├── components/          # 公共组件
        │   ├── Header.vue       # 导航栏
        │   └── ...
        │
        └── assets/              # 静态资源
            ├── css/
            ├── images/
            └── ...
```

## 安装部署

以下步骤以 Windows PowerShell 和 VS Code 为例。团队统一使用 Python 3.12、Node.js 24 和 MySQL 8.0。Python 和 Node.js 的安装位置由每位成员自行选择。疾病预测权重通过 Git LFS 下载。

### 1. 拉取代码和模型

在安装 Git LFS 后，从 GitHub 复制团队仓库的 HTTPS 地址，并替换下面的占位符。

```powershell
git lfs install
git clone <团队仓库地址>
cd <仓库目录>
git lfs pull
git lfs ls-files
```

`machine/medical_model.pth` 和 `machine/bert-base-chinese/model.safetensors` 应各有约 400 MB。`git lfs ls-files` 中两项都应标记为 `*`。若权重仍是几行文本，请确认当前账号有仓库访问权限，并检查团队仓库是否已上传 LFS 对象。

### 2. 安装 Python 和前端依赖

在仓库根目录执行以下命令。

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check

Push-Location .\front-end-template-1-master
npm.cmd ci
Pop-Location
```

在 VS Code 中使用 `Python: Select Interpreter` 选择仓库内的 `.venv\Scripts\python.exe`。下面的命令直接调用该解释器，可在 PowerShell 中执行。

### 3. 创建本地配置和数据库

首次配置时，在仓库根目录执行 `Copy-Item .env.example .env`。打开 `.env` 并填写本机 MySQL 的 `DB_HOST`、`DB_PORT`、`DB_USER`、`DB_PASSWORD` 和 `DB_NAME`。MySQL 账号需要能读写项目数据库，并能创建应用使用的数据管理表和报告模板表。需要测试 AI 对话时，填写自己的 `DEEPSEEK_API_KEY`。

启动 MySQL。在仓库根目录登录 MySQL 客户端，`-u` 后填写可创建数据库的账号，`-p` 会在终端提示输入密码。

```powershell
mysql --default-character-set=utf8mb4 -h 127.0.0.1 -P 3306 -u root -p
```

在 MySQL 提示符执行以下命令。仅对新建的空数据库执行 `SOURCE`，因为初始化 SQL 会重建已有的 `cases` 表。若自定义了 `DB_NAME`，同步调整下面的库名。

```sql
CREATE DATABASE IF NOT EXISTS medicalinfo CHARACTER SET utf8mb4;
USE medicalinfo;
SOURCE medicalinfo.sql;
SELECT COUNT(*) FROM cases;
EXIT;
```

默认示例库应包含 345 条病例。

### 4. 在 VS Code 中启动

在仓库根目录打开三个 PowerShell 终端，每个终端分别运行下面的一组命令。

```powershell
.\.venv\Scripts\python.exe app.py
```

```powershell
.\.venv\Scripts\python.exe websocket_chat.py
```

```powershell
cd .\front-end-template-1-master
$env:NODE_OPTIONS = '--openssl-legacy-provider'
npm.cmd run serve -- --host 127.0.0.1 --port 8080
```

访问 [大屏首页](http://127.0.0.1:8080/) 和 [AI 医疗助手](http://127.0.0.1:8080/ai-chat)。Flask API 使用 5000 端口，对话 WebSocket 使用 5001 端口。Flask 首次启动时会加载权重并计算病例向量，看到 `Running on http://127.0.0.1:5000` 后即可请求接口。

需要使用可选的爬虫调度时，在根目录运行 `.\.venv\Scripts\python.exe -m spiders.start_scheduler --action list` 查看可用任务，或通过 `--action start` 启动调度。

### 仓库维护

提交 `.env.example`、`requirements.txt`、`package-lock.json`、`medicalinfo.sql` 和模型文件。`.gitignore` 会忽略本机密钥和依赖目录。首次上传模型前，执行 `git lfs install` 并检查两个权重文件是否都体现在 `git lfs ls-files` 中。模型入库后，使用一个干净的克隆检查 LFS 下载和上述启动步骤。

## 使用说明

### 系统导航
1. **首页** - 数据可视化大屏，展示关键医疗数据指标
2. **数据预测** - 使用机器学习模型进行疾病预测分析
3. **数据管理** - 查看和管理医疗数据记录
4. **报告生成** - 生成数据分析报告
5. **AI医疗助手** - 智能医疗咨询对话

### AI医疗助手使用指南

#### 基本操作
- **新建对话**：点击左侧"新建对话"按钮开始新的咨询
- **切换对话**：点击左侧对话列表切换历史对话
- **发送消息**：输入问题后按Enter发送，Shift+Enter换行
- **快速提问**：点击快速问题卡片直接开始对话

#### 对话管理
- **重命名**：鼠标悬停在对话上，点击编辑图标修改标题
- **删除**：点击删除图标移除不需要的对话
- **自动保存**：所有对话自动保存30天

#### 支持的咨询类型
- 症状分析和初步诊断建议
- 用药指导和注意事项
- 体检报告解读
- 疾病预防和健康管理
- 医疗常识科普

## 配置说明

本地配置来自项目根目录的 `.env`。数据库连接由 `utils/db_config.py` 统一读取。可参照 [安装部署](#安装部署) 创建示例数据库并填入自己的 DeepSeek Key。

## 常见问题

### Q1: AI助手连接失败？
- 检查WebSocket服务是否正常启动（端口5001）
- 确认DeepSeek API Key配置正确
- 检查网络连接是否正常

### Q2: 依赖安装失败？

确认 `py -3.12 --version` 和 `node --version` 输出与安装步骤中的版本一致。Python 依赖使用仓库内的 `.venv` 安装，前端依赖在 `front-end-template-1-master` 中通过 `npm.cmd ci` 安装。若 `mysql` 命令找不到，可使用 MySQL 安装目录 `bin` 下的 `mysql.exe`。

### Q3: 数据可视化不显示？
- 检查后端API服务是否正常（端口5000）
- 查看浏览器控制台是否有错误信息
- 确认数据库中有数据

### Q4: 聊天记录丢失？
- 聊天记录保存在浏览器localStorage中
- 清除浏览器数据会导致记录丢失
- 系统自动保留30天内的对话

## 开发说明

### 添加新功能
1. 后端API：在 `app.py` 中添加新路由
2. 前端页面：在 `src/views/` 下创建Vue组件
3. 路由配置：在 `src/router/index.js` 中添加路由

### 数据格式
- API响应格式：JSON
- 时间格式：ISO 8601
- 编码：UTF-8

### 代码规范
- Python: PEP 8
- JavaScript: ESLint
- Vue: Vue Style Guide

## 注意事项

1. **数据安全**：生产环境部署时请更换所有默认密钥
2. **API限制**：DeepSeek API有调用频率限制，请合理使用
3. **浏览器兼容**：建议使用Chrome、Firefox、Edge等现代浏览器
4. **数据备份**：定期备份数据库和重要配置文件

## 许可证

本项目仅供学习和研究使用，不得用于商业目的。

## 联系方式

如有问题或建议，请通过以下方式联系：
- 项目Issues
- 邮箱：[联系邮箱]

## 更新日志

### v1.0.0 (2024-12)
- ✅ 基础功能实现
- ✅ 数据可视化大屏
- ✅ 机器学习预测模块
- ✅ AI医疗助手集成
- ✅ 多对话管理功能
- ✅ Markdown渲染支持
- ✅ 响应式设计优化

---

**声明**：本系统提供的医疗建议仅供参考，不能替代专业医生的诊断和治疗。如有健康问题，请及时就医。
