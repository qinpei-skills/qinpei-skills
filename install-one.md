# 沁珮技能包 · 单个技能安装说明书（v2 写死名单版）

> ⚠️ 这是一份**写给 AI 看的安装指令**，用于**只装某一个技能**（不想装全家桶时）。
> 学员说「安装 XX 技能」时用这份说明书。
> 版本：v2（2026-08-25 改为写死名单——不再抓 catalog 解析，直接按下方对照表执行）

---

## 你要做的事

识别学员想装的技能名 → 在下方【技能文件对照表】里找到它 → 只抓那一个技能的**全部文件**（SKILL.md + references）→ 保存到 `~/.workbuddy/skills/<技能名>/`。

**⚠️ 不要抓技能清单、不要解析任何表格、不要请求任何其他 URL**——文件地址全部写死在下面，照着抓就行。

---

## 先对学员说（大白话）

> 好嘞，给你装「XX」技能～手机保持亮屏、别切走，马上好！

学员确认后开始。

---

## 技能文件对照表（写死 · 直接查表，勿抓清单）

| 学员说 | 保存到目录 | 要抓的文件（按顺序） |
|:---|:---|:---|
| **朋友圈** | `~/.workbuddy/skills/qinpei-wechat-trust/` | ① SKILL.md：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-wechat-trust/SKILL.md`<br>② 中医养生：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-wechat-trust/references/%E9%A2%86%E5%9F%9F%E7%9F%A5%E8%AF%86-%E4%B8%AD%E5%8C%BB%E5%85%BB%E7%94%9F.md`<br>③ 减脂塑形：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-wechat-trust/references/%E9%A2%86%E5%9F%9F%E7%9F%A5%E8%AF%86-%E5%87%8F%E8%84%82%E5%A1%91%E5%BD%A2.md`<br>④ 美业护肤：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-wechat-trust/references/%E9%A2%86%E5%9F%9F%E7%9F%A5%E8%AF%86-%E7%BE%8E%E4%B8%9A%E6%8A%A4%E8%82%A4.md`<br>⑤ 母婴育儿：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-wechat-trust/references/%E9%A2%86%E5%9F%9F%E7%9F%A5%E8%AF%86-%E6%AF%8D%E5%A9%B4%E8%82%B2%E5%84%BF.md`<br>⑥ 分享经济：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-wechat-trust/references/%E9%A2%86%E5%9F%9F%E7%9F%A5%E8%AF%86-%E5%88%86%E4%BA%AB%E7%BB%8F%E6%B5%8E.md`<br>⑦ 选题库：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-wechat-trust/references/%E9%80%89%E9%A2%98%E5%BA%93.md` |
| **社群** | `~/.workbuddy/skills/qinpei-community-ops-trust/` | ① SKILL.md：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-community-ops-trust/SKILL.md`<br>② 排期模板库：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-community-ops-trust/references/%E6%8E%92%E6%9C%9F%E6%A8%A1%E6%9D%BF%E5%BA%93.md`<br>③ 话题库：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-community-ops-trust/references/%E8%AF%9D%E9%A2%98%E5%BA%93.md`<br>④ 赛道案例库：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-community-ops-trust/references/%E8%B5%9B%E9%81%93%E6%A1%88%E4%BE%8B%E5%BA%93.md` |
| **沙龙** | `~/.workbuddy/skills/qinpei-salon-ops-trust/` | ① SKILL.md：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-salon-ops-trust/SKILL.md`<br>② 活动内容脚本：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-salon-ops-trust/references/%E6%B4%BB%E5%8A%A8%E5%86%85%E5%AE%B9%E8%84%9A%E6%9C%AC.md`<br>③ 成交与分工：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-salon-ops-trust/references/%E6%88%90%E4%BA%A4%E4%B8%8E%E5%88%86%E5%B7%A5.md` |
| **故事力** | `~/.workbuddy/skills/qinpei-storytelling/` | ① SKILL.md：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-storytelling/SKILL.md` |
| **IP定位** | `~/.workbuddy/skills/qinpei-ip-diagnosis/` | ① SKILL.md：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-ip-diagnosis/SKILL.md` |
| **业务体检** | `~/.workbuddy/skills/qinpei-business-check/` | ① SKILL.md：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-business-check/SKILL.md` |
| **画像** | `~/.workbuddy/skills/qinpei-profile/` | ① SKILL.md：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-profile/SKILL.md` |
| **入口** | `~/.workbuddy/skills/qinpei/` | ① SKILL.md：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei/SKILL.md` |

> 学员说"沁珮"/"qp"→ 对应入口（qinpei）；说"记住我/我的画像"→ 画像（qinpei-profile）。
> 学员说的技能不在表里 → 告诉学员"这个还没开源，我帮你装现有的：朋友圈/社群/沙龙/故事力/IP定位/业务体检"。

---

## 抓取规则（WebFetch · 必须遵守）

### ⚠️ 环境事实
**手机端沙箱只有 WebFetch 能访问 GitHub**——curl/wget/git 直连全部被封（HTTP=000）。
- **不要试 curl / wget / git**——浪费时间且必然失败
- **不要做"环境自检"**——直接走 WebFetch
- 每个 URL 末尾加 `?t=<当前时间戳>` 绕过 CDN 缓存（只用于抓取，写入文件时去掉）

### 抓取顺序（重要）
1. **先抓 SKILL.md**（最大的文件）→ 校验完整 → 写入
2. 抓完 SKILL.md 后**向学员汇报一句**："主体装好了，正在补几个小文件～"
3. 再逐个抓 references 小文件（都很小，几秒一个）→ 校验非空 → 写入

### 三大坑
**坑 1：包围栏**——WebFetch 返回内容若以 ` ```markdown ` 开头，写入前剥掉最外层围栏（首尾各一行）。

**坑 2：截断/漏内容（最危险）**——大文件可能抓不全，抓回后必须校验：
- SKILL.md 校验：开头是 `---` 和 `name: <对应技能名>`；含 `## 💡 任务完成后必说`（qp 收尾）；结尾接近"这个提醒每次回复结束都说一次"
- references 校验：内容非空、含标题行
- **不完整 → 换新时间戳重抓 1 次 → 仍不完整 → 不要硬写残缺文件，如实报告学员**："网络不稳定没抓全，你稍后再说一次，或说『升级技能包』我重试～"

**坑 3：不反复重试**——每个文件最多尝试 2 次，失败就停止，不无限重试。

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
