# 沁珮技能包 · 单个技能安装说明书

> ⚠️ 这是一份**写给 AI 看的安装指令**，用于**只装某一个技能**（不想装全家桶时）。
> 学员/用户说「安装 XX 技能」时用这份说明书；说「安装技能包」（没指定哪个）时用全家桶的 install.md。

---

## 你要做的事

识别学员想装的技能名，只装那一个（含它的 references 知识文件），到 `~/.workbuddy/skills/<技能名>/`。

---

## 第一步：识别技能 + 读清单

1. 从学员的话里识别技能（支持显示名或技能名）：
   - 朋友圈 / qinpei-wechat-trust
   - 社群 / qinpei-community-ops-trust
   - 沙龙 / qinpei-salon-ops-trust
   - 故事力 / qinpei-storytelling
   - IP 定位 / qinpei-ip-diagnosis
   - 业务体检 / qinpei-business-check
   - 画像 / qinpei-profile
   - 入口 / qinpei
2. 用 WebFetch 抓技能清单（URL 加 `?t=时间戳`）：
   `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills-catalog.md`
   找到该技能的 **SKILL.md 地址** 和 **附加文件列表**（最后一列，逗号分隔）

---

## 第二步：抓取（WebFetch · 环境事实：curl/wget/git 全被封）

⚠️ **手机端沙箱只有 WebFetch 能访问 GitHub**——不要试 curl/wget/git，不要做环境自检，直接 WebFetch。

依次抓取：SKILL.md + 所有附加文件（references/ 等），每个 URL 加 `?t=<当前时间戳>` 绕过 CDN 缓存。

### 抓取规则（WebFetch 三大坑）

**坑 1：包围栏**——抓回内容若以 ` ```markdown ` 开头，写入前剥掉最外层围栏。

**坑 2：截断/漏内容（最危险）**——大文件可能抓不全，必须校验：
- SKILL.md 校验：开头是 `---` 和 `name: <技能名>`；含该技能的关键章节（如朋友圈含"三层信任"、社群含"诊断优先四步法"、沙龙含"诊断优先入口"）；结尾完整
- references 校验：内容非空、含标题行
- **不完整 → 换新时间戳重抓 1 次 → 仍不完整 → 不要硬写，报告学员"网络不稳定没抓全，稍后再说一次或说『升级技能包』重试"**

**坑 3：不反复重试**——每个文件最多尝试 2 次。

---

## 第三步：完成后回复（大白话 · 禁止目录/路径/CLI 等词）

```
装好啦！🎉 「XX」技能已经装好了。
以后你说「XX功能相关的话」，我就能帮你。
不知道下一步做什么？就说「qp」，我帮你诊断。
```

（XX 换成对应显示名；若某 references 没抓全，如实告知"稍后说『升级技能包』补上"）

---

## 更新说明（给 AI）

- 学员说「升级技能包」→ 走全家桶升级，已装的都会更新
- 本说明书只用于**单装指定技能**；装全家桶用 install.md
