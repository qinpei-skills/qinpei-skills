# 沁珮系列技能包 · 安装说明书（v5.0.0 · zip 极速版）

> ⚠️ 这是一份**写给 AI 看的安装指令**，不是给人读的文档。
> 当前版本：5.0.0（2026-09-10 改为 **zip 一次下载 + 解压**——每个技能 1 个压缩包，一次请求拿全部文件）

---

## 你要做的事

在用户设备上安装/升级「沁珮开源系列技能包」到 `~/.workbuddy/skills/`。
**首次安装只装核心包（很小，秒装）；大技能包按需补装（学员用到时由入口自动装）。**

---

## ⚠️ 先对学员说清楚（每次安装/升级前必说，大白话）

> 安装需要保持手机**亮屏、别切走、别接电话**，装完我会告诉你。
> 这次大概需要：**不到 1 分钟**（首次）或几十秒（升级），你准备好了跟我说一声，我就开始。

学员确认后，再开始下面的流程。

---

## ⚠️ 环境事实（决定走哪条通道）

**手机端沙箱网络实测**：

| 通道 | 状态 | 用途 |
|---|---|---|
| `raw.githubusercontent.com` GitHub 直连 | ❌ 被封（SSL 失败） | **不要用** |
| GitHub API | ❌ 被封 | **不要用** |
| **`cdn.jsdelivr.net` jsdelivr CDN** | ✅ **能直连！返回原始字节** | **首选** |
| WebFetch（AI 工具） | ✅ 能通但慢、可能转述/截断 | **备用兜底** |

**结论**：一律走 **jsdelivr CDN**（curl 直连下载原始字节，最快最稳）。

> jsdelivr 地址格式：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/<仓库内路径>`

---

## 🚀 核心方法：下载 zip + 解压（一次请求拿全部文件）

**每个技能打成一个 zip**（含 SKILL.md + references + 模板），一次请求搞定，比逐文件抓快得多。

### 技能名 ↔ zip 地址对照表（写死 · 直接查表）

| 技能名（目录名） | zip 地址 |
|:---|:---|
| qinpei | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei.zip` |
| qinpei-profile | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei-profile.zip` |
| qinpei-wechat-trust | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei-wechat-trust.zip` |
| qinpei-community-ops-trust | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei-community-ops-trust.zip` |
| qinpei-salon-ops-trust | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei-salon-ops-trust.zip` |
| qinpei-storytelling | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei-storytelling.zip` |
| qinpei-ip-diagnosis | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei-ip-diagnosis.zip` |
| qinpei-business-check | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/qinpei-business-check.zip` |

### 下载 + 解压（标准两步）

```bash
# ① 下载
curl -fsSL "<zip 地址>" -o /tmp/qinpei-skill.zip

# ② 解压（目录不存在会自动建）
mkdir -p ~/.workbuddy/skills/<技能名>
unzip -o /tmp/qinpei-skill.zip -d ~/.workbuddy/skills/<技能名>/
rm -f /tmp/qinpei-skill.zip
```

**`unzip` 不可用时**，改用 Python（沙箱一般都有 python3）：

```bash
python3 -c "import zipfile,os;d=os.path.expanduser('~/.workbuddy/skills/<技能名>');os.makedirs(d,exist_ok=True);zipfile.ZipFile('/tmp/qinpei-skill.zip').extractall(d)"
```

- URL 末尾若担心 CDN 缓存，可加 `?t=$(date +%s)` 强制回源。
- `curl -f` 失败不输出文件｜`-s` 静默｜`-S` 报错｜`-L` 跟随重定向。

### 兜底：逐文件抓取（仅当 zip 下载不到 / 解压工具都没有）

前缀：`https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/<技能名>/`
逐文件抓取清单见 **install-one.md 的「方案二」**（含每个技能的完整文件列表）。

jsdelivr 不通（HTTP 非 2xx）→ 改用 WebFetch 抓同一 URL（剥围栏后写入）。

### ⚠️ WebFetch 兜底三大坑

**坑 1：抓回内容可能包围栏** —— 返回常被包 ` ```markdown ... ``` `。写入前**必须剥掉最外层围栏**，否则 frontmatter 的 `---` 被破坏，技能失效。

**坑 2：可能截断/漏内容** —— 抓回后核对文件非空（> 500 字节）、开头是 `---`。

**坑 3：不反复重试** —— 每个文件最多 2 次（curl 1 次 + WebFetch 1 次），失败就停。

### ⚠️ 坑 4：jsdelivr 缓存

CDN 通常分钟级刷新，偶尔有旧缓存。绕过：URL 末尾加 `?t=<时间戳>`。

---

## 第一步：首次安装（只装这两个核心包）

⚠️ **本次只装以下两个技能，其他所有技能都不抓不装**：

| 技能名 | 保存位置 |
|:---|:---|
| `qinpei` | `~/.workbuddy/skills/qinpei/` |
| `qinpei-profile` | `~/.workbuddy/skills/qinpei-profile/` |

**这两个包很小（合计约 8KB），秒装。**

其他技能（朋友圈、社群、沙龙、故事力、IP定位、展业破局·诊断）都属于「按需补装」——**本次完全不抓不写**，由「沁珮入口」在学员实际要用时自动补装。

### 装完自检（防止 AI 错装）

用 `ls ~/.workbuddy/skills/` 确认：
- ✅ **应该存在**：`qinpei/`、`qinpei-profile/`
- ❌ **绝不应该存在**（除非学员之前装过）：`qinpei-wechat-trust/`、`qinpei-community-ops-trust/`

如果发现不该有的目录被本次创建 → 诚实告诉学员"刚才多装了 XX（不该装的），可以忽略"。

---

## 第二步：升级（学员说「升级技能包」时）

**升级 = 装过的都更新到最新版；没装过的按需包不装。**

### 1. 先列出本地已装的技能

用 `ls ~/.workbuddy/skills/`（或 Read 目录）**列出所有 `qinpei*` 目录**。

### 2. 只对已存在的目录，下载 zip 覆盖解压

对每个**已存在的** `qinpei*` 目录（在对照表里有 zip 地址的）：
- 下载对应 zip → 解压覆盖到原目录
- ⚠️ **不存在的 on-demand 目录直接跳过，不新装**（等学员用到时由入口补装）

> 直接覆盖解压即可，不做版本比对——zip 里永远是最新版，比"读版本+抓清单+比对"更快更可靠。

### 3. 补装缺失的知识文件

如果某技能目录里 `references/` 或 `assets/` 缺失或为空 → 重新下载该技能 zip 解压补齐（zip 已含全部文件）。

### 4. 抓取失败
跳过它、记下来，最后告诉学员"哪个没更新上，再说一次『升级技能包』重试"。**不要卡住整个流程。**

---

## ⚠️ 硬规则：保护学员自己的资料（不可违反）

学员的技能目录下可能有**学员自己产生的数据**：

- `我的画像.md`（学员的行业/人设/钩子）
- `学员档案/`（沙龙等活动记录、复盘数据、经验库）
- 其他学员自己命名并保存的文件

规则：
1. **绝对不要覆盖、不要删除、不要清空这些文件**
2. **不存在时不要替学员创建**（技能使用过程中 AI 会自动创建）
3. 分发包（zip）里**已经不含**这些学员数据文件，所以正常解压覆盖不会动到它们——但**不要额外做删除或清目录的动作**
4. 升级时**不要**使用 `rm -rf` 删整个技能目录

---

## 第三步：完成后怎么回复用户

**必须用大白话，禁止出现这些词**：目录、路径、命令行、CLI、仓库、zip、解压、终端、脚本、frontmatter、KB。

**① 首次安装（装好核心包）**
```
装好啦！🎉 不到一分钟搞定。

现在你可以直接跟我聊了。我不知道你最需要什么，先问你两件事：
1. 你是做什么行业的？（比如：艾灸养生 / 减脂 / 护肤 / 母婴 / 做代理招商…）
2. 你现在最头疼的是哪件事？
　① 朋友圈不知道怎么发，发了也没人看
　② 群建了没人说话，不知道咋运营
　③ 想先搞清楚自己该怎么做，还没想明白
　④ 别的（你说说看）

回个数字或者直接说就行～
```

**② 升级（已装过核心包）**
```
升级完成！✅ 都更新到最新版了。今天想干点啥？发朋友圈、管社群、还是先聊聊？
```

**③ 有失败**
```
大部分装好了，但 XX 没装上（网络没通）。
你再说一次「升级技能包」，我帮你重试它，其他不用管～
```

---

## 更新说明（给 AI）

- 学员说「安装技能包」「升级技能包」「更新技能包」「装最新版」→ **重跑本文件**，自动增量 + 升级
- 学员说「qp」或直接说需求（发朋友圈/运营社群等）→ 由「沁珮入口」处理，包括**按需补装对应技能包**
- 单装某一个技能 → 用 **install-one.md**
- 学员的画像/档案数据永远不动——这是底线
- 当前版本 5.0.0；技能清单数据以 `skills-catalog.md` 为准
