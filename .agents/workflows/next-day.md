---
description: 完成当天学习后标记进度、生成下一天任务并推送 GitHub
---

## /next-day — 每日学习推进工作流

每次学习完成后，告诉 AI「今天的学习任务完成了」，AI 会自动执行以下步骤：

### Step 1：确认当前完成天次

请告诉 AI：「今天完成了 Day XX」  
（或者 AI 根据 README.md 进度表自动判断当前天次）

### Step 2：标记当天进度为已完成

更新 `README.md` 进度表：
- 当天：⬜ / 🔄 → ✅ 已完成，笔记链接补充
- 下一天：⬜ → 🔄 进行中

### Step 3：更新当天的 README.md 笔记

在 `week0X_xxx/dayXX_xxx/README.md` 中：
- 勾选「完成情况」中的所有复选框
- 补充「今日总结」一行

### Step 4：生成下一天的学习文件

在对应目录下创建：
- `week0X_xxx/dayXX_xxx/main.py`：完整可运行示例，中文注释
- `week0X_xxx/dayXX_xxx/README.md`：学习目标、笔记模板、渲染命令

### Step 5：更新 notes/cheatsheet.md

将当天新学到的 API 追加到速查手册对应章节中。

### Step 6：Git 提交并推送

// turbo
```bash
cd /Users/Hana/Codes/manim-study && git add . && git commit -m "完成 Day XX: <主题名称>，生成 Day XX+1 学习任务" && git push
```

---

> **触发方式**：告诉 AI `/next-day` 或「今天的学习任务完成了」即可一键触发全流程。
