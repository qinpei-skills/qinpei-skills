> ⚠️ **当前开源状态（2026-08-05）**：本仓库目前仅开源 **「朋友圈信任经营」（qinpei-wechat-trust）** 一个技能。社群运营、故事力、课程研发、事业群带教、先学再用 共 5 个技能正在优化打磨中，暂未公开，后续版本逐步开源。
>
# 沁珮方法论技能包（qinpei-skills）

沁珮（经销商赋能方向）把常年使用的展业方法，蒸馏成一组可被 AI 一键调用的技能（Skill）。
本仓库**全部开源、免费**，任何人都能安装使用。

> 核心逻辑：**技能是方法，不是交付物。** 真正值钱的是「教你怎么用、陪你练、帮你批作业」的服务。
> 这些技能是钩子 —— 装上它，你就拿到了一套经过验证的展业方法论起点。

## 包含技能（6 个）

| 技能 | 作用 |
| --- | --- |
| `qinpei-wechat-trust` | 朋友圈信任经营：把朋友圈从卖货广告牌升级为信任银行 |
| `qinpei-community-ops-trust` | 社群运营提效：把微信群从广告死群升级为信任运营场 |
| `qinpei-storytelling` | 故事力：用「三问写故事」把经历变成信任经营的最短路径 |
| `qinpei-course-asset-workflow` | 课程研发工作流：从大纲到上架素材的标准 SOP |
| `qinpei-community-plan-gen` | 事业群带教方案生成：批量产出赛道带教方案 |
| `qinpei-knowledge-base` | 沁珮先学再用：强制学习知识库后再执行任务的纪律技能 |

## 安装方式

### 桌面端（有电脑 / 开发者）

```bash
npx -y skills add <你的GitHub用户名>/qinpei-skills -g --all
```

安装后技能会出现在 `~/.workbuddy/skills/`（WorkBuddy）或对应 Agent 的 skills 目录。

### 手机端（WorkBuddy 小程序）— 推荐

1. 打开 WorkBuddy 小程序 → 进入 **SkillHub**
2. 搜索本仓库的技能（或在会员群拿到 `unlisted` 专属安装链接）
3. 点「安装」即可，无需电脑

> 手机端安装依赖 WorkBuddy 官方的 SkillHub 通道，不依赖本仓库的 GitHub 地址。

### 通用：一句话指令安装（GitHub raw，手机/桌面都行）

不想走 SkillHub 时，也可以直接把本仓库的安装说明书地址发给 WorkBuddy，让它自己装：

```
根据 https://raw.githubusercontent.com/<你的GitHub用户名>/qinpei-skills/main/install.md 安装「沁珮方法论技能包」（可指定某个技能，如"朋友圈信任经营"）。
```

仓库根目录的 `install.md` 是一份写给 AI 的安装说明书，会自动把对应技能目录完整下载到 `~/.workbuddy/skills/`。

### 电脑端 / 手机端 双入口对照

| 人群 | 入口 | 口令（把 `<用户名>` 换成实际 GitHub 用户名） |
| --- | --- | --- |
| 电脑党（会用命令行） | `npx skills add` | `npx -y skills add <用户名>/qinpei-skills -g --all` |
| 手机党（无电脑学员） | GitHub raw 链接 | `根据 https://raw.githubusercontent.com/<用户名>/qinpei-skills/main/install.md 安装「沁珮方法论技能包」` |
| 手机党（官方通道） | SkillHub | 在 WorkBuddy 小程序 SkillHub 里搜 / 点安装 |

两条路指向同一个仓库，一份维护、两处生效。

## 更新与新增技能（持续养这套体系）

**核心机制：重跑安装 = 更新（覆盖式）。** 学员任何时候重新发一次安装口令，AI 就把仓库里当前最新的文件重新拉下来覆盖旧文件，自动就是最新版。无需你单独推包，也无需学员手动删旧版。

- **你迭代了某个 skill**：学员发「检查技能更新」→ AI 重拉覆盖 → 拿到新版
- **你写了新 skill**：在仓库 `CHANGELOG.md` 加一条记录 + 把技能目录加进 `skills/` → 学员发「有什么新技能」→ AI 读 CHANGELOG 列出 → 装
- **今年 / 明年的 365 学员**：全开源、仓库永久公开，任何时候买都指向同一个仓库，群发同一条口令即可
- **你的运营动作**：在会员群 / 公众号「喊一声」——「新增了 XX 技能 / XX 技能更新了，去更新一下」。学员回一句口令，AI 自己搞定

> 每次新增或迭代技能后，记得同步更新本仓库的 `CHANGELOG.md` 与 `skills/` 目录，并 `git push`，学员才能拿到。

## 关于「开源」与「版权」

- 本仓库所有技能以 **MIT 协议**开源，可自由使用、修改、再分发。
- 技能文件为纯文本，**任何人装到自己的设备后都能原样转发** —— 这是开源的天然属性，无法也无需阻止。
- 因此我们把护城河放在「方法 + 陪跑 + 批改」的服务里，而非文件本身。
- 公开版本已按规范**去除真实品牌名与学员个人数据**，仅保留方法论骨架。

## 目录结构

```
qinpei-skills/
├── .claude-plugin/
│   ├── marketplace.json     # 技能市场清单（每个技能可单独安装）
│   └── plugin.json          # 整仓插件清单（--all 全装）
├── skills/                  # 6 个技能，每个一个目录 + SKILL.md
├── skillhub-zips/           # 每个技能一个 ZIP，用于 SkillHub 上传
├── README.md
└── LICENSE
```

---

由沁珮与 WorkBuddy 共建 · 让好的展业方法，人人装得上。
