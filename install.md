# 沁珮方法论技能包 · 安装说明书

> **这是写给 AI 的安装说明书，不是给人看的。** 当用户说「安装 / 更新 / 检查更新 / 有什么新技能」时，请按本文档操作。


## 你的任务

用户想安装或更新沁珮（经销商赋能）的方法论技能包。请按以下步骤，把对应技能目录**完整下载并保存到本地技能目录**：


1. **定位技能目录**：用户技能根目录通常是 `~/.workbuddy/skills/`（macOS/Linux）或 `%USERPROFILE%\.workbuddy\skills\`（Windows）。找不到就先确认 WorkBuddy 是否已安装。
2. **下载文件**：本文档所在仓库的 raw 基址是 `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/`。每个技能的文件清单见下方，请逐个下载，**不要截断、不要摘要、不要改写**，原样保存。
3. **保存路径**：把每个技能目录整体保存到 `~/.workbuddy/skills/<技能文件夹名>/` 下（同名覆盖即可，这就是「更新」）。
4. **中文文件名**：若直接下载中文名文件失败，对文件名做 URL 编码后再试（文档已附编码版路径）。
5. **完成后**：用大白话告诉用户「已安装成功 / 已更新到最新，现在你可以对我说：'我要发朋友圈 / 做社群运营 / 写故事 / 研发课程'，我来帮你」。不要说「目录、路径、CLI、命令行」这类词。
6. **如实反馈**：任何文件下载失败，必须如实告知用户哪个没装上，不许假装装好。

## 更新模式（重要）

- 用户说「检查更新 / 装最新版 / 同步技能 / 更新技能包」时，**执行与首次安装完全相同的流程**（按下方清单重新拉取覆盖）。覆盖即更新，无需删除旧文件。
- 即使用户只装过部分技能，重跑本流程会补齐全部 6 个；若用户只想更新某一个，按下方清单只重拉那个技能目录即可。

## 查询新技能 / 更新记录

- 用户问「有什么新技能 / 最近更新了什么 / 新增了哪些」时，请先读取 `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/CHANGELOG.md`，把最近的新增与迭代用大白话念给用户。
- 若用户想装清单里提到的某个技能，引导他说「安装 XX 技能」，再按本文档执行。

## 可用技能清单（用户说「安装 XX」时匹配）

### qinpei-community-ops-trust  →  文件夹名 `qinpei-community-ops-trust`

| 远程路径（基址 + 相对路径） | 保存为 |
| --- | --- |
| `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-community-ops-trust/README.md` | `qinpei-community-ops-trust/README.md`  |
| `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-community-ops-trust/SKILL.md` | `qinpei-community-ops-trust/SKILL.md`  |
| `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-community-ops-trust/社群运营_快速上手话术卡.md` <br>编码版：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-community-ops-trust/%E7%A4%BE%E7%BE%A4%E8%BF%90%E8%90%A5_%E5%BF%AB%E9%80%9F%E4%B8%8A%E6%89%8B%E8%AF%9D%E6%9C%AF%E5%8D%A1.md` | `qinpei-community-ops-trust/社群运营_快速上手话术卡.md`  |

### qinpei-community-plan-gen  →  文件夹名 `qinpei-community-plan-gen`

| 远程路径（基址 + 相对路径） | 保存为 |
| --- | --- |
| `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-community-plan-gen/SKILL.md` | `qinpei-community-plan-gen/SKILL.md`  |
| `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-community-plan-gen/references/generate_plan.py` | `qinpei-community-plan-gen/references/generate_plan.py`  |

### qinpei-course-asset-workflow  →  文件夹名 `qinpei-course-asset-workflow`

| 远程路径（基址 + 相对路径） | 保存为 |
| --- | --- |
| `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-course-asset-workflow/SKILL.md` | `qinpei-course-asset-workflow/SKILL.md`  |
| `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-course-asset-workflow/references/asset-checklist.md` | `qinpei-course-asset-workflow/references/asset-checklist.md`  |
| `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-course-asset-workflow/references/visual-spec.md` | `qinpei-course-asset-workflow/references/visual-spec.md`  |

### 沁珮先学再用  →  文件夹名 `qinpei-knowledge-base`

| 远程路径（基址 + 相对路径） | 保存为 |
| --- | --- |
| `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-knowledge-base/SKILL.md` | `qinpei-knowledge-base/SKILL.md`  |

### qinpei-storytelling  →  文件夹名 `qinpei-storytelling`

| 远程路径（基址 + 相对路径） | 保存为 |
| --- | --- |
| `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-storytelling/SKILL.md` | `qinpei-storytelling/SKILL.md`  |

### qinpei-wechat-trust  →  文件夹名 `qinpei-wechat-trust`

| 远程路径（基址 + 相对路径） | 保存为 |
| --- | --- |
| `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-wechat-trust/SKILL.md` | `qinpei-wechat-trust/SKILL.md`  |
| `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-wechat-trust/安装使用指南.pdf` <br>编码版：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-wechat-trust/%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.pdf` | `qinpei-wechat-trust/安装使用指南.pdf`  |
| `https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-wechat-trust/我的画像.md` <br>编码版：`https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/qinpei-wechat-trust/%E6%88%91%E7%9A%84%E7%94%BB%E5%83%8F.md` | `qinpei-wechat-trust/我的画像.md` （空白模板，直接下载） |
