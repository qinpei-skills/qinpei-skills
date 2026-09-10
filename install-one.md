# 沁珮技能包 · 单个技能安装说明书（v5 · zip 极速版）

> ⚠️ 这是一份**写给 AI 看的安装指令**，用于**只装某一个技能**（不想装全家桶时）。
> 学员说「安装 XX 技能」时用这份说明书。
> 版本：v5（2026-09-10 改为 **zip 一次下载 + 解压**，单包从"抓 8-17 个文件"变成"下载 1 个压缩包"）

---

## 你要做的事

识别学员想装的技能名 → 下载对应 **zip 压缩包** → 解压到 `~/.workbuddy/skills/<技能名>/` → 轻量校验 → 按模板回复。

**⚠️ 不要抓技能清单、不要解析任何表格、不要请求任何其他 URL。**

---

## 先对学员说（大白话）

> 好嘞，给你装「XX」技能～手机保持亮屏、别切走，马上好！

学员确认后开始。

---

## ⚠️ 环境事实（重要 · 决定走哪条通道）

**手机端沙箱的网络状况（已实测）**：

| 通道 | 状态 | 用途 |
|---|---|---|
| `raw.githubusercontent.com` GitHub 直连 | ❌ 被封（SSL 失败） | **不要用** |
| GitHub API (`api.github.com`) | ❌ 被封 | **不要用** |
| **`cdn.jsdelivr.net` CDN 镜像** | ✅ **能直连！返回原始字节** | **首选** |
| WebFetch（AI 工具） | ✅ 能通但慢、可能转述/截断 | **备用兜底** |

**结论**：一律走 **jsdelivr CDN**（curl/wget 直连下载原始字节，最快最稳）。

> jsdelivr 地址格式：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/<仓库内路径>`

---

## 🚀 方案一（首选 · 最快 · 一步到位）：下载 zip + 解压

**每个技能打成一个 zip，一次请求拿全部文件**（含 SKILL.md + references + 模板）。

### 第 1 步：下载 zip

技能名 → zip 地址对照（**写死，直接查表**）：

| 学员说的技能 | 技能名（目录名） | zip 地址 |
|:---|:---|:---|
| 朋友圈 | qinpei-wechat-trust | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei-wechat-trust.zip` |
| 社群 | qinpei-community-ops-trust | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei-community-ops-trust.zip` |
| 沙龙 | qinpei-salon-ops-trust | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei-salon-ops-trust.zip` |
| 故事力 | qinpei-storytelling | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei-storytelling.zip` |
| IP定位 | qinpei-ip-diagnosis | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei-ip-diagnosis.zip` |
| 展业破局·诊断 | qinpei-business-check | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei-business-check.zip` |
| 画像 | qinpei-profile | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei-profile.zip` |
| 入口 | qinpei | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei.zip` |

```bash
curl -fsSL "<zip 地址>" -o /tmp/qinpei-skill.zip
```

- URL 末尾若担心缓存，可加 `?t=$(date +%s)` 强制回源（jsdelivr 有缓存）。
- `-f` 失败不输出文件｜`-s` 静默｜`-S` 报错信息｜`-L` 跟随重定向。

### 第 2 步：解压到技能目录

```bash
mkdir -p ~/.workbuddy/skills/<技能名>
unzip -o /tmp/qinpei-skill.zip -d ~/.workbuddy/skills/<技能名>/
```

**`unzip` 不可用时**，改用 Python（沙箱一般都有 python3）：

```bash
python3 -c "import zipfile,os;d=os.path.expanduser('~/.workbuddy/skills/<技能名>');os.makedirs(d,exist_ok=True);zipfile.ZipFile('/tmp/qinpei-skill.zip').extractall(d)"
```

**两种都不可用** → 走方案二（逐文件抓取）。

### 第 3 步：清理

```bash
rm -f /tmp/qinpei-skill.zip
```

---

## 🔁 方案二（兜底）：逐文件抓取

**只在方案一失败时使用**（zip 下载不到 / 解压工具都没有）。

**所有地址 = 前缀 + 下表路径**，前缀为：

```
https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/<技能名>/
```

例（朋友圈 SKILL.md）：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/qinpei-wechat-trust/SKILL.md`

写入目录：`~/.workbuddy/skills/<技能名>/`（路径原样保留，含子目录）

### 朋友圈（qinpei-wechat-trust）
```
SKILL.md
references/domain-knowledge.md
references/acceptance.md
assets/templates/01-名片装修方案.md
assets/templates/02-朋友圈文案.md
assets/templates/03-一周发圈计划.md
assets/templates/04-钩子资料.md
```

### 社群（qinpei-community-ops-trust）
```
SKILL.md
README.md
社群运营_快速上手话术卡.md
references/acceptance.md
references/track-case-library.md
assets/templates/01-群公告+欢迎语.md
assets/templates/02-一周排期表.md
assets/templates/03-群诊断+洗群.md
assets/templates/04-群互动话题.md
assets/templates/05-事业群带教.md
assets/templates/06-群运营档案.md
```

### 沙龙（qinpei-salon-ops-trust）
```
SKILL.md
README.md
沙龙_快速上手话术卡.md
references/acceptance.md
references/faq.md
assets/templates/00-一页纸办沙龙.md
assets/templates/01-活动策划单.md
assets/templates/02-物料准备清单.md
assets/templates/03-邀约话术包.md
assets/templates/04-活动执行手册.md
assets/templates/05-活动分工表.md
assets/templates/06-跟进SOP.md
assets/templates/07-复盘模板.md
assets/templates/08-线上线下一体化.md
assets/templates/09-进阶工具包.md
assets/templates/10-全量文档使用说明.md
assets/templates/主题候选-选题引擎.md
```

### 故事力（qinpei-storytelling）
```
SKILL.md
README.md
话术卡.md
```

### IP定位（qinpei-ip-diagnosis）
```
SKILL.md
README.md
话术卡.md
```

### 展业破局·诊断（qinpei-business-check）
```
SKILL.md
README.md
话术卡.md
```

### 画像（qinpei-profile）
```
SKILL.md
```

### 入口（qinpei）
```
SKILL.md
```

> 学员说的技能不在表里 → 告诉学员"这个还没开源，我帮你装现有的：朋友圈/社群/沙龙/故事力/IP定位/展业破局·诊断/画像/入口"。

---

## 抓取规则（必须遵守）

1. **先主文件、再小文件**（兜底方案下）：先抓 `SKILL.md` 再抓其余
2. **全程不要向学员汇报过程**（不说"正在装""主体装好了""正在补小文件"）——**安静执行，装完一次性说结论**
3. **不反复重试**：方案一失败 → 换方案二；方案二下每个文件最多尝试 2 次（curl 1 次 + WebFetch 1 次），失败就停，不无限重试

### 轻量校验（只查这 2 项，不要逐章节核对——快最重要）

- ✅ `SKILL.md` 存在、开头是 `---`、含 `name: <对应技能名>`、> 500 字节
- ✅ `references/`、`assets/` 目录（若有）非空

**不完整怎么办**：重新抓一次；仍不完整 → 不硬写残缺文件，如实报告学员："网络不稳定没抓全，你稍后再说一次重试～"

---

## 完成后回复（必须一字不差地按模板输出）

### ⚠️ 硬规则（最重要）
1. **只准输出下面模板里的内容**——AI 不得增加任何一句话
2. **禁止出现任何过程词**：安装明细、文件清单、校验结果、连接失败、抓取成功、路径、目录、版本、KB、zip、curl、WebFetch 等，一个都不许出现
3. 把模板里的「XX」换成对应技能的显示名

### 各技能场景开场白（把「XX」替换成下表对应内容）

| 学员装的技能 | 开场白替换 |
|:---|:---|
| 沙龙 | 以后你要办活动，说「我要办沙龙」，我帮你把流程、话术、互动全安排好 |
| 朋友圈 | 说「我要发朋友圈」，我帮你写客户爱看的圈 |
| 社群 | 说「我的群没人说话」，我帮你把群盘活 |
| 故事力 | 说「帮我写我的故事」，我帮你把个人故事写出来 |
| IP定位 | 说「帮我做IP定位」，我帮你搞清自己的方向 |
| 展业破局·诊断 | 说「帮我看看我的经营卡点」，我帮你把经营卡点捋清楚 |
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

- 学员说「升级技能包」→ 走全家桶升级，已装的都会更新
- 本说明书只用于**单装指定技能**；装全家桶用 install.md
