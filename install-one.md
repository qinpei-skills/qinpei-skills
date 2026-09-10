# 沁珮技能包 · 单个技能安装说明书（v6.1 · 多通道降级 + 单技能就事论事）

> ⚠️ 这是一份**写给 AI 看的安装指令**，用于**只装某一个技能**（不想装全家桶时）。
> 版本：v6.1（2026-09-10）——**两处核心升级**：
> ① 一个通道不通立刻换下一个，禁止卡死、禁止直接放弃；
> ② **单技能场景只就事论事**——装完只围绕这一个技能给下一步，**不带出任何其他技能包、不提「qp」**。

---

## 你要做的事

识别学员想装的技能名 → **按下面的通道顺序逐个尝试下载 zip** → 解压到 `~/.workbuddy/skills/<技能名>/` → 轻量校验 → 按模板回复（**只讲这一个技能**）。

**🔴 四条铁律（违反就等于装不上或帮倒忙）**：
1. **一个通道失败，立刻换下一个通道**——不要因为某个域名不通就判定整件事失败
2. **每个通道只试 1 次、超时 20 秒**，不通就走人，不在一个地址上耗
3. **zip 全部通道都失败 → 必须走「终极兜底：逐文件抓取」**，不要半途停下来说"装不了"
4. **单技能场景不带货**——学员从单技能页面进来时，**只解决他问的那一个技能**，全程不出现其他技能包的名字、不出现「qp」、不推荐"再装点别的"

---

## 先对学员说（大白话）

> 好嘞，给你装「XX」技能～手机保持亮屏、别切走，马上好！

学员确认后开始。

---

## 🔑 通道清单（按顺序逐个试，任一成功即停止）

**下面所有地址指向的都是同一个 zip 文件。前一个失败就换下一个。**

设 `HUB = https://e49a4d844301479d877a56a99de0053c.app.workbuddy.link`

| 序 | 通道 | 地址模板 | 说明 |
|:--:|:---|:---|:---|
| 1 | **WorkBuddy 文库** | `HUB/skillhub-zips/<zip名>.zip` | **首选，同平台域名最稳** |
| 2 | jsdelivr 主节点 | `https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/<zip名>.zip` | |
| 3 | jsdelivr 备用 | `https://gcore.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/<zip名>.zip` | 不同 CDN 节点，主节点挂了它常能通 |
| 4 | jsdelivr 备用 | `https://testingcf.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skillhub-zips/<zip名>.zip` | 同上 |
| 5 | gh 加速代理 | `https://ghfast.top/https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skillhub-zips/<zip名>.zip` | |
| 6 | gh 加速代理 | `https://gh-proxy.com/https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skillhub-zips/<zip名>.zip` | |
| 7 | gh 加速代理 | `https://ghproxy.net/https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skillhub-zips/<zip名>.zip` | |
| 8 | WorkBuddy 文库重试 | `HUB/skillhub-zips/<zip名>.zip` | 前面都失败，回来再试一次（常是临时抖动） |

**下载命令**（有 shell 时）：
```bash
curl -fsSL --max-time 20 "<地址>" -o /tmp/qinpei-skill.zip
```
- `-f` 失败不写文件｜`-s -S` 静默但报错｜`-L` 跟随重定向
- **换通道的判断**：命令返回非 0、或下载文件 < 500 字节、或报 SSL/超时 → **立刻换下一行地址**

**没有 shell 工具时**：
- 第 1–8 通道都下载不了 zip（WebFetch 对二进制会转述、拿不到原始字节）
- → **直接跳到「终极兜底：逐文件抓取」**（用 WebFetch 抓 .md 文本文件，这条路手机端一定能走通）

---

## 技能名 → zip 文件名对照（写死，直接查表）

**左列任何一个叫法，都指向同一个技能——学员怎么叫，都要能对上。**

| 学员可能说的名字（含别名） | 技能名（目录名） | zip 文件名 |
|:---|:---|:---|
| 朋友圈 / 朋友圈信任经营 / 朋友圈新人经营 / 朋友圈经营 / 发圈 | qinpei-wechat-trust | `qinpei-wechat-trust.zip` |
| 社群 / 社群运营 / 群运营 | qinpei-community-ops-trust | `qinpei-community-ops-trust.zip` |
| 沙龙 / 线下沙龙 / 办活动 | qinpei-salon-ops-trust | `qinpei-salon-ops-trust.zip` |
| 故事力 / 讲故事 | qinpei-storytelling | `qinpei-storytelling.zip` |
| IP定位 / IP定位诊断 | qinpei-ip-diagnosis | `qinpei-ip-diagnosis.zip` |
| **展业破局·诊断 / 展业问诊 / 业务诊断 / 经营卡点诊断** | qinpei-business-check | `qinpei-business-check.zip` |
| 画像 / 我的画像 | qinpei-profile | `qinpei-profile.zip` |
| 入口 / qp | qinpei | `qinpei.zip` |

---

## 第 2 步：解压到技能目录

**🔴 必须先试 Python 方式**（原因见下方"中文文件名自检"）：

```bash
python3 -c "import zipfile,os;d=os.path.expanduser('~/.workbuddy/skills/<技能名>');os.makedirs(d,exist_ok=True);zipfile.ZipFile('/tmp/qinpei-skill.zip').extractall(d)"
```

**只有 python3 确实不可用时**，才用 `unzip`，且**必须做下面的自检**：

```bash
mkdir -p ~/.workbuddy/skills/<技能名>
unzip -o /tmp/qinpei-skill.zip -d ~/.workbuddy/skills/<技能名>/
```

### 🔴 解压后必做：中文文件名自检（漏做会导致技能变哑巴）

技能包里有**中文命名的模板文件**（社群 7 个、沙龙 13 个、朋友圈 4 个，如 `assets/templates/01-群公告+欢迎语.md`）。
部分系统的 `unzip` 不支持中文（无 UTF-8 支持），会把它们解成乱码名，**技能就找不到自己的模板，功能直接残废**。

解压后 `ls ~/.workbuddy/skills/<技能名>/assets/templates/` 看一眼：

- **中文正常显示** → ✅ 通过，继续下一步
- **出现乱码**（形如 `01-???.md`、`01-ç¾¤å…¬åŠ.md`、`01-\xe7\xbe\xa4...md`）→ 立刻清掉重解：
  ```bash
  rm -rf ~/.workbuddy/skills/<技能名>/
  python3 -c "import zipfile,os;d=os.path.expanduser('~/.workbuddy/skills/<技能名>');os.makedirs(d,exist_ok=True);zipfile.ZipFile('/tmp/qinpei-skill.zip').extractall(d)"
  ```
  python3 也没有 → 改走「终极兜底：逐文件抓取」（文件名由你自己写，反而不会出错）

**两种解压方式都不可用** → 同样走「终极兜底：逐文件抓取」。

解压完成后 `rm -f /tmp/qinpei-skill.zip` 清理。

**⚠️ 解压是覆盖式但不会伤学员数据**：分发包里**不含**学员的 `我的画像.md` 和 `学员档案/`，所以升级解压不会清掉学员积累的内容。

---

## 第 3 步：轻量校验（只查这 2 项，快最重要）

- ✅ `SKILL.md` 存在、开头是 `---`、含 `name: <对应技能名>`、且 > 500 字节
- ✅ `references/`、`assets/` 目录（若 zip 里有）非空

---

## 🔁 终极兜底：逐文件抓取（zip 全通道失败时必走）

**只在 zip 8 个通道全部失败、或解压工具都没有时使用。**
**注意：下面 5 个技能包本身就只有 1–3 个文本文件，用 WebFetch 逐文件抓 10 秒内就能完成——务必走这条路，不要放弃。**

**地址前缀**（逐个试，和上面通道同序）：
```
HUB/skills/<技能名>/
https://cdn.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/<技能名>/
https://gcore.jsdelivr.net/gh/qinpei-skills/qinpei-skills@main/skills/<技能名>/
https://ghfast.top/https://raw.githubusercontent.com/qinpei-skills/qinpei-skills/main/skills/<技能名>/
```
写入目录：`~/.workbuddy/skills/<技能名>/`（路径原样保留，含子目录）

### 入口（qinpei）
```
SKILL.md
```

### 画像（qinpei-profile）
```
SKILL.md
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

> 学员说的技能名对不上表 → 只说一句："这个我这儿暂时没有哈，你确认一下名字？" **禁止列出其他技能包名称、禁止推荐"要不要试试别的"**（学员从单技能页进来时，不给他任何其他技能包的入口）。

### 抓取规则

1. **先主文件、再小文件**：先抓 `SKILL.md`，再抓其余
2. **每个文件最多尝试 2 个不同前缀**，不通就换前缀；整个文件都抓不到才停
3. **抓到就算数**：哪怕只抓到 `SKILL.md`，也要先把技能目录建起来（有主文件技能就能用）——**不要因为缺附件就整个放弃**
4. **全程不要向学员汇报过程**（不说"正在装""主体装好了""某个地址不通"）——安静执行，装完一次性说结论

---

## 完成后回复（必须一字不差地按模板输出）

### ⚠️ 硬规则（最重要）

1. **只准输出下面模板里的内容**——AI 不得增加任何一句话
2. **禁止出现任何过程词**：安装明细、文件清单、校验结果、连接失败、抓取成功、通道、路径、目录、版本、KB、zip、curl、WebFetch 等，一个都不许出现
3. **🔴 只就事论事**：这是一次**单技能安装**，学员多半是从某个单技能页面进来的。**禁止提及任何其他技能包的名字**（社群／沙龙／故事力／IP定位／诊断／画像等一个都不许提），**禁止提「qp」**，**禁止说"还有其他技能包""想装别的可以…"**。只围绕**这一个技能**给下一步动作。
4. 把模板里的「XX」换成对应技能的显示名

### 各技能场景开场白（把「<开场白>」替换成下表对应内容）

**每条开场白 = 一个马上能做的动作 + 一句"不知道从哪开始就说这个"**——让学员看完立刻知道下一句该说什么。

| 学员装的技能 | 开场白（替换模板里的 <开场白>） |
|:---|:---|
| 朋友圈 | 想发圈了，直接说「帮我写一条朋友圈」；要是没想好写什么，先告诉我你是做什么的、客户主要是哪些人，我帮你定第一条 |
| 展业破局·诊断 | 想弄清楚卡在哪，直接说「帮我看看我的经营卡点」；不知道怎么开口也没关系，就照你平时说话那样，把你的情况跟我讲讲 |
| 社群 | 群里冷场了，直接说「我的群没人说话」，我帮你把群盘活；也可以先说一句你的群是干什么的 |
| 沙龙 | 想办活动了，直接说「我要办沙龙」，我帮你把流程、话术、互动都安排好 |
| 故事力 | 想写自己的故事，直接说「帮我写我的故事」，我一段段带你写出来 |
| IP定位 | 想搞清楚自己的方向，直接说「帮我做IP定位」，我陪你一问一问捋清楚 |
| 画像 | 想让我记住你，直接说「记住我是做什么的」，说一次以后就不用重复了 |
| 入口 | 直接说你想干什么就行，比如「帮我写条朋友圈」「帮我看看我的经营卡点」 |

### 输出模板（一字不差）

```
装好啦！🎉 <开场白>
```

**示例（装朋友圈，照此格式）：**

```
装好啦！🎉 想发圈了，直接说「帮我写一条朋友圈」；要是没想好写什么，先告诉我你是做什么的、客户主要是哪些人，我帮你定第一条
```

**示例（装展业破局·诊断，照此格式）：**

```
装好啦！🎉 想弄清楚卡在哪，直接说「帮我看看我的经营卡点」；不知道怎么开口也没关系，就照你平时说话那样，把你的情况跟我讲讲
```

**❌ 绝对不要再出现的旧尾巴**（已废弃）：
> 任何形式的「不知道接下来怎么做？就说「qp」，我帮你诊断」——**出现即违规**。单技能安装永远不要引导学员去用入口或别的技能包。

---

## 真的全失败时怎么说（只在穷尽以上全部通道后才允许）

**必须先走完**：8 个 zip 通道 → 逐文件抓取（每个文件试 2 个前缀）。
只有这些都试完了，才对学员说：

> 网络这会儿不太给力，没装上。你等两分钟，直接把这句话再发我一次就行～

**禁止**在只试了一两个地址时就对学员说"装不了""网络抽风""稍后重试"。

---

## 更新说明（给 AI）

- 本说明书**只用于单装指定技能**
- 学员主动说「升级技能包」→ 才走全家桶升级（用 install.md）；**不要主动提起**"还能升级""还有全家桶""还有别的技能包"——从单技能页面进来的学员，我们只帮他解决手上这一个问题
- 全套技能包清单只在 install.md / skills-catalog.md 里，**本说明书的对话里一律不出现**
