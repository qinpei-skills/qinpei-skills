# 沁珮技能包清单（skills-catalog）

> 本文件是学员端安装/升级技能的**唯一数据源**，由沁珮维护。
> 新增技能 = 加一行；技能升级 = 改版本号。学员端一句「升级技能包」自动生效。
> 安装模式：`core` = 首次必装（小、秒装）；`on-demand` = 按需补装（学员用到时由入口自动装）。
> **安装方式（2026-09-10 v6 起）：优先下载 zip 一次解压**（1 个请求拿全部文件，最快）。
> ⚠️ **下载地址不固定**：8 条通道（WorkBuddy 文库 → jsdelivr 主/备用节点 → gh 加速代理）**按序自动降级，一个不通立刻换下一个**——完整通道清单见 `install.md` / `install-one.md`。zip 全通道都不通再走逐文件抓取（清单见 install-one.md「终极兜底」）。
> 格式：技能名 | 显示名 | 版本 | 安装模式 | zip 文件名

| 技能名 | 显示名 | 版本 | 安装模式 | zip 文件名 |
|:---|:---|:---:|:---:|:---|
| qinpei | 沁珮入口（引导+导航） | 1.5.0 | core | skillhub-zips/qinpei.zip |
| qinpei-profile | 共享画像银行 | 1.0.1 | core | skillhub-zips/qinpei-profile.zip |
| qinpei-wechat-trust | 朋友圈信任经营 | 2.3.1-student | on-demand | skillhub-zips/qinpei-wechat-trust.zip |
| qinpei-community-ops-trust | 社群运营提效 | 3.2.1 | on-demand | skillhub-zips/qinpei-community-ops-trust.zip |
| qinpei-salon-ops-trust | 线下沙龙信任经营 | 2.1.0 | on-demand | skillhub-zips/qinpei-salon-ops-trust.zip |
| qinpei-storytelling | 故事力提效 | 1.1.0 | on-demand | skillhub-zips/qinpei-storytelling.zip |
| qinpei-ip-diagnosis | 个人IP定位诊断 | 1.1.0 | on-demand | skillhub-zips/qinpei-ip-diagnosis.zip |
| qinpei-business-check | 展业破局·诊断 | 2.0.0 | on-demand | skillhub-zips/qinpei-business-check.zip |

---

## ⚠️ 关于「分发包」与「学员数据」的边界（重要）

zip 分发包里**只含技能本体**（SKILL.md / references / assets 模板 / README / 话术卡），
**不含**任何学员产生的数据文件：

- `我的画像.md`（学员画像）
- `学员档案/`（沙龙等活动档案、复盘数据、经验库）

→ 所以安装/升级时的覆盖解压**不会动到学员数据**。
→ AI 也**不要**额外做删除或清目录动作，不要用 `rm -rf` 删技能目录。

## 待同步清单（下一批）

以下两个包的电脑端版本高于开源版，本期未同步，留待下一批处理：

| 技能名 | 电脑端版本 | 开源版版本 | 差距 |
|:---|:---|:---|:---|
| qinpei-storytelling | 2.0.0 | 1.1.0 | 差 3 版 + 架构代差 |
| qinpei-ip-diagnosis | 2.0.1 | 1.1.0 | 差 4 版 + 架构代差 |
