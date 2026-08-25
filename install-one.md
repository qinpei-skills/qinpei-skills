# 沁珮技能包 · 单个技能安装说明书（v3 · jsdelivr CDN 版）

> ⚠️ 这是一份**写给 AI 看的安装指令**，用于**只装某一个技能**（不想装全家桶时）。
> 学员说「安装 XX 技能」时用这份说明书。
> 版本：v4（2026-08-25 回复话术写死+每技能场景开场白+禁止过程词；校验轻量化；过程零汇报）

---

## 你要做的事

识别学员想装的技能名 → 在下方【技能文件对照表】里找到它 → 抓取全部文件（SKILL.md + references）→ 保存到 `~/.workbuddy/skills/<技能名>/`。

**⚠️ 不要抓技能清单、不要解析任何表格、不要请求任何其他 URL**——文件地址全部写死在下面，照着抓就行。

---

## 先对学员说（大白话）

> 好嘞，给你装「XX」技能～手机保持亮屏、别切走，马上好！

学员确认后开始。

---

## ⚠️ 环境事实（重要 · 决定走哪条抓取通道）

**手机端沙箱的网络状况（已实测）**：

| 通道 | 状态 | 用途 |
|---|---|---|
| `raw.githubusercontent.com` GitHub 直连 | ❌ 被封（SSL 失败） | **不要用** |
| GitHub API (`api.github.com`) | ❌ 被封 | **不要用** |
| **`cdn.jsdelivr.net` CDN 镜像** | ✅ **能直连！返回原始字节** | **首选** |
| WebFetch（AI 工具） | ✅ 能通但慢、可能转述/截断 | **备用兜底** |

**结论**：抓文件**首选 jsdelivr CDN 镜像**（curl/wget 直连下载原始字节，最快最稳）；jsdelivr 不通才用 WebFetch 兜底。

> jsdelivr URL 格式：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/<仓库内路径>`
> 例如：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-wechat-trust/SKILL.md`

---

## 技能文件对照表（写死 · 直接查表，勿抓清单）

每行都给了**首选 jsdelivr URL**（原始字节）和**备用 raw URL**（WebFetch 用）；优先用 jsdelivr。

### 朋友圈（qinpei-wechat-trust）
保存到 `~/.workbuddy/skills/qinpei-wechat-trust/`
- SKILL.md（首选）：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-wechat-trust/SKILL.md`
- 领域-中医养生：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-wechat-trust/references/领域知识-中医养生.md`
- 领域-减脂塑形：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-wechat-trust/references/领域知识-减脂塑形.md`
- 领域-美业护肤：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-wechat-trust/references/领域知识-美业护肤.md`
- 领域-母婴育儿：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-wechat-trust/references/领域知识-母婴育儿.md`
- 领域-分享经济：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-wechat-trust/references/领域知识-分享经济.md`
- 选题库：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-wechat-trust/references/选题库.md`

### 社群（qinpei-community-ops-trust）
保存到 `~/.workbuddy/skills/qinpei-community-ops-trust/`
- SKILL.md：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-community-ops-trust/SKILL.md`
- 排期模板库：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-community-ops-trust/references/排期模板库.md`
- 话题库：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-community-ops-trust/references/话题库.md`
- 赛道案例库：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-community-ops-trust/references/赛道案例库.md`

### 沙龙（qinpei-salon-ops-trust）
保存到 `~/.workbuddy/skills/qinpei-salon-ops-trust/`
- SKILL.md：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-salon-ops-trust/SKILL.md`
- 活动内容脚本：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-salon-ops-trust/references/活动内容脚本.md`
- 成交与分工：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-salon-ops-trust/references/成交与分工.md`

### 故事力（qinpei-storytelling）
保存到 `~/.workbuddy/skills/qinpei-storytelling/`
- SKILL.md：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-storytelling/SKILL.md`

### IP定位（qinpei-ip-diagnosis）
保存到 `~/.workbuddy/skills/qinpei-ip-diagnosis/`
- SKILL.md：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-ip-diagnosis/SKILL.md`

### 业务体检（qinpei-business-check）
保存到 `~/.workbuddy/skills/qinpei-business-check/`
- SKILL.md：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-business-check/SKILL.md`

### 画像（qinpei-profile）
保存到 `~/.workbuddy/skills/qinpei-profile/`
- SKILL.md：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-profile/SKILL.md`

### 入口（qinpei）
保存到 `~/.workbuddy/skills/qinpei/`
- SKILL.md：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei/SKILL.md`

> 学员说的技能不在表里 → 告诉学员"这个还没开源，我帮你装现有的：朋友圈/社群/沙龙/故事力/IP定位/业务体检/画像/入口"。

---

## 抓取规则（jsdelivr 优先 · 必须遵守）

### 抓取顺序（重要）
1. **先抓 SKILL.md**（最大的文件）→ 轻量校验 → 写入
2. 再逐个抓 references 小文件（都很小，几秒一个）→ 轻量校验 → 写入
3. **全程不要向学员汇报过程**（不说"正在装""主体装好了""正在补小文件"）——**安静执行，装完一次性说结论**。等待就等待，学员只需要看到最终结果。

### 抓取方式

**首选**：用 curl/wget 直连 jsdelivr CDN 下载原始字节到目标文件。
```bash
curl -fsSL "<jsdelivr URL>" -o "<目标路径>"
```
- 加 `-f`：HTTP 错误不输出文件（失败立即停）
- 加 `-s`：静默模式（不刷进度条干扰）
- 加 `-S`：错误时显示错误信息
- 加 `-L`：跟随重定向（jsdelivr 偶尔重定向）

**备用**：jsdelivr 不通时（HTTP 不在 200-299），用 WebFetch 抓取目标 URL，剥围栏后写入。

### 轻量校验（只查这 2 项，不要逐章节核对——快最重要）

**SKILL.md 校验**：
- ✅ 开头是 `---` 且含 `name: <对应技能名>`
- ✅ 文件非空（> 500 字节）

**references 校验**：
- ✅ 文件非空（> 500 字节）

**不完整怎么办**：重新抓一次（换工具：curl 不通换 WebFetch，反之亦然）；仍不完整 → 不硬写残缺文件，如实报告学员："网络不稳定没抓全，你稍后再说一次重试～"

### 不反复重试
每个文件最多尝试 2 次（curl/wget 1 次 + WebFetch 1 次），失败就停止，不无限重试。

---

## 完成后回复（必须一字不差地按模板输出）

### ⚠️ 硬规则（最重要）
1. **只准输出下面模板里的内容**——AI 不得增加任何一句话
2. **禁止出现任何过程词**：安装明细、文件清单、校验结果、连接失败、抓取成功、路径、目录、版本、KB、curl、WebFetch 等，一个都不许出现
3. 把模板里的「XX」换成对应技能的显示名

### 各技能场景开场白（把「XX」替换成下表对应内容）

| 学员装的技能 | 开场白替换 |
|:---|:---|
| 沙龙 | 以后你要办活动，说「我要办沙龙」，我帮你把流程、话术、互动全安排好 |
| 朋友圈 | 说「我要发朋友圈」，我帮你写客户爱看的圈 |
| 社群 | 说「我的群没人说话」，我帮你把群盘活 |
| 故事力 | 说「帮我写我的故事」，我帮你把个人故事写出来 |
| IP定位 | 说「帮我做IP定位」，我帮你搞清自己的方向 |
| 业务体检 | 说「帮我体检业务」，我帮你看看卡在哪 |
| 画像 | 说「记住我是做什么的」，存一份画像，以后所有技能都记得你 |
| 入口 | 说「qp」，或直接说你想干啥，我帮你安排 |

### 输出模板（一字不差）

```
装好啦！🎉 <开场白>。

不知道接下来怎么做？就说「qp」，我帮你诊断。
```

（示例：装沙龙 → "装好啦！🎉 以后你要办活动，说「我要办沙龙」，我帮你把流程、话术、互动全安排好。\n\n不知道接下来怎么做？就说「qp」，我帮你诊断。"）

---

## 更新说明（给 AI）

- 学员说「升级技能包」→ 走全家桶升级，已装的都会更新（含 references 补装）
- 本说明书只用于**单装指定技能**；装全家桶用 install.md