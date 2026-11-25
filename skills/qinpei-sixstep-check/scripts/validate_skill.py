#!/usr/bin/env python3
"""Static validation for qinpei-sixstep-check. No third-party dependencies."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
CRITERIA = (ROOT / "references/sixstep-criteria.md").read_text(encoding="utf-8")
TEMPLATE = (ROOT / "assets/templates/01-六步链路诊断简报.md").read_text(encoding="utf-8")

rings = ["拓客", "养客", "邀约", "成交", "养潜在伙伴", "赋能伙伴"]
checks = {
    "frontmatter_name": "name: qinpei-sixstep-check" in SKILL,
    "agent_created": "agent_created: true" in SKILL,
    "version_100": "version: 1.0.0" in SKILL,
    "prototype": "prototype: qinpei-business-check v3.1.0" in SKILL,
    "six_rings_in_skill": all(r in SKILL for r in rings),
    "three_states": all(s in SKILL and s in CRITERIA for s in ["立得住", "有点晃", "断了"]),
    "three_break_patterns": all(s in CRITERIA for s in ["只拓不养", "只养不约", "只成不带"]),
    "single_action": "一次只补一个动作" in SKILL,
    "earliest_source": "最靠前" in SKILL and "先修源头" in CRITERIA,
    "no_forced_pattern": "不硬套三种典型断法" in CRITERIA,
    "skill_mapping": all(s in CRITERIA for s in ["qinpei-wechat-trust", "qinpei-community-ops-trust", "qinpei-salon-ops-trust"]),
    "course3_fallback": "第 3 课" in CRITERIA and "不虚构" in CRITERIA,
    "one_signature": all(s in SKILL for s in ["👍 认可你", "🧭 说句实在话", "❓ 该你答了", "📖 给你参考", "👉 你现在做这件事"]),
    "history_append_only": "只追加，不覆盖" in SKILL,
    "partner_mode": "伙伴自己回答六问" in SKILL,
    "template_complete": all(s in TEMPLATE for s in ["断点环", "断法", "先补这一个动作", "建议技能包", "课后打卡", "给助教老师的跟进参考"]),
    "no_student_records": not any(p.name == "我的画像.md" or "学员档案" in p.parts for p in ROOT.rglob("*") if p.is_file()),
    "valid_utf8": all("�" not in p.read_text(encoding="utf-8") for p in ROOT.rglob("*.md")),
}

failed = [name for name, passed in checks.items() if not passed]
for name, passed in checks.items():
    print(("PASS" if passed else "FAIL"), name)
print("FILES", len([p for p in ROOT.rglob("*") if p.is_file()]))
if failed:
    print("VALIDATION_FAILED", ",".join(failed))
    sys.exit(1)
print("VALIDATION_OK")
