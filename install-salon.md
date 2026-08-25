# 线下沙龙技能包 · 单独安装说明书（现场版 v2）

> ⚠️ 这是一份**写给 AI 看的安装指令**，用于线下课/活动结束时现场快速安装。
> 只装「线下沙龙技能包」一个包，不用装全家桶。
> 版本：v2（补齐内容校验 + 失败降级——2026-08-25 修复安装失败问题）

---

## 你要做的事

在学员设备上安装 `qinpei-salon-ops-trust`（线下沙龙技能包）到 `~/.workbuddy/skills/qinpei-salon-ops-trust/`。

---

## ⚠️ 先对学员说（大白话，现场气氛）

> 来，给你装一个「办沙龙」的 AI 技能，10 秒钟装好——以后你办活动，它就帮你把流程、话术、互动全安排明白。
> 手机保持亮屏别切走，马上好～

学员确认后开始。

---

## ⚠️ 环境事实（必须遵守）

**手机端沙箱网络实测**：

| 通道 | 状态 | 用途 |
|---|---|---|
| `raw.githubusercontent.com` GitHub 直连 | ❌ 被封 | **不要用** |
| **jsdelivr CDN 镜像** | ✅ **能直连！返回原始字节** | **首选** |
| WebFetch | ✅ 能通但慢、可能转述/截断 | **备用兜底** |

**结论**：抓文件**首选 jsdelivr CDN 镜像**（用 `curl -fsSL "<URL>" -o "<path>"` 直连下载原始字节）；jsdelivr 不通才用 WebFetch。

> jsdelivr URL 格式：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/<仓库内路径>`
> ⚠️ `cdn.jsdelivr.net` 才是通的；不要去试 `raw.githubusercontent.com`（被封）。

---

## 抓取文件（jsdelivr 优先 · 全部必需）

依次抓取以下 3 个文件：

| 保存为 | jsdelivr URL（首选） |
|:---|:---|
| `~/.workbuddy/skills/qinpei-salon-ops-trust/SKILL.md` | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-salon-ops-trust/SKILL.md` |
| `~/.workbuddy/skills/qinpei-salon-ops-trust/references/活动内容脚本.md` | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-salon-ops-trust/references/活动内容脚本.md` |
| `~/.workbuddy/skills/qinpei-salon-ops-trust/references/成交与分工.md` | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-salon-ops-trust/references/成交与分工.md` |

### 抓取命令（首选）
```bash
curl -fsSL "<上表jsdelivr URL>" -o "<上表目标路径>"
```
- `-f`：HTTP 错误不输出文件
- `-sS`：静默但错误时显示
- `-L`：跟随重定向

jsdelivr 不通（HTTP 非 2xx）→ 改用 WebFetch 抓同一地址，剥围栏后写入。

---

## 抓取规则（WebFetch 三大坑 + 校验，必须遵守）

### 坑 1：抓回内容可能包围栏
WebFetch 返回 markdown 时经常被外层包了 ` ```markdown ... ``` ` 围栏。
**写入前必须剥掉最外层的 ` ```markdown ` 和末尾的 ` ``` `**，否则 frontmatter（`---`）被破坏。

### 坑 2：抓回内容可能截断 / 丢内容（最危险）
WebFetch 抓大文件（30KB）时**可能截断或漏段**——AI 必须做**内容完整性校验**：

**SKILL.md 校验清单**（抓回后逐项核对，缺一项 = 不完整）：
- ✅ 开头是 `---` 和 `name: qinpei-salon-ops-trust`
- ✅ 含 `## 📄 产出与交付规则`
- ✅ 含 `## 🔎 诊断优先入口`
- ✅ 含 `## 📂 素材路由表`
- ✅ 含 `## 🎯 定位与边界`
- ✅ 含 `## 💡 任务完成后必说`（qp 收尾）
- ✅ 结尾接近"这个提醒每次回复结束都说一次"

**references 校验**：
- `活动内容脚本.md`：含「活动微课脚本」
- `成交与分工.md`：含「信号识别提醒卡」或「邀约三路」

**不完整怎么办**：
1. 重新 WebFetch 一次（URL 换新时间戳 `?t=`）
2. 仍不完整 → **不要硬写残缺文件**，报告学员："网络不稳定，技能内容没抓全。你稍后再说一次『我要办沙龙』或『升级技能包』，我重试～"

### 坑 3：不要反复重试
每个文件最多尝试 2 次（WebFetch 2 次），失败就停止，不无限重试。

---

## 完成后回复（大白话 · 禁止目录/路径/CLI 等词）

```
装好啦！🎉 以后你想办沙龙，直接跟我说「我要办沙龙」就行——
AI 会先问你几件事（活动目标/人群/能投入多少），帮你把活动从流程到话术全安排明白。
不知道下一步做什么？就说「qp」，我帮你诊断。
```

**如果某个文件没抓全**，如实告诉学员："沙龙技能装好了大部分，有个小文件没抓全，稍后说『升级技能包』我帮你补上～"

---

## 更新说明（给 AI）

- 学员说「升级技能包」→ 走全家桶升级流程，本包自动更新（含 references 补装）
- 本说明书只用于**现场快速单装**，完整体系请用全家桶安装说明书
