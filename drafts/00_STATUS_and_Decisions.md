# DRAFT PACKAGE — STATUS AND DECISIONS
## EPSRC Standard Grant: "Foundations of Monolithically Integrated Per-Slot Machine Drives for Reconfigurable Aerospace Propulsion"

*Index to the `drafts/` folder. Every remaining section of the application is drafted here in EPSRC Funding Service format, each already through an independent compliance-verification pass, a revision pass, a cross-section consistency check, and a primary-source cross-check against the uploaded papers, theses and viva. This file lists (1) the decisions only the PI can make, (2) corrections applied where the primary sources contradicted the handover, (3) known tensions left deliberately unresolved, and (4) the consolidated [PI TO CONFIRM] checklist.*

---

## 1. The files

| File | Section (separate Funding Service limits) | Variants |
|---|---|---|
| 01_Summary.md | Summary (550 w, plain English, public) | 3 — keyed to Vision openings A/B/C |
| 02_Vision.md | Vision (~2 of the 6 V&A pages) | Openings A/B/C are the one live decision; continuation is settled text |
| 03_Approach.md | Approach (~4 of the 6 V&A pages) | 2 variants each for *Hypotheses and objectives* and *Project management*; rest single |
| 04_Workplan_Gantt.md + gantt.html | +1 diagrammatic workplan page | Data tables + print-ready A4-landscape chart |
| 05_Capability_R4RI.md | Applicant & team capability (1,500 w, R4RI) | 2 — team-woven vs role-blocked |
| 06_References.md | References (1,000 w) + citation renumbering map | Single + Map A/B |
| 07_Resources_Justification.md | Resources & cost justification (1,000 w) | 2 — narrative-led vs table-led |
| 08_Ethics_RRI.md | Ethics & RRI (500 w) | 2 — AREA-framework vs theme-structured |
| 09_Partner_Contributions.md | Project partners (template table) | Prepared skeleton pending letters |
| 10_Facilities.md | Facilities (250 w) | 2 — minimal vs fuller N/A-style statement |

All word counts are stated at the end of each variant and verified within limits (Summary Variant 1 was trimmed to 549).

## 2. Decisions awaiting the PI (in priority order)

1. **Vision opening — A, B, C, or hybrid (A's reframe → C's mechanism sentence).** The master live decision. If C: trim the restating first sentences of *The Research Opportunity* per the integration note in 02.
2. **Summary variant (1/2/3).** Written to mirror openings A/B/C respectively, but any pairing works — the Summary carries no citation keys.
3. **Approach internal variants:** *Hypotheses and objectives* A (hypothesis-led H1–H5 + O1–O4) vs B (objective-led O1–O5); *Project management* A (milestone-gate) vs B (roles-and-cadence).
4. **Capability variant (A/B)** — plus: both variants order the Module-1 evidence silicon-first (A8, A6, A5, A7), deviating from the handover instruction to headline A5, A6, A8, A7. Retain or restore.
5. **Workplan skeleton sign-off.** All task codes, deliverables (Dn.k) and milestones (MS1–MS6) in 03/04/gantt.html are a drafting-team proposal.
6. **References:** (a) resolve the old-[4] thesis key — fold into [1,2] or insert the Nov 2025 thesis as an entry (confirmed details supplied in Map B); (b) select the IMD review — recommendation: Abebe et al., IET Electr. Power Appl., 2016 (canonical; best fit for the partition claim); (c) decide on the two candidate additions (hybrid-BTMLC stacking preprint — recommended, it strengthens the scaling argument; on-chip balancer preprint — optional).
7. **Resources / Ethics / Facilities variants** (lower stakes; structural choice only).

## 3. Corrections applied from primary sources (drafts deliberately deviate from the handover here)

1. **SkyDrive partner is "ARC Aerosystems", not "ARC Additive"** (master handover error; the SkyDrive Q7/Q9/Q12 documents name ARC Aerosystems throughout). Fixed in 03 and 05. [PI TO CONFIRM: exact company styling — the SkyDrive documents alternate between "ARC Aerosystems" and "ARC Aero Systems".]
2. **BTMLC paper is fully published:** IEEE Trans. Power Electron., vol. 41, no. 8, pp. 12842–12854, Aug. 2026 — no longer "accepted 2026". Updated in 05 and 06.
3. **TCAS-I 17× / 22–66× figures are post-layout and Monte Carlo simulation results, not silicon measurements** (silicon measurements independently confirm functionality: ~2 ns propagation at 3.3 V; programmable dead-time 25–200 ns). Capability text rephrased; do not present these as measured.
4. **The "~0.5% switching losses" figure does not appear in the published BTMLC text** — the paper says "negligible switching losses and dominant conduction losses" (modelled total 1.522 W at 2 A / 10 kHz). No draft quotes 0.5%; keep it out.
5. **The 50–66 °C chip-temperature range** was measured under loaded 5 kHz NLC operation (peak ~1.8 A), not an explicit continuous 2 A test. Phrase accordingly if quoted.
6. **The thesis underpinning the BTMLC is dated 25 November 2025** (not 2026): "On-Chip Power Conversion and Battery Balancing Circuits for Battery-Powered Applications," Faculty of Engineering Sciences, UCL. Its Chapter 12 lists verbatim "Experimental evaluation with various load types (e.g., inductive and motor loads)" as future work — now quoted in the Approach's Building-on-previous-work section as the positioning anchor.
7. **No published "Edwards IMD review" exists** (handover checklist item 10) — the transfer viva is unpublished and not citable. Three published candidates it relies on are listed in 06 (Residual check 3); Abebe et al. 2016 recommended.
8. **Doctoral-researcher destination sharpened:** "research fellow in high-frequency power electronics at Queen's University Belfast" (from the published author biography; name withheld per anonymisation rule).
9. **Eaton's SkyDrive role confirmed from the Q12 appendix:** non-funded Tier-1 adviser on certification, industrialisation readiness and system safety. The corresponding [PI TO CONFIRM] in 09 is resolved; the wording asserts no commitment to this proposal.
10. **Kolahian-thesis precision points** (if quoted): HB-MLI peak 99.46% at ~400 W (99.14% at the 1.2 kW maximum tested power); 46 °C recorded at an 800 W load under passive cooling.

## 4. Known tensions left for the PI (deliberately not "fixed")

1. **"5–50 kW per-motor class" in the Vision's Timeliness paragraph** does not match the §3 parameter table (5–15 kW demonstrator; 50–100 kW application narrative). The sentence is part of the settled, verbatim-locked §5b text, so it stands — but the PI should reconcile it when finalising.
2. **Page budget:** assembled Vision (~1,100 w) + Approach (~2,945 w) ≈ 5.8 pages at 700 words/page — inside 6 pages but with ~0.2 page headroom, and the Approach's three tables make the conversion optimistic. Expect a ~150-word trim at final assembly (resolving [PI TO CONFIRM] scaffolding will recover most of it).
3. **Uncited references:** entries [5], [6], [7], [8], [15], [16], [17] currently have no inline citation in the V&A drafts (Capability uses venue-naming, not keys, per R4RI practice). Every listed reference must be cited at least once — natural anchors are suggested in 06 Residual checks.
4. **Acronym expansion:** if opening A or B is chosen, "PD" and "IC" first appear unexpanded in the settled continuation — a minimal parenthetical insertion will be needed (noted in 02).
5. **Gantt font size:** the workplan page uses 7–9 pt labels. The Arial 11 pt rule governs the six prose pages; the diagrammatic page is standard practice at smaller sizes, but confirm the PI is comfortable.
6. **Citation renumbering is staged, not done:** inline keys in 02/03 keep their old numbering by design until the PI resolves the Map A/B ambiguities in 06; renumber immediately before export (master handover §9 critical warning).

## 5. Consolidated [PI TO CONFIRM] checklist

**Resolved by primary-source mining (no PI action needed beyond noting):**
- BTMLC final citation ✔ (item 1 partially); TCAS-I exact title ✔; both theses' titles/dates/department ✔; Eaton SkyDrive engagement ✔; IMD-review candidates identified ✔ (selection still needed); EP/T517793/1 acknowledgement confirmed in print ✔.

**Still open (from master handover §11 + new):**
1. Venue/year/DOI for A3 (NPC), A4 (equalizer), A5 (eVTOL — venue + institutions), A6 (flux-reversal — vol/issue/pages/DOI), A7 (thermal).
2. PD companion reference(s) [14]; hairpin winding reference(s) [17].
3. ATI edition (supports £3.2 bn by 2030); ADS edition (supports ~111,000 jobs).
4. Ordering of [1]–[3]; thesis insertion points; old-[4] resolution.
5. Renumber all inline keys once References is final (Map A/B in 06).
6. APL dynamometer envelope 6,000–10,000 RPM at 5–15 kW (confirmed NOT resolvable from the SkyDrive documents — no UCL dynamometer is described there).
7. Eaton / Airbus letters of support (gates 09 and the Vision's partner naming).
8. PI/Co-I community roles (R4RI Module 3); PI/Co-I FTE percentages (Resources).
9. IMD-review selection + full bibliographic details.
10. Hybrid-BTMLC and balancer preprints: hosting archive, DOI, peer-review status.
11. Exact styling of "ARC Aerosystems"; Co-I involvement in WP3; per-task lead split in WP2; project start date (for the Gantt calendar); DCAT acronym expansion.

## 6. Route to submission (per master handover §12)

1. PI makes the §2 decisions above (opening first).
2. Resolve remaining [PI TO CONFIRM] flags; drop resolved scaffolding text.
3. Renumber inline citations per 06 Map A/B; delete the map; re-verify the References word count.
4. Assemble Vision + Approach + Gantt page into one PDF (Arial 11, margins ≥ 2 cm, ≤ 8 MB), named "<application number> Vision and Approach"; type "attachment supplied" in the Funding Service text box.
5. Enter the separate sections (Summary, Capability, References, Resources, Ethics, Partners, Facilities) into their own Funding Service fields.
