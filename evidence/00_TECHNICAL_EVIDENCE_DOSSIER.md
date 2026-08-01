# TECHNICAL EVIDENCE DOSSIER — MASTER INDEX
## EPSRC Standard Grant: "Foundations of Monolithically Integrated Per-Slot Machine Drives for Reconfigurable Aerospace Propulsion"

*Complete page-by-page technical extraction of every source document in the repository, prepared 1 August 2026. Eight digests, ~34,000 words, every number carrying a page or line locator to its source. Use this dossier as the knowledge base for any drafting environment: nothing in the proposal should assert a technical fact that cannot be traced to a locator in these digests. Author names appear freely here (this is an internal working dossier); the anonymisation rule applies only to proposal text.*

---

## The digests

| File | Source | Words | What it holds |
|---|---|---|---|
| 01_BTMLC_TPEL_paper_digest.md | BTMLC IC paper, IEEE TPEL 41(8):12842–12854, Aug. 2026 | ~4,100 | All 13 pages: topology laws (switch count, blocking voltage, switching frequency), every measured number with condition and page (15.2 mm², 0.472 Ω, 1.522 W modelled vs ~1.88 W measured, 2 A/26 V/52 W, DC–5 kHz, 50–66 °C, 50 ns overshoot, 128-tap ≈ 400 V scaling), 10 exact quotes, limitations, WP/RQ map |
| 02_TCASI_level_shifters_digest.md | Level-shifter paper, IEEE TCAS-I, Early Access 2026 | ~3,000 | All 14 pages incl. visually-read tables; every result tagged [SIM] (17× delay, 22–66× dead-time-spread, Monte Carlo) or [MEAS] (~2 ns continuous-LS delays at 3.3 V, 25–200 ns programmable dead-time, 2–4.3 V range); a Table III/IV area discrepancy flagged |
| 03_Farhat_thesis_digest.md | Farhat PhD thesis, UCL, 25 Nov 2025 (all 12,162 lines) | ~5,000 | Four silicon prototypes (3.4/4.68/15.2/20.52 mm², 130 nm BCD); the IC-necessity argument quoted verbatim with line numbers; Ch. 11 limits (25–30 V/6 A/resistive-only); Ch. 12 future work verbatim (motor loads, full AC, 12–16 modules → 300–400 V); bootstrap/motor-PWM incompatibility; stacked 50 V/6 A/98.5%/60–85 mΩ; EP/T517793/1 acknowledgement |
| 04_Tazehkand_thesis_digest.md | Tazehkand PhD thesis, UCL, Apr. 2026 (234 pp) | ~5,800 | The UPU concept defined as printed (pp. 34–36); on-chip transformer digital isolation (AM to ~1.5 MHz, PM ~418 kHz, ~40 ns transitions); silicon-validated 5-level CHB/4-level MMC/isolated half-bridges; integration-boundary principle; CS2CAB balancing 37 s vs 330–750 s prior art; the UPU-to-per-slot conceptual bridge with the thesis's own extension warrant (pp. 3, 218) |
| 05_Kolahian_thesis_digest.md | Kolahian PhD thesis, UCL, Feb. 2026 (226 pp) | ~4,200 | THE motor-drive validation in full depth: 40 W/240 V machine at 489.3 rpm and the 4 kW-rated 400 V industrial machine, back-to-back bench, 150–500 rpm under cascaded dq0 + third-harmonic injection at 120 V peak phase, 6 A supply-limit diagnosis, back-EMF quote (p. 174); HB-MLI 99.46% peak (~400 W)/99.14% (1.2 kW)/46 °C at 800 W passive; MS² 98%/98.8%/450 W/47 °C/167 nH; MFWE 98.937%; 52 planar prototypes; two internal inconsistencies flagged |
| 06_Edwards_transfer_viva_digest.md | Edwards MPhil→DPhil transfer report, UCL, May 2026 — NOT CITABLE | ~4,300 | Full IMD taxonomy with real examples; every quantified claim WITH provenance and age (Lee 2018 10–20%/30–40%; Wheeler 2005 40%-capacitor; Bartos 2000 7.5 kW barrier; uncited "30%+ efficiency"); Table 3.1 wiring study and Table 3.3 36-level DCAT design reproduced; all report defects catalogued; 44-source citable-substitute inventory; 11 claims that must never be sourced to this report |
| 07_2026_preprints_digest.md | Hybrid-stacked BTMLC preprint (Mar. 2026) + on-chip balancer preprint (Mar. 2026) | ~4,000 | Stacked-module results (16-level ~49.5 V half-sine at up to 6 A, 98.5% peak, 60–85 mΩ); both preprints print the EP/T517793/1 + Project Ref 2600345 acknowledgement and the "based on a chapter of the author's 2025 UCL PhD thesis" statement — a citable four-output EPSRC lineage; neither carries a DOI (cite by title/date/hosting); machine-load applicability asserted but demonstrations are resistive-only |
| 08_SkyDrive_appendices_digest.md | SkyDrive Q7/Q9/Q12/Q13/Q10 appendices — CONTEXT ONLY | ~3,600 | Every market figure with its (mostly absent) stated source; Pegasus III → Linx P9 phasing; customer-pull companies; Q12 WP structure and verbatim Eaton "non-funded Tier-1 adviser" wording; full 55-risk register with L×I scores; explicit note that UCL APL facilities appear NOWHERE in the SkyDrive documents; internal inconsistencies catalogued |

## The evidence chains (claim → sources)

**1. "The complete per-slot drive fits on one chip" (feasibility of integration).** BTMLC paper (01): switches, gate drivers, level shifters, dead-time, Zener floating supplies on 15.2 mm²/130 nm BCD, silicon-measured. Farhat thesis (03): the four-prototype progression and scaling tables behind it. Preprints (07): the platform stacks — two ICs + off-chip half-bridge reach 16 levels/~49.5 V/6 A at 98.5%.

**2. "Discrete implementation is physically unrealisable — IC integration is necessary."** Farhat thesis (03) quoted verbatim at ll. 2355–2359, 3328–3343, 4819–4828 (prohibitive complexity, unscalable gate-drive/isolation infrastructure, discrete-device unsuitability); the bootstrap-incompatibility-with-motor-PWM argument at ll. 4200–4207 strengthens the machine-drive case specifically.

**3. "The binary-tree family already drives real machines with back-EMF" (the WP2 precedent).** Kolahian thesis (05): both machine benches with full conditions and locators. This is the single strongest feasibility datum; quote its conditions exactly, never inflate (150–500 rpm, cascaded dq0 + THI, 120 V peak phase, supply-limited at 6 A).

**4. "Floating-domain control signalling is solved in this process."** TCAS-I paper (02) with the [SIM]/[MEAS] provenance discipline; Tazehkand thesis (04) for the on-chip transformer digital isolation (AM ~1.5 MHz, ~40 ns).

**5. "Magnetic voltage distribution at >99% efficiency" (the DCAT principle).** Handover-carried DCAT 2016 facts, corroborated by Kolahian (05) MS² operating in DCAT mode at 98.8%.

**6. "Distributing conversion to the point of consumption is a validated design philosophy."** Tazehkand thesis (04): the UPU definition and its printed warrant for extension beyond batteries — the Vision's conceptual bridge.

**7. "IMD shortens the partition; per-slot dissolves it" (differentiation).** Edwards viva (06) maps the IMD landscape and supplies the citable substitutes (Abebe 2016; Lee 2018; Jahns & Sarlioglu 2020 — full details verified in drafts/06_References.md). Never cite the viva itself.

**8. SkyDrive as translation context.** Digest 08 under the context-only rule: partner roles verbatim, no research-target numbers.

## Corrections registry (facts the dossier changed)

1. BTMLC paper is fully published (TPEL 41(8):12842–12854, Aug. 2026), not "accepted".
2. TCAS-I 17×/22–66× figures are post-layout/Monte Carlo simulation; silicon measurements are the ~2 ns delays, 25–200 ns dead-time, 2–4.3 V range.
3. Farhat thesis is dated 25 November 2025 (cite 2025).
4. The "0.5% switching losses" figure is not in the BTMLC text (paper says "negligible"; modelled total 1.522 W at 2 A/10 kHz).
5. The 50–66 °C chip range was measured under loaded 5 kHz NLC (peak ~1.8 A), not continuous 2 A.
6. The drafted PD anchor citation was wrong (DOI belonged to an unrelated paper); genuine anchor: Lusuardi et al., IEEE Access 9:27485–27495, 2021; companion: Meyer et al., TDEI 25(3):873–882, 2018.
7. The "200–300 V PD inception at quarter-atmosphere" claim is unsupported; literature supports PDIV roughly halving to ~350–500 V peak at cruise with a pressure-independent ~330 V Paschen floor — the re-derived margin is stronger. [PI TO CONFIRM: sweep]
8. "£3.2 bn UK AAM by 2030" unsupported; verified substitutes PwC 2023 (£2.1 bn annual by 2040) or DfT 2024 (£45 bn by 2030, whole drone/eVTOL economy). "111,000 jobs" is ADS 2019; current verified ~104,000 (ADS Outlook 2024).
9. SkyDrive partner is ARC Aerosystems (not "ARC Additive"); Eaton's role verbatim: non-funded Tier-1 adviser on certification, industrialisation readiness and system safety.
10. No published "Edwards IMD review" exists; the viva is not citable.

## How to use this dossier in a new Claude page

Upload `exports/EVIDENCE_Dossier_Bundle.md` (this index + all eight digests in one file) as project knowledge, alongside `NEW_SESSION_Handover.md` and `EPSRC_Master_Handover.md`. Standing rule for any assistant using it: every technical assertion in drafted text must trace to a locator in these digests or carry a [PI TO CONFIRM] flag; where a digest and the master handover disagree, the digest (primary-source-derived) wins, flagged for the PI.
