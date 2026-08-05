---
name: qinpei-community-plan-gen
audience: 自用版
category: 社群带教方案生成
version: 1.0.0
description: 基于 qinpei-community-ops-trust v2.0 社群方法论，批量生成多赛道「事业群带教方案」Word 文档（.docx）。当用户（沁珮）要为某大健康/分享经济赛道产出事业群带教/团队长训练场方案、或需要一次出多个赛道的带教方案时使用。
---

# 事业群带教方案生成器（多赛道批量 · Word 版）

## 触发场景
- "给[赛道]出个事业群带教方案" / "视康、艾灸、儿童喂养、40+体质调理各出一个"
- 需要把社群 skill 方法论落成可交付给学员的 Word 文档
- 批量产出多赛道方案，统一风格、统一去品牌（通用"团队长"版）

## 依赖环境
- Python 隔离环境（已装 python-docx）：
  `/Users/queen1015/.workbuddy/binaries/python/envs/default/bin/python3`
- 验证：`python3 -c "import docx; print(docx.__version__)"`

## 用法（两步）
1. 编辑 `references/generate_plan.py` 里的 `get_tracks()` 函数，增删赛道（每个 track 是一个参数字典，见下）。
2. 运行：
   ```bash
   /Users/queen1015/.workbuddy/binaries/python/envs/default/bin/python3 \
     /Users/queen1015/.workbuddy/skills/qinpei-community-plan-gen/references/generate_plan.py \
     /Users/queen1015/Desktop [赛道名...可选过滤]
   ```
   - 不传赛道名 = 生成全部 5 个；传 `减脂 视康` = 只生成这两个。
   - 输出：桌面 `<赛道>IP事业群带教方案.docx`。

## track 参数字典字段（必填）
| 字段 | 含义 |
|:---|:---|
| `name` | 短名，用于文件名/标题，如 `减脂` `视康` `艾灸` `儿童喂养` `40+体质调理` |
| `track` | 赛道全称，如 `减脂塑形/体重管理` |
| `awareness` | 养客阶段要建立的认知，如 `科学减脂认知` |
| `recruit` | 一对一招募钩子话术 |
| `dig` | 挖需求动作（自测/问卷） |
| `invite` | 私聊邀约话术 |
| `solution` | 给伙伴的组合方案（产品+服务，非单品） |
| `m2` / `m3` | 能力地图阶段2/3里程碑描述 |
| `week_ex` | 列表7项：周一到周日固定栏目的"内容示例" |
| `week_hook` | 列表7项：对应钩子+行动指令 |
| `p0` `p2` `p3` `p4` | 销售五步（养客/挖需求/邀客户/给方案）的话术或动作 |
| `examples` | 列表3项：{title, body, hook, action} 群内容示例 |
| `action1` | 本周行动清单第1条（从哪个群挑人） |

## 文档结构（固定 9 节，build 函数生成）
1. 群定位与目标（4 小目标 + 沁珮心法）
2. 带教全链路 5 步（招募→培训→实战带教→出单→表彰）
3. 主理人能力地图（4 阶段里程碑）
4. 事业群一周排期（套模板D，7 天带钩子+行动指令）
5. 发现潜在业务伙伴机制（KOC 培育+一对一钩子+信号清单）
6. 销售产品&解决方案带教（五步）
7. 群内容示例（3 条带四标签）
8. 合规底线（不夸大/不焦虑/建议咨询）
9. 本周行动清单

## 硬规则（来自用户级 MEMORY · 永久生效）
- **社群方案/排期/钩子资料默认出 Word（.docx）到桌面**，不用 .md；学员对 .md 不熟悉。
- 文档**不绑定任何品牌名**（某营养保健品牌等），统一用"团队长"通用版，方便任意品牌学员复用。
- 数字真实：不编造具体出单率/业绩数字，用方法论+区间+定性。
- 合规：不用"治愈/根除/最有效/第一"等绝对词，不制造焦虑，涉及诊断引导正规医生。
- 儿童健康喂养为赛道库外赛道，按同逻辑现场构建（已内置示例 track）。

## 注意事项
- 生成脚本临时写项目根再运行会污染技能包目录，故生成器脚本直接放在本 skill 的 `references/` 下，运行输出到桌面，干净可复用。
- 改赛道只改 `get_tracks()`，不要动 `build()` 渲染逻辑。
- 路径含中文/空格用引号包裹。
