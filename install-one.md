# 沁珮技能包 · 单个技能安装说明书（v6 · 多通道自动降级）

> ⚠️ 这是一份**写给 AI 看的安装指令**，用于**只装某一个技能**（不想装全家桶时）。
> 版本：v6（2026-09-10）——**核心升级：一个通道不通立刻换下一个，禁止卡死、禁止直接放弃。**

---

## 你要做的事

识别学员想装的技能名 → **按下面的通道顺序逐个尝试下载 zip** → 解压到 `~/.workbuddy/skills/<技能名>/` → 轻量校验 → 按模板回复。

**🔴 三条铁律（违反就等于装不上）**：
1. **一个通道失败，立刻换下一个通道**——不要因为某个域名不通就判定整件事失败
2. **每个通道只试 1 次、超时 20 秒**，不通就走人，不在一个地址上耗
3. **zip 全部通道都失败 → 必须走「终极兜底：逐文件抓取」**，不要半途停下来说"装不了"

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
| 朋友圈 / 朋友圈信任经营 / 朋友圈经营 / 发圈 | qinpei-wechat-trust | `qinpei-wechat-trust.zip` |
| 社群 / 社群运营 / 群运营 | qinpei-community-ops-trust | `qinpei-community-ops-trust.zip` |
| 沙龙 / 线下沙龙 / 办活动 | qinpei-salon-ops-trust | `qinpei-salon-ops-trust.zip` |
| 故事力 / 讲故事 | qinpei-storytelling | `qinpei-storytelling.zip` |
| IP定位 / IP定位诊断 | qinpei-ip-diagnosis | `qinpei-ip-diagnosis.zip` |
| **展业破局·诊断 / 展业问诊 / 业务诊断 / 经营卡点诊断** | qinpei-business-check | `qinpei-business-check.zip` |
| 画像 / 我的画像 | qinpei-profile | `qinpei-profile.zip` |
| 入口 / qp | qinpei | `qinpei.zip` |

---

## 第 2 步：解压到技能目录

```bash
mkdir -p ~/.workbuddy/skills/<技能名>
unzip -o /tmp/qinpei-skill.zip -d ~/.workbuddy/skills/<技能名>/
```

**`unzip` 不可用时**改用 Python：
```bash
python3 -c "import zipfile,os;d=os.path.expanduser('~/.workbuddy/skills/<技能名>');os.makedirs(d,exist_ok=True);zipfile.ZipFile('/tmp/qinpei-skill.zip').extractall(d)"
```

**两种都不可用** → 走「终极兜底：逐文件抓取」。

然后 `rm -f /tmp/qinpei-skill.zip` 清理。

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

> 学员说的技能不在表里 → 告诉学员："这个还没开源，我帮你装现有的：朋友圈 / 社群 / 沙龙 / 故事力 / IP定位 / 展业破局·诊断 / 画像 / 入口"。

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

## 真的全失败时怎么说（只在穷尽以上全部通道后才允许）

**必须先走完**：8 个 zip 通道 → 逐文件抓取（每个文件试 2 个前缀）。
只有这些都试完了，才对学员说：

> 网络这会儿不太给力，没装上。你等两分钟，直接把这句话再发我一次就行～

**禁止**在只试了一两个地址时就对学员说"装不了""网络抽风""稍后重试"。

---

## 更新说明（给 AI）

- 学员说「升级技能包」→ 走全家桶升级，已装的都会更新（用 install.md）
- 本说明书只用于**单装指定技能**
