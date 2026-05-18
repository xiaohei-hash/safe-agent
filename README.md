# Safe Theory Agent

本地可运行的可证明安全理论 AI 智能体

---

# 项目简介

Safe Theory Agent 是一个围绕：

- 可证明安全（Provable Security）
- 密码学理论
- Capability Security
- 本地 AI Runtime

构建的本地 AI Agent 系统。

项目目标：

构建一个：

- 可本地运行
- 可实时交互
- 可展示 Runtime
- 可回答安全理论问题

的智能体系统。

---

# 项目特点

## 本地 AI 模型

使用：

- Ollama
- qwen2.5:3b

实现：

- 本地推理
- 无需云 API
- 离线运行

---

## 安全理论问答

支持：

- IND-CPA
- 随机预言机模型
- Capability Security
- 最小权限原则
- RSA
- AES
- 可证明安全理论

等问题。

---

## Runtime 实时日志

系统支持：

- WebSocket Runtime
- task_running
- task_completed

实现：

AI Agent 运行过程可视化。

---

## 交互式前端

前端支持：

- 示例问题按钮
- 实时 AI 回答
- Runtime Logs
- 本地 Dashboard

---

# 技术栈

## 前端

- Next.js
- React
- TypeScript

## 后端

- FastAPI
- Python

## AI 模型

- Ollama
- qwen2.5:3b

## Runtime

- WebSocket
- 本地 Runtime Queue

---

# 项目结构

```text
safe_agent/
│
├── backend/
│   ├── api/
│   │   └── chat.py
│   │
│   ├── llm/
│   │   └── ollama_client.py
│   │
│   ├── ws/
│   │   ├── manager.py
│   │   └── router.py
│   │
│   └── main.py
│
├── frontend/
│   └── app/
│       └── page.tsx
│
└── README.md
```

---

# 安装步骤

# 1. 克隆项目

```bash
git clone <你的仓库地址>
cd safe_agent
```

---

# 2. 配置后端

进入 backend：

```bash
cd backend
```

创建虚拟环境：

```bash
python -m venv .venv
```

激活虚拟环境：

## Windows

```bash
.venv\Scripts\activate
```

安装依赖：

```bash
pip install fastapi uvicorn requests websockets
```

---

# 3. 安装 Ollama

官网下载：

```text
https://ollama.com
```

下载模型：

```bash
ollama pull qwen2.5:3b
```

测试模型：

```bash
ollama run qwen2.5:3b
```

---

# 4. 启动后端

```bash
uvicorn main:app --reload
```

后端地址：

```text
http://127.0.0.1:8000
```

Swagger 文档：

```text
http://127.0.0.1:8000/docs
```

---

# 5. 配置前端

进入 frontend：

```bash
cd frontend
```

安装依赖：

```bash
npm install
```

启动前端：

```bash
npm run dev
```

前端地址：

```text
http://localhost:3000
```

---

# 使用方法

## 示例问题

可以直接点击：

- 什么是 IND-CPA
- Capability Security
- 随机预言机
- 最小权限原则

---

## 自由提问

也可以输入：

```text
AES 为什么安全？
RSA 的安全基础是什么？
什么是可证明安全？
```

系统会调用：

本地 qwen 模型进行回答。

---

# Runtime 日志

系统支持 Runtime 可视化。

提问时：

页面会实时显示：

```json
{
  "type": "task_running",
  "task": "llm_reasoning"
}
```

以及：

```json
{
  "type": "task_completed",
  "task": "llm_reasoning"
}
```

---

# 项目目标

本项目用于：

- AI Agent 学习
- 安全理论展示
- 可证明安全课程项目
- 本地 AI Runtime 实验

---

# 后续可扩展方向

未来可以继续扩展：

- RAG 理论知识库
- 多工具调用（Tool Calling）
- Docker Sandbox
- 多步推理（Multi-step Planning）
- Formal Verification
- Agent Memory
- 自动论文总结

---

# 项目效果

项目最终实现：

- 本地 AI Agent
- 实时 Runtime
- WebSocket 通信
- 安全理论问答
- 本地 Dashboard

是一个完整的本地安全理论智能体 Demo。

---

# License

MIT License
