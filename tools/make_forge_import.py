#!/usr/bin/env python3
"""Regenerate exports/FORGE_Import.md from the canonical drafts/ files.

Forge command contract, Command 1 ("export to GitHub for Forge"):
exchange-format blocks only (## PART: Section :: Part / ### VARIANT: CODE
[status] (source)), settled verbatim-locked text as [chosen] (handover),
drafted content as [candidate] (claude), skeletons as [draft], every
[PI TO CONFIRM] flag byte-identical, no commentary between blocks, no
preamble. Run from the repository root.
"""
import re

def read(p): return open(p, encoding='utf-8').read()

def section(text, start_pat, end_pats):
    m = re.search(start_pat, text, re.M)
    if not m: raise SystemExit(f"start not found: {start_pat}")
    rest = text[m.end():]
    end = len(rest)
    for ep in end_pats:
        m2 = re.search(ep, rest, re.M)
        if m2: end = min(end, m2.start())
    return rest[:end].strip()

blocks = []
def add(part, code, status, source, text):
    blocks.append(f"## PART: {part}\n### VARIANT: {code} [{status}] ({source})\n{text.strip()}\n")

H2 = r"^## "

# ---------- Vision ----------
v = read('drafts/02_Vision.md')
bg = section(v, r"^## Background and Research Challenge.*$", [H2])
for label, code in [("Option A", "VIS-OPEN-v1"), ("Option B", "VIS-OPEN-v2"), ("Option C", "VIS-OPEN-v3")]:
    m = re.search(r"\*\*" + label + r"[^\n]*\n\n(.*?)(?=\n\n\*\*Option |\n\n\*Hybrid note)", bg, re.S)
    lab = re.search(r"\*\*" + label + r"[^\n]*", bg).group(0)
    add("Vision :: Opening: stand beside the expert", code, "candidate", "claude", lab + "\n\n" + m.group(1))

ro = section(v, r"^## The Research Opportunity\s*$", [H2])
paras = [p for p in re.split(r"\n\s*\n", ro) if p.strip()]
add("Vision :: The unseen line", "VIS-LINE-v1", "chosen", "handover", paras[0])
add("Vision :: Crossing the line: the 50 V claim", "VIS-CROSS-v1", "chosen", "handover", paras[1])
add("Vision :: The cascade and its price", "VIS-CASC-v1", "chosen", "handover", "\n\n".join(paras[2:]))
add("Vision :: Novelty and scientific contribution", "VIS-NOV-v1", "chosen", "handover", section(v, r"^## Novelty and Scientific Contribution\s*$", [H2]))
add("Vision :: Timeliness: the ATI collision", "VIS-TIME-v1", "chosen", "handover", section(v, r"^## Timeliness\s*$", [H2]))
add("Vision :: National importance", "VIS-NATL-v1", "chosen", "handover", section(v, r"^## Impact and Beneficiaries\s*$", [H2]))
add("Vision :: Scope and funding rationale", "VIS-SCOPE-v1", "chosen", "handover", section(v, r"^## Scope and Funding Rationale\s*$", [H2]))

# Arc revision variants (candidate), if present
import os, glob
if os.path.exists('drafts/02_Vision_ArcRevision.md'):
    arc = read('drafts/02_Vision_ArcRevision.md')
    for m in re.finditer(r"^## PART: (.+?)\n### VARIANT: (\S+) \[(\w+)\] \((\w+)\)\n(.*?)(?=^## PART: |\Z)", arc, re.S | re.M):
        add(m.group(1).strip(), m.group(2), m.group(3), m.group(4), m.group(5))

# ---------- Approach ----------
a = read('drafts/03_Approach.md')
ho_intro = section(a, r"^## Hypotheses and objectives\s*$", [r"^### Variant A"])
ho_a = section(a, r"^### Variant A — hypothesis-led\s*$", [r"^### Variant B"])
ho_b = section(a, r"^### Variant B — objective-led\s*$", [H2])
add("Approach :: Hypotheses and objectives", "APP-HYPO-v1", "candidate", "claude", ho_intro + "\n\n**Variant A — hypothesis-led**\n\n" + ho_a)
add("Approach :: Hypotheses and objectives", "APP-HYPO-v2", "candidate", "claude", ho_intro + "\n\n**Variant B — objective-led**\n\n" + ho_b)
add("Approach :: Research design and methodology", "APP-RDM-v1", "candidate", "claude", section(a, r"^## Research design and methodology\s*$", [H2]))
add("Approach :: Work package structure and parallelism", "APP-WPS-v1", "candidate", "claude", section(a, r"^## Work packages\s*$", [r"^### WP1"]))
add("Approach :: WP1 (scope to confirm)", "APP-WP1-v1", "candidate", "claude", section(a, r"^### WP1 — Machine Electromagnetic Design.*$", [r"^### WP2"]))
add("Approach :: WP2: circuit in winding", "APP-WP2-v1", "candidate", "claude", section(a, r"^### WP2 — Per-Slot Circuit Module Architecture.*$", [r"^### WP3"]))
add("Approach :: WP3: coupled control", "APP-WP3-v1", "candidate", "claude", section(a, r"^### WP3 — Reconfigurable Field Control.*$", [r"^### WP4"]))
add("Approach :: WP4 (scope to confirm)", "APP-WP4-v1", "candidate", "claude", section(a, r"^### WP4 — Integrated Demonstrator.*$", [H2]))
add("Approach :: Building on previous work", "APP-PREV-v1", "candidate", "claude", section(a, r"^## Building on previous work\s*$", [H2]))
add("Approach :: APL facilities and equipment", "APP-APL-v1", "candidate", "claude", section(a, r"^## Research environment and facilities\s*$", [H2]))
add("Approach :: Risk register and mitigation", "APP-RISK-v1", "candidate", "claude", section(a, r"^## Feasibility and risk management\s*$", [H2]))
pm_intro = section(a, r"^## Project management and delivery\s*$", [r"^### Variant A"])
pm_a = section(a, r"^### Variant A — milestone-gate governance\s*$", [r"^### Variant B"])
pm_b = section(a, r"^### Variant B — roles and cadence\s*$", [H2])
add("Approach :: Management and partnership", "APP-MGMT-v1", "candidate", "claude", pm_intro + "\n\n**Variant A — milestone-gate governance**\n\n" + pm_a)
add("Approach :: Management and partnership", "APP-MGMT-v2", "candidate", "claude", pm_intro + "\n\n**Variant B — roles and cadence**\n\n" + pm_b)
add("Approach :: Maximising translation of outputs", "APP-TRAN-v1", "candidate", "claude", section(a, r"^## Maximising translation of outputs into outcomes and impact\s*$", [H2]))
add("Approach :: Gantt, milestones and deliverables", "APP-GANTT-v1", "candidate", "claude", section(a, r"^## Project plan\s*$", [H2]))

# ---------- Capability ----------
c = read('drafts/05_Capability_R4RI.md')
add("Applicant and Team Capability :: Full R4RI section draft", "CAP-FULL-v1", "candidate", "claude", section(c, r"^## Variant A - Team-woven\s*$", [r"^## Variant B"]))
add("Applicant and Team Capability :: Full R4RI section draft", "CAP-FULL-v2", "candidate", "claude", section(c, r"^## Variant B - Role-blocked\s*$", [r"^\Z"]))

# ---------- Resources ----------
r7 = read('drafts/07_Resources_Justification.md')
add("Resources and Cost Justification :: Full section draft", "RES-FULL-v1", "candidate", "claude", section(r7, r"^## VARIANT A — Narrative-led.*$", [r"^## VARIANT B"]))
add("Resources and Cost Justification :: Full section draft", "RES-FULL-v2", "candidate", "claude", section(r7, r"^## VARIANT B — Table-led.*$", [r"^\Z"]))

# ---------- Ethics ----------
e = read('drafts/08_Ethics_RRI.md')
add("Ethics and RRI :: Ethics and RRI statement", "ETH-RRI-v1", "candidate", "claude", section(e, r"^## VARIANT A — AREA framework\s*$", [r"^## VARIANT B"]))
add("Ethics and RRI :: Ethics and RRI statement", "ETH-RRI-v2", "candidate", "claude", section(e, r"^## VARIANT B — Thematic structure\s*$", [r"^\Z"]))

# ---------- Facilities ----------
f10 = read('drafts/10_Facilities.md')
add("Facilities :: Facilities statement", "FAC-FACS-v1", "candidate", "claude", section(f10, r"^## Variant A — Minimal statement\s*$", [r"^## Variant B"]))
add("Facilities :: Facilities statement", "FAC-FACS-v2", "candidate", "claude", section(f10, r"^## Variant B — Statement with capability summary\s*$", [r"^\Z"]))

# ---------- Partners ----------
p9 = read('drafts/09_Partner_Contributions.md')
add("Project Partners :: Partner contributions and letters", "PRT-LTRS-v1", "draft", "claude", re.sub(r"^# [^\n]*\n", "", p9).strip())

# ---------- References ----------
r6 = read('drafts/06_References.md')
add("References :: Reference list", "REF-LIST-v1", "candidate", "claude", section(r6, r"^## Part 1 — Reference list.*$", [r"^---$", r"^## Citation renumbering map"]))
add("References :: Citation renumbering map", "REF-MAP-v1", "candidate", "claude", "## Citation renumbering map\n\n" + section(r6, r"^## Citation renumbering map\s*$", [r"^\Z"]))

# ---------- Summary ----------
s1 = read('drafts/01_Summary.md')
for i, (pat, endp) in enumerate([(r"^## Variant 1 - The binding constraint\s*$", r"^## Variant 2"),
                                  (r"^## Variant 2 - The self-inflicted failure mode\s*$", r"^## Variant 3"),
                                  (r"^## Variant 3 - The impossible trade-off dissolved\s*$", r"^\Z")], 1):
    add("Summary :: Public summary (550 words)", f"SUM-PUB-v{i}", "candidate", "claude", section(s1, pat, [endp]))

out = "\n".join(blocks)
open('exports/FORGE_Import.md', 'w', encoding='utf-8').write(out)
print(f"{len(blocks)} blocks")
