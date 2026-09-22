<!-- ==================== VERSION-MANIFEST ====================
学员端「升级到最新版本」的比对源。格式：包名=版本（一行一个，勿改格式）
qinpei=1.5.4
qinpei-profile=1.1.4
qinpei-wechat-trust=2.3.7-student
qinpei-community-ops-trust=3.3.5
qinpei-salon-ops-trust=2.1.5
qinpei-storytelling=2.0.3
qinpei-ip-diagnosis=3.0.7
qinpei-business-check=3.0.5
==================== VERSION-MANIFEST END ==================== -->

# 沁珮技能包清单（skills-catalog）

> 本文件是学员端安装/升级技能的**唯一数据源**，由沁珮维护。
> 🔄 **升级流程的说明文档是 `upgrade.md`**（学员粘贴一条指令 → AI 读它 → 覆盖升级 + 写永久口令）；本节顶部的 VERSION-MANIFEST 就是它比对的版本真源。
> 新增技能 = 加一行；技能升级 = 改版本号。学员端一句「升级技能包」自动生效。
> 安装模式：`core` = 首次必装（小、秒装）；`on-demand` = 按需补装（学员用到时由入口自动装）。
> **安装方式（2026-09-10 v6 起）：优先下载 zip 一次解压**（1 个请求拿全部文件，最快）。
> ⚠️ **下载地址不固定**：8 条通道（WorkBuddy 文库 → jsdelivr 主/备用节点 → gh 加速代理）**按序自动降级，一个不通立刻换下一个**——完整通道清单见 `install.md` / `install-one.md`。zip 全通道都不通再走逐文件抓取（清单见 install-one.md「终极兜底」）。
> 格式：技能名 | 显示名 | 版本 | 安装模式 | zip 文件名

| 技能名 | 显示名 | 版本 | 安装模式 | zip 文件名 |
|:---|:---|:---:|:---:|:---|
| qinpei | 沁珮入口（引导+导航） | 1.5.4 | core | skillhub-zips/qinpei.zip |
| qinpei-profile | 共享画像银行 | 1.1.4 | core | skillhub-zips/qinpei-profile.zip |
| qinpei-wechat-trust | 朋友圈信任经营 | 2.3.7-student | on-demand | skillhub-zips/qinpei-wechat-trust.zip |
| qinpei-community-ops-trust | 社群运营提效 | 3.3.5 | on-demand | skillhub-zips/qinpei-community-ops-trust.zip |
| qinpei-salon-ops-trust | 线下沙龙信任经营 | 2.1.5 | on-demand | skillhub-zips/qinpei-salon-ops-trust.zip |
| qinpei-storytelling | 故事力提效 | 2.0.3 | on-demand | skillhub-zips/qinpei-storytelling.zip |
| qinpei-ip-diagnosis | 个人IP定位诊断 | 3.0.7 | on-demand | skillhub-zips/qinpei-ip-diagnosis.zip |
| qinpei-business-check | 展业诊断 | 3.0.5 | on-demand | skillhub-zips/qinpei-business-check.zip |

> ⚠️ **本表的「版本」= zip 分发包里 SKILL.md 的版本**（学员实际装到的版本），不是仓库源码版本。
> **2026-09-12 对账修正**：`qinpei-ip-diagnosis` 原写 `1.1.0` 系笔误，实际 zip 已是 **3.0.1**（09-11 已推成功）；`qinpei-storytelling` 仓库源码已是 **2.0.0** 但 zip 未重打，学员仍装到 1.1.0。

---

## ⚠️ 关于「分发包」与「学员数据」的边界（重要）

zip 分发包里**只含技能本体**（SKILL.md / references / assets 模板 / README / 话术卡），
**不含**任何学员产生的数据文件：

- `我的画像.md`（学员画像）
- `学员档案/`（沙龙等活动档案、复盘数据、经验库）

→ 所以安装/升级时的覆盖解压**不会动到学员数据**。
→ AI 也**不要**额外做删除或清目录动作，不要用 `rm -rf` 删技能目录。

## 待办清单（下一批 · 2026-09-12 重新核对后更新）

> ⚠️ **判据修正**：不能只看「仓库里 SKILL.md 的版本」就以为同步完了——**学员装的是 zip**。仓库源码更新 ≠ 分发包更新，**zip 必须重打**。下面按「源码是否已同步」和「zip 是否已重打」两栏分开记。

| 技能名 | 电脑端真源 | 仓库源码 | zip 分发包 | 状态 |
|:---|:---|:---|:---|:---|
| qinpei-wechat-trust | 2.3.7-student | ✅ | ✅ | ✅ 已完成（入口补强 + 一句话升级） |
| qinpei-business-check | 3.0.5 | ✅ | ✅ | ✅ 已完成（入口补强 + 单装独立 + 一句话升级） |
| qinpei-salon-ops-trust | 2.1.5 | ✅ | ✅ | ✅ 已完成（手工合并，剥离差异仍在） |
| qinpei-ip-diagnosis | 3.0.7 | ✅ | ✅ | ✅ 已完成（含一句话升级） |
| qinpei-community-ops-trust | 3.3.5 | ✅ | ✅ | ✅ 已完成（入口修复 + 画像路径 + 一句话升级） |
| qinpei-storytelling | 2.0.3 | 2.0.3 ✅ | ✅ 2.0.3 | ✅ 已完成（补一句话升级章节） |
| qinpei | 1.5.4 | 1.5.4 ✅ | ✅ 1.5.4 | ✅ 已完成（补一句话升级章节） |
| qinpei-profile | 1.1.4 | 1.1.4 ✅ | ✅ 1.1.4 | ✅ 已完成（补一句话升级章节） |

**核对方法（每次推之前跑一遍）**：取 `skills-catalog.md` 的版本列 → 与 `skillhub-zips/*.zip` 内 SKILL.md 的 version 逐一比对 → 再与电脑端真源比对。**两个都比，缺一个都不算同步。**
**🔴 判据铁律：仓库源码更新 ≠ 学员能装到新版。学员装的是 zip。zip 没重打 = 没更新。**

---

## 🔒 链接稳定性（2026-09-12 起）

**学员手里已发出去的 5 条安装页链接 + 文库链接，永远不需要重发**——更新内容只改文件字节，不动目录名与文件名，链接天然不变（已实操验证 3 次）。

🔴 **四条红线（动一条链接就废）**：
1. 不许改 `技能安装页/<目录>` 的目录名
2. 不许改 zip 文件名（别加版本号）
3. 不许改 `install-one.md` 的文件名
4. 不许把引用换成 `@tag` / `@sha`

**完整交接说明见**：`~/Desktop/手机端_链接不变只换内容_交接文档_20260912.md`
