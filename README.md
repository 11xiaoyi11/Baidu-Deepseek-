# 🧠 Baidu+Deepseek 智能问答助手（Search-Augmented QA System）

一个结合 **百度搜索引擎** 与 **Deepseek 大语言模型** 的智能问答系统，具备实时信息检索能力，并通过大模型对搜索结果进行理解和整合，最终以自然语言形式返回回答。本项目为课程作业开发，展示了搜索增强技术在问答系统中的应用价值。

---

## 📌 项目亮点

* 🔍 实时调用 **百度搜索** 获取信息片段
* 🧩 基于搜索结果构造 Prompt 提问 **Deepseek LLM**
* 💬 支持 **Socket.IO** 实时通信的 Web 聊天前端
* ⚙️ 后端基于 **Flask**，结构清晰、可拓展性强
* 📚 适合 NLP、人工智能导论、Python程序设计等课程项目

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

### 克隆仓库

```bash
git clone https://github.com/11xiaoyi11/Baidu-Deepseek_SearchQA.git
cd Baidu-Deepseek_SearchQA
```

### 使用虚拟环境

```bash
# 使用 conda（推荐）
conda create -n SearchQA python=3.10 -y
conda activate SearchQA
```

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


## 🔑 配置

1. **设置 AI API 密钥**：  
   这里课程要求使用deepseek，我使用的是 [腾讯云](https://cloud.tencent.com/document/product/1772/115969)（因为现在免费）  
   在 chat_api.py 修改 ([here](https://github.com/11xiaoyi11/Baidu-Deepseek_SearchQA/blob/main/chat_api.py#L12))：  
   ```
   api_key= "Your_API_KEY"
   ```

---

## 🧠 系统流程图

![](https://github.com/11xiaoyi11/Baidu-Deepseek_SearchQA/blob/main/assets/image0.png)

---

## 📌 示例问答

### 问答界面
![](https://github.com/11xiaoyi11/Baidu-Deepseek_SearchQA/blob/main/assets/image1.png)

### 搜索过程
![](https://github.com/11xiaoyi11/Baidu-Deepseek_SearchQA/blob/main/assets/image2.png)

### 问答显示
![](https://github.com/11xiaoyi11/Baidu-Deepseek_SearchQA/blob/main/assets/image3.png)

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
