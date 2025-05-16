# 🧠 Baidu+Deepseek 智能问答助手（Search-Augmented QA System）

一个结合 **百度搜索引擎** 与 **Deepseek 大语言模型** 的智能问答系统，具备实时信息检索能力，并通过大模型对搜索结果进行理解和整合，最终以自然语言形式返回回答。本项目为课程作业开发，展示了搜索增强技术在问答系统中的应用价值。

---

## 📌 项目亮点

* 🔍 实时调用 **百度搜索** 获取信息片段
* 🧩 基于搜索结果构造 Prompt 提问 **Deepseek LLM**
* 💬 支持 **Socket.IO** 实时通信的 Web 聊天前端
* ⚙️ 后端基于 **Flask**，结构清晰、可拓展性强
* 📚 适合 NLP、人工智能导论等课程项目

---

## 🧱 项目结构

```
search-augmented-qa/
├── app.py                 # Flask 主程序，处理搜索与大模型交互
├── search.py        # 百度搜索调用与结果解析(爬虫）
├── chat_api.py             # Deepseek API 接口封装
├── templates/
│   └── index.html         # 聊天界面（Web前端）
├── requirements.txt       # Python 项目依赖
└── README.md              # 项目说明文件
```

---

## 🚀 项目运行

### 环境依赖

```bash
pip install -r requirements.txt
```

### 启动服务

```bash
python app.py
```

### 打开浏览器访问

```
http://localhost:5000
```

---

## 🧠 系统流程图

1. 用户输入问题 →
2. 使用百度搜索相关信息摘要 →
3. 构造带上下文的 Prompt →
4. 提交至 Deepseek LLM →
5. 返回模型生成的答案 →
6. 显示在 Web 聊天窗口中

---

## 📌 示例问答

**Q:** 李白和杜甫是什么关系？
**🔍 Search Extracted:** 李白与杜甫是唐代著名诗人，两人互有唱和。
**🤖 Answer:** 李白和杜甫是唐代的著名诗人，他们在诗歌创作上互相交流、惺惺相惜。

---

## 💡 技术细节

| 模块        | 技术栈 / 服务          |
| --------- | ----------------- |
| 后端服务      | Flask + Socket.IO |
| 搜索爬虫      | 百度搜索（requests 调用） |
| 大模型接口     | Deepseek Chat API |
| Prompt 构造 | 基于搜索摘要的模板构建       |
| 前端界面      | HTML + JS + CSS   |

---

## 📚 课程背景

本项目为《Python语言程序设计》课程作业，旨在实践“**信息增强大语言模型问答系统**”的设计与实现。通过本项目，我们探索了将大语言模型与外部检索系统结合的可行性，以及 Prompt 工程在实际应用中的效果。

---

## 🔒 注意事项

* 请合理使用搜索接口，避免频繁访问导致 IP 限制
* Deepseek API Key 请根据个人账号获取，自行配置

---
