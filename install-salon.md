# 线下沙龙技能包 · 单独安装说明书（现场版）

> ⚠️ 这是一份**写给 AI 看的安装指令**，用于线下课/活动结束时现场快速安装。
> 只装「线下沙龙技能包」一个包，不用装全家桶。

---

## 你要做的事

在学员设备上安装 `qinpei-salon-ops-trust`（线下沙龙技能包）到 `~/.workbuddy/skills/qinpei-salon-ops-trust/`。

---

## ⚠️ 先对学员说（大白话，现场气氛）

> 来，给你装一个「办沙龙」的 AI 技能，10 秒钟装好——以后你办活动，它就帮你把流程、话术、互动全安排明白。
> 手机保持亮屏别切走，马上好～

学员确认后开始。

---

## 抓取文件（WebFetch · 每个 URL 加 `?t=时间戳` 绕过缓存）

依次抓取以下文件（全部必需）：

| 保存为 | 抓取地址 |
|:---|:---|
| `~/.workbuddy/skills/qinpei-salon-ops-trust/SKILL.md` | `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-salon-ops-trust/SKILL.md` |
| `~/.workbuddy/skills/qinpei-salon-ops-trust/references/活动内容脚本.md` | `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-salon-ops-trust/references/%E6%B4%BB%E5%8A%A8%E5%86%85%E5%AE%B9%E8%84%9A%E6%9C%AC.md` |
| `~/.workbuddy/skills/qinpei-salon-ops-trust/references/成交与分工.md` | `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-salon-ops-trust/references/%E6%88%90%E4%BA%A4%E4%B8%8E%E5%88%86%E5%B7%A5.md` |

**规则**：
- 不用 curl，一律 WebFetch；URL 加 `?t=<当前时间戳>` 绕过 CDN 缓存
- 抓回内容剥掉最外层的 ` ```markdown ` 围栏再写入
- 每个文件最多尝试 2 次，失败就跳过记下，不反复重试
- 判定标准：SKILL.md 约 30KB、开头是 `---` 和 `name: qinpei-salon-ops-trust`

---

## 完成后回复（大白话 · 禁止目录/路径/CLI 等词）

```
装好啦！🎉 以后你想办沙龙，直接跟我说「我要办沙龙」就行——
AI 会先问你几件事（活动目标/人群/能投入多少），帮你把活动从流程到话术全安排明白。
不知道下一步做什么？就说「qp」，我帮你诊断。
```

---

## 更新说明（给 AI）

- 学员说「升级技能包」→ 走全家桶的升级流程，本包会自动更新
- 本说明书只用于**现场快速单装**，完整体系请用全家桶安装说明书
