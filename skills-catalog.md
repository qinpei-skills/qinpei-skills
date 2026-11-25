<!-- ==================== VERSION-MANIFEST ====================
学员端「升级到最新版本」的比对源。格式：包名=版本（一行一个，勿改格式）
qinpei=1.12.1
qinpei-profile=1.4.0
qinpei-wechat-trust=2.6.0
qinpei-community-ops-trust=3.5.0
qinpei-salon-ops-trust=2.3.0
qinpei-storytelling=2.3.0
qinpei-ip-diagnosis=5.0.1
qinpei-business-check=3.1.0
qinpei-video-trust=1.0.1
qinpei-1v1-sales=1.2.0
qinpei-sixstep-check=1.0.3
==================== VERSION-MANIFEST END ==================== -->

# 沁珮技能包清单（skills-catalog）

> **当前安装口径**：新学员统一从 WorkBuddy 技能中心 / SkillHub 安装，发布者为 `indiv-qinpei`。
> GitHub 保存公开源码和同名 zip 镜像，既有文件路径不变，供历史安装链路与开源使用。
> 顶部 VERSION-MANIFEST 是仓库内版本比对源；每次发布必须同时核对技能源码、zip 内版本和本表。

| 技能名 | 显示名 | 版本 | 安装模式 | zip 文件名 |
|:---|:---|:---:|:---:|:---|
| qinpei | QP展业管家 | 1.12.1 | core | skillhub-zips/qinpei.zip |
| qinpei-profile | 共享画像银行 | 1.4.0 | core | skillhub-zips/qinpei-profile.zip |
| qinpei-wechat-trust | 朋友圈信任经营 | 2.6.0 | on-demand | skillhub-zips/qinpei-wechat-trust.zip |
| qinpei-community-ops-trust | 社群运营提效 | 3.5.0 | on-demand | skillhub-zips/qinpei-community-ops-trust.zip |
| qinpei-salon-ops-trust | 线下沙龙信任经营 | 2.3.0 | on-demand | skillhub-zips/qinpei-salon-ops-trust.zip |
| qinpei-storytelling | 故事力提效 | 2.3.0 | on-demand | skillhub-zips/qinpei-storytelling.zip |
| qinpei-ip-diagnosis | 差异化业务定位诊断 | 5.0.1 | on-demand | skillhub-zips/qinpei-ip-diagnosis.zip |
| qinpei-business-check | 展业诊断 | 3.1.0 | on-demand | skillhub-zips/qinpei-business-check.zip |
| qinpei-video-trust | 口播视频AI搭子 | 1.0.1 | on-demand | skillhub-zips/qinpei-video-trust.zip |
| qinpei-1v1-sales | 一对一顾问式销售 | 1.2.0 | on-demand | skillhub-zips/qinpei-1v1-sales.zip |
| qinpei-sixstep-check | 六步展业链路诊断 | 1.0.3 | on-demand | skillhub-zips/qinpei-sixstep-check.zip |

## 2026-11-25 同步验收

| 范围 | 结果 |
|:---|:---|
| SkillHub 最新 10 包源码 | 已与桌面 SkillHub 终包逐一同步 |
| SkillHub 最新 10 个 zip | 已按原文件名同步，字节不变 |
| 新增到 GitHub 主分支 | 一对一顾问式销售、六步展业链路诊断、口播视频AI搭子 |
| 原有展业诊断 | 保留 3.1.0，不覆盖、不删除 |
| 版本清单与首页 | 已更新为同一组版本号 |
| 学员数据 | 不包含我的画像、学员档案或私有凭证 |

## 分发包与学员数据边界

zip 只含技能本体及公开模板，不含学员在使用过程中产生的：

- `我的画像.md`
- `学员档案/`
- 学员自行创建的其他资料

安装或升级不得额外删除、清空学员目录。源码与 zip 必须同时更新；只更新其中一个，不算同步完成。

## 链接稳定性

1. 不改技能目录名。
2. 不改 zip 文件名，不在文件名中追加版本号。
3. 不把既有引用改成固定 tag 或 commit SHA。
4. 新安装引导以 SkillHub 为准；历史 GitHub 路径只更新内容，不随意改名。
