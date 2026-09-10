# 沁珮系列技能包 · 安装说明书（v6.0.0 · 多通道自动降级）

> ⚠️ 这是一份**写给 AI 看的安装指令**，不是给人读的文档。
> 当前版本：6.0.0（2026-09-10）——**核心升级：8 条下载通道按序自动降级，一个不通立刻换下一个；zip 全挂还能逐文件抓，禁止卡死或半途放弃。**

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

## 🔑 通道清单（多通道自动降级 · 一个不通立刻换下一个）

**学员端网络环境不完全可控，某些域名可能被干扰（已实测出现"三条通道同时 SSL 断"）。**
**所以：不许只试一个地址就放弃 —— 按下面顺序逐个试，任一成功即停止。**

设 `HUB = https://e49a4d844301479d877a56a99de0053c.app.workbuddy.link`

| 序 | 通道 | 地址模板 | 说明 |
|:--:|:---|:---|:---|
| 1 | **WorkBuddy 文库** | `HUB/skillhub-zips/<技能名>.zip` | **首选，同平台域名最稳** |
| 2 | jsdelivr 主节点 | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/<技能名>.zip` | |
| 3 | jsdelivr 备用 | `https://gcore.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/<技能名>.zip` | 不同 CDN 节点，主节点挂了它常能通 |
| 4 | jsdelivr 备用 | `https://testingcf.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/<技能名>.zip` | 同上 |
| 5 | gh 加速代理 | `https://ghfast.top/https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skillhub-zips/<技能名>.zip` | |
| 6 | gh 加速代理 | `https://gh-proxy.com/https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skillhub-zips/<技能名>.zip` | |
| 7 | gh 加速代理 | `https://ghproxy.net/https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skillhub-zips/<技能名>.zip` | |
| 8 | WorkBuddy 文库重试 | `HUB/skillhub-zips/<技能名>.zip` | 前面都失败，回来再试一次（常是临时抖动） |

**铁律**：
1. **一个通道失败立刻换下一个**，不要因为某个域名不通就判定整件事失败
2. **每个通道只试 1 次、超时 20 秒**（`curl --max-time 20`）
3. 判定"这个通道失败"：命令返回非 0 / 下载文件 < 500 字节 / 报 SSL 或超时
4. **zip 全通道都失败 → 走「兜底：逐文件抓取」**（见下），不要半途停下来说装不了

**没有 shell 工具时**：8 个 zip 通道都下载不了 zip（WebFetch 对二进制只会转述）→ **直接走逐文件抓取**（用 WebFetch 抓 .md 文本，手机端一定能走通）。

---

## 🚀 核心方法：下载 zip + 解压（一次请求拿全部文件）

**每个技能打成一个 zip**（含 SKILL.md + references + 模板），一次请求搞定，比逐文件抓快得多。

### 技能名 ↔ zip 文件名对照表（写死 · 直接查表）

| 技能名（目录名） | zip 文件名 |
|:---|:---|
| qinpei | `qinpei.zip` |
| qinpei-profile | `qinpei-profile.zip` |
| qinpei-wechat-trust | `qinpei-wechat-trust.zip` |
| qinpei-community-ops-trust | `qinpei-community-ops-trust.zip` |
| qinpei-salon-ops-trust | `qinpei-salon-ops-trust.zip` |
| qinpei-storytelling | `qinpei-storytelling.zip` |
| qinpei-ip-diagnosis | `qinpei-ip-diagnosis.zip` |
| qinpei-business-check | `qinpei-business-check.zip` |

> 完整下载地址 = 上面「通道清单」里的地址模板，把 `<技能名>` 换成上表的技能名。

### 下载 + 解压（标准两步）

```bash
# ① 下载（把 <地址> 换成通道清单里的第 1 个；失败就换第 2、3…个）
curl -fsSL --max-time 20 "<地址>" -o /tmp/qinpei-skill.zip

# ② 解压 —— 🔴 优先用 Python（原因见下方自检）
python3 -c "import zipfile,os;d=os.path.expanduser('~/.workbuddy/skills/<技能名>');os.makedirs(d,exist_ok=True);zipfile.ZipFile('/tmp/qinpei-skill.zip').extractall(d)"
rm -f /tmp/qinpei-skill.zip
```

**只有 python3 确实不可用时**，才用 `unzip`：

```bash
mkdir -p ~/.workbuddy/skills/<技能名>
unzip -o /tmp/qinpei-skill.zip -d ~/.workbuddy/skills/<技能名>/
```

### 🔴 解压后必做：中文文件名自检（漏做会导致技能变哑巴）

技能包里有**中文命名的模板文件**（社群 7 个、沙龙 13 个、朋友圈 4 个，如 `assets/templates/01-群公告+欢迎语.md`）。
部分系统的 `unzip` 不支持中文，会把它们解成乱码名，**技能就找不到自己的模板，功能直接残废**。

解压后 `ls ~/.workbuddy/skills/<技能名>/assets/templates/` 看一眼：

- **中文正常显示** → ✅ 继续下一步
- **出现乱码**（形如 `01-???.md`、`01-ç¾¤å…¬å'Š.md`）→ 清掉重解：
  ```bash
  rm -rf ~/.workbuddy/skills/<技能名>/
  python3 -c "import zipfile,os;d=os.path.expanduser('~/.workbuddy/skills/<技能名>');os.makedirs(d,exist_ok=True);zipfile.ZipFile('/tmp/qinpei-skill.zip').extractall(d)"
  ```
  python3 也没有 → 改走「兜底：逐文件抓取」（文件名由你自己写，反而不会错）

- ⚠️ **下载失败不要停**：换通道清单里的下一个地址继续，8 个都试完才走逐文件抓取
- `curl -f` 失败不输出文件｜`-s` 静默｜`-S` 报错｜`-L` 跟随重定向｜`--max-time 20` 防卡死

### 兜底：逐文件抓取（仅当 zip 全通道失败 / 解压工具都没有）

**前缀按同样顺序试**：
```
HUB/skills/<技能名>/
https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/<技能名>/
https://gcore.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/<技能名>/
https://ghfast.top/https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/<技能名>/
```
逐文件抓取清单见 **install-one.md 的「终极兜底」**（含每个技能的完整文件列表）。

某个前缀不通 → 换下一个前缀；仍不通 → 改用 WebFetch 抓同一 URL（剥围栏后写入）。
**抓到 SKILL.md 就先建起技能目录**——不要因为缺附件整个放弃。

### ⚠️ WebFetch 兜底三大坑

**坑 1：抓回内容可能包围栏** —— 返回常被包 ` ```markdown ... ``` `。写入前**必须剥掉最外层围栏**，否则 frontmatter 的 `---` 被破坏，技能失效。

**坑 2：可能截断/漏内容** —— 抓回后核对文件非空（> 500 字节）、开头是 `---`。

**坑 3：不反复重试** —— 每个文件最多 2 次（curl 1 次 + WebFetch 1 次），失败就停。

### ⚠️ 坑 4：CDN 缓存

jsdelivr 有缓存，偶尔返回旧版。绕过：URL 末尾加 `?t=<时间戳>`。
**但不用为此担心**：通道 1（WorkBuddy 文库）是我们自己发布的，每次更新同步即时生效；且它排在最前面，正常情况走的就是它。

### ⚠️ 坑 5：学员端网络有多张网

不同学员的运营商/WiFi 不一样，**同一个域名有人通有人不通**。
已实测出现过「jsdelivr + GitHub raw + GitHub API 三条全断（SSL 握手直接断）」。
**这就是为什么要按 8 条通道逐个试**——一条断了换下一条，不要下"网络抽风、稍后重试"的结论。

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
- 当前版本 6.0.0；技能清单数据以 `skills-catalog.md` 为准
