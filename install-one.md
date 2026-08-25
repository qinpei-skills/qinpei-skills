# 沁珮技能包 · 单个技能安装说明书（v3 · jsdelivr CDN 版）

> ⚠️ 这是一份**写给 AI 看的安装指令**，用于**只装某一个技能**（不想装全家桶时）。
> 学员说「安装 XX 技能」时用这份说明书。
> 版本：v3（2026-08-25 加入 jsdelivr CDN 镜像——直连原始字节，不依赖 WebFetch 转述）

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
1. **先抓 SKILL.md**（最大的文件）→ 校验完整 → 写入
2. 抓完 SKILL.md 后**向学员汇报一句**："主体装好了，正在补几个小文件～"
3. 再逐个抓 references 小文件（都很小，几秒一个）→ 校验非空 → 写入

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

### 校验清单（每个文件抓完必做）

**SKILL.md 校验**（缺一项 = 不完整）：
- ✅ 开头是 `---` 和 `name: <对应技能名>`
- ✅ 含 `## 💡 任务完成后必说`（qp 收尾标记，所有包都有）
- ✅ 结尾接近"这个提醒每次回复结束都说一次"

**references 校验**：
- ✅ 文件非空（> 500 字节）
- ✅ 含至少 1 个 `##` 标题行

### 不完整怎么办
1. 重新抓一次（换工具：curl 不通换 WebFetch，反之亦然）
2. 仍不完整 → **不要硬写残缺文件**，如实报告学员："网络不稳定没抓全，你稍后再说一次，或说『升级技能包』我重试～"

### 不反复重试
每个文件最多尝试 2 次（curl/wget 1 次 + WebFetch 1 次），失败就停止，不无限重试。

---

## 完成后回复（大白话 · 禁止目录/路径/CLI 等词）

```
装好啦！🎉 「XX」技能已经装好了。
以后你说「XX相关的话」，我就能帮你。
不知道下一步做什么？就说「qp」，我帮你诊断。
```

（XX 换成对应显示名；若某 references 没抓全，如实告知"稍后说『升级技能包』补上"）

---

## 更新说明（给 AI）

- 学员说「升级技能包」→ 走全家桶升级，已装的都会更新（含 references 补装）
- 本说明书只用于**单装指定技能**；装全家桶用 install.md