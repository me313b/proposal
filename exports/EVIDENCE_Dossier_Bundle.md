<!-- ==================== FILE: evidence/00_TECHNICAL_EVIDENCE_DOSSIER.md ==================== -->

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

## The gap-research files (11–16): literature filling the corpus gaps

Each digest above now also carries a detailed "PROPOSAL USE MAP" — fact-by-fact mapping to exact proposal locations with ★-marked load-bearing items, ready-to-use fragments in the proposal register, and "Traps" lists of usages that would be wrong. The six research files below fill the gaps the corpus could not cover, each with verified citations and its own use map:

| File | Gap filled | Headline outcome |
|---|---|---|
| 11_open_end_winding_research.md | No OEW literature held despite the architecture being a bilateral OEW drive | Canon secured (Stemmler & Guggenbach EPE 1993; variants; zero-sequence/common-mode challenges); differentiation: conventional OEW keeps two lumped machine-rated inverters and bus-scale winding voltage |
| 12_gearbox_burden_research.md | Gearbox vulnerability claims uncited | CS-29.927(c) 30-minute loss-of-lubrication endurance; chip detectors; Super Puma planet-gear fatigue accidents (29 fatalities across two); 0.5–1% loss per mesh; wind-turbine reliability canon (Carroll 2016; NREL); eVTOL direct-drive trend (Joby abandoned gearing; Archer geared as counterexample) |
| 13_end_winding_research.md | 20–40% resistance share and cooling claims uncited | Recast as aspect-ratio-dependent range (short stacks up to 50–57%; FSCW well below 20%); hot-spot claim strongly citable (Madonna TIE 2019 DOI 10.1109/TIE.2018.2868288; oil-spray/potting literature); hairpin axial figures (Nottingham VPPC 2023) |
| 14_per_slot_prior_art_research.md | ⚠️ NOVELTY-CRITICAL: closest prior art unexamined | ISCAD (Dajaku/Gerling, SAE 2016-01-1179) did per-slot excitation AND electronic pole changing at 48 V/110 kW — but SUPPLIES 48 V externally at kA currents rather than deriving safe voltages from a HV bus; Wisconsin GaN IMMD (Wang/Li/Han TIA 2015) series-stacks modules to fraction the bus capacitively outside the winding. The unique claim survives as the CONJUNCTION (bilateral open-end + magnetic bus distribution + monolithic IC + PD-by-design + adiabatic ZVS). 8-row differentiation table + Novelty-paragraph fragments included; the proposal MUST cite both |
| 15_multiphase_research.md | Multiphase costs argued from reasoning alone | Levi 2008/2016 reviews with DOIs; derating numbers (five-phase ~70%, six-phase 65–70% single-neutral, dual three-phase 50%, three-phase zero); both differentiators confirmed; the nine-phase pole-phase-modulation line flagged as the citable exception to "pole count fixed"; no published mass/volume audit exists (channel-count arithmetic supplied instead) |
| 16_aero_environment_research.md | 270 V, certification and power-class claims unsourced | MIL-STD-704F + B787 ±270 V anchor the bus choice; SC-VTOL-01 (2019) continued-safe-flight requirement grounds the fault-tolerance framing (no standard says "gradual degradation" verbatim — corrected wording supplied); "5–50 kW per-motor" WRONG for passenger eVTOL (Joby ~236 kW, Archer 120 kW×12) — replacement wording positions the 5–15 kW demonstrator as the scalable per-module building block |

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
11. The Novelty claim must be reframed as a conjunction and must openly cite ISCAD (per-slot excitation + electronic pole changing exist at 48 V) and the Wisconsin GaN IMMD (series-stacked modules see bus fractions) — differentiation table and fragments in file 14. [PI TO CONFIRM: adopt the reframed Novelty passage]
12. "5–50 kW per-motor class" is wrong for passenger eVTOL; replacement wording in file 16. [PI TO CONFIRM]
13. The 20–40% end-winding share is supportable only as an aspect-ratio-dependent range, not a literature constant — recast per file 13; certification framing must say "partial, bounded, predictable failures" (SC-VTOL continued-safe-flight), not "gradual degradation" — per file 16.

## How to use this dossier in a new Claude page

Upload `exports/EVIDENCE_Dossier_Bundle.md` (this index + all eight digests in one file) as project knowledge, alongside `NEW_SESSION_Handover.md` and `EPSRC_Master_Handover.md`. Standing rule for any assistant using it: every technical assertion in drafted text must trace to a locator in these digests or carry a [PI TO CONFIRM] flag; where a digest and the master handover disagree, the digest (primary-source-derived) wins, flagged for the PI.


<!-- ==================== FILE: evidence/01_BTMLC_TPEL_paper_digest.md ==================== -->

# Digest 01 — Battery-Cell-Level Binary-Tree Multilevel Converter (TPEL 2026)

> **Note on anonymisation:** author names appear in this internal digest for traceability. The anonymisation rule applies only to proposal text — do not carry author names into the proposal itself.
>
> Page references below use the **printed journal page numbers 12842–12854** (PDF pages 1–13). All numbers are transcribed verbatim from the extracted text; nothing is inferred. Table I's cell contents and all oscilloscope traces are graphics not recoverable by text extraction and are marked [not extractable].

---

## 1. Identity

- **Title:** "On-Chip Design and Implementation of a Battery-Cell-Level Binary-Tree Multilevel Converter"
- **Authors:** Qassam Farhat and Mehdi Baghdadi
- **Affiliation:** Advanced Propulsion Laboratory (APL), Faculty of Engineering Sciences, University College London, WC1E 6BT London, U.K. (e-mail: qassamfarhat@gmail.com; m.baghdadi@ucl.ac.uk). Corresponding author: Qassam Farhat.
- **Venue:** IEEE Transactions on Power Electronics, vol. 41, no. 8, pp. 12842–12854, August 2026.
- **DOI:** 10.1109/TPEL.2026.3675044
- **History:** Received 18 September 2025; revised 6 December 2025 and 30 January 2026; accepted 10 March 2026; published 17 March 2026; current version 5 June 2026. Recommended by Associate Editor Y. Yan.
- **Funding:** Q. Farhat supported by an EPSRC Ph.D. Research Studentship at UCL, grant EP/T517793/1, project reference 2600345 (p. 12853).
- **Index terms:** BCD Technology; battery-integrated multilevel inverter; DC–AC conversion; monolithic integration; power-system-on-chip.

## 2. Significance for the per-slot proposal

This paper is the direct predecessor of the proposed per-slot IC drive: it demonstrates, for the first time, monolithic integration of a complete multilevel DC–AC power stage — power switches, gate drivers, level shifters, dead-time generation, floating supplies and ESD protection — on a single 130-nm BCD silicon die operating directly at Li-ion/LiFePO4 cell voltages, delivering 2 A at up to ~26 V and DC–5 kHz output into **resistive loads only**. It supplies the proposal's foundational evidence on three fronts: (i) the binary-tree topology laws (switch count 2n−2, blocking voltage Vcell·2^(j−1), switching frequency n·f_bus/2^(j−1)) that make cell-level quantisation tractable on-chip; (ii) measured silicon data (0.472 Ω path resistance, 1.522 W modelled vs 1.88 W measured loss at 2 A, 50–66 °C die temperature) that calibrate WP2's circuit and WP5-relevant thermal models; and (iii) explicitly stated gaps — no inductive/machine load, no back-EMF, no operation above 5 kHz, no thermal co-design, no fault protection — which are precisely the open territory the per-slot programme claims.

## 3. Page-by-page technical walk

### p. 12842 (PDF p. 1) — Abstract and Introduction (opening)

Establishes the claim set: a fully integrated **bidirectional** binary-tree multilevel converter (BTMLC) operating directly at battery cell voltage; binary tree used as a voltage tap selector over series-connected DC sources; **eight distinct voltage levels from only three control signals**; conduction-path switch count scales **logarithmically** with output level count; nearest-level modulation (NLM/NLC); full system (power stages, control, gate drivers, level shifters, protection) in a **130-nm process with junction-isolated lateral devices**; total chip area **15 mm²** (abstract figure; refined to 15.2 mm² on p. 12849); output current **2 A**. Introduction frames battery-powered drive systems, MLC advantages (low-voltage high-performance switches; reduced EMI, THD, device stress) and the cell-level integration problem: many switches, gate drivers, isolated supplies. **Table I** (p. 12842) tabulates switch counts N_sw of representative MLC topologies (NPC, FC, CHB, MMC, P2, SSPS, SCSS, MLM implied by text) versus level count n — cell values [not extractable].

### p. 12843 (PDF p. 2) — Introduction (completion) and topology definition

- Prior art: hybrid unipolar level-generation + H-bridge topologies (P2, SSPS, SCSS, MLM) cut device count but bring "higher voltage stress, reduced redundancy, loss of modularity, and the need for costly bidirectional switches". BIMIs/BI-MMCs (Fig. 1, p. 12843) pair each small cell group with HB/FB/BM3 submodules but "suffer from higher conduction losses compared to silicon-carbide (SiC)-based two-level converters and impose substantial gate-driving complexity, as most switches must be referenced to floating potentials".
- GaN ICs: promising (half-bridge, three-level, matrix converters) but constrained by external gate drive, lack of complementary devices, GaN-on-Si substrate effects, cost. BCD chosen as the mature platform (CMOS + bipolar + capacitors + diodes + LDMOS). Gap: multilevel **DC–AC** conversion from multiple battery cells via large-scale on-chip integration has had "comparatively little attention".
- Novelty claims: BTMLC topology assigns **high-frequency operation to switches blocking near cell-level voltages**; higher-blocking switches switch slower. Gate-drive supplies come **directly from the battery cells via fully integrated regulators — no isolated floating supplies**. Claimed as "the first demonstration of integrating a large number of power switches together with their control logic, gate drivers, floating supplies, and level shifters on a single silicon chip for a multilevel DC–AC converter". Integration methodology stated to be portable to other cell-level MLC topologies.
- Topology (Fig. 2, p. 12844): **seven series-connected battery inputs B1–B7**, typical cell voltage V_cell; three switch levels (Level I/II/III) of half-bridges/choppers, each level driven by one complementary logic pair with identical blocking rating; level count scales as **log2(n)**; **Eq. (1): n = 2^k, k ∈ Z≥1**. n = 8 chosen because of "the voltage breakdown limits of the chosen semiconductor technology".

### p. 12844 (PDF p. 3) — Operation, control logic, scaling laws

- **Table II** (p. 12844): control logic and current paths — S1, S2, S3 control Levels I, II, III; entries [not extractable].
- Output: eight levels 0, V_cell, 2V_cell … 7V_cell from three control signals.
- **Eq. (2) — switch count law:** N_sw = Σ_{j=1}^{log2 n} 2^j = **2n − 2** for the level-generation stage. A polarity-generation full bridge adds four switches rated for the full DC input voltage, but these switch only at output frequency so can be paralleled for low conduction loss.
- Complementary operation within each pole; **dead time mandatory** to avoid shorting battery cells.
- **Eq. (3) — blocking-voltage law:** V_blk,j = V_cell · 2^(j−1), j = 1…log2(n).
- **Eq. (4) — switching-frequency law:** f_sw,j = n·f_bus / 2^(j−1); **Eq. (5)** with H-bridge polarity reverser: f_sw,j = 2n·f_out / 2^(j−1).
- Concretely: Level I/II/III block V_cell, 2V_cell, 4V_cell and toggle at 8f_bus, 4f_bus, 2f_bus. High-voltage capability by a single HV device or by stacking lower-voltage units. Key architectural consequence: fast switches see low voltage and vice versa, enabling hybrid on-chip/off-chip scaling with relaxed dynamics for off-chip devices.

### p. 12845 (PDF p. 4) — Loss modelling and switch sizing

- Three switches conduct at any instant (for n = 8) from batteries to output bus.
- **Eq. (6):** p_cond(t) = i_c² Σ R_on,j; **Eq. (7):** P_cond = I_rms² Σ R_on,j (fundamental only).
- **Eq. (8):** total dynamic loss summing f_sw,j · (n/2^(j−1)) · C·ΔV² terms over C_gs, C_gd, C_ds per level; **Eq. (9):** ΔV_gd = ΔV_gs + ΔV_ds; **Eq. (10):** P_losses = P_dyn + P_cond.
- Finger-based sizing: width-proportional scaling — **Eqs. (11)–(14):** R_on,j = r_on,j/W_s,j; C_gs,j = c_gs,j·W_s,j (similarly C_gd, C_ds); channel length fixed by process per voltage rating (not adjustable for LDMOS).
- **Eq. (15):** β_j = c_gs ΔV_gs² + c_gd ΔV_gd² + c_ds ΔV_ds²; **Eq. (16):** per-switch loss P_switch,j = f_sw,j·W_s,j·β_j + (r_on,j/W_s,j)·I_rms².
- **Fig. 3** (p. 12845): per-switch total losses for Levels I–III at **2 A converter current and 10 kHz AC output frequency**, plotted from (16).

### p. 12846 (PDF p. 5) — Optimal sizing, loss breakdown, level shifting

- **Eq. (17) — optimum width (in words):** the loss-optimal switch width equals the square root of (I_rms²·r_on,j) divided by (f_sw,j·β_j).
- Device sizes here were **area-constrained**, chosen "to illustrate the fundamental operation… rather than to target specific performance limits".
- **Fig. 4** (p. 12846): breakdown of **total power loss 1.522 W** at **2 A output current, f_out = 10 kHz**, for **switch widths 64–80 mm**. Findings: switching losses negligible; conduction losses dominant, split between channel and metallisation resistance — "the metallization resistance is approximately equal to the channel on-state resistance".
- Section III opens: power stages use **N-channel LDMOS**; control comprises level shifters, dead-time generators, gate drivers and their supply generation.
- **Fig. 5** (p. 12846): (a) multiple-output level shifter (MOLS) + dead-time generator architecture; (b) DT Gen. circuit — RC delay R_dt1·C_dt1 on the rising edges of both complementary signals creates the dead-time band; (c) MOLS I/II: **stack of series-connected NDMOS** with gates tied to an **eight-tap resistive divider (R1–R8)** across VDD8; diode-connected device M_D shifts divider voltages up by ~one threshold. Divider current designed to stay within **1–2.5 mA** across input-voltage variation. Direct gate connection to cell taps avoided for ESD immunity.

### p. 12847 (PDF p. 6) — Level shifter operation; Level I circuit (Figs. 6–7)

- Stacked NDMOS shifter distributes VDD8 equally across devices in both input states; saturation when input low, cut-off when high; drain voltages approach gate voltages (diode-connected behaviour, effective resistance ∝ 1/g_m). Power/delay set by NDMOS dimensions.
- Fully differential scheme: dead time introduced **only at the input** of the stacked shifters, eliminated from half-bridge stages; symmetric low-/high-side signals; "universal dead-time controllability" from a **single** dead-time circuit referenced between the first battery tap and ground — contrasted with conventional local dead-time + asymmetric shifting which forces extended dead times and extra loss. Dead-time circuit can even be omitted with two externally buffered complementary signals per level (off-chip dead time).
- **Fig. 6** (p. 12847): bottom half of Level I — **four half-bridge power stages using 5 V NDMOS devices** across four battery cells; CMOS-inverter gate drivers/buffers, cross-coupled level shifters ("LS"), and two Zener-based voltage limiters per stage. **Fig. 7** (p. 12847): Level II and III circuits; driver rails VDRV2/VDRV6 reused from Level I Zener regulators.

### p. 12848 (PDF p. 7) — Gate drive supplies (Zener regulators); Level II/III drive chains

- LS block: aspect ratios of intermediate PDMOS (Mpd3/Mpd4) and bottom NDMOS (Mnd1–Mnd4) versus pull-up PDMOS (Mpd1/Mpd2) set by worst-case corner simulation per [32]. An **identical LS block in the low-side path acts as a delay-matching dummy** (VDDH/VSSH tied to VDDL/VSSL) preserving dead time across process and temperature.
- Zener regulators generate both high- and low-side drive rails from the cells; regulation ensures equal gate overdrive, hence matched on-resistances (low-side could connect directly to cells if area is prioritised). Implementation: **6-V Zener diodes Z1–Z4**, source followers MR1–MR4, resistor bias (Rz1–Rz4, Rs1–Rs4), filter capacitors (Cz1–Cz4, Cs1–Cs4). Output V_DRV ≈ V_Z − V_GS; Zener bias current "on the order of a few microamperes"; large-W/L follower keeps V_DRV variation "within a few hundred millivolts". Open-loop operation gives immediate response to driver current transients; buffer capacitor across each Zener stabilises the reference and avoids open-circuit conditions.
- Level II drive: MOLS II shifts logic to the lowest tap of each Level II submodule (e.g. Top Submodule switches M11/M12: shifted to VDD4, giving VLS2_L5/VLS2_R5 toggling between VDD4 and VDD5), then floating cross-coupled shifters, then CMOS drivers. Low-side Level II rails reuse Level I high-side regulator outputs (VDRV2, VDRV6 — shared source nodes); high-side Level II uses dedicated regulators VDRV9/VDRV10 fed from taps VDD6 and VDD8.
- Level III: VCNT3 → two-phase dead-timed signal, shifted from logic domain (VSS1–VDD1) to the Level III low-side domain (VDRV9 to VSW1,L2); symmetric propagation via VLS3_L1/VLS3_R1; low-side rail from Level II high-side limiter, high-side from a dedicated limiter on VDD8.

### p. 12849 (PDF p. 8) — Expansion strategy; process; fabrication; test-rig entry; first measurement

- **Section III-C expansion:** higher current needs more silicon area (cost/yield penalty), so "low-current designs (5–10 A) are more practical" with **parallel ICs** for higher system current. Voltage limited by junction breakdown of the BCD process; scale by higher-breakdown technologies or module stacking: **"a 128-tap system (approx. 400 V) can be implemented by stacking sixteen BTMLC ICs"** — either direct modular stacking (Fig. 1) or external discrete switches completing a larger binary tree, with external blocking voltages per (3) and frequencies per (4): lower tree levels on-chip (high speed, fine quantisation), levels beyond BCD limits off-chip. Cites [34], [35] for hierarchical/hybrid multilevel scaling precedent.
- **Fig. 8** (p. 12849): process cross-section, N-/P-channel devices with deep (buried) N-layer substrate isolation, bodies tied to sources.
- Process: **130-nm BCD, standard industrial flow on 12-inch wafers**; FEOL forms isolated LDMOS and Zener diodes; BEOL: silicidation, contacts, **six metal layers**, passivation opened only at bond pads.
- All power switches N-type for minimum R_on and area. **Level III needed ≤16 V devices for Li-ion/LiFePO4 range, but the tape-out run only offered a 24 V device** — "a suboptimal voltage rating… which contributed to a substantial increase in the overall path resistance".
- Layout: power pads adjacent to and **directly over active regions (bond-on-active-circuit)**; **total chip area 15.2 mm²** (Fig. 9(a)); **33 μm aluminium bond wires** (Fig. 9(b)); output pads centred with multiple bonds for low resistance; two-layer daughterboard with decoupling; 50-contact card-edge connector, four contacts per pad, two per logic input; motherboard test board; control from a digital microcontroller via **three logic signals**.
- **First measurement (DC tap-selector mode):** constant **2 A** load per tap; **measured path resistance ≈ 0.472 Ω**; average I²R loss ≈ **1.88 W**, "about 20% higher than the losses predicted by the model" — excess attributed to connector wires, board routing and wire bonds.

### p. 12850 (PDF p. 9) — Dynamic characterisation (Figs. 9–10) and load tests

- **Fig. 9** (p. 12850): (a) layout **3.530 mm × 4.297 mm**; (b) die micrograph; (c) test bench (multichannel supplies, power resistor loads, oscilloscope, V/I probes); (d) motherboard.
- **Fig. 10** (p. 12850): no-load NLC waveforms — (a) 2.5 V taps, 10 Hz; (b) 2.5 V, **5 kHz**; (c) 3.7 V, 10 Hz; (d) 3.7 V, 5 kHz. Fine step resolution over wide frequency range.
- **Overshoot artefact:** transitioning down from 10 V (2.5 V cells) or 14.8 V (3.7 V cells) — i.e. turning off M5, M11, M14 then on M4, M10, M13 — the output is "momentarily pulled toward the maximum voltage for approximately **50 ns**" because Level I/II high-side switches turn on faster than the Level III low-side switch; mitigable "by synchronizing these switching events through driver design".
- Load operation required tap decoupling with ceramic capacitors of **0.1 μF, 0.33 μF, 10 μF, and 22 μF**.
- Ratings summary: max output current ≈ **2 A**; per-cell voltage **3.7 V** → output magnitude ≈ **26 V**; maximum load power ≈ **52 W**. "The current capability is primarily limited by the selected switch dimensions, whereas the voltage capability is constrained by the breakdown voltage of the adopted BCD technology."
- Arbitrary-waveform test: **uniformly distributed random control sequence, 3.3 V taps, 12.7 Ω resistive load** (Fig. 12, p. 12851) — validates arbitrary tap transitions at high rate under continuous load current.

### p. 12851 (PDF p. 10) — Fig. 11 test matrix

**Fig. 11** (p. 12851), half-wave sinusoidal NLC, measured V and I:
- (a)/(c)/(e) voltages at **1 kHz reference, 3.3 V supply**, loads **33 Ω / 22 Ω / 12.7 Ω**; currents in (b)/(d)/(f).
- (i)/(k)/(m) voltages at **3.3 V, 12.7 Ω**, reference frequencies **10 Hz / 1 kHz / 5 kHz**; currents (j)/(l)/(n).
- (q)/(s)/(u) voltages at **fixed 5 kHz reference**, tap voltages **3 V / 3.4 V / 3.5 V**, loads **10 Ω / 12.7 Ω / 12.7 Ω**; currents (r)/(t)/(v). Waveform values themselves [not extractable — oscilloscope images].

### p. 12852 (PDF p. 11) — Dynamic modulation (Fig. 13), thermal results (Fig. 14), practical considerations (start)

- **Fig. 13** (p. 12852): frequency transitions 1 kHz→5 kHz, 100 Hz→1 kHz, 5 kHz→100 Hz, 100 Hz→5 kHz; amplitude transitions **3.3 V→23.1 V** and back. "Smooth dynamic response despite the abrupt frequency changes" — flagged as "essential for integration into larger DC–AC stages for drive applications".
- **Thermal (Fig. 14, p. 12852):** under NLC with **12.7 Ω load** at the Fig. 11(n) operating point (3.3 V, 5 kHz): measured temperature **≈ 50 °C to 66 °C**; chip ≈ **65 °C** while PCB ≈ **26 °C**, attributed to "weak thermal coupling between the chip and the large copper pads". Conclusion: "even under moderate conduction losses, insufficient thermal extraction can lead to local temperature rises"; remedies suggested: large thermal pad to a copper plane via thermal vias, larger heat-spreading area. No heatsink, no thermal co-design performed.
- Section V opens: **only essential ESD protection integrated**; "comprehensive fault detection, cell monitoring, and protection mechanisms were not included in this initial design due to silicon-area constraints".

### p. 12853 (PDF p. 12) — Fault tolerance, application classes, comparison, Conclusion

- Single shorted cell (any of B1–B7): no catastrophic failure; level count reduces, small drop in output magnitude and resolution; THD impact "expected to be limited for a single-cell short" but degradation depends on conditions. Fault detection/bypassing "remain essential for practical deployment"; BCD enables future integration of current/voltage/temperature sensing, diagnostics, autonomous cell bypassing.
- Two application classes: (1) as a modular subunit within BIMIs (series/parallel stacking); (2) standalone for "compact and lightweight drive applications… such as drones, mobile robotics, and Brushless DC motor drives, where size, mass, and PCB footprint are tightly constrained".
- Qualitative comparison: constant-blocking-voltage topologies (MMC, CHB, P2) put many devices in the conduction path at cell-level resolution; minimum-conduction-path topologies need bidirectional or high-V/high-f switches; BTMLC is "an intermediate and favourable balance" (fast switches see lowest stress per (3); high-stress switches switch slowly per (4)–(5) and can be paralleled).
- **Conclusion:** prototype in 130-nm BCD; "reliable operation with load currents up to 2 A, limited by the current silicon area of switches, and an output frequency range from DC to 5 kHz"; extension paths: higher-breakdown processes, wider devices, board/package-level series/parallel stacking; benefits: compactness, high-resolution synthesis, reduced EMI/THD, simplified routing, and future embedded sensing/diagnostics/protection.

### p. 12854 (PDF p. 13) — References and biographies

35 references (NPC [7], FC [8], CHB/MMC [9]–[11], reduced-count topologies [12]–[17], BIMI/BM3 [18]–[22], GaN ICs [23]–[28], BCD/PMIC [29]–[31], level shifters [32], PMIC design [33], extended MMC roadmaps [34], [35]). Biographies: Farhat (Ph.D. UCL 2026; ex-pSemi RFIC; now Research Fellow, Queen's University Belfast); Baghdadi (Ph.D. Cambridge 2015; Associate Professor, UCL; leads Electric Propulsion Group; Co-Director, UCL Advanced Propulsion Laboratory).

## 4. Quotable passages

1. p. 12843: "To the best of our knowledge, this work represents the first demonstration of integrating a large number of power switches together with their control logic, gate drivers, floating supplies, and level shifters on a single silicon chip for a multilevel DC–AC converter."
2. p. 12843: "While demonstrated using the BTMLC topology, the proposed integration methodology is applicable to other multilevel architectures intended for battery-cell-level operation."
3. p. 12843: "the battery cells are directly used to supply the gate-driving circuits through fully integrated voltage regulators, eliminating the need for isolated floating supplies."
4. p. 12844: "the proposed BTMLC architecture allows switches with higher voltage-blocking requirements to operate at lower switching frequencies and vice versa."
5. p. 12846: "The distribution reveals negligible switching losses and dominant conduction losses… The low switching losses demonstrate the excellent dynamic performance of the on-chip lateral switches and their high-speed capability."
6. p. 12849: "a 128-tap system (approx. 400 V) can be implemented by stacking sixteen BTMLC ICs."
7. p. 12850: "the maximum power that can be delivered to the load is approximately 52 W. The current capability is primarily limited by the selected switch dimensions, whereas the voltage capability is constrained by the breakdown voltage of the adopted BCD technology."
8. p. 12852: "even under moderate conduction losses, insufficient thermal extraction can lead to local temperature rises."
9. p. 12852: "These observations demonstrate the converter's ability to operate reliably under variable-voltage, variable-frequency conditions, which are essential for integration into larger DC–AC stages for drive applications."
10. p. 12853: "the IC supports compact and lightweight drive applications whose voltage and current requirements fall within the rating of a single module, such as drones, mobile robotics, and Brushless DC motor drives, where size, mass, and PCB footprint are tightly constrained."

## 5. Limitations and open territory

Everything below is absent from the paper and constitutes the open ground the per-slot proposal occupies:

- **No machine/winding load.** All experiments use **power resistor loads** (10–33 Ω, Fig. 9(c), Fig. 11); drive applications are only anticipated: "essential for integration into larger DC–AC stages for drive applications" (p. 12852) and named as future use cases (drones, robotics, BLDC drives, p. 12853). No inductive load, no motor, no winding is ever connected.
- **No back-EMF or inductive-source interaction.** The converter is characterised as a tap selector into resistive loads with ceramic decoupling (0.1–22 μF, p. 12850); commutation against a winding's stored energy, freewheeling, or ZVS exploitation of inductive current is unaddressed.
- **No operation above 5 kHz output.** "an output frequency range from DC to 5 kHz" (p. 12853); the 10 kHz figure appears only in the loss **model** (Figs. 3–4, pp. 12845–12846), never in measurement. Effective device switching rates follow 8f_bus but electrical-output bandwidth beyond 5 kHz is untested.
- **No mutual coupling / multi-phase operation.** Single-phase only ("The single-phase converter architecture…", p. 12842); no polyphase demonstrator, no inter-module magnetic or electrical coupling studied.
- **No transient voltage-distribution study.** The only transient anomaly reported is the ~50 ns overshoot on downward level transitions (p. 12850), with mitigation deferred to "synchronizing these switching events through driver design"; dv/dt distribution across stacked devices or into a winding is not analysed.
- **No thermal co-design.** Thermal data are observational (50–66 °C die vs ~26 °C PCB, p. 12852); improvements (thermal pad, vias, heat spreading) are suggested, not implemented; no coupled electro-thermal model, no heatsinking, no integration with a machine's thermal environment.
- **No vibration/mechanical environment testing.** Not mentioned anywhere; bond-on-active pads and 33 μm Al wire bonds (p. 12849) are unqualified mechanically.
- **No protection, monitoring or fault management in silicon.** "Comprehensive fault detection, cell monitoring, and protection mechanisms were not included in this initial design due to silicon-area constraints" (p. 12852); "Fault detection and bypassing remain essential for practical deployment of this architecture" (p. 12853).
- **No efficiency figure under AC operation, no THD/EMI measurement.** Losses are reported as DC I²R (1.88 W at 2 A, p. 12849) and a model total (1.522 W, p. 12846); EMI/THD reduction is claimed generically, never measured.
- **Sub-optimal, area-constrained silicon.** Device sizes "were constrained by the total available silicon area… rather than to target specific performance limits" (p. 12846); the 24 V (instead of 16 V) Level III device "contributed to a substantial increase in the overall path resistance" (p. 12849); measured losses exceed the model by ~20% due to packaging/board parasitics (p. 12849). Headroom for an optimised per-slot design is thus documented by the authors themselves.
- **Scaling asserted, not demonstrated.** The 128-tap/~400 V sixteen-IC stack (p. 12849) and 5–10 A parallel-IC guidance are design arguments only.

## PROPOSAL USE MAP (detailed)

**Key.** In the current drafts this paper is inline citation **[1]** (pre-renumbering; reconcile via Map B against Part 1 of drafts/06_References.md before submission). Proposal locations use: Vision part names as in drafts/02_Vision_ArcRevision.md (Opening: stand beside the expert / The unseen line / Crossing the line: the 50 V claim / The cascade and its price / Timeliness: the ATI collision / National importance); Approach subsections, RQ/H/O/Gap/WP/T/D identifiers and risk-table rows as in drafts/03_Approach.md; "Summary" = the EPSRC summary; "Capability module" = the separate R4RI 1,500-word capability section (Handover S10). Fragments are in proposal register: UK English, no em dashes; unconfirmed items carry [PI TO CONFIRM].

### Identity and provenance

1. **Venue/bibliography (TPEL vol. 41 no. 8, pp. 12842–12854, Aug 2026; DOI 10.1109/TPEL.2026.3675044).** (a) References list entry for [1]; every inline [1] in Vision and Approach. (b) Direct citation; this digest is the verified bibliographic record. No fragment needed.
2. **EPSRC studentship funding (EP/T517793/1, ref. 2600345, p. 12853).** (a) Capability module; optionally National importance. (b) Supporting narrative: prior EPSRC investment produced the enabling silicon, and this programme is its continuation. Fragment: "The enabling silicon was itself delivered under EPSRC doctoral funding; this programme carries that investment from the battery-cell demonstration to the machine winding. [PI TO CONFIRM: whether to name the studentship grant]"
3. **Anonymisation note (digest header).** (a) All proposal text. (b) Compliance rule: cite as [1] or "the group"; author names never appear in the proposal body.
4. **Biographies (Baghdadi: Associate Professor, UCL; leads Electric Propulsion Group; Co-Director, APL. Farhat: now Research Fellow, QUB).** (a) Capability module only. (b) Track-record facts for the PI paragraph; the first author's move to QUB also evidences researcher development. Do not use in Vision or Approach.

### Core silicon claims

5. ★ **First-demonstration claim (Quotable 1, p. 12843: "the first demonstration of integrating a large number of power switches together with their control logic, gate drivers, floating supplies, and level shifters on a single silicon chip for a multilevel DC–AC converter").** (a) Vision, Crossing the line: the 50 V claim (the "buildable now, and only now" paragraph); Summary; Capability module. (b) Direct citation establishing priority and feasibility in one stroke. ★ Load-bearing because the entire "the technology exists and is validated" pivot of the Vision rests on this single priority statement. Fragment: "the group has demonstrated the first monolithic integration of a complete multilevel DC to AC power stage, including gate drivers, level shifters, dead-time generation and floating supplies, on a single die [1]".
6. ★ **Complete integration inventory on 15.2 mm² in 130 nm BCD (pp. 12842, 12849; abstract's 15 mm² is the rounded figure).** (a) Vision, Crossing the line (already drafted: "on a single 15.2 mm² die in 130 nm BCD [1]"); Approach, Building on previous work and lineage-table row "BTMLC IC (2026)"; Capability module. (b) Quoted number with condition; always 15.2 mm², never 15. ★ Load-bearing because it is the size argument that makes per-slot placement physically credible and the discrete alternative absurd.
7. ★ **Measured envelope: 2 A, ≈26 V (3.7 V cells), ≈52 W, DC–5 kHz (pp. 12850, 12853; Quotable 7).** (a) Approach, WP2 opening and Feasibility and risk management; WP4 benchmark (T4.2); supports plausibility of H2's 100 Hz–3 kHz target. (b) Quoted numbers with condition (resistive load, NLC). ★ Load-bearing because the demonstrator's electrical range must sit inside a measured envelope for feasibility to survive review. Fragment: "the silicon-validated platform delivers 2 A at up to approximately 26 V over DC to 5 kHz into resistive loads [1], an envelope that encloses the 100 Hz to 3 kHz electrical range of the proposed machine".
8. **Eight levels from three control signals; n = 2^k (Eq. 1); N_sw = 2n − 2 (Eq. 2) (pp. 12842–12844).** (a) Approach, WP2 (architecture basis) and WP3/RQ4 (control compression). (b) Feasibility evidence that per-slot control complexity scales logarithmically. Fragment: "the binary-tree structure synthesises eight voltage levels from three control signals, so control signal count grows logarithmically rather than linearly with voltage resolution [1]".
9. **Blocking-voltage law V_blk,j = V_cell·2^(j−1) (Eq. 3) and frequency laws (Eqs. 4–5): fast switches see the lowest voltage, high-stress switches switch slowly (p. 12844; Quotable 4).** (a) Approach, WP2 T2.1 design basis; also the "ZVS lost under inductive winding source" risk row, whose fallback (hard-switched parallel low-voltage devices) is credible precisely because the high-rate devices block only cell-level voltages. (b) Direct citation of the architectural law. Fragment: "switches with the highest switching rates block only the lowest voltages, and the highest-stress devices switch at output frequency [1]".
10. ★ **Gate-drive supplies taken directly from the cells through integrated regulators; no isolated floating supplies (Quotable 3, p. 12843).** (a) Vision, Crossing the line (the necessity argument: a discrete implementation would repeat the floating-domain infrastructure roughly 36 times); Approach, WP2 T2.2. (b) Direct citation; technical foundation of "why IC integration is necessary, not optional" (Handover 2b). ★ Load-bearing because without it the reviewer can ask why discrete electronics would not suffice, and the novelty case collapses to packaging. Fragment: "every floating gate-drive domain is supplied from the local cell through integrated regulators, with no isolated supplies [1]; replicated discretely across 18 bilaterally driven slots this infrastructure alone would exceed the machine volume".
11. **Portability claim (Quotable 2, p. 12843: methodology "applicable to other multilevel architectures intended for battery-cell-level operation").** (a) Approach, Research design and methodology or Building on previous work. (b) Direct citation licensing the transfer from battery taps to winding sections. Fragment: "the integration methodology is stated by its authors to be portable to other cell-level architectures [1]; this programme ports it from battery taps to winding sections".
12. **Dead-time architecture: mandatory dead time (p. 12844); single universal dead-time circuit with fully differential propagation (p. 12847); delay-matching dummy level shifter (p. 12848).** (a) Approach, WP2 T2.2 and T2.4 (the discrete boards must replicate this scheme). (b) Feasibility evidence that timing integrity across 12–18 floating domains is a solved sub-problem in this family.
13. **MOLS stacked-NDMOS level shifter, resistive-divider bias 1–2.5 mA, ESD-motivated isolation from cell taps (pp. 12846–12847).** (a) Approach, WP2 T2.2; Capability module (silicon-proven design flows). (b) Feasibility detail; cite, do not re-derive.
14. **Zener-regulated drive rails: 6 V Zeners, microampere bias, output variation within a few hundred millivolts, open-loop response (p. 12848).** (a) Approach, WP2 T2.2/T2.4. (b) Feasibility evidence that per-slot floating rails need neither isolated converters nor closed-loop regulators.

### Loss, sizing and thermal numbers

15. ★ **Calibration pair: 0.472 Ω measured path resistance; 1.88 W measured vs 1.522 W modelled at 2 A, ≈20% excess attributed to connector wires, board routing and wire bonds (pp. 12846, 12849).** (a) Approach, WP2 T2.1 (SPICE calibration baseline); Feasibility (model credibility with a known error bar). (b) Quoted numbers with condition (DC tap-selector mode, 2 A per tap). ★ Load-bearing because it is the only quantitative silicon-versus-model anchor in the lineage, and WP2's simulation-led method stands on it. Fragment: "loss models of this circuit family predicted the measured dissipation within 20%, the residual being board and packaging parasitics [1], which sets the calibration baseline for T2.1".
16. ★ **Loss breakdown: switching losses negligible, conduction dominant; metallisation resistance approximately equal to channel resistance (p. 12846; Quotable 5).** (a) Approach, RQ2/H2 framing and WP2 T2.1; also supports the hard-switched fallback in the risk table (losing ZVS does not collapse efficiency, because switching loss is already small). (b) Limitation-aware sharpening: it reframes RQ2 towards commutation quality and dv/dt rather than pure loss recovery. ★ Load-bearing because it is the evidential basis for the risk-table claim that the ZVS fallback retains per-slot voltage distribution at acceptable loss. Fragment: "in the predecessor silicon switching losses were negligible against conduction losses [1], so the value of adiabatic operation under a winding source lies in commutation quality and transient stress, not headline efficiency".
17. **Area-constrained sizing: switch widths 64–80 mm, chosen to illustrate operation "rather than to target specific performance limits"; loss-optimal width law Eq. 17 (pp. 12845–12846).** (a) Approach, WP2 (headroom argument); Feasibility. (b) Limitation defining the gap, documented by the authors themselves. Fragment: "the prototype's devices were deliberately area-constrained rather than loss-optimal [1], so the per-slot module inherits documented headroom before any process change".
18. **24 V Level III device where ≤16 V was wanted, contributing "a substantial increase in the overall path resistance" (p. 12849).** (a) Approach, WP2 (second headroom item; a known defect to correct). (b) Limitation as improvement budget; also context for the semiconductor-allocation risk row (device availability shaped even the tape-out).
19. ★ **Thermal result: die ≈50–66 °C, chip ≈65 °C against PCB ≈26 °C, weak chip-to-board coupling, no heatsink, no thermal co-design; measured under NLC at the Fig. 11(n) point, 3.3 V taps, 12.7 Ω, 5 kHz (p. 12852; Quotable 8).** (a) Approach, RQ5/H5, WP2 T2.3, and the "IC junction temperature exceeds limit" risk row; Vision, The cascade and its price (the 120–150 °C winding environment question). (b) Quoted numbers with condition, and the limitation that defines RQ5. ★ Load-bearing because it is the only measured thermal datum in the entire lineage; RQ5 is seeded by it. Fragment: "in the predecessor the die reached approximately 65 degrees C while its board sat near 26 degrees C under moderate conduction loss [1]; inside a winding at 120 to 150 degrees C no such passive margin exists, and RQ5 exists to establish what replaces it".
20. **Load operation required tap decoupling of 0.1, 0.33, 10 and 22 μF ceramics (p. 12850).** (a) Approach, WP2 T2.4 (board design detail) and honest framing of RQ2: the converter is validated only against stiff, decoupled taps, never against an inductive source. (b) Feasibility detail plus gap marker.

### Dynamics and control evidence

21. ★ **50 ns overshoot: downward level transitions momentarily pull the output toward maximum voltage because Level I/II high-side switches turn on faster than the Level III low-side switch; mitigation deferred to driver synchronisation (p. 12850).** (a) Approach, RQ3/H3 and WP1 T1.3; WP2 "known defects to fix". (b) Limitation that makes the research question concrete: the only measured transient anomaly in the lineage. ★ Load-bearing because RQ3's premise (steady-state margin does not guarantee transient margin) would otherwise be hypothetical. Fragment: "even into resistive loads the predecessor exhibited an approximately 50 ns full-bus excursion during downward level transitions [1]; the transient distribution against an inductive winding is unknown, and RQ3 bounds it against the 200 to 300 V Paschen threshold".
22. **No-load NLC operation 10 Hz–5 kHz at 2.5 V and 3.7 V taps (Fig. 10, p. 12850).** (a) Approach, WP3 (controllability envelope). (b) Feasibility evidence of fine step resolution across the frequency range.
23. **Loaded test matrix: 10–33 Ω resistive loads, 3–3.5 V taps, 10 Hz–5 kHz (Fig. 11, p. 12851).** (a) Approach, WP2/WP4 (the baseline the demonstrator extends); Section 5's resistive-only limitation is read off this matrix. (b) Feasibility evidence and gap evidence simultaneously. Waveform values are not extractable; cite conditions only.
24. **Arbitrary uniformly random control sequences under continuous load current (Fig. 12; 3.3 V taps, 12.7 Ω, p. 12850).** (a) Approach, RQ4/H4 and WP3 (arbitrary spatial harmonic synthesis requires arbitrary per-slot waveforms). (b) Feasibility evidence. Fragment: "the platform has executed uniformly random level sequences under continuous load current [1], so arbitrary per-slot current waveforms lie within its demonstrated control envelope".
25. **Smooth dynamic modulation: frequency steps between 100 Hz, 1 kHz and 5 kHz and amplitude steps 3.3 V to 23.1 V with "smooth dynamic response"; flagged as "essential for integration into larger DC–AC stages for drive applications" (Fig. 13, p. 12852; Quotable 9).** (a) Approach, WP3 T3.3 (software-defined pole transitions demand exactly this actuation); the quotation itself can close a WP3 paragraph. (b) Direct citation plus feasibility. Fragment: "abrupt frequency and amplitude reconfiguration has been demonstrated with smooth response on the predecessor silicon [1], which is precisely the actuation a software-defined pole change requires".

### Scaling, process and packaging

26. **Practical current guidance: 5–10 A per IC, parallel ICs for higher current (p. 12849).** (a) Approach, WP1 (sets the per-slot current design space the winding must match) and WP2. (b) Design guidance, not demonstration; phrase accordingly.
27. **Voltage scaling: "a 128-tap system (approx. 400 V) can be implemented by stacking sixteen BTMLC ICs" (p. 12849; Quotable 6).** (a) Approach, WP2 (route to the 270 V bus); optionally Vision, Timeliness. (b) Design argument only; must be flagged as such. Fragment: "the platform's authors outline scaling to approximately 400 V by stacking sixteen ICs [1]; the 270 V bus of this programme sits inside that envelope, though the scaling is a design argument rather than a measurement".
28. **Standard industrial 130 nm BCD flow on 12-inch wafers, six metal layers, buried-N junction isolation (p. 12849).** (a) Approach, Research environment and facilities; Translation (route to volume is conventional foundry manufacture); Capability module. (b) Feasibility and manufacturability evidence. Fragment: "the process is a standard industrial 130 nm BCD flow on 300 mm wafers [1]; the route to volume is conventional foundry manufacture, not research fabrication".
29. **Physical geometry: die 3.530 mm × 4.297 mm; bond-on-active-circuit pads; 33 μm aluminium bond wires (pp. 12849–12850).** (a) Approach, WP1/RQ1 (bilateral end-face IC access must accommodate this footprint) and WP2 T2.3 (packaging spec); the mechanically unqualified assembly also feeds the risk discussion. (b) Quoted numbers bounding the design space; limitation for the mechanical environment. Fragment: "[PI TO CONFIRM: whether to add a vibration and mechanical-environment risk row; the predecessor's bond-on-active assembly is unqualified mechanically [1]]".
30. **Test methodology: daughterboard/motherboard, card-edge interfacing, microcontroller drive via three logic signals, thermal imaging (pp. 12849–12852).** (a) Approach, WP4 T4.1 and Research environment and facilities. (b) Feasibility: the demonstrator extends a proven test methodology from resistive to machine loads rather than inventing one.

### Fault behaviour, applications and comparison

31. **Single shorted-cell tolerance: no catastrophic failure, reduced level count, limited THD impact expected (p. 12853).** (a) Approach, WP3 fault framing (qualitative support for graceful degradation). (b) Supporting evidence only; see Traps: this is a cell-level fault, not the module-failure case behind the 89%/58% torque figures.
32. **Protection explicitly absent: "comprehensive fault detection, cell monitoring, and protection mechanisms were not included... due to silicon-area constraints" (p. 12852); "Fault detection and bypassing remain essential for practical deployment" (p. 12853); BCD enables future sensing/diagnostics/bypassing.** (a) Approach, RQ4 (fault re-optimisation) and WP2 module specification; Translation (integration headroom). (b) Limitation defining the gap, stated by the authors. Fragment: "protection, sensing and cell bypassing were explicitly deferred in the predecessor for area reasons [1]; the per-slot module specification treats them as first-class requirements".
33. **Application classes: modular BIMI subunit, and standalone "compact and lightweight drive applications... such as drones, mobile robotics, and Brushless DC motor drives" (p. 12853; Quotable 10).** (a) Vision, Timeliness: the ATI collision (the authors' own trajectory points at drives); Approach, Building on previous work. (b) Direct citation showing drive application was the declared destination, never the demonstration. Fragment: "the predecessor work names drive applications as its target trajectory [1]; this programme is that trajectory, taken to per-slot resolution".
34. **Qualitative topology comparison: BTMLC is "an intermediate and favourable balance" between constant-blocking-voltage topologies (MMC, CHB, P2) and minimum-conduction-path topologies (p. 12853).** (a) Approach, Building on previous work (differentiation paragraph). (b) Direct citation positioning the chosen topology against MMC/CHB alternatives.
35. **Limit attribution: current limited by selected switch dimensions, voltage by BCD breakdown (p. 12850; Quotable 7; Conclusion, p. 12853).** (a) Approach, WP2 and Feasibility. (b) Limitation as headroom: both limits are design and process choices, not architectural ceilings. Fragment: "the demonstrated limits are set by chosen device dimensions and by the breakdown voltage of the adopted process [1], not by the architecture".

### The gap map (Section 5 items as proposal territory)

36. ★ **Resistive loads only; no machine, winding or inductive load ever connected (Section 5; Fig. 9(c), Fig. 11).** (a) Vision, Crossing the line closing sentence ("what does not yet exist is the science of operating it inside a rotating machine"); Approach, lineage-table row "Battery-cell resistive loads only"; Gap 2. (b) The limitation that defines the entire programme's territory. ★ Load-bearing because it converts the paper from competitor into predecessor: everything demonstrated, nothing yet operated in a machine. Fragment: "every published measurement of this platform is against resistive loads [1]; no inductive load, winding or machine has ever been connected, and that is the boundary this programme crosses".
37. ★ **No back-EMF or inductive-source interaction; converter characterised as a tap selector into decoupled resistive loads (Section 5).** (a) Approach, RQ2/H2, WP2 T2.1, and the "ZVS lost under inductive winding source" risk row. (b) Limitation defining the single hardest technical unknown. ★ Load-bearing because H2 is the programme's highest-risk hypothesis and this documents, from the predecessor itself, that the question is genuinely open. Fragment: "commutation against a winding's stored energy and back-EMF is unaddressed in the predecessor work [1]; establishing the envelope over which adiabatic operation survives an inductive source is the substance of RQ2".
38. **No measured operation above 5 kHz output; 10 kHz appears only in the loss model (Section 5; pp. 12845–12846, 12853).** (a) Approach, RQ2 envelope framing: the machine's 100 Hz–3 kHz range sits inside the measured DC–5 kHz envelope, so cite the measured figure and never the modelled one. (b) Quoted number with condition.
39. **Single-phase only; no mutual coupling or multi-slot interaction studied (Section 5).** (a) Approach, RQ1, Gap 1, and WP1 T1.2 (the inter-slot coupling matrix exists nowhere and must be produced). (b) Limitation defining the gap. Fragment: "no multi-section or magnetically coupled operation of this platform has been studied [1]; the inter-slot coupling matrix WP3 requires does not exist and is produced by WP1".
40. **No vibration or mechanical-environment qualification (Section 5).** (a) Approach, Feasibility (candidate additional risk row) and WP2 T2.3 packaging scope. (b) Risk identification; see item 29 fragment.
41. **No efficiency figure under AC operation; no THD or EMI measurement; EMI/THD benefits claimed generically (Section 5).** (a) Approach, WP4 T4.2/T4.4: the open dataset supplies the first measured figures for this platform class. (b) Limitation that raises the value of the WP4 dataset. Fragment: "no efficiency, THD or EMI measurement under AC operation exists for this platform [1]; the WP4 campaign and open dataset supply the first".
42. **Scaling asserted, not demonstrated: the sixteen-IC 400 V stack and 5–10 A guidance are design arguments (Section 5).** (a) Qualifier attached wherever items 26–27 are used. (b) Honesty condition; see Traps.

### Traps — usages that would be WRONG

- **Do not quote 50–66 °C as a continuous-2 A result.** The thermal data were taken under NLC at the Fig. 11(n) point (3.3 V taps, 12.7 Ω load, 5 kHz), not at 2 A continuous. State the condition or omit the number.
- **Do not cite any switching-loss percentage (e.g. 0.5%).** The paper says only "negligible"; no percentage exists in the text.
- **Do not present 10 kHz as a demonstrated output frequency.** It appears only in the loss model (Figs. 3–4); the measured maximum output frequency is 5 kHz.
- **Do not call this converter adiabatic or ZVS.** The BTMLC is hard-switched NLC. The above-99% adiabatic result belongs to DCAT [3]; keep the two citations separate everywhere adiabatic switching is claimed.
- **Do not claim measured AC efficiency, THD or EMI from this paper.** Only DC I²R loss (1.88 W at 2 A) and a model total (1.522 W) exist; the 98.5% figure belongs to the 2026 stacking preprint, not to [1].
- **Do not cite the 128-tap ~400 V stack or 5–10 A operation as achievements.** Both are design arguments; phrase as "outlined" or "argued", never "demonstrated".
- **Do not quote Table I switch-count values or any oscilloscope waveform numbers.** Both are graphics marked [not extractable]; cite conditions and captions only.
- **Do not use the paper's "bidirectional" claim as evidence of bilateral machine drive.** Bidirectionality is claimed at converter level into resistive loads; absorbing energy from a back-EMF source is untested (that is RQ2).
- **Do not derive the 89%/58% torque-retention figures from the single-shorted-cell result (p. 12853).** That is a cell-level supply fault with reduced level count; the Vision's figures concern module failure in a nine-section machine and have a separate basis.
- **Do not carry author names into proposal text.** Anonymisation rule (digest header); cite as [1] or "the group".
- **Do not write 15 mm².** The abstract's figure is rounded; the proposal standard is 15.2 mm² (p. 12849).
- **Do not cite [1] for the 20–50 V per-slot envelope, the 200–300 V Paschen threshold, or any altitude/partial-discharge figure.** None of these appears in the paper; they carry their own citations ([13] et al.) in the drafts.


<!-- ==================== FILE: evidence/02_TCASI_level_shifters_digest.md ==================== -->

# Evidence Digest 02 — TCAS-I Multiple-Output Level Shifters (A8)

> **Internal dossier note.** Author names appear throughout this digest for traceability. Anonymisation ("[Author]", "the group") applies **only** to text destined for the proposal itself.
>
> **Provenance discipline.** Every quantitative result below is tagged **[SIM]** (post-layout transient / PVT-corner / Monte Carlo simulation) or **[MEAS]** (silicon measurement). The headline **17× propagation-delay reduction and 22×–66× dead-time-spread reduction are SIMULATION results** (post-layout + Monte Carlo); the silicon measurements are the ~2 ns continuous-LS delays, the 25–200 ns programmable dead-time windows, the 2–4.3 V supply range and the waveforms of Figs. 19–21, 23. The proposal was previously caught misattributing these — do not conflate them.

## 1. Identity

Q. Farhat and M. Baghdadi, "Multiple-Output Level Shifters With Dead-Time Control for Gate Driving in Series-Stacked Voltage Domains," *IEEE Transactions on Circuits and Systems I: Regular Papers*, Early Access, DOI: 10.1109/TCSI.2026.3676412. Received 18 December 2025; revised 23 February 2026; accepted 18 March 2026. © 2026 IEEE (1549-8328).

- **Early Access status:** every page carries the banner "This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination." Page numbers cited below are the Early Access PDF's printed pages 1–14, **not** final journal pagination. Metadata: vol. PP, no. 99. [PI TO CONFIRM volume/issue/pages at final publication — matches drafts/06_References.md entry [2].]
- Recommended by Associate Editor C.-S. Lam. Farhat's affiliation: Queen's University Belfast **and** UCL Advanced Propulsion Laboratory; Baghdadi: UCL APL (p. 1).
- **Funding (p. 1):** Farhat supported by EPSRC PhD Research Studentship at UCL, Grant EP/T517793/1, Project Reference 2600345 — an EPSRC-lineage output, useful for track-record framing.
- Acknowledges Dr Atheer Barghouthi (p. 14).

## 2. Significance for the per-slot proposal

The paper solves the **floating-domain control-signal problem**: how to translate one low-voltage logic-domain PWM signal into complementary, dead-time-protected gate signals in *many series-stacked floating voltage domains simultaneously*, on-chip, in 130 nm BCD — the same process as the BTMLC IC. Per-slot bilateral drive needs exactly this: each of 12–18 slot ICs contains stacked half-bridge submodules whose high-side/low-side switches float at winding-defined potentials; without a scalable multi-output level shifter with preserved dead-time, every floating stage would need replicated local dead-time and isolation circuitry, which is what makes discrete implementations physically impossible at slot scale. The paper's key architectural move — **generating dead-time once at the input logic domain and proving (analytically and in silicon) that it survives level shifting across all stacked domains** — is the enabling signal-routing primitive for WP2. It is the "Generation 2" silicon anchor (with the BTMLC IC) in the evidence chain: floating-domain gate-drive infrastructure demonstrably works in this process, in the **stacked-battery domain only**.

## 3. Page-by-page technical walk

**p. 1 — Abstract, Introduction.** Three integrated multiple-output level shifters (LSs) with input-side dead-time generation: (i) cross-coupled active LS, (ii) continuous active-coupled LS, (iii) capacitive-coupled LS. All differential, with dead-time control, fabricated in 130 nm Bipolar-CMOS-DMOS (BCD). Abstract claims, explicitly framed as coming from "comprehensive post-layout transient and Monte Carlo simulations": **17× reduction in propagation delay** and **22×–66× reduction in average dead-time spread** under process/mismatch variations **[SIM]**; operating input range "from 4.3 V down to 2 V"; "Measurement results validate correct operation" **[MEAS]** for voltage compatibility, speed and dead-time controllability. Introduction taxonomy: active-coupled (AC-LS, sub-ns delays, strong dV/dt immunity, but single-output; refs [6]–[10]) vs capacitive-coupled (CC-LS, zero static power, but single/dual output; refs [13], [14]); threshold-voltage loss at intermediate nodes in conventional cross-coupled HV structures (~one |Vt| swing loss, ref [11]).

**p. 2 — Application context and design constraints.** Fig. 1: inverter-integrated battery balancing architectures (capacitor- and transformer-based) needing multiple level-shifted control signals. For multicell balancing (2–5 V/cell), extreme dV/dt immunity matters less than in GaN/SiC converters; the dominant constraints are the six-bullet list: scalability for daisy-chain communication, full rail-to-rail intermediate swing, low delay and pulse-width distortion, PVT robustness, minimal area/isolation overhead, and accurate programmable dead-time. Key architectural distinction stated here: **relocation of dead-time generation to the input logic domain**, versus replicating it in each floating stage.

**p. 3 — Stacked gate-driver architectures and dead-time erosion theory (Section II).** Fig. 2 compares: (a) conventional PMOS/NMOS half-bridge with *local* dead-time per submodule; (b) proposed PMOS/NMOS with a *single* input-side dead-time circuit; (c) proposed dual-NMOS with input dead-time plus drive-rail supply generators (high-side NMOS overdrive taken from the adjacent upper cell for the first n−1 submodules; topmost stage uses PMOS/NMOS or bootstrap/charge-pump). Analytical dead-time-erosion model, Eqs. (1)–(9): output dead-time in domain k is t_dt,out,k = t_dt,in + Δt_k with Δt_k = t^R_PLH,k − t^L_PHL,k (Eq. 5); worst-case erosion E across n domains gives the design constraint **t_dt,in ≥ t_dt,safe + E** (Eq. 9). Worked five-domain example: E = 0.6 ns, t_dt,safe = 2 ns → t_dt,in ≥ 2.6 ns; choosing 3 ns guarantees ≥ 2.4 ns output dead-time.

**p. 4 — Table I, process, layouts, testbench.** **Table I** (delay-asymmetry example): domains 1–5 with t^L_PHL = 1.6/1.8/2.0/2.2/2.4 ns, t^R_PLH = 1.4/1.5/1.6/1.7/1.8 ns, E = 0.2–0.6 ns. Fig. 3: cross-sections of **5 V N-type and P-type LDMOS** with deep isolation; N-buried layer (NBL) biased at highest potential for NDMOS, tied to source/bulk for PDMOS. Each LS up-shifts to **seven battery domains** (simulation configuration). **Fig. 4 layout areas** (as annotated): conventional (cross-coupled) LS **135 µm × 733 µm**; continuous LS **94 µm × 800 µm**; capacitive LS **111 µm × 1300 µm**, with MoM capacitors (2 × 1 pF). All layouts post-layout extracted with RCC parasitics; Monte Carlo evaluates 3σ spread of delay, preset dead-time and switching energy **[SIM]**. Fig. 5 testbench: 0/3.3 V, 1 MHz input, 1 ns edges, input-side dead-time generator producing **3.5 ns non-overlap**, each output loaded by two cascaded inverters, **194 fF** total input capacitance. Power model Eqs. (10)–(11).

**p. 5 — Cross-coupled LS circuit and swing analysis.** Fig. 6(a)/(b): conventional and proposed multi-output cross-coupled LS with input dead-time; device dimensions in µm (cross-coupled PMOS pair 10/0.32; intermediate stacks 250/0.32 and 150/0.37; input NMOS 150/0.37; dead-time block R1 = R2 = 670 Ω, C1 = C2 = 6.6 pF, shunt devices M_dt 160/0.5). Operating principle: sequential threshold-limited propagation up the stack; falling transitions inherently faster than rising → pulse-width distortion accumulating with stack height. **Table II** (extreme-condition parameters): at 125 °C, |V_tpd| = 674 mV, V_tnd = 1.084 V; at −40 °C, |V_tpd| = 844 mV, V_tnd = 1.248 V; V_DDmin = 2.0 V, V_DDmax = 4.3 V. Overdrive degradation Eqs. (12)–(17): intermediate nodes limited to ≈ (V_DD − |Vt|); reduced-swing overdrive V_DD − 2|Vt| vs full-swing V_DD − |Vt|.

**p. 6 — Input-side dead-time generation; cross-coupled results [SIM].** RC dead-time model Eqs. (18)–(21): t_dt,in = 0.693τ for a symmetric inverter threshold; tunable via switched-capacitor units. Seven-level extracted simulation (Fig. 7): **≈17 ns dead-time expansion from V_OUT1 to V_OUT7**; threshold-limited swing observed; **≈2.3 mA pulse current** during dead-time from partial conduction of both branches. Fig. 8: delay/energy worst at slow-PMOS, high-temperature corners (shown at 2.8 V and 4.2 V). **Fig. 9 Monte Carlo (125 °C, 2.8 V): ≈27 ns average dead-time shift, 8 ns 3σ** — the baseline against which the 22×–66× improvement is computed **[SIM]**. Concluding critique: cross-coupled structure poorly suited to modular chip stacking for daisy-chain expansion.

**p. 7 — Continuous active-coupled LS (Fig. 10).** Stack of continuously biased NDMOS forming a "bias-stabilized resistive ladder"; charge-based, continuous (not sequential) propagation; tapped nodes restored to full swing by locally referenced CMOS buffers. Variants: (a) fully differential; (b) R-ladder bias generator with diode-connected device compensating threshold swing loss; (c) **single-ended realisation reducing device count by ≈50%**; (d) modified version with minimum-size cross-coupled PDMOS pairs restoring rail-to-rail swing without the RC ladder's static power. Elmore delay model Eqs. (22)–(24).

**p. 8 — Continuous-LS sizing model and results [SIM].** Power/delay trade-off Eqs. (25)–(31); fitted constants for this BCD process: K_P ≈ 8.3 × 10³ W/m (static power vs width), a = 1.65 × 10⁻¹⁴ s·m, b ≈ 335 ps (buffer-dominated delay floor). Contention sizing Eq. (32): XCP PDMOS at minimum 10/0.32 µm, NDMOS 50/0.5 µm → effective ratio 3.2 vs required worst-case ≈1.15. Fig. 11 (extracted, seven-level): **nearly constant dead-time to V_OUT7; falling-edge delay 0.8 ns, ≈21× lower than the cross-coupled rising-edge delay; DC current ≈15 mA** during the low state (reducible by resizing). Across PVT corners **max delay 4 ns** (Slow-N/Fast-P), **≈9.5× better** than cross-coupled (Fig. 12).

**p. 9 — Continuous-LS Monte Carlo [SIM]; capacitive-LS theory.** **Fig. 13 MC (125 °C, 2.8 V): mean propagation delay 0.87 ns, 3σ ≈ 0.5 ns — "16× improvement over the cross-coupled case"; average dead-time reduced from 3.7 ns to 2.5 ns** with minimal stacking drift; energy/transition ≈2× lower than conventional though its σ rises with g_m variation. Capacitive LS (Section III-F): self-commutated charge pump extending single-output CC-LS [14] to multiple stacked outputs; two low-voltage coupling capacitors plus PDMOS/NDMOS half-latch per stage; CMOS buffers isolate stages → **linear scalability with domain count**. Regeneration model Eqs. (33)–(41) covering piecewise-linear inputs, simultaneous complementary transitions, blanking intervals and single-ended transitions; total delay ≈ n·t*_PD (Eq. 41).

**p. 10 — Capacitive-LS design and results [SIM]; Table III.** Fig. 14 schematic: C_C = 1 pF coupling capacitors, C_N = 0.2 pF node capacitances; charge-injection design equations (42)–(44) with four design bullets (delay depends only logarithmically on ΔV0 → tolerant to capacitor sizing error). Fig. 15: highly symmetric edges, **≈3 ns nearly constant dead-time; typical rising delay 2.1 ns, ≈8× lower than cross-coupled**; output swing reduction < 0.3 V → **zero static power**; **PVT max delay 4.5 ns (SS, 125 °C), 9× improvement**; energy up to **16× lower**. MC: **dead-time drift only 3.65–4.05 ns; 3σ delay 0.7 ns about a 2.89 ns mean**, negligible energy spread. **Table III — Summary of Post-Layout Simulation Results [SIM]** (Cross-Coupled / Continuous / Capacitive): input voltages 2.8–4.2 V (all); output voltage 19.6–29.4 V (all); **t_pd 8.7 / 0.5 / 2 ns** (the 8.7→0.5 ratio ≈ **17×** is the abstract's headline delay claim); 3σ delay 4.23 / 0.54 / 0.7 ns; E_T 1100 / 700 / 70 pJ; area 0.09895 / 0.0752 / 0.1443 mm²; driver power 59 µW (all); PVT robustness Medium / High / High. (Note: Table IV on p. 13 prints slightly different areas — 0.0423 and 0.1125 mm² for continuous/capacitive — presumably excluding buffer/test overhead; both values are as printed, discrepancy unexplained in text.)

**p. 11 — Silicon validation setup and measured headline numbers (Section IV) [MEAS].** Fabricated in 130 nm BCD. Continuous LS (Fig. 10(d) variant) integrated in the multi-stacked half-bridge architecture of Fig. 2(b) for **four battery inputs**; capacitive LS as a **standalone five-level structure** (five battery inputs). Fig. 18: chip layout. Packaging: 33 µm aluminium wire bonds (continuous) vs 17 µm gold (capacitive) — dictated by pad pitch only. Test setup: die on custom two-layer PCB, card-edge connector to motherboard, five independent supplies (2–4.3 V), eight-channel Teledyne LeCroy oscilloscope. **Measured, continuous LS:** at 1 MHz with inputs 2.5 V and 4.3 V, **programmable dead-time windows 25–200 ns**; reliable drive of stacked half-bridge modules over the full range; **≈18 mA current consumption at the 4.3 V maximum input**; across **10 kHz–1 MHz and 2.5–4.3 V**, **propagation delays ≈2 ns at 3.3 V for both edges** (Fig. 20) — "confirming strong symmetry and high-speed silicon performance". **Measured, capacitive LS:** operating range **2 V–4.3 V and 1 kHz–1 MHz**; at 3.3 V, **measured delays ≈70 ns (rising) / 20 ns (falling)** — the sim-vs-silicon discrepancy is attributed to external loading of the weak inter-stage buffers. Verification simulation with representative RLC loading (pad-to-pad 2 pF, pad-to-ground 8 pF, probe tip 11 pF, ground-lead 50 nH, PCB trace 100 nH, bond wire 5 nH) reproduces **63 ns / 25 ns [SIM]**, closely matching measurement — external loading, not intrinsic circuit limitation.

**p. 12 — Measured waveform figures [MEAS].** Fig. 19: measured continuous-LS outputs at all-cells-2.5 V and all-cells-4.3 V with overlap windows 25/50/100/200 ns. Fig. 20: measured single-ended outputs at 10 kHz and 1 MHz for 2.5/3.3/4.3 V cells. Duty-cycle generality: Fig. 23 (p. 13) shows measured 25% and 75% duty operation — not restricted to 50%. Comparative-discussion caveat begins: Table IV is "a qualitative architectural comparison rather than a strict performance ranking".

**p. 13 — Fig. 21, Table IV, Figs. 22–23.** Fig. 21 [MEAS]: measured differential capacitive-LS outputs at 1 kHz and 1 MHz for 2.0/3.3/4.3 V cells; annotated delays 70 ns (1 kHz panel) and 20 ns (1 MHz panel). **Table IV — comparison with refs [7], [9], [12], [13], [15], [18]:** proposed Cross-Coupled / Continuous / Capacitive LS in 0.13 µm; outputs **7 / 4 / 5**; input voltage 2.8–4.3 / 2.5–4.3 / **2–4.3 V**; output voltage 0–29.4 / 0–17.2 / 0–21.5 V; delay 8.7 ns [SIM] / **2 ns [MEAS]** / **45 ns [MEAS] with 2 ns\* (\*post-layout simulated value)**; area 0.09895 / 0.0423 / 0.1125 mm²; dead-time control Yes for all three (No for all six prior works); measurement No / **Yes / Yes**; application BMS. Prior-work delays range 0.5–22.5 ns but all are single-output or lack dead-time control; the proposed area includes buffers, dedicated wells, guard rings and NBL isolation "required for reliable operation in floating high-voltage environments". Fig. 22 [SIM]: RLC-parasitic simulation (delays 63/25 ns annotated). Fig. 23 [MEAS]: duty-cycle waveforms.

**p. 14 — Conclusion, references, biographies.** Conclusion: continuous LS = smallest area, lowest cost, optional non-differential mode halving hardware; capacitive LS = zero static power, low dynamic power, low delay; both support **2–4.3 V per domain**, "enabling compatibility with a broad range of battery chemistries". 18 references. Biographies confirm Farhat (PhD UCL 2026; now Research Fellow, Queen's University Belfast; ex-pSemi RFIC) and Baghdadi (PhD Cambridge 2015; UCL Associate Professor; Co-Director, UCL Advanced Propulsion Laboratory).

## 4. Quotable passages

- "Results demonstrate a 17× reduction in propagation delay and a 22×–66× reduction in average dead-time spread under process and mismatch variations, while supporting a wide operating input voltage range from 4.3 V down to 2 V." (Abstract, p. 1 — **simulation claim**; the sentence follows "validated through comprehensive post-layout transient and Monte Carlo simulations".)
- "Measurement results validate correct operation and confirm the proposed circuits' performance in terms of voltage compatibility, speed, and dead-time controllability." (Abstract, p. 1.)
- "a key architectural distinction is the relocation of dead-time generation to the input logic domain." (p. 2.)
- "Across 10 kHz to 1 MHz and 2.5–4.3 V operation, propagation delays of approximately 2 ns are observed at 3.3 V for both rising and falling edges, confirming strong symmetry and high-speed silicon performance." (p. 11 — **measured**, continuous LS.)
- "programmable dead-time windows from 25 ns to 200 ns are demonstrated. The circuit reliably drives stacked half-bridge modules over the full voltage range." (p. 11 — **measured**.)
- "This result confirms that the observed discrepancy originates from external loading rather than intrinsic circuit limitations." (p. 11 — capacitive-LS 70/20 ns measured vs 2 ns simulated.)
- "CMOS buffers isolate consecutive stages, eliminating the need for large inter-stage coupling capacitors and enabling linear scalability with the number of voltage domains." (p. 9.)
- "the circuits support a wide operating voltage range from 2-4.3 V per voltage domain, enabling compatibility with a broad range of battery chemistries." (Conclusion, p. 14, as printed.)

## 5. Limitations and open territory

1. **Stacked-battery domain only.** Every validation context is series-connected battery cells (2–4.3 V/domain) feeding balancing converters. The supply rails are stiff, monotonic DC taps. A **winding domain** adds: inductive source impedance, back-EMF that moves with rotor speed, bidirectional power flow, and domain potentials set magnetically rather than by cell stacking — none of which is characterised here (this is exactly the gap row in the handover novelty table: "Stacked battery domain only").
2. **dV/dt immunity deliberately de-prioritised** (p. 2): acceptable for battery balancing, but per-slot half-bridges switching against winding inductance will see faster common-mode transients; immunity would need re-verification.
3. **Not gate drivers**: outputs drive minimum-size pre-driver buffers only (p. 4); a per-slot IC still needs the tapered driver chain (the capacitive LS "inherently incorporates the first pre-driver stage", p. 10).
4. **Measured capacitive-LS delay (70/20 ns) is loading-limited**; the intrinsic 2 ns figure at silicon level is inferred via RLC-matched simulation, not directly measured (alternative on-chip delay-extraction structures acknowledged but not implemented, p. 11).
5. Simulated at **seven** domains, fabricated at **four (continuous) and five (capacitive)** domains; 12–18-slot scaling rests on the linear-scalability argument (Eq. 41), not silicon.
6. Continuous LS draws **≈15 mA DC [SIM] / ≈18 mA [MEAS]** in the conducting state — a static-power scalability question for many-domain ICs (capacitive LS avoids it).
7. Table III vs Table IV area figures differ for two circuits (see p. 10 note); cite whichever table is referenced, with the table number.

## PROPOSAL USE MAP (detailed)

Citation key: this paper is **[2]** in the Vision draft (drafts/02_Vision_ArcRevision.md, VIS-CROSS-v7 and VIS-TIME-v7) and A8 in the handover reference plan; the Approach draft currently uses a different local numbering (its [5] is the on-chip isolation thesis, its [1,2,4] the BTMLC set). Reconcile per Handover S9/S11 item 5 before reuse.

### Fact-by-fact map

**★ 1. Same-process silicon anchor: floating-domain level shifting demonstrated in the very 130 nm BCD process as the BTMLC IC (Identity; S2).**
One line: this is the fact that lets the Vision say the architecture is "buildable now, and only now".
(a) Vision, "Crossing the line: the 50 V claim" (VIS-CROSS-v7, already cited as [2]); Vision, "Timeliness" (VIS-TIME-v7, "its floating-domain infrastructure [2]"); Approach, "Research environment and facilities" ("IC design flows developed for the group's prior chip work ... transfer directly into WP2"); Capability module (R4RI), "BTMLC/TCAS-I BCD design flows transfer directly".
(b) Usage: direct citation as Generation 2 silicon evidence; buildability and timeliness warrant.
(c) Fragment: "Floating-domain level shifting with preserved dead-time has been demonstrated in silicon in the same 130 nm BCD process as the per-slot drive die [2], so the complete control-signal chain for stacked floating domains already exists in the target technology."

**★ 2. Input-side dead-time generation with an analytical erosion budget (Eqs. (1)–(9); pp. 2–3).**
One line: the architectural move (dead-time generated once, proven to survive level shifting) is the methodological template WP2 re-derives for winding-referenced domains.
(a) Approach, WP2 T2.2 (floating-domain control-signal architecture, M4–M10; RQ2); also the discrete-board build T2.4, which can reuse the erosion analysis directly; Fig. 2(c) dual-NMOS rail harvesting maps onto per-slot rail generation in the same task.
(b) Usage: methodological precedent; the design constraint t_dt,in >= t_dt,safe + E is directly transplantable.
(c) Fragment: "The group has shown analytically and in silicon that dead-time generated once in the input logic domain survives level shifting across all stacked domains, with a closed-form erosion budget [2]; WP2 re-derives that budget for winding-referenced domains, where the rails are magnetically defined rather than cell-defined."

**★ 3. Silicon-measured performance: 25–200 ns programmable dead-time windows, delays of approximately 2 ns at 3.3 V (continuous LS), 2–4.3 V per domain, 10 kHz–1 MHz [MEAS] (pp. 11–13).**
One line: the only fully silicon-measured timing envelope the programme has, and it bounds the ZVS commutation windows RQ2 needs.
(a) Approach, WP2 T2.1 (ZVS envelope mapping; RQ2) and Objective O2 / Hypothesis H2; Approach, "Building on previous work" narrative and gap table.
(b) Usage: quantitative silicon evidence; frames RQ2's open question (do preserved dead-times remain valid when rails are winding taps with back-EMF, not battery cells).
(c) Fragment: "Silicon measurement of the multiple-output level shifters demonstrates programmable dead-time windows of 25–200 ns and propagation delays of approximately 2 ns across 2.5–4.3 V and 10 kHz–1 MHz [2]; RQ2 asks whether this timing envelope survives when each domain rail is an inductive winding tap with speed-dependent back-EMF."

**★ 4. Headline improvement figures: 17x propagation-delay reduction and 22x–66x dead-time-spread reduction [SIM] (Abstract; Table III; Figs. 9, 13).**
One line: the strongest performance numbers, but they are post-layout and Monte Carlo verification, never silicon measurement, and the proposal has been caught conflating them once already.
(a) Vision, "Crossing the line" or "Timeliness" only if a performance figure is wanted (prefer the measured 2 ns instead); Approach, "Building on previous work"; Capability module track-record narrative.
(b) Usage: supporting evidence with mandatory provenance framing.
(c) Fragment: "Post-layout and Monte Carlo verification of the multiple-output level shifters shows a 17-fold reduction in propagation delay and a 22- to 66-fold reduction in dead-time spread under process and mismatch variation [2], with silicon measurement confirming approximately 2 ns delays and 25–200 ns programmable dead-time in operation."

**★ 5. Per-circuit dissipation inputs: E_T = 70–1100 pJ per transition, 59 uW driver power per output, approximately 15 mA [SIM] to 18 mA [MEAS] continuous-LS conduction current (Table III; p. 11).**
One line: the only quantified self-heating data for the floating-domain signal chain, feeding Co-I Everts' junction-temperature model directly.
(a) Approach, WP2 T2.3 (thermal resistance network and packaging specification, M6–M14; RQ5); Objective O2 / Hypothesis H5.
(b) Usage: quantitative model input; also motivates the capacitive (zero static power) option for many-domain scaling.
(c) Fragment: "Characterised level-shifter dissipation from the group's silicon, 70–1100 pJ per transition and 59 uW per output in post-layout verification, with approximately 18 mA conduction current measured on silicon for the continuous variant [2], provides validated self-heating inputs to the WP2 thermal network from month 1."

**6. Simulated 3-sigma dead-time spread of approximately 0.5–0.7 ns (continuous/capacitive) versus an 8 ns cross-coupled baseline [SIM] (Figs. 9, 13; Table III).**
(a) Approach, WP2 T2.1 and RQ2 (timing-precision envelope available for ZVS commutation control).
(b) Usage: quantitative bound, cited as post-layout Monte Carlo verification.
(c) Fragment: "Post-layout Monte Carlo verification bounds the 3-sigma dead-time spread below 1 ns for the continuous and capacitive level shifters [2], an order of magnitude inside the ZVS commutation windows WP2 targets."

**7. Linear scalability of the capacitive LS with domain count (Eq. (41); p. 9) versus silicon at only four/five domains, simulation at seven (p. 11; Limitation 5).**
(a) Approach, WP2 T2.2 and T2.4 (12–18 floating per-slot domains); Feasibility and risk management (supports the discrete-board primary vehicle and honest framing of the tape-out stretch goal).
(b) Usage: scalability argument plus explicit risk framing: 12–18-domain scaling rests on the analytical linearity argument, not silicon.
(c) Fragment: "Inter-stage buffering makes the capacitive structure linearly scalable with domain count [2]; silicon exists at four and five domains, so extension to 12–18 per-slot domains is an analytical extrapolation that WP2 verifies on the discrete prototype boards before any tape-out."

**8. Stacked-battery-domain-only validation; dV/dt immunity deliberately de-prioritised; outputs are pre-drivers, not gate drivers (Limitations 1–3).**
(a) Approach, "Building on previous work" gap table (row "TCAS-I level shifter (2026) | Floating-domain gate-drive circuits work in the same process | Stacked battery domain only", accurate as it stands, keep verbatim); Vision, "Novelty and Scientific Contribution" (handover S5b: constituent capabilities demonstrated, combination inside a winding is not); Approach, Feasibility and risk management (dV/dt re-verification under winding switching belongs in the WP2 risk narrative).
(b) Usage: gap statement; this limitation IS the research case, so state it prominently rather than defensively.
(c) Fragment: "Every validation context to date is a stack of stiff battery cells; a winding domain adds inductive source impedance, speed-dependent back-EMF, bidirectional power flow and magnetically defined domain potentials, none of which has been characterised. That gap is the substance of RQ2, not a risk to it."

**9. EPSRC lineage: Farhat funded by EPSRC studentship EP/T517793/1 (Project Reference 2600345); PhD UCL 2026, now Research Fellow at Queen's University Belfast (p. 1; p. 14).**
(a) Capability module (R4RI): track record ("doctoral researchers publishing IEEE Transactions during their programmes", handover S10) and prior-EPSRC-investment framing; anonymise in proposal body per dossier note.
(b) Usage: track-record evidence, name-free in body text.
(c) Fragment: "A doctoral researcher funded by an EPSRC studentship (EP/T517793/1) published this line's floating-domain silicon in IEEE TCAS-I during their programme and now holds a research fellowship, evidence that prior EPSRC investment in this platform is already yielding people and publications."

**10. Application framing: 2–4.3 V per domain, battery-chemistry compatibility, BMS context (pp. 2, 14; Table IV).**
(a) Approach, WP2 opening sentence ("previously validated only against low-impedance battery-cell sources"); differentiation passages.
(b) Usage: context only; do not imply the paper addressed machine drives. Its own application column reads "BMS".

**11. Dead-time control as the differentiator against all six prior works in Table IV (p. 13).**
(a) Vision, "Crossing the line" (supporting the claim that the group holds the enabling signal-routing primitive); Approach, "Building on previous work".
(b) Usage: comparative positioning.
(c) Fragment: "No prior multiple-output or high-speed level shifter surveyed offers dead-time control; the group's circuits are the only reported multiple-output level shifters with preserved, programmable dead-time, silicon-measured across the full 2–4.3 V domain range [2]."

**12. Area figures (0.04–0.14 mm² per level shifter, buffers and isolation included) (Table III; Table IV; Fig. 4).**
(a) Approach, WP2 stretch tape-out feasibility (signal-chain area is a small fraction of the 15.2 mm² BTMLC die, so per-slot integration is area-plausible).
(b) Usage: quantitative feasibility support; cite one table by number and note the buffers-and-isolation inclusion (see Traps).

### Traps

1. **Do not misattribute [SIM] figures as measured.** The 17x delay and 22x–66x dead-time-spread reductions, the 0.5 ns / 2 ns Table III delays, the 3-sigma spreads and all Table III energies are post-layout and Monte Carlo verification. Silicon measurements are only: approximately 2 ns continuous-LS delays, 25–200 ns dead-time windows, 2–4.3 V range, approximately 18 mA conduction current, and the waveforms of Figs. 19–21 and 23. The proposal was caught on this once already. Sub-trap: the capacitive LS measured 70 ns/20 ns, not 2 ns; the 2 ns capacitive figure carries an asterisk in Table IV as a post-layout simulated value and must never be quoted as measured.
2. **Early Access citation.** The paper is Early Access: vol. PP, no. 99, no final pagination. Cite as DOI 10.1109/TCSI.2026.3676412, Early Access; never invent volume, issue or page numbers. Page numbers in this digest are the Early Access PDF's pages 1–14 only. [PI TO CONFIRM final metadata at publication.]
3. **Table III versus Table IV area discrepancy.** Continuous LS: 0.0752 (Table III) versus 0.0423 mm² (Table IV); capacitive: 0.1443 versus 0.1125 mm². The text never explains the difference (presumably buffer/test overhead). Always cite the table number alongside any area figure and never mix values from the two tables in one comparison.
4. **Citation-number drift between drafts.** This paper is [2] in the Vision draft but the Approach draft's [2] belongs to the BTMLC set and its [5] is the isolation thesis. Renumber against the final reference list (Handover S9/S11 item 5) before lifting any fragment above into either draft.


<!-- ==================== FILE: evidence/03_Farhat_thesis_digest.md ==================== -->

# Digest: Farhat PhD Thesis — "On-Chip Power Conversion and Battery Balancing Circuits for Battery-Powered Applications"

**Source:** `/home/user/proposal/QFT.txt` (12,162 lines, full thesis text). All locators below are line numbers in that file. Digest prepared for the EPSRC proposal evidence dossier.

---

## 1. Identity

- **Title:** "On-Chip Power Conversion and Battery Balancing Circuits for Battery-Powered Applications" (ll. 1–3).
- **Author:** Qassam Farhat (l. 7); thesis submitted for the degree of Doctor of Philosophy at University College London, Faculty of Engineering Sciences (ll. 12–20); dated **25 November 2025** (l. 24).
- **Supervisor:** Dr Mehdi Baghdadi (l. 142).
- **EPSRC studentship acknowledgement (verbatim, ll. 142–145):** "I also wish to acknowledge the full scholarship support provided by the Engineering and Physical Sciences Research Council under grant number **EP/T517793/1** and **Project Reference 2600345** at UCL."
- **Declared publications (ll. 44–54):** (i) Q. Farhat and M. Baghdadi, "On-Chip Design and Implementation of a Battery-Cell-Level Binary-Tree Multilevel Converter," TechRxiv, 15 Oct 2025, DOI 10.36227/techrxiv.176049762.21205011/v1 — basis of Chapter 6, also submitted to IEEE Trans. Power Electronics; (ii) "On-Chip High-Speed Multistacked Half-Bridge Converters for Compact Battery Balancing Systems," submitted to IEEE Trans. Power Electronics — basis of Chapter 5.
- **Headline abstract claims (ll. 84–96):** wide operating-voltage support 2.4–4.3 V per cell, multi-MHz switching, balancing currents up to 2.5 A, multilevel waveforms of typically 50 V amplitude delivering 6 A constant load current at ≥98.5% system efficiency in stacked binary-tree configurations; "the first miniaturised multilevel conversion system operating directly at the cell-voltage level" (ll. 90–92).

## 2. Thesis argument in one paragraph

The thesis argues that the functions of multilevel voltage synthesis and active battery balancing — both requiring very large numbers of floating, low-voltage switches with per-domain gate drivers, level-shifted control signals and floating driver supplies — **cannot be scaled by discrete/board-level implementation**, because (a) no high-quality discrete switches exist in the Li-ion cell range of 2.5–4.3 V (ll. 1732–1739, 3339–3341), (b) discrete floating-domain infrastructure (multi-winding transformers, opto-couplers, isolated DC–DC supplies, bootstrap ICs) is bulky, costly and does not modularise as level/cell count rises (ll. 4142–4183), and (c) board-level parasitic resistance and inductance directly cap balancing current and switching frequency (ll. 1695–1707, 3331–3336). The solution is architectural: process power at the battery-cell voltage level with a binary-tree multilevel converter (BTMLC) whose fast, cell-voltage-blocking switches are integrated laterally on-chip in a mature, low-cost 130 nm BCD process, while a small number of high-voltage off-chip switches operate at low frequency and can be paralleled for low conduction loss (ll. 1804–1843, 3302–3318). Four silicon fabrications (three level-shifters; half-bridge, full-bridge and complementary half-bridge balancers; two BTMLC generations) validate the approach experimentally, culminating in two stacked BTMLC ICs plus one off-chip half-bridge synthesising 50 V, 6 A half-sine waveforms at up to 98.5% efficiency (ll. 1984–1994, 9679–9688), establishing on-chip integration as a necessity — not an optimisation — for cell-level multilevel conversion.

## 3. Chapter-by-chapter walk

### Chapter 1 — Introduction (ll. 1280–2012)

**Claim:** Integration is the key trend in drivetrain power electronics; a low-voltage, cell-level design approach on mature silicon avoids sole reliance on scarce SiC/GaN (ll. 1306–1358, UK national semiconductor strategy, Jet Zero context ll. 1294–1335). Table 1.1 (ll. 1413–1439, from the Advanced Propulsion Centre UK roadmap) sets 2025→2030 targets: LDV inverters 60–80 → 120 kW/l, ≥98 → 98.5% efficiency, 400/800 V DC links. Problem statement (ll. 1717–1752): MLCs at battery-voltage level lack suitable discrete switches; floating rails need isolated PWM signals via "bulky and costly circuitry, such as opto-couplers or transformer- and capacitor-based digital isolation" (ll. 1736–1740). Methodology (ll. 1804–1843): divide the HV DC link into ~5 V segments; binary-tree switch array selects segments; on-chip switches switch fast at cell voltage, off-chip switches extend to "400 V–800 V systems" at low frequency (ll. 1820–1823); off-chip devices can be paralleled without added switching loss. The chapter's contribution summaries (ll. 1894–2008) pre-state the key numbers used below.

### Chapter 2 — Multicell Power Converters and Battery Balancing Circuits (ll. 2013–3362)

**Claim:** Literature review establishing why multilevel synthesis and why existing topologies/balancers fail at high level counts. Covers Fourier synthesis, harmonic elimination/cancellation, EMI spectrum model (eq. 2.9, ll. 2135–2160), switching loss ∝ V·I·f (eq. 2.11, ll. 2172–2176). **Switch-count scaling laws:** one-branch converter needs s = n−1 sources (l. 2378); NPC per phase leg: 2n−2 switches + 2n−4 clamping diodes + n−1 DC-link capacitors (ll. 2528–2530); FCML: 2n switches + Σ(n−i) clamping capacitors (ll. 2532–2535); P2 topology: M(M−1) switches/diodes and M(M−1)/2 capacitors (ll. 2590–2592); three-phase floating-neutral yields n_p-N = 4n−3 levels (l. 2469). Cell-level scaling example: Tesla Cybertruck 192S7P pack — processing cells individually "cannot be effectively addressed solely through fully onboard solutions based on discrete switches" (ll. 2352–2359). **Balancer component counts** (§2.7, ll. 2875–3011): STSC N−1 caps/2N switches; DTSC 3(n−1)/2 caps; SSC N+5 switches; star-SC n caps/2n switches with AC2AC transfer; CS2CAB full-bridge extension 2N caps/4N switches with capacitor stress (N−1)V_DD/2 (ll. 3009–3011). BIMI critique: at equal embodied carbon a BIMI uses ~3.25× more Si die area than a 2L SiC inverter; SiC 2L achieves ~5× lower losses; BIMIs double battery losses via 2f pulsation (ll. 1649–1660, 2699–2708). §2.10 (ll. 3249–3357) formalises the research gaps — see the verbatim quotes in §4 below.

### Chapter 3 — Semiconductor Devices and Circuit Building Blocks (ll. 3363–4843)

**Claim:** Survey of device technologies and the floating-domain circuit infrastructure the thesis integrates. Discrete devices: planar/superjunction MOSFETs, NPT/PT IGBTs, WBG (Table 3.1, ll. 3556–3565: Si/SiC/GaN E_g 1.12/3.2/3.4 eV, E_crit 0.3/3.5/2.0 MV/cm, power density 1.5/4/4–12 W/mm²). Integrated devices: DEMOS, LDMOS with N-buried-layer junction isolation (ll. 3630–3659); SOI/DTI alternatives (higher cost, worse thermal, latch-up immune, ll. 3663–3688); parasitic SCR latch-up mechanics and countermeasures (ll. 3691–3733). **Switch stacking** (ll. 3772–3866): series stacking to 2–3 V_DD; "this approach can reduce switching losses by a factor of 2–3.6" (ll. 3800–3802); bootstrap-based stacks "become impractical for low-speed operation or circuits without periodic switching" (ll. 3860–3862). **Level shifters** (ll. 3869–4095): cross-coupled HV shifters with sizing eqs. (3.1)–(3.2); pulse-triggered shifters fail above ~15 V/ns dV_SSH/dt (ll. 3984–3986); enhanced designs reach >100 V/ns and −1.5 V tolerance but at complexity/area cost unsuitable "for large-scale integration across multiple half-bridge modules" (ll. 3995–4002); capacitive-coupled shifters with ~50 fF coupling caps (l. 4088). **Dead-time generators** (ll. 4097–4139). **Driver-rail supply generation** (§3.3.4, ll. 4141–4543): discrete options (multi-winding transformer, opto-coupler + boost IC — Li-ion cells "reach only up to about 4.3 V, which is inadequate for driving discrete MOSFETs that generally require 12–20 V gate-source voltage", ll. 4153–4156); nine integrated floating-supply architectures (Fig. 3.11); bootstrap capacitance ~100 nF "generally too large for monolithic integration" (ll. 4213–4215); bootstrap unsuitable for multilevel converters at modulation index below (m−3)/(m−1) (ll. 4436–4443); the bootstrap-vs-motor-PWM incompatibility (ll. 4204–4207, quoted in §4d). **Packaging** (§3.4, ll. 4547–4808): QFP/QFN/BGA/WLCSP/CSP; ball vs wedge bonding; flip-chip flow (C4 reflow ~250 °C, ll. 4732–4734); Au wire ampacity table (ll. 4800–4807, e.g. 2.0 mil × 1 mm = 4.075 A); die-to-board RLC model. Conclusion quote in §4a (ll. 4819–4828).

### Chapter 4 — Circuit Designs for Modular Battery-Balancing Architectures (ll. 4844–5861) — *the TCAS-I level-shifter silicon*

**Claim:** Three integrated multi-output voltage level-shifters with input dead-time control replace per-switch isolated gate-drive signalling for series-stacked voltage domains. Architectures: PMOS/NMOS sub-modules with single input dead-time generator; dual-NMOS sub-modules with SPDT-derived high-side rails (ll. 4952–5019). Implemented in **130 nm BCD** with 5 V asymmetric HV NDMOS/PDMOS (L = 0.37 µm NMOS / 0.32 µm PMOS, l. 5793) isolated by N-buried layer (ll. 5045–5050). Testbench: 1 MHz 0/3.3 V input, 3.5 ns preset dead-time, 194 fF load (ll. 5060–5065). **Table 4.1 (ll. 5079–5086):** cross-coupled ALS 0.098 mm², t_pd 18.75 ns, E_T 1863 pJ, 0 static, 4.2–2.8 V, low PVT robustness; continuous ACLS 0.075 mm², 2.02 ns, 1417 pJ, 15 mA static, 4.2–1.8 V, high robustness; capacitive CLS 0.144 mm², 4.16 ns, 112 pJ, 0 static, 4.2–1.8 V, high robustness. Cross-coupled reference: dead-time expands ~17 ns input→VOUT7, ~2.3 mA cross-current pulse (ll. 5246–5250); worst-case delay ~38 ns (FS corner) (ll. 5316–5319); Monte Carlo dead-time shift ~27 ns with 3σ ≈ 8 ns (ll. 5334–5344). Continuous ACLS: falling-edge delay 0.8 ns (~21× lower than cross-coupled rising edge), 15 mA DC draw, max corner delay 4 ns (~9.5× better) (ll. 5428–5435); Monte Carlo t_pd 0.87 ns avg, 3σ 0.5 ns — "16x improvement" (ll. 5518–5520). Capacitive CLS: rising delay 2.1 ns (~8× better), max 4.5 ns at SS/125 °C, up to 16× lower E_T, dead-time 3.65–4.05 ns, 3σ delay 0.7 ns about 2.89 ns; 1 pF MoM pump capacitors (ll. 5612–5637, 5806–5807). **Measured silicon:** continuous shifter at 2.5/3.3/4.2 V, 10 kHz and 1 MHz, ~2 ns propagation both edges at 3.3 V (ll. 5744–5748); capacitive shifter at 2/3.3/4.3 V, 1 kHz and 1 MHz, 70 ns rise / 20 ns fall (probe-loading limited; ll. 5750–5766). Table 4.3 comparison (ll. 5814–5833): 7×2 complementary outputs, output range 0–29.4 V, dead-time control "Yes" vs "No" for all prior art. Chapter conclusion: "17× reduction in propagation delay and a 22×–66× decrease in average dead-time spread" with 5 V-to-1.8 V range (ll. 1929–1934, 5846–5856).

### Chapter 5 — Integrated Capacitively Coupled Modular Half-Bridge Battery Balancing (ll. 5862–6984)

**Claim:** First on-chip high-current battery-balancing module: four stacked half-bridge sub-modules + off-chip star-configured capacitors, autonomous (sensorless, single PWM signal). Full time-domain model of star-SC balancing (eqs. 5.1–5.17) with SSL/FSL regimes; switch loss model gives optimum width eq. (5.27); chosen width 64 mm → ~76 mW combined loss at 100 kHz / 2.5 A (ll. 6372–6374). **Silicon:** 130 nm BCD, 5 V NLDMOS, chip area **3.4 mm²** (ll. 6500–6501), bond-on-active (BOA) and circuit-under-pad (CUP) pad structures both proven reliable under wedge and ball bonding (ll. 6489–6499); 33 µm Al wedge-wedge bonds, 6–8 wires/pad (Table 5.2, ll. 6533–6542). Conditions: 2×100 µF 16 V MLCC per output (self-resonance ~200 kHz, ESR ~10 mΩ, ll. 6578–6581), inputs 2.4–4.2 V, FPGA control 1 kHz–5 MHz (ll. 6562–6564). **Measured:** correct sub-module, capacitor and bus waveforms at 2.5/3.3/3.7/4.2 V, 1 kHz and 1 MHz (ll. 6584–6605); average balancing current rises from ~0.5 A at 8 kHz to ~1.25 A at 250–500 kHz for maximum imbalance (4.2 V vs 3.3 V) (ll. 6671–6678); SSL below ~32 kHz with ~0.66 Ω SSL resistance; FSL switched-capacitor resistance ~0.6 Ω implying total circuit resistance ~0.12 Ω (ll. 6683–6698); self-resonance limit ~250 kHz (ll. 6712–6714); measurement artefacts explained by ~140 µF decoupling + ~1 µH cable inductance (13 kHz LC) (ll. 6720–6729). Efficiency converges at high frequency; best equalisation at 100–200 kHz; 75% efficiency at worst-case imbalance delivering 1.4 A average (chapter summary ll. 1944–1949). Table 5.3 (ll. 6792–6812): fully integrated 5 V HV NMOS, 2 switches/cell, 50 mΩ switch resistance, one PWM signal, no algorithm, 3.4 mm² — vs [142]'s integrated 50 V PMOS at 8 Ω and 100 mA.

### Chapter 6 — Integrated Binary-Tree Multilevel Converter at the Battery-Cell Level (ll. 6985–7812) — *first BTMLC silicon (TechRxiv/TPEL paper)*

**Claim:** First fully integrated cell-level multilevel converter: eight-tap binary tree over seven series cells, three logic signals → eight levels (0…7V_cell). **Scaling laws:** levels of switching stages = log₂(n) (l. 7129); N_sw = 2n−2 (eq. 6.2, l. 7154); blocking voltage V_blk,j = V_cell·2^(j−1) (eq. 6.3, l. 7169); switching frequency f_sw,j = n·f_bus/2^(j−1) (eq. 6.4) — i.e. Level I/II/III block V_cell/2V_cell/4V_cell and toggle at 8f/4f/2f (ll. 7206–7208): higher-voltage switches switch slower, enabling off-chip scaling with paralleled low-frequency devices (ll. 7210–7217). **Table 6.1 (ll. 7051–7073), switch count vs level count n:** NPC 4(n−1); FC 4(n−1); CHB 4(n−1); MMC 4(n−1); P2 n(n−1)+4; MLDCL 2(n−1)+4; T-Type (n−3)*/2+4; SSPS 3(n−1)+4; SCSS 2(n−1)+4; CBSC (n+1)*; MLM n*+4; RV 2(n−1)+4; 2SELG (n−1)*+8; **BTMLC 2(n−1)+4** (* = bidirectional switches). Loss model (eqs. 6.6–6.19): predicted total loss **1.522 W at 2 A / 10 kHz** with negligible switching loss; metallisation resistance ≈ channel resistance (ll. 7357–7362). Circuits: stacked-NDMOS level shifter gated from an 8-tap resistive divider (1–2.5 mA, ll. 7433–7435); cross-coupled floating shifters; gate-drive rails from **Zener-based voltage limiters** (6 V Zener + source follower, V_DRV ≈ V_Z − V_GS, ll. 7528–7537). Level III forced to use 24 V devices (only option ≥17 V in the run), inflating path resistance (ll. 7606–7610). **Silicon:** 130 nm BCD, chip area **15.2 mm²** (l. 7614; layout 3.530 mm × 4.297 mm, l. 7640), 33 µm Al wires. **Measured:** path resistance ~0.472 Ω at 2 A DC → ~1.88 W I²R, ~20% above model due to board/bond resistance (ll. 7646–7652); NLC waveforms at 2.5 V and 3.7 V taps, 10 Hz–5 kHz (ll. 7654–7663); ~50 ns overshoot on specific down-transitions (ll. 7664–7678); loaded operation at 33/22/12.7/10 Ω, 3–3.5 V taps, currents to 2 A (Fig. 6.10, ll. 7702–7712); arbitrary random tap sequencing at 12.7 Ω (ll. 7688–7694); dynamic frequency (100 Hz↔5 kHz) and amplitude (3.3 V↔23.1 V) transitions (ll. 7695–7699); chip temperature **50–66 °C** under NLC with 12.7 Ω load (l. 7778). Conclusion: reliable operation DC–5 kHz at up to 2 A, cell voltages 2.5–3.7 V (ll. 7794–7796).

### Chapter 7 — Integrated Capacitively Coupled Modular Full-Bridge Battery Balancing (ll. 7813–8725)

**Claim:** Stackable full-bridge balancer giving continuous cell current (vs half-bridge terminal-cell dead half-cycles), with all switches, drivers, level shifters and dead-time generation on-chip; drive voltages generated internally "at no additional cost" (ll. 1973–1975). New dynamic model for series-connected (non-isolated) cells with derived initial conditions (eqs. 7.1–7.26). Simulations: V₁ = 4.3 V/V₂ = 3.3 V, C_e = 256 µF; at 16 kHz capacitor swing falls to ~0.1 V (resistance-limited); conduction losses dominate at 200 kHz (ll. 8214–8249). Device width ~200 mm (area-constrained, not optimal; ll. 8207–8212). **Silicon:** 130 nm BCD, 5 V NLDMOS, chip **4.68 mm²** (l. 8418; layout 1250 µm × 3750 µm, l. 8424); packaged in an **84-pin JLCC** with two 25 µm gold wires per power pad (ll. 8430–8437). Test: Keithley 2281S-20-6 battery simulators emulating Samsung 18650 Li-ion 3.7 V, 50 mAh, initial SOCs 2%/90–100%; 6×22 µF (132 µF) balancing capacitance; 1–256 kHz (Table 7.1, ll. 8460–8471). **Measured:** gate V_GS rise/fall 24–35 ns, dead-time ~80 ns as designed (ll. 8500–8503); output rise/fall 12–17 ns (ll. 8545–8546); average balancing current ~50 mA at 1 kHz → ~0.55 A above 16 kHz, then resistance-limited (ll. 8566–8569); on-chip switch resistance only ~30 mΩ incl. metallisation — current severely limited by bonds/package/PCB (ll. 8573–8613); continuous current from 8 kHz (FSL onset, ll. 8618–8628); capacitor-voltage swing collapse with frequency to the cell average (ll. 8644–8653); **SOC convergence improves from 17% residual to 1.1% between 5 kHz and 50 kHz over equal time** (ll. 8654–8659); balancing efficiency ~**75% over 10–100 kHz** at 1 V imbalance (ll. 8660–8665). **Table 7.2 (ll. 8673–8686):** This Work = 0.13 µm BCD, fully integrated 5 V HV NDMOS, 4 switches/cell, 0 inductors, 2 caps/cell (132 µF), 0 transformers, AC2AC active, 2 PWM signals, 4.6 mm²; vs [142] (integrated 50 V PMOS, flyback transformer per 7 cells, complex control), [187], [83], [88] (external/discrete switches).

### Chapter 8 — Scalable BTMLC for Higher-Current and Higher-Voltage Operation (ll. 8726–9951) — *the flagship BTMLC IC*

**Claim:** Second-generation eight-tap BTMLC that derives **all** gate-driver supply rails from the battery stack via compact push–pull stages — no Zener regulators, bootstrap capacitors, charge pumps or isolated DC–DCs (ll. 8845–8859); contributions list (ll. 8862–8873): (1) low-cost driver-rail generators + multi-output level shifters at CMOS-compatible voltages; (2) LDMOS switches "providing up to 6 A maximum current capability"; (3) reliable bonding on bond-on-active-circuit (BOAC) pads in low-k technology; (4) "Validation of the stacking capability of the proposed converter design to synthesize 50 V half-sine waveforms under variable-voltage and variable-frequency operation." Same scaling laws as Ch. 6 (eqs. 8.1–8.6, output level eq. 8.2). Loss model at 5 A rms / 10 kHz: total 0.7 W — switching 6.5%, channel conduction 42.6%, metallisation 50.9%; for a 16-tap stack switching rises to 21.7% (ll. 9081–9091). Power devices 5 V / 10 V / 16 V NDMOS for Levels I/II/III (l. 9104); driver-rail synthesis hierarchy in Fig. 8.7 keeps exactly one cell voltage across every gate driver (ll. 9214–9218, 9246–9248); works for cell voltages above 2.5 V given 0.9–1.3 V thresholds (ll. 9216–9218). Converter extension: (log₂n − 1) stacked submodules plus external low-frequency switches (ll. 9292–9313). **Silicon:** 130 nm BCD, chip **20.52 mm²** (l. 9326; 5474 µm × 3750 µm, l. 9334). **JLCC validation:** three 25 µm Au wires/pad; delivers ~2.5 A ("close to the fusing current of the three parallel 25 µm gold wire bonds", ll. 9482–9484); Table 8.1 (ll. 9460–9470): V_in 3.3–23.1 V at ~2 A, R_path 0.385–0.409 Ω; input–output current difference ≤ ~10 mA (level-shifter consumption, ll. 9492–9494); thermal: 66 °C peak at 2 A DC, ~46 °C under NLC (ll. 9495–9505); dead-times 80–85 ns (Levels I–II) and ~250 ns (Level III); V_GS rise/fall 60/30 ns (L-I), 190/35 ns (L-II), 350/50 ns (L-III) (ll. 9511–9516); V_DS confirmed within 3.3/6.6/13.2 V (ll. 9521–9524). **Custom wire-bonded assembly (higher current):** ENIG PCB, 10–12 Al 33 µm wires per pad, output bonded from both sides (ll. 9549–9558). **Path resistance 60–85 mΩ across all taps over 2–6 A** (ll. 9609–9612); **efficiency 98.5% down to 85% across the 2–6 A range** (ll. 9615–9617); heat map at 6 A DC from the eighth tap **without any external cooling** with scale up to 102 °C (Fig. 8.21, ll. 9733–9738); NLC delivery into 4 Ω at 10 Hz–2 kHz, dynamic 10 Hz↔1 kHz and 3.3 V↔23.1 V (ll. 9623–9678). **Stacked-module demonstration:** two BTMLC dies + one off-chip half-bridge of 50 V power MOSFETs across sixteen supply taps, 8 Ω load: sixteen 3.3 V steps forming "smooth half-sine waveforms while simultaneously delivering current to the load", reference stepped 3.3 V ↔ 49.5 V, frequencies 10 Hz–500 Hz (ll. 9679–9731). §8.5 (ll. 9744–9927) proposes a BTMLC with embedded voltage balancing (Level I choppers double as star-SC balancer; halves the switch count vs a separate balancing stage, ll. 9807–9813) with two IC-level designs (Figs. 8.24, 8.25) — design-only, flagged as needing flip-chip for pad count (ll. 9890–9898).

### Chapter 9 — Complementary Integration of Stacked Half-Bridge Circuits for Battery Balancing (ll. 9952–11090)

**Claim:** Two half-bridge balancer chips operated complementarily (dual star networks, two open-loop PWM signals) recover full-bridge performance — continuous cell current, cell-location-independent AC2AC balancing — from the compact half-bridge silicon. Table 9.1 (ll. 10062–10076) extends the component-count comparison with voltage stresses (e.g. star-SC caps stressed to (n−1)V_cell/2; SSC switch stress nV_cell). Analytical model (eqs. 9.1–9.18) shows half-bridge-only operation gives terminal cells zero current for half the cycle and a poor DC-to-RMS ratio (ll. 10276–10286). Device width 64 mm → ~76 mW at 100 kHz / 2.5 A (ll. 10479–10482). **Silicon:** same 3.4 mm² 130 nm BCD chip as Ch. 5 (l. 10621), two chips + eight capacitors in dual-star; Table 9.2 (ll. 10700–10714): 2×100 µF per output, inputs 2.5–4.3 V, 1 kHz–1 MHz, B-Box RCP controller, 6–8 Al 33 µm wires/pad. **Measured:** average balancing current 0.5 A at 4 kHz → ~2.25 A at 32–64 kHz for terminal cells; **middle cells from ~1 A up to ~2.5 A** at maximum imbalance (ll. 10759–10772); SSL below ~8 kHz, FSL above; **average-to-RMS current ratio approaches unity above 20 kHz** for all cells (ll. 10817–10823); the single half-bridge reference achieves roughly half the average current and needs ~4× the frequency for the same DC-to-RMS ratio at terminal cells (ll. 10823–10828); SOC equalisation at 32 kHz with 25 mAh emulated cells to residual SOC deltas of 1.0–2.8% across scenarios (Fig. 9.21, ll. 10864–10889). Table 9.3 (ll. 10914–10927): fully integrated 5 V NLDMOS, 4 switches/cell, 2×200 µF caps/cell, no inductors/transformers. Chapter delivers the headline "up to 2.5 A average balancing current under a 0.75 V voltage difference between any cell and the overall average" (ll. 2005–2007).

### Chapter 10 — Conclusions (ll. 11091–11120)

Restates the demonstrated platform: three level-shifter circuits, integrated half-/full-bridge balancers, fully integrated BTMLCs with high-resolution cell-level synthesis, all "using mature, low-cost silicon technologies, avoiding reliance on expensive and scarce wide-bandgap devices" (ll. 11100–11102).

### Chapter 11 — Work Limitations (ll. 11121–11171) — quoted in §4b

BTMLC: ~25–30 V / 6 A limits; no full-AC polarity stage; no floating supply for topmost high-side switch (direct supply used); **resistive-load-only validation, no motor/inductive loads, no charging tests, ESD-only protection**. Balancers: static-load validation only; battery simulators, not physical cells; JLCC packaging limited the full-bridge balancer to ~0.5 A against a >3 A design target while the custom-bonded half-bridge reached 2.5 A (ll. 11158–11164); no fault protection or sensing; magnetic balancing networks unexplored.

### Chapter 12 — Future Work (ll. 11177–11257) — quoted in §4c

Technology level: BCD-on-SOI; automated power-switch layout CAD. Circuit level: merged balancing+conversion chip (flip-chip), device stacking for Levels II/III from 5 V devices, on-chip charge-pump auxiliary rails. System/board level: inductive and motor loads; full AC output; charging mode; stacking 12–16 modules to 300–400 V; real battery packs. Balancer enhancements: mesh/delta networks; 22/44 µF capacitors at 500 kHz–1 MHz; series inrush inductors; stud-bumping; multi-winding transformer alternative. Monitoring: fault diagnosis, on-chip thermal sensing, MEMS thermal management, electrochemical state-of-health sensing.

## 4. Proposal-critical passages (exact quotes with line numbers)

### (a) Discrete floating-domain infrastructure cannot scale; IC integration is a necessity

- ll. 2355–2359: "If these cells are to be processed individually or interfaced with the motor through decentralised converter units operating at the cell level, the approach offers several advantages; however, it also introduces a substantial increase in the number of required switches. Consequently, **this issue cannot be effectively addressed solely through fully onboard solutions based on discrete switches and conventional gate-driving techniques.**"
- ll. 1732–1736: "The availability of high-quality discrete semiconductor switches is particularly limited in low-voltage applications, as encountered in Multilevel Converters (MLCs) operating at battery-voltage levels (e.g., Li-ion cells with a voltage range of 2.5 V–4.3 V). These voltages are insufficient to drive discrete semiconductor switches directly and thus require dedicated isolated DC–DC converters."
- ll. 3328–3343 (research-gap list, §2.10): "Discretely implemented switched-capacitor balancing networks are also impractical for the following reasons: 1. Parasitic resistance (Rpar) directly limits the achievable balancing current at high switching speeds. 2. High voltage ratings of capacitors necessitate operation at very high frequencies… 3. Parasitic inductance (Lpar) constrains the switching frequency, hence reducing balancing speed. 4. The overall component count is excessive, requiring numerous switches, gate drivers, signal isolators, and floating driver supplies. 5. **Suitable discrete switches are unavailable for low-voltage operation (e.g., 2–4.3 V typical for Li-ion cells)**, leading to suboptimal designs with increased switching losses, higher leakage, and complex gate-drive requirements. 6. Integration with BMS functionalities becomes challenging…"
- ll. 4819–4828 (Ch. 3 conclusions): "In contrast, discrete vertical devices are not well suited for highly integrated, large-scale converter implementations where a large number of switches is required. Their bulkiness, the need for dedicated gate drivers and isolated supplies, and the reduced reliability arising from numerous electrical connections, joints, and soldered interfaces limit their applicability. Therefore, **a key theme pursued in this thesis is reducing the number of discrete devices and migrating the high-switch-count portion of multilevel converters onto the chip**, whilst retaining only a small number of off-chip switches that handle high voltage but operate at low switching speeds."
- ll. 4146–4148 (multi-winding transformer gate drive): "However, this solution becomes bulky, expensive, and difficult to scale or modularize as the number of converter levels or battery cells increases."
- ll. 1696–1700: "conventional board-level implementations using discrete switches and bulky components introduce significant parasitic effects, resulting in slower balancing and reduced efficiency due to additional losses and leakage currents."

### (b) Chapter 11 work limitations (verbatim)

- ll. 11130–11137: "First, **the current implementation is limited to operating voltages of approximately 25–30 V** due to the breakdown characteristics of the selected semiconductor process, **and to output currents up to 6 A** based on the switch sizing and the in-house wire-bonded prototype. Furthermore, the converter has not been extended to full AC waveform generation; achieving bipolar output in single-phase operation would require an additional full-bridge or polarity-reversal stage."
- ll. 11145–11148: "**The converter has been experimentally validated only under predominantly resistive loads. Its performance under highly inductive or dynamically varying loads (e.g., motor loads) has not been rigorously evaluated.** Similarly, battery-charging operation has not yet been tested, although the bidirectional architecture is expected to support it."
- ll. 11153–11156 (balancers): "Experimental validation was conducted under static load conditions only… testing was performed using precision battery simulators emulating Li-ion behaviour, rather than physical battery cells."
- ll. 11159–11164: "The use of a standard JLCC package with wire bonding introduced large parasitic inductances and resistances, limiting the maximum balancing current to approximately 0.5 A, despite the design target exceeding 3 A."

### (c) Chapter 12 future work (verbatim items, ll. 11216–11223)

"**12.3 System and Board Level** • Experimental evaluation with various load types (e.g., **inductive and motor loads**) and corresponding output-filtering strategies. • **Extension to full-bridge or waveform-reversal topologies to enable full AC output.** • **Implementation of charging-mode functionality.** • **Scaling the system by stacking multiple modules to increase current and/or voltage capability (e.g., 12–16 modules to reach 300–400 V).** • Integration with real battery packs (pouch, prismatic, and cylindrical Li-ion cells)."

### (d) Bootstrap-supply incompatibility with motor-drive PWM

- ll. 4200–4207: "A widely adopted method for supplying a floating rail to a high-side gate driver is the bootstrap (BS) charge-pump configuration… This solution provides a cost-effective and simple means of generating the required gate bias in systems characterized by repetitive switching patterns, such as pulse-width modulated (PWM) converters… **Conversely, drive systems such as motor inverters, which may experience irregular PWM patterns (e.g., during regenerative braking), are generally incompatible with pure bootstrap solutions** [149, 49]."
- Supporting: ll. 4436–4443 — "the BS technique becomes unsuitable for multilevel converters operating with modulation indices below (m−3)/(m−1)"; ll. 3860–3862 — bootstrap-based stacked topologies "become impractical for low-speed operation or circuits without periodic switching"; ll. 4213–4215 — "Typical bootstrap capacitance values are on the order of 100 nF, which is generally too large for monolithic integration."

### (e) Stacked-module results (50 V / 6 A / 98.5%, 60–85 mΩ)

- ll. 1990–1994 (Ch. 8 summary): "The stacking capability is further demonstrated by integrating two modules on board and combining their outputs through an off-chip half-bridge power stage. **Measurements confirm that the converter can synthesize variable-frequency and/or variable-magnitude half-sine waveforms while delivering up to 6 A to a resistive load with a peak efficiency of 98.5%.**"
- ll. 9609–9612: "the path resistance was evaluated by operating a single converter module as a DC–DC tap-selector while sourcing DC currents from 2 A to 6 A. As shown in Fig. 8.19, **the estimated total resistance across all voltage taps ranged from 60 mΩ to 85 mΩ over the tested current range.**"
- ll. 9615–9617: "the converter efficiency across all taps within the 2–6 A range is presented in Fig. 8.20. **The measured efficiency varied from 98.5% to 85%**, demonstrating the effectiveness of the optimized converter layout and the positive impact of the BOAC pads design."
- ll. 9684–9688: "the stacked configuration synthesizes voltage waveforms with sixteen discrete steps of 3.3 V resolution, producing smooth half-sine waveforms while simultaneously delivering current to the load at varying frequencies and voltage levels. For example, **the reference modulation waveform was stepped from 3.3 V to 49.5 V** and vice versa."
- l. 8872–8873 (contribution 4): "Validation of the stacking capability of the proposed converter design to synthesize **50 V half-sine waveforms** under variable-voltage and variable-frequency operation."

## PROPOSAL USE MAP (detailed)

**Conventions.** (i) **Anonymisation:** the thesis is never named or attributed in proposal body text. Vision wording: "the group's doctoral work". Approach wording: "the doctoral thesis underpinning the BTMLC platform" or "the group's doctoral work". The author appears only in the reference list entry and, subject to PI confirmation, in the R4RI track-record section. (ii) **Citation keys** cited below are the current draft-local keys (Vision: [1] BTMLC IC, [2] TCAS-I level shifters, [20] HB-MLI motor drive, [21] doctoral work; Approach: [1,2,4] BTMLC lineage, [3] DCAT, [5] on-chip isolation, [6] HB-MLI). All keys renumber via Map B before submission. (iii) **Usage modes:** QUOTE (verbatim, quotation marks, anonymised attribution), PARA (close paraphrase), NUM (specific measured figure), GAP (defines the research gap the proposal fills), CAP (capability and track-record evidence). (iv) Fragments are UK English, free of em dashes, and drop-in ready. (v) The ten highest-value items are marked ★.

### A. The three Chapter 12 future-work items (ll. 11216 to 11223): the proposal's licence to exist

These bullets are the highest-leverage passages in the thesis: the platform's own documentation names the proposed programme as its next step. Each anchors three proposal locations simultaneously: the "why this is now possible" argument (Vision, VIS-CROSS-v7 second paragraph "The claim is buildable now, and only now", reinforced in VIS-TIME-v7 / the settled Timeliness sub-heading); the Approach section "Building on previous work" (whose drafted closing sentence already quotes the first item); and the WP2 gap statement ("previously validated only against low-impedance battery-cell sources [1,2,4]").

**A1 ★ — "inductive and motor loads" future-work bullet (ll. 11217 to 11218, quoted in section 4c).**
- (a) Location: Approach, "Building on previous work", final sentence (already drafted; retain); WP2 aim sentence and gap statement (RQ2, H2, Gap 2, O2); risk-table row "ZVS lost under inductive winding source"; Vision VIS-CROSS-v7 closing sentences ("what does not yet exist is the science of operating it inside a rotating machine").
- (b) Mode: QUOTE + GAP. The single cleanest warrant for RQ2/H2: the platform's designers state in print that inductive and motor loads are untested, so the proposal's central circuit question is the declared continuation of the group's own roadmap, not a retrofitted justification.
- (c) Fragment (Building on previous work, as drafted, keep): "And the doctoral thesis underpinning the BTMLC platform explicitly lists 'experimental evaluation with various load types (e.g., inductive and motor loads)' as future work; the programme proposed here is precisely that work, extended to per-slot resolution inside the machine." Fragment (WP2 aim variant): "The per-slot circuit architecture has been silicon-validated only against low-impedance battery-cell sources, and the group's doctoral work identifies inductive and motor loads as the platform's untested frontier. WP2 crosses that frontier: it establishes whether, and over what envelope, adiabatic operation survives when the source is an inductive winding section with speed-dependent back-EMF."

**A2 ★ — full-AC future-work bullet ("Extension to full-bridge or waveform-reversal topologies to enable full AC output", l. 11219), paired with the Chapter 11 admission that the converter has no polarity stage (ll. 11134 to 11137).**
- (a) Location: WP2 gap statement and RQ2/H2 (the bilateral requirement); lineage table, BTMLC row, gap column; Vision VIS-CROSS-v7 ("bilateral integrated-circuit pair" as the architectural move) and the "buildable now" paragraph.
- (b) Mode: GAP + PARA. All demonstrated waveforms are unipolar half-sines; a machine winding needs bipolar drive. This converts the proposal's bilateral IC pair from a design choice into the exact structural answer to a gap the thesis names, and simultaneously polices the capability claims (see Trap 4).
- (c) Fragment: "The demonstrated converter synthesises unipolar half-sine waveforms; full AC output is identified in the group's doctoral work as requiring an additional polarity-reversal stage. The bilateral per-slot IC pair proposed here supplies exactly that capability, realised not as an appended full bridge but as the machine's own excitation architecture."

**A3 ★ — stacking route "12 to 16 modules to reach 300 to 400 V" (ll. 11221 to 11222), read together with the demonstrated two-module stack (Chapter 8, section 4e).**
- (a) Location: Vision VIS-TIME-v7 and VIS-CROSS-v7 ("buildable now"); Approach, "Building on previous work", the drafted stacking sentence (approximately 49.5 V, up to 6 A, 98.5% peak, [PI TO CONFIRM: preprint citation]); WP4 aim (credibility of the 270 V bus); WP2 CAP.
- (b) Mode: NUM + GAP + CAP. Two halves of one argument: the measured half (two BTMLC dies plus one off-chip half-bridge reached 49.5 V at up to 6 A, 98.5% peak efficiency, ll. 9679 to 9731) and the declared route (12 to 16 modules to 300 to 400 V). The proposal's 270 V bus therefore sits inside the platform's own documented scaling envelope: an engineering step along a stated route, not a speculative leap.
- (c) Fragment: "The platform already stacks: two converter dies combined through one off-chip half-bridge synthesised sixteen-step half-sine waveforms to approximately 49.5 V while delivering up to 6 A at 98.5% peak efficiency, and the group's doctoral work sets out the module-stacking route to 300 to 400 V. The 270 V aerospace bus targeted here lies within that documented envelope."

### B. The discrete-cannot-scale passages (section 4a): the necessity argument

These quotes carry the proposal's strongest structural claim: monolithic integration is a necessity, not an optimisation. They anchor (i) the Vision "buildable now, and only now" paragraph, which turns on the impossibility of a discrete implementation ("roughly 36 times for 18 slots... the control hardware alone would exceed the machine volume"); (ii) the Timeliness argument ("physically unrealisable before this silicon existed"); and (iii) the WP2 gap statement. **Handling note:** WP2's own experimental vehicle is 12 to 18 discrete boards, so deploy these passages against product-scale implementation, never against bench feasibility; the drafted phrases "discrete functional-equivalent prototype boards" and "monolithic IC fabrication is therefore a stretch enhancement, not a programme dependency" hold that distinction and must be preserved wherever a section 4a quote is used (see Trap 8).

**B1 ★ — ll. 2355 to 2359: cell-level processing "cannot be effectively addressed solely through fully onboard solutions based on discrete switches and conventional gate-driving techniques".**
- (a) Location: Vision VIS-CROSS-v7, the discrete-implementation sentence and the two sentences that follow it; Vision Timeliness; preamble of the WP2 gap statement (RQ2, H2).
- (b) Mode: PARA (or QUOTE with anonymised attribution) + GAP. Direct evidential backing for "The architecture was not previously undiscovered; it was physically unrealisable before this silicon existed."
- (c) Fragment: "Driving power at the level of individual winding sections multiplies the number of floating switching domains, and the group's doctoral work shows that this cannot be addressed with discrete switches and conventional gate-driving techniques: the floating-domain infrastructure must be monolithic."

**B2 ★ — section 2.10 research-gap list, ll. 3328 to 3343: no suitable discrete switches at 2 to 4.3 V; board-level parasitic resistance and inductance cap current and switching frequency; excessive component count (switches, gate drivers, signal isolators, floating supplies).**
- (a) Location: WP2 gap statement (RQ2, H2); Vision VIS-CROSS-v7; "Feasibility and risk management" (why 20 to 50 V per-section operation is poorly served by discrete devices at product scale).
- (b) Mode: PARA + GAP + NUM. The itemised list is the most citable form of the necessity argument; items 1, 3 and 5 map one-to-one onto the per-slot case.
- (c) Fragment: "At tens of volts per section, high-quality discrete switches are scarce, and board-level parasitic resistance and inductance directly cap the achievable current and switching frequency; the group's doctoral work documents both limits and demonstrates the monolithic alternative in a mature 130 nm process."

**B3 ★ — Chapter 3 conclusion, ll. 4819 to 4828: migrate the high-switch-count portion on-chip, retain few off-chip high-voltage low-frequency switches.**
- (a) Location: Vision VIS-CROSS-v7 (why the IC is simultaneously excitation source and switching element); WP2 architecture rationale; "Building on previous work" prose.
- (b) Mode: PARA. The thesis's design philosophy in one sentence, and it is also the per-slot architecture's: many fast low-voltage switches integrated at section level, few slow high-voltage devices, and in the proposed machine no full-voltage stage at all.
- (c) Fragment: "The design principle established in the group's doctoral work, migrating the high-switch-count low-voltage portion of a multilevel system onto the chip while retaining only a few slow high-voltage devices off-chip, transfers directly to the stator: each slot's fast switching is monolithic, and no full-voltage power stage exists anywhere in the machine."

**B4 ★ — bootstrap incompatibility with motor-drive PWM (ll. 4200 to 4207; supported by ll. 4436 to 4443, 3860 to 3862, 4213 to 4215).**
- (a) Location: RQ2/H2 motivation; WP2 T2.2 and T2.3 (floating-domain control and supply under irregular excitation); risk-table row on ZVS loss.
- (b) Mode: PARA + GAP. Evidences why per-slot floating supplies cannot be bootstrap-based under machine-drive conditions (irregular PWM, regenerative intervals, low modulation index, roughly 100 nF capacitances too large to integrate), which motivates Chapter 8's battery-derived push-pull rail generation (ll. 9206 to 9285) as WP2's starting point and sharpens RQ2's "circuit conditions" clause.
- (c) Fragment: "Bootstrap floating supplies fail precisely under motor-drive conditions: irregular modulation patterns, regenerative intervals and low modulation indices defeat the periodic refresh they require, and typical bootstrap capacitances are too large to integrate monolithically. The group's doctoral work demonstrated the alternative, deriving every gate-drive rail from the stack itself; WP2 adapts that principle to winding-fed domains."

### C. Chapter 11 limitations: the honest gap ledger

**C1 ★ — resistive-load-only validation (ll. 11145 to 11148: "experimentally validated only under predominantly resistive loads... motor loads... has not been rigorously evaluated").**
- (a) Location: WP2 gap statement (drafted: "previously validated only against low-impedance battery-cell sources [1,2,4]"); lineage table, BTMLC row, gap column ("Battery-cell resistive loads only"); Gap 2 in "Hypotheses and objectives"; H2.
- (b) Mode: QUOTE or PARA + GAP. The mirror image of A1: A1 is the forward-looking declaration, C1 the backward-looking admission. Use it to keep every capability claim reviewer-proof: nothing in the silicon record has touched a machine (see Trap 2).
- (c) Fragment: "Every silicon demonstration to date, including the stacked 49.5 V, 6 A system, was validated under predominantly resistive loads from low-impedance battery-cell sources; behaviour with inductive sources and back-EMF is explicitly untested. That untested regime is exactly where this programme operates."

**C2 — 25 to 30 V and 6 A operating envelope (ll. 11130 to 11134).**
- (a) Location: WP2 (RQ2, H2); Vision VIS-CROSS-v7 (congruence with "no section ever sees more than 20-50 V").
- (b) Mode: NUM + CAP. The proposal's 20 to 50 V per-section envelope lies at, and slightly beyond, the demonstrated silicon range; state the demonstrated range honestly and let WP2 own the extension.
- (c) Fragment: "The proposed 20 to 50 V per-section envelope corresponds to the range already demonstrated in silicon, approximately 25 to 30 V and up to 6 A in the group's doctoral work, with the upper portion reached by the same module-stacking mechanism the programme employs."

**C3 — packaging-limited current: 0.5 A in a standard JLCC against a design target above 3 A; approximately 2.5 A near bond-wire fusing; custom assembly needed for 6 A (ll. 11158 to 11164; Ch. 8 ll. 9482 to 9484, 9549 to 9558; Ch. 3 packaging survey ll. 4547 to 4808).**
- (a) Location: RQ5, H5, Gap 2; WP2 T2.3 packaging specification (Co-I Everts strand); risk row "IC junction temperature exceeds limit"; WP4 T4.2 thermal characterisation.
- (b) Mode: NUM + GAP + CAP. Proves packaging, not silicon, is the binding constraint, which is precisely why RQ5 makes packaging geometry a research question and why the thermal strand exists.
- (c) Fragment: "In the group's doctoral work the same silicon delivered 0.5 A in a standard wire-bonded package and 2.5 A to 6 A with progressively customised bonding: an order-of-magnitude spread set entirely by packaging. Packaging geometry, not device capability, therefore defines the per-slot module's current and thermal envelope, and WP2 treats it as a research output rather than an implementation detail."

### D. Measured silicon facts: capability and parameter anchors

**D1 ★ — complete per-slot drive infrastructure on one 15.2 mm² die (Ch. 6, l. 7614; second generation 20.52 mm², Ch. 8, l. 9326).**
- (a) Location: Vision VIS-CROSS-v7, the drafted sentence citing [1]; lineage table, BTMLC row; "Research environment and facilities" ("IC design flows... transfer directly into WP2"); Capability module (R4RI).
- (b) Mode: NUM + CAP. The physical basis of "buildable now": power switches, gate drivers, level shifters, dead-time generation and floating supplies on one die.
- (c) Fragment (drafted, keep): "The group has demonstrated the complete per-slot drive infrastructure, power switches, gate drivers, level shifters, dead-time generation and floating supplies, on a single 15.2 mm² die in 130 nm BCD [1]." Note: if both generations are mentioned, distinguish them; the 20.52 mm² second generation adds battery-derived driver rails and the 6 A capability.

**D2 ★ — Chapter 8 measured performance: path resistance 60 to 85 milliohms over 2 to 6 A (ll. 9609 to 9612); efficiency 98.5% to 85% (ll. 9615 to 9617); 6 A DC without external cooling (l. 9733); 66 degrees C at 2 A DC and approximately 46 degrees C under NLC (ll. 9495 to 9505).**
- (a) Location: WP2 CAP and T2.3 parameterisation of the thermal network (RQ5, H5); WP4 efficiency and thermal baselines; Vision Timeliness ("demonstrated only within the present cycle").
- (b) Mode: NUM + CAP. These numbers make the per-slot power level credible; the thermal figures seed H5's junction-temperature analysis (see Trap 5 on quoting the efficiency range).
- (c) Fragment: "The second-generation module measured 60 to 85 milliohms of total path resistance while sourcing 2 to 6 A, with efficiency from 98.5% peak, and delivered 6 A continuously without external cooling."

**D3 — multi-output level shifters with dead-time control (Ch. 4): approximately 2 ns measured propagation, 22 to 66 times dead-time-spread reduction, supply compliance to 1.8 V, 130 nm BCD.**
- (a) Location: Vision VIS-CROSS-v7, "[2] floating-domain level shifting in the same process"; lineage table row "TCAS-I level shifter (2026)"; WP2 T2.2 adjacency; Capability module.
- (b) Mode: NUM + CAP. Cite through the published TCAS-I paper (A8) rather than the thesis wherever possible; Chapter 4 is its basis. Note the attribution boundary in Trap 7: the separate "on-chip digital isolation" claim ([5] in Approach, [21] in Vision) belongs to the other doctoral thesis.
- (c) Fragment: "Floating-domain gate-drive signalling with built-in dead-time control has been silicon-validated in the same 130 nm BCD process, with measured propagation delays of approximately 2 ns and supply compliance below 2 V [2]."

**D4 — bounded per-domain voltage stress: measured V_DS confined within 3.3/6.6/13.2 V against 5/10/16 V ratings (ll. 9521 to 9524); every gate domain held to one cell voltage by construction (ll. 9246 to 9248); 50 to 100 ns transition overshoots observed (ll. 7664 to 7678, 9412 to 9445).**
- (a) Location: RQ3, H3 (transient per-slot voltage distribution against the Paschen threshold); WP1 T1.3 cross-reference; Vision "The unseen line" (Paschen argument) as supporting evidence.
- (b) Mode: NUM + CAP + GAP. Module-level proof that per-domain stress is controllable and measurable; the observed overshoots are the exact class of event targeted by RQ3's clause "even if the steady-state per-slot voltage remains safely below it", scaled to the winding.
- (c) Fragment: "Measured device stresses in the stacked module remained confined within each level's rating, and every gate domain was bounded to one cell voltage by construction; the nanosecond-scale transition overshoots observed at module level are precisely the class of transient RQ3 quantifies at winding scale."

**D5 — arbitrary and dynamic reconfiguration: random tap sequencing under load (ll. 7688 to 7694); dynamic reference transitions 3.3 V to 23.1 V and 10 Hz to 1 kHz single-module, 3.3 V to 49.5 V stacked (ll. 7695 to 7699, 9670 to 9688); eight levels from three logic signals, N_sw = 2(n-1)+4 (Table 6.1).**
- (a) Location: RQ4, H4; WP3 (2N-DOF reconfiguration and fault re-optimisation); Vision "The cascade and its price" (pole count as a software parameter).
- (b) Mode: CAP + NUM. Demonstrates fast arbitrary per-level reconfigurability with minimal control overhead, the property WP3's spatial-field control assumes.
- (c) Fragment: "The converter followed arbitrary random tap sequences and stepped its reference between 3.3 V and 49.5 V, and between 10 Hz and 1 kHz, while delivering load current; three logic signals command eight levels. This is the fast, low-overhead reconfigurability that software-defined spatial field control requires."

**D6 — four silicon generations of stacked-domain power ICs (Chs. 4 to 9): 3.4, 4.68, 15.2 and 20.52 mm² chips; 1 kHz to 5 MHz operation; up to 2.5 A balancing and 6 A conversion; autonomous sensorless open-loop equalisation.**
- (a) Location: Capability module (R4RI track record); "Research environment and facilities". Not WP content.
- (b) Mode: CAP. Track-record breadth: design, fabrication, packaging and characterisation repeatedly closed in the same process.
- (c) Fragment: "Across four silicon generations in one 130 nm BCD process the group has designed, fabricated, packaged and characterised stacked-domain power ICs from 3.4 to 20.5 square millimetres, operating from 1 kHz to 5 MHz and delivering up to 6 A."

**D7 — EPSRC studentship funding of the doctoral work (grant EP/T517793/1, Project Reference 2600345; ll. 142 to 145).**
- (a) Location: Vision "National importance" and funder-fit paragraph; Capability module.
- (b) Mode: CAP. Continuity-of-investment argument: the enabling silicon lineage was itself EPSRC-funded.
- (c) Fragment: "The doctoral work that produced the enabling silicon was supported by an EPSRC studentship; this programme carries that investment from the battery domain into the machine."

**D8 — APC roadmap targets and policy context (Table 1.1, ll. 1413 to 1439; Jet Zero and UK semiconductor strategy, ll. 1294 to 1335).**
- (a) Location: Vision Timeliness and National importance.
- (b) Mode: background locator only. Cite the APC roadmap and Jet Zero strategy directly as primary sources; use the thesis only to locate them, never as the citation.

### Traps

1. **Dating.** The thesis title page is dated 25 November 2025; the degree completes in 2026 and the derived papers (TPEL, TCAS-I) are 2026 publications. Do not cite the thesis itself as a 2026 document: a reviewer who retrieves it will see 2025 on the title page. The "doctoral thesis, 2026" rows in the drafted lineage table refer to the other two group theses (February and April 2026); keep this thesis's reference-list entry at 2025 (or the confirmed award date) and let the 2026 dates attach to the published papers only.
2. **Resistive-only is not machine-validated.** Nothing in this thesis drove a machine. The induction-motor demonstration in the lineage (HB-MLI motor drive, [6]/[20]) is a different doctoral project. Never imply the BTMLC IC or its stacked configuration was validated on inductive or motor loads; the 98.5%, 6 A and 49.5 V figures are all resistive-load results (Ch. 11, ll. 11145 to 11148) and should carry the words "resistive load" whenever quoted as performance.
3. **Author naming.** In all proposal body text the thesis is "the group's doctoral work" or "the doctoral thesis underpinning the BTMLC platform". The author's name appears only in the reference list and, if the PI approves, in the R4RI track record. Avoid possessives or descriptions that de-anonymise (for example "our recently graduated student's thesis").
4. **Half-sine is not AC.** The stacked 49.5 V waveforms are unipolar half-sines; do not describe them as AC output or sine waves. Full AC is a declared gap (item A2); claiming it as demonstrated would contradict the proposal's own gap statement.
5. **Efficiency is a range with a peak.** Measured efficiency runs from 98.5% down to 85% over 2 to 6 A. Write "98.5% peak" or give the range; do not reproduce the abstract's flat "at least 98.5% system efficiency" phrasing as if it held across the envelope.
6. **Current claims are assembly-specific.** 6 A: custom wire-bonded assembly; approximately 2.5 A: JLCC package, near bond-wire fusing; approximately 0.5 A: full-bridge balancer in JLCC against a design target above 3 A. Attach the assembly context, or reserve "up to 6 A" for the custom assembly only.
7. **Isolation attribution.** The "on-chip digital isolation" claim ([5] in Approach T2.2, [21] in Vision) belongs to the other doctoral thesis, not this one. This thesis contributes the level shifters (published as the TCAS-I paper, [2]/A8). Do not cite this thesis, or this digest's Chapter 4 material, for the isolation claim.
8. **Necessity argument versus WP2's discrete boards.** The discrete-cannot-scale quotes (section B) target product-scale, roughly 36-domain implementation; WP2's 12 to 18 boards are research-scale functional equivalents. Keep the drafted line "monolithic IC fabrication is therefore a stretch enhancement, not a programme dependency" adjacent to any use of these quotes, or a reviewer will read the two as contradictory.
9. **First-claims.** "The first miniaturised multilevel conversion system operating directly at the cell-voltage level" is the thesis's own claim in the battery domain; if used, attribute it and keep it there. It must not be conflated with the proposal's separate first-claim that no prior work achieves per-slot bilateral IC drive in a rotating machine.
10. **Citation keys are draft-local.** The Approach preamble states its keys are pre-renumbering; every key quoted in this map must be renumbered against Part 1 of drafts/06_References.md via Map B before any fragment is pasted into submission text.
---
*Digest covers ll. 1–11262 (front matter through Chapter 12); references (ll. 11263 ff.) consulted for citation identity only. No content invented; all figures as printed in the thesis text.*


<!-- ==================== FILE: evidence/04_Tazehkand_thesis_digest.md ==================== -->

# Thesis Digest — Tazehkand, "Cell Scale Power Processing for Battery Electric Vehicles"

*Evidence dossier item 04 for the EPSRC per-slot machine drives proposal. Internal document — author names appear here but must NOT appear in proposal text (anonymisation rule, Master Handover §3). Page numbers are printed thesis pages. Source: `/home/user/proposal/Final_Thesis_Mehdi_Z_00.pdf` (234 pp., created 15 April 2026).*

---

## 1. Identity

As printed on the title page (p. 1):

> **Cell Scale Power Processing for Battery Electric Vehicles**
> Mehdi Zarei Tazehkand
> A dissertation submitted in partial fulfillment of the requirements for the degree of Doctor of Philosophy of University College London.
> Department of Mechanical Engineering, University College London
> April, 2026

Declaration of sole authorship signed by the candidate (p. 2). Principal supervisor: Dr Mehdi Baghdadi; subsidiary supervisor: Dr Dai Jiang (Acknowledgements, p. 5). Seven chapters, bibliography from p. 221.

## 2. Thesis argument in one paragraph

The thesis argues that the conventional BEV powertrain — discrete inverter, on-board charger, DC/DC converter and balancer around a monolithic battery pack — should be replaced by distributed power processing built from repeated, identical, low-voltage modules. The load-bearing definition appears in §1.4 (p. 34): "the powertrain is composed of modular elements referred to as unified power units (UPUs). Each UPU consists of a single battery cell or a small group of cells integrated with its own power electronics. These UPUs are interconnected to form a unified powertrain that combines the functionalities of multiple components used in conventional architecture." With appropriate control the same hardware drives the motor, charges from the grid, supplies auxiliary loads and self-balances, eliminating the dedicated DC/DC converter and external balancer (pp. 34–35). Claimed dividends: high-voltage scalability from cheap low-voltage semiconductors, fault bypass and graceful degradation, filter-free multilevel waveforms, high partial-load efficiency across the drive cycle, maintainability and recyclability (pp. 34–36). The remaining chapters remove the obstacles in turn: discrete UPU design practice (Ch. 2), monolithic integration of the power submodule including on-chip galvanic signal isolation across floating domains (Ch. 3), sensor-free modulation for equal energy extraction (Ch. 4), a high-speed switched-capacitor active balancer (Ch. 5), and near-perfectly coupled low-impedance magnetics for magnetic balancers (Ch. 6).

## 3. Chapter-by-chapter walk

### Chapter 1 — Overview and Objectives (pp. 25–38)

**Claim.** BEV adoption is limited by charging time, range and price premium (Deloitte 2025 survey, p. 30); BEV manufacturing cost is ~11 % above ICEV (ICCT), the gap sitting entirely in the powertrain ($11,030 vs $6,800), of which the battery pack is ~72 % and power electronics ~12 % (pp. 30–31). Power electronics, though a small cost fraction, leverage every other subsystem (pp. 31–32). Conventional-architecture shortfalls (pp. 32–34): six-pack IGBT inverters reach ~97 % at rated power but ~80 % at 10 % load, 80–95 % over WLTP; the trend to 800–900 V packs (Table 1.1, p. 34: Taycan, Lucid Air, EV6, IONIQ 6, BYD HAN, XPENG G9) demands costly high-blocking-voltage devices; poor recyclability; permanently live high-voltage DC after a crash. §1.4 (pp. 34–37) gives the UPU answer and the thesis roadmap (Fig. 1.13, p. 38).

### Chapter 2 — A Discrete Cell Scale System: Challenges and Considerations (pp. 39–62)

**Claim.** Distributed battery inverters are an emerging industrial trend, but no certified product serves BEVs; a discrete UPU is therefore designed end-to-end to expose the real engineering challenges.

**State of the art (pp. 39–42).** Module level: Element Energy (claims up to 50 % lifetime and 50 % energy-throughput gains), Stellantis/Saft/CNRS IBIS, TAE ACi Pack, Scalvy (claims 5× footprint and 30 % capex reduction, AC to 3 kV). Cell level: SwitchESS (15 % lifetime claim), BAVERTIS/Pulstrain, Hagal, Exro. Only three certified products: Instagrid (20 × 2 kWh, 3.6 kW/1 kW), SAX Power Home (5.76 kWh, 4.6 kW), Relectrify AC1 (~4,000 individually controlled cells; up to 20 % more usable energy, 40 % less degradation over 20 years). "Significantly, none of the companies with certified products currently serve the BEV sector, underscoring a critical gap in the market" (p. 41).

**Topology assessment (pp. 42–47).** Multilevel architectures are justified for low-voltage BEV use via [12]: a 7-level Si CHB beats six-pack IGBT and SiC inverters on drive-cycle efficiency (p. 43); its inverter cost is 41 % above IGBT but 32.6 % below SiC, and with the battery included it yields the lowest total cost (p. 44). Of six compared topologies (p. 45), series-connected-cell types (flying capacitor, diode-clamped, P2) are rejected as still centralised; isolated-cell types (MMC, BM3, CHB) form identical battery-integrated submodules (Table 2.2, p. 46: MMC half-bridge bypass/series-positive; BM3 adds parallel, one extra switch; CHB H-bridge adds series-negative, two extra). Three-phase CHB needs half the submodules of MMC/BM3 for the same line-to-line voltage, generating negative levels natively (p. 47). The CHB H-bridge is selected for the discrete UPU.

**Case-study UPU design (pp. 47–62), key decisions.** Configurations (p. 48): one-cell-per-UPU (highest fault tolerance/cost), parallel-group-per-UPU, series-string-per-UPU (high voltage, low current, circulating-current risk), all combinable. UPU anatomy (p. 50): battery, power stage, gate drivers, isolation, signal conditioning, protections, local microcontroller, supply regulators, terminals, thermal management. Supply architecture (p. 51): autonomous UPUs powered from their own cell are adopted over centrally distributed isolated supplies — each UPU then needs a **digital isolator** to recover the central controller's signal across the isolation boundary (pp. 51–52), the requirement Chapter 3's OCI internalises on-chip. Battery: four 43 Ah same-side-tab pouch cells in parallel, **≈620 Wh and 620 W / 1.24 kW continuous/peak (1C/2C)** (p. 54). Microcontroller: STM32G4A1KEU6 (170 MHz, p. 55). Supplies (pp. 55–56): battery 2.5–4.2 V; ISL9120IRTNZ 3.3 V regulator; LTC3122EDE 10 V gate rail guaranteeing PMOS turn-off margin (V_GS,off ≈ 5.8 V vs −1.5 V threshold). Switches (pp. 56–57): low-side NMOS SiSA40DN (20 V, ~1.1 mΩ at V_GS = 10 V, 162 A); high-side PMOS DMP2003UPS (−20 V, 4 mΩ at −2.5 V, 2.5 mΩ at −4.5 V); NMOS-low/PMOS-high removes bootstrap and isolated high-side supplies (p. 59). Signalling (pp. 57–59): I2C over two shared lines; open-drain Si8606AD-B-IS isolator (two I2C channels, 1.7 MHz; two 10 Mbps) since push-pull isolators would short the bus. Gate drive: SN74HC125PWR buffers into two 2EDN7524GXTMA1 dual 5 A drivers (p. 59). PCB/assembly (pp. 59–62): battery tabs through PCB slots, copper clamps as combined busbars/thermal spreaders, nine-step assembly, enclosure as heat sink.

### Chapter 3 — Integrated Power Sub-module Design: A Unified Perspective (pp. 63–126)

This is the chapter the per-slot proposal leans on most heavily: monolithic integration of the UPU power electronics in **130 nm BCD**, including the on-chip transformer digital isolation (OCI).

**Motivation (pp. 63–67).** Per the cost model of [16] (100 kW/600 V automotive inverter), power components dominate at high production volumes (>2/3 of cost), so cheap low-voltage devices plus multilevel architectures attack cost directly; integration also collapses signalling and housing costs (pp. 63–64). A PMIC review (Table 3.1, p. 67; 13 works, including a 0.18 µm 80 V BCD dual-active-bridge PMIC at 50 W/1 MHz/94 % with air-core transformer and digital isolator) shows watt-to-tens-of-watt integrated isolated stages are feasible, but none addresses cell-scale multilevel BEV submodules.

**Technology (pp. 68–69).** 130 nm Bipolar-CMOS-DMOS; only the low-voltage 5 V CMOS subset used. The NMOS carries an N-type buried layer (NBL). Parasitic-diode rules: substrate to the lowest system potential, NBL to the highest local potential, bodies tied to sources.

**(c) The integration-boundary principle (pp. 69–71).** The chapter's governing design rule. Two constraints bound the integration level: (i) total stacked voltage on one die must stay below process breakdown (each submodule sits at cell voltage, 4.2 V); (ii) current-path analysis separates *orthogonal* currents (die↔package, unavoidable) from *lateral* currents, which may run through external conductors or IC metal. "Since IC metal layers are relatively thin, their current-handling capability is limited. For applications requiring high current, it is preferable to use external conduction paths, such as reinforced PCB traces, to minimize resistive losses" (p. 70). Pulling the other way, "it is advantageous to integrate components that can share circuitry onto the same die" — the two half-bridges of one CHB level share control, communication and monitoring; two full-bridges share little. Hence "the optimal level of integration should be determined by carefully balancing voltage limitations, current-handling capability, power loss, and the opportunity to eliminate repeated circuitry within the system design" (pp. 70–71). In short: integrate enough to delete repeated control/support circuits; never so much that IC metal becomes the power bus.

**Feasibility per topology (pp. 71–73).** Half-bridge/full-bridge: fully feasible (isolated secondary's substrate pins tied to central-controller ground). MMC: feasible (bottommost ground is a guaranteed minimum-potential node). CHB: no terminal has a fixed reference, so the shared substrate must float — flagged for experimental verification, with a SUB pin brought out for arbitrary biasing (pp. 73, 77).

**Circuits designed (pp. 73–89).** Five circuit sets: three half-bridges (one per modulation scheme), a four-level MMC, a five-level CHB. Building blocks: inverter (t_PHL/t_PLH = 54/83 ps), NAND (100/107 ps), XOR (90/350 ps), D flip-flop (pp. 79–80); NAND-based non-overlap dead-time generator, 1 kΩ/1 pF RC, **≈90 ns dead time** (p. 80); level shifter translating global-ground commands to each MMC level's local ground (pp. 80–81); 9-stage voltage-controlled ring oscillator (8 current-starved inverters plus an enabling NAND) (pp. 81–83).

**(a) OCI digital isolation — modulation schemes (pp. 83–89).** Chain: modulator → on-chip transformer (OCI) → demodulator. *Amplitude modulation (AM)* (pp. 83–84): the input enables the VCRO and supplies two complementary modulating inverters, driving the OCI with ±VDD bursts for the whole input high state. *Pulse modulation (PM)* (pp. 84–85, proposed): an XOR of the input and a delayed copy emits one narrow pulse per edge — only edges are transmitted, eliminating AM's standing oscillator loss; unlike the literature's set/reset (two OCIs), pulse-polarity (negative-level demodulation) and pulse-count (edge discrimination) schemes, PM needs one OCI, no negative levels, no edge-type detection (p. 85). *Pulse-train modulation (PTM)* (pp. 85–86, proposed): the XOR pulse gates the oscillator, sending a burst per edge for robustness. *Demodulators* (pp. 86–89): for AM, a proposed PMOS-based peak-hold (three inverters + PMOS) replaces the diode rectifier-and-hold, removing reverse-recovery droop and shrinking area (p. 87); for PM/PTM, a proposed toggling demodulator clocks a D flip-flop with OCI pulses, its D input a delayed inverted copy of its own output, a weak pull-down defining the start-up state (p. 88).

**(a) OCI transformer construction (pp. 89–95).** Maximum footprint 500 µm set by layout. Six metal layers available — thick metal 5, ultra-thick metal 6; top-metal rules 5 µm width / 3 µm spacing. Design flow (p. 90): HFSS model → Touchstone .s2p → Virtuoso/Spectre co-simulation → iterate → GDS. Three winding arrangements characterised in HFSS (pp. 91–92): (aʹ) side-by-side on metal 6 (5 µm/12 turns; 7 µm/10 turns; 500 × 250 µm) — adequate Q and self-resonance, very low coupling (k ≈ 0.1–0.3); (bʹ) stacked metal 6 over metal 5 (7 µm/10 and 20 turns; 14 µm/5 and 10 turns) — high k but poor secondary Q and low self-resonance from interwinding capacitance; (cʹ) **interleaved, both windings on top metal** (7 µm/5 and 10 turns; 14 µm/3 and 6 turns; 500 × 500 µm) — top-metal Q, k ≈ 0.9–0.98, sidewall-only parasitic capacitance. **Selected: interleaved, 7 µm trace, ten turns, 500 µm**, stable over the intended range "up to 100 MHz and, if feasible, up to 0.5 GHz" (pp. 92–94). Dummy-metal fill beneath the coil degrades inductance/Q only out-of-band (pp. 94–95). Shrink study (p. 100): 300 µm/7 turns still works; 100 µm/2 turns induces too little secondary voltage to drive the demodulator — bounding minimum viable OCI size between 100 and 300 µm in this process.

**Simulation results (post-parasitic extraction, Spectre; pp. 95–112).** VCRO: control voltage 1–4.2 V sweeps oscillation **≈500 kHz to 500 MHz** (p. 96). AM half-bridge: rising delay ≈2 ns, falling ≈790 ns (RC-discharge dominated) (p. 101); integrated switch R_ON ≈ 75–105 mΩ over 2.6–4.4 V — high only because die area was shared among five experiments (p. 102). PM half-bridge: rise/fall 1.73/1.84 ns (p. 104). PTM: 550 ns edge pulses gate the oscillator; the demodulator triggers on the first burst pulse (p. 105). **Comparative study (Table 3.2, p. 107**; 10 µs/5 µs input, V_ctrl = 1.2 V): rising delay 2 / 1.73 / 1.73 ns, falling delay 790 / 1.84 / 1.84 ns for AM/PM/PTM; total isolation loss **335.04 / 42.15 / 117.9 mW** — PM cuts total loss 87.4 % (modulator loss 92.4 %) versus AM; PTM cuts 64.8 %. Four-level MMC: staircase synthesis verified; level-shifter rise delays 1.225/1.018/0.728 ns, fall 3.48/4.02/4.538 ns for levels 1–3 (p. 111).

**Fabrication and packaging (pp. 112–115).** Die: **4 mm × 4 mm** in 130 nm BCD carrying all five circuits (micrograph Fig. 3.47, p. 112). Interconnect: 50 µm aluminium wedge-bonded wire to a cartridge PCB. Supply-bounce spikes from parasitic inductance exceed device ratings and are suppressed with a 22 µF off-chip plus 50 pF on-chip decoupling capacitor (pp. 113–114). Two bond-out plans cover (i) MMC + AM half-bridge and (ii) CHB + PM + PTM half-bridges (p. 115). Test rig: cartridge board into a motherboard with fibre-optic control delivery and terminal-block power (pp. 115–116).

**(b) Experimental validation (pp. 115–125).**
- *Five-level CHB* (pp. 115–117): two 3 V cells, external gate signals, 50 ns dead time; full five-level ±6 V output at 50 Hz; leg transition delays **7.6 ns rise / 4 ns fall** (p. 117) — the floating-substrate CHB works in silicon.
- *Four-level MMC* (pp. 118–119): one command per level, internal level-shifting/dead-time/gate-drive; steps 0/3/6/9 V at 50 Hz; level order interchangeable.
- *Half-bridge, AM* (pp. 119–123): functional at 10 kHz (4 V); delays **38.4 ns rising, 498.8 ns falling** (p. 120). A **1.5 MHz** input at duty 0.1 is reproduced, asymmetric delays stretching output duty to ≈0.8 (p. 120). Loaded tests 100 Hz–1.5 MHz into an R–L load (≈1.2 µH, 2.45–2.9 Ω): 1.44 A with 0.33 V drop at 100 Hz; body-diode conduction during dead time observed at −0.15 V, analysed to 500 kHz (pp. 120–122).
- *Half-bridge, PM* (pp. 123–124): **39 ns rising / 36.4 ns falling** — falling delay improves from 498.8 to 36.4 ns versus AM. Stable to **418 kHz**; the naïve limit from the 3 µs demodulator feedback delay would be 166 kHz, so the measurement implies an effective delay ≈1.2 µs, attributed to MOM-capacitor behaviour.
- *Half-bridge, PTM* (pp. 124–125): rise and fall both **≈40 ns**, matching PM.

**Conclusion (pp. 125–126).** Integration levels, five topologies, all blocks, and simulation-plus-silicon validation delivered; Ch. 7 adds: "The pulse modulation method effectively eliminates the need for a high-frequency oscillator and a high-falling-delay demodulator, enabling low-loss and high-frequency digital isolation" (p. 217).

### Chapter 4 — Equalized Energy Extraction in MLIs: Minimizing Imbalance (pp. 127–166)

**Claim.** Preventive, sensor-free modulation can equalise energy extraction across MLI cells, avoiding SoC imbalance before it arises; two methods are proposed, needing no voltage/current measurement and no hardware change. (Balancing literature is classified into charge-transfer, selective-extraction and preventive families, pp. 127–130.)

**Method 1 — Decomposed Sweeping Window (DSW) modulation (pp. 130–148)**, for isolated-cell MLIs (CHB/MMC). The modulating vector of a circular nearest-level-control representation is decomposed into two vectors bounding a "window" of active cells that sweeps around the ring; the sweep-speed law (Eqs. 4.16–4.22) holds the ratio of instantaneous power to rotation speed constant so all cells yield equal energy. A coefficient k sets rotations per period; choosing k with 1/k irreducible and a large denominator (k = 0.3, 1.3 → direction period 10T; k = 0.33 → 100T) maximises condition diversity — k = 1.3 gives a cell 18 distinct contribution sections versus 3 for k = 3 (pp. 139–141). Simulation (20-cell single-phase CHB, 20 V cells, 75 kVA at 0.8 lag): charge-variance bounded and periodic (period 10 cycles) versus monotonic growth under NLC; switching losses rise with k; self-heating (max squared RMS cell current) falls ~5–80 % depending on output voltage (pp. 141–143). **Experiments** (pp. 143–148): 12 Keithley 2281S-20-6 battery simulators, 25-level CHB, 16 Ω load, 0.1 Hz (simulator SoC-reporting limit), LV/MV/HV ≈10/30/60 V, run from 100 % until any cell hits 65 % SoC. LV durations (20 mAh/cell): NLC 75 s; swapping 487 s; DSW k = 1.3 476 s (p. 145). Mean coefficient of variation of SoC profiles (p. 146): LV 0.0604 (NLC) / 0.0252 (swapping) / 0.0076, 0.0051, 0.0021 (DSW k = 1.3, 3.3, 9.3); MV 0.0861 / 0.0112 / 0.0081, 0.0037, 0.0014; HV 0.0514 / 0.0079 / 0.0078, 0.0024, 0.0025. Cost: THD rises from 7.45 % to 10.54 % (k = 1.3) and 10.25 % (k = 3.3) (p. 146). Chapter 7 summarises this as "up to a 98 % improvement in state-of-charge (SoC) balancing compared to standard methods" on the 25-level prototype (p. 218).

**Method 2 — Adaptive Harmonic Injection (AHI) modulation (pp. 148–166)**, for series-connected-cell MLIs (no bypass capability). Third-harmonic injection is generalised: instead of the fixed k = 1/6 that merely maximises output voltage, the coefficient is recomputed for each commanded amplitude (cubic Eq. 4.29) so the phase control voltage always spans the full ±V_DC/2, engaging *every* cell at *every* output level; the common-mode term cancels line-to-line. Sinusoidal and triangular injection waveforms are both derived (Eqs. 4.30–4.36), each superior at different operating points. Standalone simulation (12 levels, 4 V cells, 8–44 V, 1 Ω): CV of extracted energy cut ≈85/80/65 % at 2/4/6 V_cell outputs (p. 157). Combined with the generalised MLI's intrinsic capacitor self-balancing (200 µF/2 mF capacitors, 2 kHz/200 kHz transition frequencies), the proposed method at low capacitance and frequency beats the conventional method even at high capacitance and frequency for LV and MV (p. 159); load-supply switching losses rise ≈180/100/21 % (LV/MV/HV) while balancing conduction/switching losses fall 98/89 % (LV) and 71/61.5 % (MV) (p. 160). **Experiments** (pp. 162–165; Table 4.4, p. 163): 12 cells on Keithley 2281S-20-6 simulators (Samsung 18650 3.7 V model, 6 Ah), B-Box RCP 3.0 controller, TPH1R405PL MOSFETs, 8/16/32 V_RMS into 2/8/32 Ω, 3-minute runs; adaptive k = 0.2974/1.276/2.7584 (sin), 3.1742/1.3371/0.4186 (tri). At 8 V, NLC draws from only four of twelve cells (B5–B8, up to I_DC = 3.164 A); AHI spreads near-identical currents across all twelve (I_DC ≈ 0.49–1.16 A) (p. 163). Used-capacity variance (Table 4.5, p. 164): 8 V — 4×10⁻³ mAh² (NLC) vs 1.14×10⁻⁴ (sin), 6.79×10⁻⁵ (tri); 16 V — 1.3×10⁻³ vs 1.38×10⁻⁴, 3.63×10⁻⁴; 32 V — converged (5.99–8.28×10⁻⁵). THD comparable across methods (p. 166). Chapter 7 records validation "on a 12-cell 48 V system under multiple operating conditions (8 V, 16 V, and 32 V)" (p. 218).

### Chapter 5 — Proper Active Balancing Solution: Fully Balance Realization (pp. 167–190)

**Claim (d).** The Complementary Star Switched-Capacitor Active Balancer (CS2CAB) achieves fast, sensor-less, location-independent, continuous-current balancing compatible with both series-connected and isolated cells — a combination no prior switched-capacitor balancer (DTSCAB, SCSLAB, BBCAB, S3CAB; reviewed pp. 167–169) offers.

**Topology and control (pp. 169–170).** Each cell gets an H-bridge; each output leg feeds one plate of a capacitor whose other plate joins a shared star node (two stars: upper and lower legs). Control is only **two complementary 0.5-duty pulses** for the whole pack. Static analysis yields the governing result (Eq. 5.13): I_Bk = (C/Δt)(V_k − V̄) — every cell's current is set solely by its voltage relative to the pack average (above-average cells discharge, below-average charge, at-average carry zero), "independent of its location and the state of adjacent cells" (p. 173). Dynamic analysis gives closed-form capacitor voltage/current including ESR, R_DS(on) and cell resistance (Eqs. 5.19–5.21, pp. 173–175).

**Design considerations (pp. 175–179).** DC balancing current grows with frequency and capacitance (two cells, 5 V/4 V, r_e = 30 mΩ: up to ~8 A over 0–800 µF, 0–300 kHz; p. 176). Conduction-loss analysis uses measured MLCC ESR (100 µF: 70 mΩ at 100 Hz → 3.1 mΩ at 36 kHz → 9 mΩ at 800 kHz; p. 176). Maximum frequency is bounded by capacitor self-resonance, ≈300 kHz–1 MHz for the 22–100 µF MLCCs surveyed (p. 177). Optimum: the lowest frequency giving continuous, low-ripple cell current — beyond it only switching loss grows (pp. 177–179).

**Comparative analysis (pp. 179–185).** Four-cell string [3.2, 3.4, 3.8, 4.0 V]: only CS2CAB gives continuous cell currents; DC/RMS 18.64/19.45 A versus S3CAB-system3's 9.38/13.78 A — roughly double the DC current at equal capacitance, with the best DC-to-RMS ratio (pp. 179–180). Twenty-cell SPICE studies (10 mΩ cells, 560 µF/50 mΩ capacitors, 33 µH/50 mΩ inductors where applicable, Si7234DP, 50 kHz, four initial-voltage patterns): CS2CAB alone is insensitive to cell ordering, with the highest mean currents and shortest balancing times, though not the lowest balancing energy (higher RMS current and component count) (pp. 181–182). Table 5.1 (p. 183): 4n switches at cell voltage, 2n capacitors, no inductors, speed/loss H/M, the only compared balancer supporting isolated cells. Connection independence is shown on a 4-cell/9-level CHB whose cells re-group continuously during modulation (pp. 183–184). Robustness: ±20 % deviations in cell resistance and capacitance shift initial I_DC from 13.85 A to 12.26 A and efficiency from 91.83 % to 91.38 % worst case (Table 5.2, p. 185).

**(d) Experimental results (pp. 185–189).** Five-cell rig on Keithley 2281S-20-6 simulators (Samsung 18650 model scaled to 20 mAh), FDS8978 MOSFETs, 2 × 100 µF C1210C107M4PACTU per leg, 1/5/10 kHz; initial SoCs {86, 74, 70, 80, 90 %} and a reordered variant. CS2CAB reaches the 2 % maximum-ΔSoC criterion in **37 s at 10 kHz, 90 s at 5 kHz, 580 s at 1 kHz**, identically for both cell orders and with monotonic SoC trajectories (no unwanted charge/discharge intervals) (pp. 186–187). The S3CAB-system3 benchmark at 10 kHz needs **330 s (favourable order) or 750 s (unfavourable order)** — CS2CAB is ~9–20× faster and order-independent (pp. 187–188). Two-cell characterisation (Table 5.4, p. 188: 5 V source, Keithley 2380 sink at 4.7/4.9 V, Si7234DP, 300/900 µF, 1–100 kHz): DC current follows the model; efficiency rises with frequency, plateaus at ≈90 % over 5–25 kHz where current becomes continuous, then falls from switching loss (p. 189).

### Chapter 6 — Low Leakage Transformers: Perfectly Coupled Magnetics (pp. 191–215)

**Claim.** For magnetic active balancers needing low-impedance n:n transformers, a fully-interleaved *parallel–parallel* foil-winding arrangement (interleaved both between windings and among the paralleled sheets within each turn) minimises leakage inductance and AC resistance; an explicit Maxwell-equation analytical model with no frequency or geometry assumptions predicts both.

**Model (pp. 194–203).** 1-D Helmholtz solution per foil sheet; 2n field coefficients solved from four boundary-condition families (zero H at the core-side surface, H continuity across gaps, Faraday loops between paralleled sheets, and an Ampère loop or total-current integral), assembled as structured 2n × 2n matrices (Eqs. 6.17, 6.18, 6.28) for the non-interleaved and fully-interleaved cases. Leakage inductance follows from stored energy with the secondary shorted; AC resistance from the Poynting vector; n:n values are the 1:1 values times n (pp. 201–202).

**Findings (pp. 203–210).** FEA/analytical field maps agree at 500 Hz/200 kHz/1 MHz (Figs. 6.3–6.4). Sample study (0.5 mm total conductor, 160 mm height): four paralleled sheets carry at 1 MHz the current a single sheet carries at 50 kHz (p. 206); at 10 MHz four-sheet AC resistance is 7× lower and impedance up to 85 % lower than single-sheet (pp. 207–209). A skin-depth rule (Eq. 6.39) recommends 1/2/3/4 sheets up to 18/70/160/280 kHz for this case (p. 208). An equi-impedance design chart trades copper usage against maximum frequency (Fig. 6.9, p. 209): 0.3 mΩ is met by one 0.2 mm sheet at 200 kHz or by four paralleled sheets of the same total copper at ≈4 MHz.

**Validation (pp. 210–215).** Two prototypes (Table 6.1, p. 211): non-interleaved (1 × 200 µm sheet per winding) and fully-interleaved (4 × 50 µm), both 4.8 mm wide, 2 m long, 70 µm polyimide insulation, FLP240/60/8-BH1T ferrite, 40 mm × 10 mm window; measured with a Keysight E4990A, five-terminal, 20 Hz–1 MHz (sub-50 kHz values excluded for analyser accuracy). Full interleaving cuts leakage inductance **≈90 % across the band** and makes it nearly frequency-flat; reactance falls ≈120 mΩ at 200 kHz and ≈400 mΩ at 1 MHz; resistance falls <5 % below 100 kHz rising to **≈60 % at 800 kHz** (p. 214). Model accuracy: resistance error <10 % versus measurement throughout; leakage error <15 % (non-interleaved), exceeding 20 % only below 150 kHz for the interleaved part (analyser-limited near 10 nH); versus FEA, <1 % (interleaved, except <4 % at low frequency) and <5 % (non-interleaved) (pp. 213–214).

### Chapter 7 — Conclusion and Future Works (pp. 216–220)

Per-chapter remarks restate the contributions. **Stated further work:** *Discrete system* — build enough units for a full three-phase traction/charging system; characterise the integrated cooling and its limits at higher charge rates; volumetric/gravimetric benchmarking (pp. 216–217). *Integrated submodule* — integrate the ICs with batteries into a fully integrated UPU at system level; extend to higher-power devices; expand integration to more functional components; "extend the concept to use different technologies for power devices and control devices" (pp. 217–218). No further-work subsections are given for Chapters 4–6 (remarks only).

## 4. Quotable passages (verbatim, with page numbers)

1. **UPU definition** (p. 34): "the powertrain is composed of modular elements referred to as unified power units (UPUs). Each UPU consists of a single battery cell or a small group of cells integrated with its own power electronics. These UPUs are interconnected to form a unified powertrain that combines the functionalities of multiple components used in conventional architecture."
2. **Beyond-BEV scope** (Impact Statement, p. 4): "This research aims to advance the consideration of cell-scale power processing concepts across a range of applications, with a particular focus on battery electric vehicles."
3. **Market gap** (p. 41): "none of the companies with certified products currently serve the BEV sector, underscoring a critical gap in the market."
4. **Integration boundary, power side** (p. 70): "Since IC metal layers are relatively thin, their current-handling capability is limited. For applications requiring high current, it is preferable to use external conduction paths, such as reinforced PCB traces, to minimize resistive losses."
5. **Integration boundary, synthesis** (pp. 70–71): "the optimal level of integration should be determined by carefully balancing voltage limitations, current-handling capability, power loss, and the opportunity to eliminate repeated circuitry within the system design."
6. **Isolation contribution** (p. 217): "The pulse modulation method effectively eliminates the need for a high-frequency oscillator and a high-falling-delay demodulator, enabling low-loss and high-frequency digital isolation."
7. **CS2CAB mechanism** (p. 219): "each cell's charge or discharge behavior is automatically governed by the ratio of its voltage to the average pack voltage."
8. **Transfer intent** (p. 218): "Extend the concept to use different technologies for power devices and control devices."

## 5. Limitations / future work as stated

- The discrete UPU is a single-unit demonstrator; a three-phase multi-unit traction/charging system, cooling characterisation and volumetric/gravimetric benchmarking remain (pp. 216–217).
- The ICs are validated as circuits, not yet co-packaged with cells into a working UPU; power devices are deliberately undersized (shared research die, R_ON ≈ 65–110 mΩ); higher-power devices, broader integration and heterogeneous power/control technologies are future work (pp. 102, 217–218).
- CHB integration relies on a floating substrate, flagged pre-silicon as needing experimental verification and de-risked via a bond-out SUB pin (p. 73).
- AM isolation is asymmetric (498.8 ns falling delay; duty distortion at 1.5 MHz); PM is limited to 418 kHz by demodulator feedback delay, with the 1.2 µs vs 3 µs discrepancy attributed to MOM-capacitor variability (pp. 120, 123–124).
- DSW costs higher switching loss and THD (7.45 % → ~10.5 %); AHI raises load-supply switching losses (up to +180 % at low voltage) and its balancing-loss advantage inverts at high output voltage (pp. 143, 146, 160).
- Ch. 4 experiments ran at 0.1 Hz fundamental because the simulators cannot report SoC in real time at speed (stated as having "no bearing on the results", p. 144).
- CS2CAB uses the most switches (4n) and its balancing energy loss is not the lowest despite the shortest balancing time (pp. 182–183).
- The Ch. 6 model neglects edge effects (accuracy degrades as width-to-thickness ratio falls); sub-50 kHz measurements were analyser-limited (pp. 213–214).

## PROPOSAL USE MAP (detailed)

Standing rule for every item below: the thesis is ANONYMISED in proposal text (Master Handover §3 and §7c). In the Vision and Approach it appears only as "the group's doctoral work" or "a doctoral thesis from the group"; the full bibliographic entry goes in the References section. Author names never appear in body text. Citation keys are unreconciled between drafts (the Vision uses [21] for the doctoral OCI work, the Approach uses [5]); renumber per Handover §9 before reuse.

The EIGHT highest-value items are marked ★.

**★ 1. UPU concept as the conceptual bridge to per-slot drive (pp. 34-36; §1.4 definition p. 34).**
(a) Location: Vision, "Crossing the line: the 50 V claim" (VIS-CROSS-v7 in drafts/02, the sentence citing on-chip digital isolation "demonstrated in the group's doctoral work [21]") and, per Handover §7c, an optional framing paragraph in "The Research Opportunity" grounding per-slot drive in a validated battery-domain precedent.
(b) Usage mode: anonymised conceptual precedent. The thesis pairs each battery cell with its own power electronics in identical stackable units that absorb the functions of centralised converter blocks; the proposal makes the same move on the machine side, pairing each stator slot with its own integrated converter section. Same dividends claimed in both: low-voltage devices, graceful degradation, no centralised converter.
(c) Fragment: "The architectural move has a validated precedent within the group: doctoral work on cell-scale power processing demonstrated that a centralised converter can be dissolved into identical low-voltage units, each pairing an energy element with its own integrated electronics, and validated the approach from concept through custom silicon to experimental proof in the battery domain. This programme carries the same principle across to the machine winding, pairing each stator slot with its own integrated drive section."

**★ 2. On-chip transformer digital isolation (OCI), silicon validated (pp. 83-95, 115-125).**
(a) Location: Approach, WP2 T2.2 (floating-domain control-signal architecture, D2.2, M10), serving RQ2; already anchored there as "the on-chip digital isolation the group demonstrated in the same 130 nm BCD process [5]".
(b) Usage mode: enabling-capability evidence plus design input. Supplies the validated circuit family (AM, PM, PTM modulators and demodulators), the HFSS to Spectre to GDS design flow, and sizing bounds (500 um ten-turn interleaved top-metal transformer selected; 300 um still works; 100 um fails), all reusable for the 12 to 18 floating per-slot domains.
(c) Fragment: "Control-signal isolation across floating domains is already proven in the target process: the group's doctoral work fabricated coreless on-chip transformer isolation in the same 130 nm BCD technology, with three modulation schemes validated in silicon and measured edge delays of approximately 38 to 40 ns, requiring no external isolator and no per-domain isolated supply. T2.2 adapts this signal path to the 12 to 18 floating per-slot domains of the proposed machine."

**★ 3. Integrated power submodule die, 4 mm x 4 mm in 130 nm BCD, five circuits fabricated and tested (pp. 112-125).**
(a) Location: Capability Module 1 of the R4RI track-record section (Handover §10), as anonymised evidence of in-house full-custom power IC capability; also supports the facilities claim that "BTMLC/TCAS-I BCD design flows transfer directly".
(b) Usage mode: capability evidence. Doctoral output demonstrating the group takes multilevel power submodules from architecture through layout, tape-out, packaging and experimental validation.
(c) Fragment: "Doctoral work within the group carried an integrated multilevel power submodule from architecture to validated silicon: a 4 mm by 4 mm die in 130 nm BCD carrying five complete circuit sets, including five-level cascaded H-bridge and four-level modular multilevel stages, packaged, bonded and experimentally verified. The design flow, from electromagnetic field simulation through co-simulation to layout, is established in-house and transfers directly to the per-slot module."

**★ 4. Integration-boundary principle (pp. 69-71).**
(a) Location: Approach, "Building on previous work", and the WP2 rationale for what sits on the per-slot die versus the board and busbar.
(b) Usage mode: prior in-house design methodology, paraphrased. Rule: integrate until repeated control and support circuitry is eliminated; keep lateral power currents out of thin IC metal; bound total stacked voltage per die by process breakdown.
(c) Fragment: "The partitioning of the per-slot module follows a design rule established in the group's doctoral work on integrated submodules: integration proceeds until repeated control, communication and monitoring circuitry is eliminated, while high-current paths remain in external conductors rather than thin on-chip metal. Applied here, gate drive, dead-time generation, isolation and monitoring belong on the per-slot die; the slot current does not."

**★ 5. Floating-substrate CHB verified in silicon (pp. 73, 115-117).**
(a) Location: Approach, WP2 T2.2 and the feasibility and risk narrative, serving RQ2. The per-slot stack has no fixed substrate reference; this is the direct de-risking evidence.
(b) Usage mode: risk retirement. The configuration with no guaranteed minimum-potential node, flagged pre-silicon as the open question, worked in fabricated silicon: full five-level output at 50 Hz with leg transition delays of 7.6 ns rising and 4 ns falling.
(c) Fragment: "The configuration most relevant to a per-slot series stack, in which no terminal has a fixed substrate reference, was identified before fabrication as the open risk and then verified experimentally: the floating-substrate cascaded H-bridge produced full five-level operation in silicon, retiring the principal feasibility concern for stacked floating domains."

**★ 6. Pulse-modulation isolation performance and its known ceiling (Table 3.2, p. 107; pp. 123-124).**
(a) Location: Approach, WP2 T2.2 specification and the honesty line in feasibility and risk management (RQ2 frequency envelope).
(b) Usage mode: quantified starting point plus stated improvement target. PM cuts total isolation loss 87.4 percent versus AM (42.15 mW against 335.04 mW) and holds symmetric delays near 39 ns, but is measured stable only to 418 kHz, limited by demodulator feedback delay.
(c) Fragment: "The pulse-based isolation scheme reduced total isolation loss by 87.4 percent relative to amplitude modulation while holding symmetric edge delays below 40 ns; its measured operating ceiling of 418 kHz, set by demodulator feedback delay, is a characterised limitation that WP2 addresses in specifying the per-slot signal path."

**★ 7. The thesis's own warrant for extension beyond batteries (Impact Statement, p. 4; further work, p. 218).**
(a) Location: Vision, "Timeliness" or the closing of "Crossing the line"; also Approach, "Building on previous work" (which already uses the parallel Kolahian future-work device).
(b) Usage mode: continuation-of-line argument, paraphrased and anonymised. The Impact Statement aims to advance cell-scale power processing "across a range of applications" (verbatim, p. 4) and the stated further work is to "extend the concept to use different technologies for power devices and control devices" (verbatim, p. 218). Quote only with the page-checked wording in §4 of this digest; otherwise paraphrase.
(c) Fragment: "The doctoral work that established the group's cell-scale platform explicitly frames its concept as extensible across applications and identifies extension to other device and control technologies as the natural next step. The programme proposed here is that step, taken into the rotating machine at per-slot resolution."

**★ 8. Fast, order-independent active balancing as capability evidence (CS2CAB, pp. 185-189; published as A2, ref [6]).**
(a) Location: Capability Module 1 (development of others; doctoral researchers publishing in IEEE Transactions during their programmes, Handover §10) and the evidence base behind "Building on previous work".
(b) Usage mode: measured-numbers capability evidence, citable via the published TPEL paper rather than the thesis where a named citation is needed.
(c) Fragment: "The group's switched-capacitor active balancer reached the 2 percent state-of-charge criterion in 37 seconds at 10 kHz where the best prior-art benchmark required 330 to 750 seconds depending on cell ordering, with balancing behaviour independent of cell location and only two complementary control signals for the whole stack."

**9. Level shifter plus OCI: the two isolation regimes a per-slot stack needs (pp. 80-81, 111; pairs with A8, ref [2]).**
(a) Location: Approach, WP2 T2.2 narrative.
(b) Usage mode: completeness argument. Sub-5 ns level shifters serve stacked domains sharing a ground reference; the OCI serves domains with no common reference. Together they span the signal-routing regimes of a per-slot stack.
(c) Fragment: "Between the group's silicon-validated floating-domain level shifters and its on-chip transformer isolation, both fabricated in the same 130 nm BCD process, the two signal-routing regimes of a series-stacked per-slot drive, shared-reference and fully floating, each have a demonstrated on-chip solution."

**10. OCI sizing and shrink bounds (pp. 92-94, 100).**
(a) Location: Approach, WP2 T2.2 design detail, or held in reserve for reviewer response.
(b) Usage mode: design-space input. Interleaved top-metal winding selected (coupling approximately 0.9 to 0.98); viable size bounded between roughly 300 and 500 um in this process; 100 um fails to drive the demodulator.
(c) Fragment: "The isolation transformer design space in this process is already bounded by experiment: interleaved top-metal windings at 300 to 500 um function, while 100 um induces insufficient secondary voltage, giving T2.2 a characterised starting envelope rather than an open search."

**11. Packaging and supply-integrity lessons (pp. 113-114).**
(a) Location: Approach, WP2 T2.3 packaging specification and T2.4 board build, minor supporting detail.
(b) Usage mode: engineering-maturity evidence. Bond-wire parasitic-inductance supply bounce was diagnosed and suppressed with combined 22 uF off-chip and 50 pF on-chip decoupling.
(c) Fragment: "Packaging-level supply-integrity effects in this process family are already characterised from the group's prior tape-out, including the decoupling strategy that suppresses bond-wire supply bounce."

**12. Sensor-free preventive balancing results (Ch. 4; DSW and AHI).**
(a) Location: Capability Module 1 supporting evidence only; not load-bearing for any work package.
(b) Usage mode: breadth-of-platform evidence, anonymised or cited through the associated publications. Use the Ch. 7 wording "up to a 98 % improvement" in state-of-charge balancing on the 25-level prototype, not a flat "98 percent".
(c) Fragment: "The platform's modulation-level work demonstrated sensor-free equalised energy extraction with up to a 98 percent improvement in state-of-charge balance on a 25-level experimental prototype, without hardware modification."

**13. Validated analytical magnetics modelling (Ch. 6).**
(a) Location: Capability Module 1 supporting evidence; tangentially supports WP1's multi-winding modelling credibility alongside A1.
(b) Usage mode: modelling-capability evidence. Maxwell-equation model with no thin-conductor or frequency assumptions, resistance error under 10 percent against measurement; full interleaving cut leakage inductance by approximately 90 percent across the band.
(c) Fragment: "The group's analytical magnetics modelling, validated to within 10 percent of measurement across the instrument band, and its demonstrated 90 percent reduction in leakage inductance through full interleaving, evidence the electromagnetic modelling depth WP1 draws on."

### Traps

1. **"Point of consumption" is a paraphrase, not a quotation.** Handover §7c glosses the UPU concept as "distributing conversion to the point of consumption". That phrase does not appear in the thesis. The verbatim definition (p. 34) is the UPU passage in §4 item 1 of this digest. Never present the gloss inside quotation marks or attribute it to the thesis; either quote the p. 34 passage exactly or paraphrase without quotation marks.
2. **Battery-domain isolation results must not be claimed for winding domains.** Every OCI, floating-substrate and level-shifter result was obtained against battery-cell or bench-supply conditions. The lineage table states the gap explicitly: "Battery domain only, not winding domain". Write "demonstrated for floating battery-cell domains in the same process" and let WP2 T2.2 carry the extension; claiming winding-domain validation would contradict the proposal's own gap table and hand a reviewer an inconsistency.
3. **Anonymisation.** The candidate's name must not appear in Vision or Approach body text; the thesis is cited only in the References section (Handover §3, §7c). Where a named, numbered citation is needed in body text, prefer the published CS2CAB paper (A2, ref [6]).
4. **Citation-key drift.** The doctoral OCI work is [21] in the Vision draft and [5] in the Approach draft; neither matches the §9 master list. Do not copy fragments with hard-coded keys into proposal text; reconcile per Handover §9 first.
5. **Numbers with hidden caveats.** The 98 percent balancing figure is "up to", from experiments run at 0.1 Hz fundamental (a simulator reporting limit the thesis states has no bearing on the results, p. 144). The integrated switch R_ON of 75 to 105 mOhm reflects a shared research die, not the technology's capability; do not quote it as representative. PM isolation is validated only to 418 kHz; avoid the unqualified phrase "high-frequency isolation" for the as-built silicon.

---
*Digest prepared 1 August 2026 from a full pdftotext extraction of the 234-page PDF; all figures, tables and quotations verified against the extracted text. Note: an early extraction in this session was overwritten by a sibling task's identically named scratch file (Kolahian thesis content); the extraction was redone to a uniquely named file and every quoted passage re-verified against the Tazehkand PDF directly.*


<!-- ==================== FILE: evidence/05_Kolahian_thesis_digest.md ==================== -->

# Evidence Digest 05 — Kolahian PhD Thesis (UCL, February 2026)

**Source file:** `/home/user/proposal/PhD_Thesis_Pouya.pdf` (226 pp., A4, pdfTeX). Page references below are the **printed thesis page numbers**; the printed page N appears on PDF page N+34.

---

## 1. Identity

Title page (as printed, p. i): **"Ultra efficient Bidirectional Power Converter for Battery Energy resources"** — Pouya Kolahian, Department of Mechanical Engineering, University College London. "This dissertation is submitted for the degree of Doctor of Philosophy. University College London, February 2026." Declaration signed Pouya Kolahian, February 2026 (p. v). Primary supervisor: Dr Mehdi Baghdadi; the author thanks "colleagues in the electric propulsion research group" at UCL (Acknowledgements, p. vii). PDF metadata: Author "Pouya Kolahian", created 22 February 2026.

## 2. Thesis argument in one paragraph

The thesis proposes a unified, ultra-efficient bidirectional power interface for battery energy resources (BERs) built from three hardware-optimised subsystems that replace control-side complexity with structural optimisation: (i) a **Hierarchical Binary Multi-Level Inverter (HB-MLI)** whose binary-weighted, tree-structured half-bridge hierarchy synthesises 2^N voltage levels from 2^N−1 half-bridges under a hybrid-frequency modulation that confines 100 kHz PWM to the lowest-voltage stage while high-voltage stages switch at (near-)fundamental frequency, decoupling voltage resolution from switching loss; (ii) the **MS2** multi-port pack-level balancing converter, which uses planar Litz-structured magnetics and a novel adiabatic-inspired soft-switching method that resonates MOSFET parasitic capacitances against transformer **magnetising** (not leakage) inductance, so ZVS/ZCS survives deliberately minimised leakage; and (iii) the **MFWE** (Multi-winding Foil-Wound Equalizer) cell-level balancer, whose single-turn copper-foil transformer minimises leakage inductance for fast, precise cell equalisation. Each subsystem was independently prototyped and experimentally validated (HB-MLI 99.46% peak efficiency; MS2 98%/98.8%; MFWE 98.94%), and the abstract (p. ix–x) claims that this modular, decoupled validation "confirms the efficacy of the proposed hierarchical architecture".

## 3. Chapter-by-chapter walk

### Chapter 1 — Introduction and Background (pp. 1–11)

Claim: decarbonisation requires BERs; their efficacy is constrained by conversion-interface efficiency and battery management. Context figures cited: IPCC 45% CO2 cut by 2030 vs 2010; Li-ion pack prices fell 87% (>$1100/kWh in 2010 to $156/kWh in 2019); Li-ion market $28bn (2020) → forecast $116bn (2030) (pp. 1–2). Problem statement (pp. 3–5): two-level inverters need large filters for acceptable THD; MLIs bring efficiency, harmonic, dv/dt, filter-size and fault-tolerance advantages but suffer topology complexity, modulation burden and component stress; balancing faces cell mismatch, method trade-offs, and sensor reliance. Table 1.1 (p. 6) maps challenges to thesis foci, notably "Achieve ultra-low converter losses to enable passive air cooling". Research aim (pp. 7–9): a unified architecture (Fig. 1.2) integrating hierarchical balancing layers with multi-level conversion between the energy source and "AC Motor / Load"; a **modular validation strategy** is explicitly adopted — the three subsystems are developed and tested independently "to verify that it meets the efficiency and stability requirements necessary for future system-level integration" (p. 7). Stated key features (p. 8): only five control signals per inverter phase; four signals for pack-level balancing and two for cell-level; high-frequency switching at low voltage, low-frequency at high voltage. Outline (pp. 10–11).

### Chapter 2 — Literature Review (pp. 13–56)

Two survey strands. **Balancing (pp. 14–27):** passive balancing dismissed as dissipative; switched-capacitor (adjacent-only, slow), flying-capacitor (N² scaling), inductor-per-cell DC-DC (prohibitive component count), and reconfigurable matrices (unstable pack voltage) are ruled out; multi-winding-transformer (MWT) topologies (flyback, forward, double-forward, self-driven, star-core, cascaded modular) are surveyed with a comparison table (Table 2.1, pp. 22–23). Three technology gaps (pp. 21–24): high-frequency AC resistance (R_AC) in planar windings (skin/proximity; Litz wire is bulky and ill-suited to planar integration); leakage inductance L_lk limits balancing speed and — via manufacturing asymmetry — balancing accuracy; and the "conventional soft-switching conflict": flyback-type balancers' discontinuous/bidirectional currents are "fundamentally incompatible with conventional ZVS techniques" (pp. 23–24). Hierarchical architectures (pp. 24–26) reviewed (control hierarchies, power-flow hierarchies incl. H-DCB and C2P2C, integrated inverter hierarchies), leading to the "Homogeneity Gap": current hierarchies replicate the same converter at both cell and pack level, ignoring their distinct physics (p. 27). **MLIs (pp. 27–52):** NPC, FC, CHB, MMC, ANPC, TNPC, NNPC, asymmetrical (binary-weighted: s sources give m = 2^(s+1) − 1 levels, e.g. 15 levels from 3 sources with 10 switches, p. 41), and the Generalized P2 hierarchical inverter, explicitly identified as "a critical intellectual antecedent for designing more efficient and practical hierarchical converters" despite its M(M−1) switch count (p. 43). Modulation (LSPWM, PSPWM, SVM, MPC) and AC-side control reviewed. **Section 2.4 (pp. 53–54)** poses four research questions: (1) decoupling voltage resolution from switching frequency via hybrid modulation; (2) planar Litz magnetics + magnetising-inductance soft switching for pack-level R_AC mitigation; (3) foil-wound leakage minimisation vs voltage-discrepancy error at cell level; (4) system impact of a hardware-optimised hierarchy. **Section 2.5 (pp. 54–56)** presents the proposed architecture (Fig. 2.20): a "binary-weighted 16-unit configuration" with hierarchical cell/pack balancing, validated by isolating the three subsystems.

### Chapter 3 — Battery Balancing (pp. 57–135)

**(e) The 52-prototype planar magnetics study (pp. 65–84).** To ground the balancers' magnetics, 52 planar inductor prototypes were fabricated and measured (Newton 4th PSM1735 impedance analyser, four-wire method, 10 Hz–1 MHz, EE ferrite cores; p. 69–71). Four conductor structures — solid track, multi-track (each track split into three sub-tracks), in-layer twisted (10/30/60 twist points) and planar Litz (10/30/60 transposition points via vias) — each in inside-/middle-/outside-edge placements, with air and ferrite cores; all four-turn windings; geometric parameters catalogued in Fig. 3.4 (p. 66: track widths 0.71/1.68/3.5 mm; sub-track 0.56 mm; clearances 0.25 mm; central limb 8 mm). Key quantified findings (pp. 71–84): planar Litz is the only structure that tames the proximity effect in ferrite-core inductors — at 500 kHz a Litz inductor measures 13 Ω vs ≈20 Ω for the others; at 400 kHz R_AC/R_DC is 23.6 (Litz) vs 50.8 (solid); at 800 kHz 528 vs 1746; Litz reduces ferrite-core resistance by 13.5%/26%/35.6%/55% at 100/250/500/800 kHz relative to solid (p. 83). Penalties: Litz raises R_DC and cuts inductance (−17.7% to −34.4% across 100–800 kHz; 317 µH vs ≈480 µH at 800 kHz, p. 84). In-layer twisting alone is shown *not* to work (resistance rises with twist count, pp. 75–76). For air cores, Litz never pays off below 1 MHz (+25%/+14%/+11% resistance at 250/500/800 kHz vs solid, p. 82). Self-resonance for ferrite cores ≈1 MHz. Design guidance figure (Fig. 3.15, p. 80) maps structure adequacy at 50 kHz vs 600 kHz. The optimal transposition count is emphatically **not** the maximum — proximity mitigation saturates while R_DC grows linearly (pp. 83–84). These findings fed the MS2 prototype, whose Litz windings cut winding resistance ~30% at 50 kHz vs solid wire (pp. 84, 103).

**Soft-switching theory (pp. 62–65).** Conventional leakage-based ZVS (DAB/PSM) is load-dependent and fails at low L_lk; EPS/DPS/TPS add prohibitive control burden; LLC/CLLC add passives and variable-frequency control. The thesis' answer adapts **adiabatic-logic principles**: use magnetising inductance L_m in parallel resonance with MOSFET C_DS/C_GS to recycle capacitive energy, "effectively decoupling the requirements for balancing accuracy from the requirements for high efficiency" (p. 64).

**(c) MS2 pack-level converter (pp. 84–119).** Topology (Fig. 3.16, p. 85): multiple full-bridge modules on one multi-winding power transformer, plus a second **control/gate transformer** that distributes synchronised gate signals — only four microcontroller signals (G1–G4) drive all switches regardless of module count (p. 87). Terminals can be independent, parallel, series, or combined, plus a non-isolated **DCAT** (DC autotransformer) mode with all taps in series and both electric and magnetic power paths (pp. 86–87) — this is the thesis' direct continuation of the DCAT lineage. Soft switching: ZVS at turn-on and ZCS at turn-off by resonating C_DS against power-transformer L_mp and C_GS against gate-transformer L_mg during precisely computed dead-times (full four-state power-side and eight-state gate-side derivations with closed-form dead-time equations, Eqs. 3.1–3.28, pp. 92–101; experimental ZVS/ZCS waveforms Fig. 3.19, p. 91). **Prototype (pp. 101–104):** eight-port, single shared core; 32 PCBs vertically stacked as 8 windings × 4 parallel boards; interleaved winding order cuts leakage from 805 nH to **167 nH** between adjacent terminals (≈4.8×), and by up to **26×** between the most-separated terminals 1↔8 (p. 103). Design values (Table 3.1, p. 105): V_in/V_out 50 V per module; f_sw 50 kHz; switches FDMS86300 (power)/IRFS3006 (gate drive); C_DS 1850 pF, C_GS 5850 pF; leakage 167 nH. (The design-trade-off text on p. 104 quotes an optimised magnetising inductance of 1638 µH with 3.5 µs dead-time and <100 mA magnetising current, whereas Table 3.1 lists L_mp = 25.4 µH, L_mg = 4.7 µH — an internal inconsistency to note if quoting.) **Results (pp. 104–115):** five configurations tested (I4-I4, P4-P4, S4-S4, P4-S4, S4-P4, DCAT), up to 400 V series stack from 50 V modules; peak efficiency **98% at 250 W in the P4-S4 configuration**, >96% over most of the range (Fig. 3.26, p. 109); **DCAT mode peaks at 98.8%** at elevated power because the core shifts to voltage-balancing rather than bulk transfer (p. 110). DCAT dynamic test: stepped 0→4 A load in 1 A/10 s steps on one 50 V tap; the loaded tap shows only the internal-impedance drop while the unloaded tap "remains firmly at its nominal 50 V level" — inherent magnetic balancing (Fig. 3.27, pp. 110–112). Thermal: **below 47 °C at 450 W** steady state, passively cooled (Fig. 3.28, p. 112). Balancing tests with eight Keithley 2281 simulators emulating 4-series Samsung 18650 (3500 mAh) strings, five SOC scenarios incl. 100/100/90/90/80/80/70/70%; static scenarios converge, and under one/two continuous 4 A loads max SOC divergence is contained to ≈20%/≈25% (pp. 113–115). Loss analysis vs a conventional DAB (Fig. 3.30, p. 116): total loss 11→3.8 (traditional) vs 7.3/7.1→2/2.8 units across 50 W/250 W/1 kW cases; capacitive-loss study shows up to 3.7% loss reduction from the adiabatic drain-source scheme at low power (pp. 117–119).

**(d) MFWE cell-level converter (pp. 120–133).** Topology (Fig. 3.32, p. 120): batteries connected electrically in series and magnetically in parallel on one core; one switch per cell plus a flying capacitor C1 for volt-second balance; no controller feedback needed (p. 121). Switching frequency 100 kHz; same magnetising-inductance soft-switching with closed-form dead-time (Eqs. 3.33–3.44, pp. 122–124). Construction (pp. 124–125): 4-cell prototype; ferrite-slab core; **single-turn 150 µm copper-foil windings** insulated with Kapton, stacked in extreme proximity for ultra-low leakage; Toshiba TPHR6503PL main switches (30 V, 0.65 mΩ typ.), Infineon IPT007N06N flying-capacitor switch; Imperix B-Box control; multi-level PCB stack with foil soldered directly at MOSFET drain/source to shorten the AC loop. **Results (pp. 126–133):** loss characterisation at no-load/0.2 A/1 A (no-load: switching 58.8% + core 17.5% of losses; at 1 A winding losses dominate at 29.2%; absolute winding loss 1.755 mW → 114.49 mW, matching I²R, pp. 127–128). Eleven port-configuration experiments: efficiency >90% above 5 W, >96% in single-supply multi-load (SLLL/SLLO) cases; **peak 98.937% in the S2L2 configuration** (two series supplies → two series loads); **12 A from a single tap at 97.06%**; >95% in asymmetric S2LL/SSL2 cases (Fig. 3.36, pp. 128–129). Transformer voltage shows the linear resonant ramp confirming ZVS (Fig. 3.38, p. 131), "directly enabling the peak efficiency of 98.94% observed during the experiments" (p. 130). Balancing validation with eight Keithley 2281S-20-6 simulators emulating Samsung 18650 3.7 V/2.6 Ah cells, two parallel groups of four: static Cases 1–3 (100/90/80/70; 100/80/80/60; 100/100/60/60%) converge, with **SOC difference consistently reduced to <1% within the 60-minute logging window** (p. 131); dynamic Cases 4–5 (one or two continuous 4 A loads) contain max SOC divergence to ≈40% (pp. 132–133). Chapter conclusion (pp. 134–135) restates: MS2 98% isolated / 98.8% DCAT, 47 °C at 450 W; MFWE 98.94% peak, "rapid static balancing within 60 minutes", "an order-of-magnitude reduction in parasitic impedance" from foil winding.

### Chapter 4 — HB-MLI: Hardware Design and Single-Phase Characterization (pp. 137–153)

**Topology (pp. 138–140):** a hierarchical *binary tree* of half-bridges, Level 1 at the output down to Level N at the DC sources; N-level leg uses 2^N − 1 half-bridges to generate 2^N output levels spanning 0 to 2^(N−1)·V_DC; "the architecture functions as a power digital-to-analog converter" (p. 139). **One control signal per level** drives all half-bridges of that level (p. 139). Hybrid-frequency principle: Level 1 (full voltage) switches at ~fundamental; Level N (lowest voltage) carries the 100 kHz CBPWM (pp. 139, 142). Single-phase legs are unipolar; the three-phase line-to-line differencing removes the DC offset and raises the level count to up to 2k−1 (p. 140). **Control (pp. 141–144):** carrier-based PWM with a single dynamically level-shifted triangular carrier; implemented via Simulink → HDL Coder → VHDL → AMD Vivado on the FPGA of an Imperix B-Box (CPU handles references, FPGA the deterministic PWM), because the CPU alone could not sustain the 100 kHz + multi-rate signal set (pp. 142–144). **Prototype (pp. 144–147):** 5-level, **16 independent DC inputs**, circular vertically-stacked 3D packaging; gate-driver boards double as structural members; 8-layer 2 oz-copper power board; optional custom heatsink in the central void, but nominal cooling is natural convection. MOSFETs per level (Table 4.2, p. 145): L1 750 V UJ4SC075009K4S SiC 9 mΩ @ 50 Hz; L2 300 V IXFX210N30X3 5.5 mΩ @ ~100 Hz; L3 150 V NTMTSC4D3N15MC 4.45 mΩ @ ~200 Hz; L4 80 V NTMFWS1D5N08XTIG 1.43 mΩ @ ~400 Hz; L5 40 V TPWIR104PB 1.14 mΩ @ 100 kHz. **(b) Efficiency campaign (pp. 147–151).** Test bench: Keithley 2281S-20-6 supplies, 5 kW adjustable resistive load, Imperix B-Box, LeCroy MDA 8208HD scope, **Hioki PW8001 power analyser** in wide-band mode (1 Hz–several MHz), NI DAQ thermocouples (p. 147). Conditions (Table 4.3, p. 149): 15 V DC per Level-5 module; AC output 0–240 V sinusoidal; max tested power 1.2 kW; switching 50/100/200/400 Hz and 100 kHz per level; output LC filter 270 µH / 9 nF. Results, single-phase resistive load: **98.91% at 120 W; peak 99.46% at ≈400 W; 99.14% at the 1.2 kW maximum tested power** (Fig. 4.6, p. 149–150). The analyser's ±0.03% basic accuracy gives a 99.43–99.49% confidence band on the peak (p. 148). **Thermal:** sustained 800 W single-phase for 15 min under passive convection only; steady state reached in ≈5 min; **maximum ≈46 °C** on a Level-1 MOSFET (Fig. 4.7, p. 150); steady-state temperature vs power to 800 W correlates with R_DS(on) — Level 5 (100 kHz, 1.14 mΩ, 15 V) runs coolest, validating the hybrid-frequency thermal strategy (Fig. 4.8, pp. 150–151). Conclusion (pp. 151–153): 17-level phase voltage (incl. zero) from 16 DC units; ">99% across the majority of the power range"; high resolution "effectively eliminates the requirement for bulky LC filters".

### Chapter 5 — HB-MLI: Three-Phase Implementation (pp. 155–171) — THE MOTOR-DRIVE VALIDATION

**System and control (pp. 156–161).** Solid copper rods bus the 16 DC units to all three phases (p. 156). Closed-loop control is a **cascaded synchronous-reference-frame (dq0) dual-loop PI controller** on the B-Box CPU (outer voltage loop generating i_d/i_q references, inner high-bandwidth current loop, PLL, Park/inverse-Park; FPGA does modulation) with a **Third Harmonic Injection (THI)** block (V3 = Vm/6) ahead of PWM giving the standard 2/√3 ≈ 1.1547 (≈15.5%) DC-bus utilisation boost, fully derived in Eqs. 5.1–5.11 (pp. 157–161; Fig. 5.2 block diagram).

**Experimental validation on passive loads (pp. 161–167).** No-load: staircase phase voltages peak at 240 V (= 16 × 15 V); filtered line-to-line ≈415 V peak (≈240·√3) (p. 162). Under an 800 W inductive load (R = 26 Ω, L = 832 µH per phase): stable 120 V-peak sinusoidal phase voltages, 4.6 A-peak sinusoidal currents (p. 163). Open-loop start-up direct into the R-L load settles "almost immediately" (pp. 163–164). Closed-loop load steps 200 Ω → 100 Ω → 40 Ω: no perceptible sag/overshoot; line-to-line peak ≈204 V under SPWM (pp. 164–165). With THI: flat-topped 120 V-peak phase voltages, sinusoidal line-to-line at **≈240 V peak** (vs 204 V), currents ≈3 A peak; load-step test repeated with THI, boost maintained through transients (pp. 165–166). Harmonic analysis at 800 W (Fig. 5.10, pp. 166–167): phase-voltage THD 7.14% unfiltered → **1.16%** filtered; line-to-line 4.45% → **1.10%**; phase current 1.20% unfiltered → **1.17%** with filter (text attributes the filtered-current figure to "PR control"); explicitly linked to reduced torque ripple and IEEE 519 compliance. (Note: the Abstract (p. ix) quotes "THD of 1.04%" and Chapter 6 (p. 174) quotes "2.15% in line-to-line voltage and 1.04% in phase current" — slightly different figures from the Chapter 5 measurements; cite whichever with its page.)

**(a) Machine-load tests — the feasibility precedent (pp. 161, 168–170).**
1. **40 W induction motor.** "its performance was evaluated while driving a 40W, 240V three-phase induction motor... moving beyond the characterization with passive R-L loads. During the steady-state test, the motor was observed to be operating at a speed of 489.3 rpm" (p. 168). Fig. 5.11 (p. 168) shows filtered sinusoidal phase voltages at 120 V scale-peak with 120° displacement and clearly sinusoidal phase currents of ≈±1.5 A, "demonstrating the inverter's ability to supply the necessary magnetizing and torque-producing currents to the motor."
2. **400 V industrial machine on a back-to-back bench.** The full test platform (Fig. 5.1, p. 156) comprises the Imperix B-Box + motor interface, the 3-phase HB-MLI prototype, DC power supplies, a 3-phase electronic load, a thermal camera, an oscilloscope, and a **back-to-back induction-motor test bench**. Machine ratings (Table 5.1, p. 169): 2 pole pairs; rated line voltage 380 V (50 Hz) / 460 V (60 Hz); **rated power 4 kW**; rated torque 26 / 21.5 Nm; rated speed 1464 / 1769 rpm; rated current 8.4 / 7.1 A; power factor 0.81 / 0.79. Test regime: "the proposed 3-phase prototype as the primary driver for a 400V industrial induction machine... targeting a 120V peak phase voltage regime to analyze the performance of the inverter at reduced modulation indices. The machine was subjected to a series of stepped speed commands from 150 rpm up to 500 rpm" (p. 168). Fig. 5.12 (p. 169) presents four panels: (a) high-resolution 120 V-peak phase voltages tracking the frequency steps; (b) balanced three-phase currents on a ±20 A axis "illustrating balanced operation and the impact of the 6A power supply current limitation at higher speeds"; (c) staircase line-to-line voltages "demonstrating high-resolution staircase approximation and dq0 regulation stability"; (d) measured-vs-desired stepped speed tracking 150–500 rpm, "highlighting the stable response in the 150 rpm region and supply-induced mechanical ripples during high-current demand stages." Interpretation (p. 170): speed follows the setpoints; in the 150 rpm region "the speed profile is remarkably stable"; ripple at 400–500 rpm "primarily attributed to the current limitations of the laboratory DC power supplies, which are rated for a maximum output of 6A" — supply saturation limits the dq0 controller's voltage stiffness, and "the overall system performance at high speeds is constrained by the external power infrastructure rather than the inverter topology itself." Chapter conclusion (pp. 170–171): THI's 15.5% boost delivered the "required 240V peak line-to-line output for machine excitation"; line-to-line THD 1.10%; dq0 loops "remained converged and the switching logic remained stable even when the system was pushed into an external power-limited regime"; the HB-MLI is "not only an efficient power converter but also a robust motor drive capable of meeting the demands of industrial automation and electric propulsion."

### Chapter 6 — Conclusion and Future Work (pp. 173–180)

Summarises the three contributions with the headline numbers (HB-MLI: 99.46% peak, 46 °C at 800 W, 17-level output; MS2: 98% isolated, 98.8% DCAT, 47 °C at 450 W, inherent magnetic balancing; MFWE: 98.94% peak, 30% SOC discrepancy resolved to equilibrium within 60 min) (pp. 174–176). Interoperability is argued analytically, not experimentally: the MS2 "was experimentally verified to maintain voltage stiffness with less than 1% deviation under dynamic load steps", supporting the "Non-Isolated Tap" architecture the HB-MLI needs (p. 176). Objectives table (p. 177) marks all five objectives "Fully achieved/met". Limitations and future work: see §5 below.

## 4. Quotable passages (with pages)

- **Machine loads / back-EMF (the WP2 anchor):** "The system was successfully integrated with a 400V industrial induction machine, proving that **the hierarchical architecture can maintain electrical stability under the complex back-EMF of high-voltage machinery**. The dq0 controller demonstrated precise regulation in the 150 rpm region, confirming the effectiveness of the proposed voltage and current control loops." (p. 174)
- "The successful and stable operation of the inverter while driving the induction motor provides crucial validation of its suitability for electric drive applications." (p. 168)
- "...the proposed HB-MLI is not only an efficient power converter but also a robust motor drive capable of meeting the demands of industrial automation and electric propulsion." (p. 171)
- "This result confirms that while the dq0 control framework remains stable, the overall system performance at high speeds is constrained by the external power infrastructure rather than the inverter topology itself." (p. 170)
- **Hybrid-frequency principle:** "By confining high-frequency PWM to the lowest voltage stage while operating high-voltage stages at the fundamental frequency, the topology minimizes switching losses without compromising waveform quality." (Abstract, p. ix)
- **Efficiency:** "The inverter achieved a remarkable peak efficiency of 99.46% at approximately 400 W. Even at the maximum tested power of 1.2 kW, the efficiency remained extremely high at 99.14%." (p. 149)
- **Passive cooling:** "The maximum temperature recorded during this test was approximately 46°C... achieved without any forced cooling" (800 W, p. 150); "a maximum temperature of only 47°C under a 450W load" (MS2, p. 134).
- **Soft-switching decoupling:** "This approach theoretically allows for robust ZVS transitions even in transformers with the minimized leakage inductance required for precise balancing, effectively decoupling the requirements for balancing accuracy from the requirements for high efficiency." (p. 64)
- **Filter elimination:** "The high voltage resolution achieved in this chapter effectively eliminates the requirement for bulky LC filters, addressing the weight and volume constraints that typically limit the deployment of high-power BER interfaces." (p. 152)
- **Battery-string alignment (Vision):** "This work proves that by aligning the switching logic with the physical structure of the battery string, energy interfaces that are inherently more reliable, thermally stable, and economically viable can be created." (p. 180)
- **Statements of limitation that per-slot / open-end machine operation would address:** the machine tests were run at a *reduced modulation index* ("targeting a 120V peak phase voltage regime", p. 168) against a 400 V machine, and full-power machine operation was blocked by the 6 A lab supplies ("the laboratory power supply's 6A current limitation prevented the characterization of the system at its maximum theoretical thermal and electrical limits during high-speed motor operation", p. 178). The inverter remained an *external* drive feeding a standard star-connected machine through an LC filter and busbars; nothing in the thesis integrates the converter into the machine winding — the closest statement of forward direction is scaling "to 800V electric vehicle (EV) platforms and kilovolt-scale grid-tie storage" (p. 179), leaving converter-in-winding/per-slot operation entirely open.

## 5. Limitations / future work as stated (pp. 178–179)

Limitations: (1) **No system-level integration** — HB-MLI and balancers were "designed, prototyped, and validated as separate, standalone components... the dynamic interactions and control-system interoperability of the complete, unified system have not yet been experimentally verified." (2) **Battery simulators, not cells** — Keithley simulators do not capture electrochemical ageing, cycle life or impedance growth. (3) **Instrumentation constraints** — peak 99.46% is a single-phase measurement (three-phase operation validated via motor tests, but total three-phase efficiency may vary with parasitics/tolerances); the 6 A supply limit capped high-speed motor characterisation. Future work: unified hardware integration with a unified control architecture; validation on automotive-grade Li-ion packs with long-term cycling; scaling to 800 V EV and kV grid platforms (incl. parasitic-inductance study of the circular 3D busbar at higher level counts and WBG devices for the high-frequency submodule); Model Predictive Control for joint modulation/balancing optimisation; advanced packaging plus cost/manufacturability analysis.

## PROPOSAL USE MAP (detailed)

Conventions. (a) gives the exact proposal location(s); (b) the usage mode (anchor = load-bearing feasibility evidence; corroboration; background; defensive = pre-empts a reviewer objection); (c) a ready-to-use fragment in UK English where one is worth pre-drafting. Standing rule (Master Handover S7c): the thesis is ANONYMISED in all proposal body text. Refer to "doctoral research in the group" or "the group's HB-MLI motor drive"; the named thesis appears only in the reference list. Citation keys differ by document: the machine-drive result is [20] in the Vision drafts and [6] in the Approach draft; reconcile per Master Handover S9/S11 before submission. The eight highest-value items are marked ★.

**★ 1. The 400 V industrial machine drive test (pp. 156, 168–170; Table 5.1 p. 169; Fig. 5.12).** THE feasibility anchor of the whole proposal: a hierarchical binary-tree multilevel converter of the group's family drove a 4 kW-rated, 400 V industrial induction machine (2 pole pairs, rated 8.4 A / 1464 rpm at 50 Hz) on a back-to-back bench under closed-loop cascaded dq0 dual-loop PI control with third-harmonic injection, through stepped speed commands from 150 rpm to 500 rpm in a 120 V peak phase-voltage regime, with balanced three-phase currents up to the 6 A laboratory supply limit.
(a) Vision "Crossing the line: the 50 V claim" (VIS-CROSS-v7, drafts/02, the clause "binary-tree converters of this family driving industrial induction machines with back-EMF under closed-loop control [20]"); Approach "Building on previous work" (drafts/03, the HB-MLI sentence citing [6] and the lineage-table row "HB-MLI motor drive (doctoral thesis, 2026)"); Approach WP2 preamble, RQ2 and H2 (the precedent that makes "adiabatic ZVS from an inductive back-EMF source" an extension of a working baseline, not a cold start); Capability Module 1 (drafts/05, the anonymised sentence "Doctoral research in the group has since driven an industrial induction machine...").
(b) Anchor; quote conditions exactly, never beyond them (see Traps).
(c) Fragment: "Doctoral research in the group has driven a 4 kW-rated, 400 V industrial induction machine with a converter of this binary-tree family under closed-loop cascaded dq0 control with third-harmonic injection, tracking stepped speed commands from 150 rpm to 500 rpm in a 120 V peak phase-voltage regime, and remaining stable up to the 6 A current limit of the laboratory supplies."

**★ 2. The bottleneck attribution (p. 170).** "the overall system performance at high speeds is constrained by the external power infrastructure rather than the inverter topology itself"; speed ripple at 400–500 rpm is attributed to the 6 A supply rating, and the dq0 loops and switching logic remained stable into the supply-limited regime (p. 171).
(a) Approach "Feasibility and risk management" and the WP2/RQ2 feasibility argument; usable verbatim (referenced, anonymised) wherever a reviewer might read the 500 rpm ceiling as a converter limitation.
(b) Defensive.
(c) Fragment: "Performance at the highest tested speeds was bounded by the 6 A rating of the laboratory DC supplies, not by the converter: the control loops and switching logic remained stable throughout the supply-limited regime."

**★ 3. The back-EMF stability statement (p. 174).** "The system was successfully integrated with a 400V industrial induction machine, proving that the hierarchical architecture can maintain electrical stability under the complex back-EMF of high-voltage machinery."
(a) Approach RQ2/H2 and WP2 preamble; Vision "Crossing the line" as the evidential warrant for claiming the family already meets back-EMF.
(b) Anchor (quotable thesis conclusion; anonymise attribution in body text).
(c) Fragment: "The group's binary-tree converter family has already maintained electrical stability under the back-EMF of a 400 V industrial machine under closed-loop control; this programme asks the per-slot form of that question."

**★ 4. The 40 W motor test (p. 168; Fig. 5.11).** A 40 W, 240 V three-phase induction motor ran at 489.3 rpm steady state with sinusoidal phase currents of approximately ±1.5 A; the thesis calls this "crucial validation of its suitability for electric drive applications."
(a) Approach "Building on previous work" (secondary machine precedent alongside item 1); Capability Module 1 if a second machine data point is wanted.
(b) Corroboration.
(c) Fragment: "The same converter family has also driven a 40 W, 240 V induction motor at 489.3 rpm steady state with sinusoidal phase currents, beyond characterisation on passive resistive-inductive loads."

**★ 5. MS2 DCAT-mode result (pp. 86–87, 110–112, 134).** The MS2 converter in non-isolated DC-autotransformer (DCAT) mode peaked at 98.8% efficiency, held an unloaded tap "firmly at its nominal 50 V level" under 0 to 4 A stepped loading on another tap, and ran below 47 °C at 450 W with passive cooling.
(a) Approach "Building on previous work" and the intellectual-lineage table: this is the 2026 corroboration of the 2016 DCAT anchor reference (magnetic voltage distribution plus adiabatic switching), showing the lineage is live, reproduced in current hardware, and inherently voltage-stiff; Capability Module 1 (anonymised); Master Handover S7c lists it as one of the two proposal-critical thesis results.
(b) Corroboration of the adiabatic lineage.
(c) Fragment: "The magnetic voltage-distribution principle established by the group's adiabatic DC-AC converter has since been reproduced in a multi-port pack-level converter operating in DC-autotransformer mode at 98.8% efficiency, whose unloaded taps hold their nominal 50 V level under stepped loading of neighbouring taps."

**★ 6. HB-MLI efficiency set (pp. 147–150; Table 4.3, Fig. 4.6).** 98.91% at 120 W, peak 99.46% at approximately 400 W, 99.14% at the 1.2 kW maximum tested power; single phase, resistive load, 15 V per Level-5 module, 16 DC inputs, 100 kHz lowest stage, Hioki PW8001 wide-band measurement with a 99.43–99.49% confidence band on the peak.
(a) Capability Module 1 (drafts/05, both variants; anonymised: "doctoral research in the group"); Approach "Building on previous work"; supports the Vision clause "adiabatic switching at above 99% efficiency [3]" as family-level corroboration.
(b) Corroboration; always state "single-phase, resistive load, up to 1.2 kW tested" alongside the 99.46% figure.
(c) Fragment: "The group's hierarchical binary multilevel inverter measured 99.46% peak efficiency at approximately 400 W and 99.14% at its 1.2 kW maximum tested power, in single-phase operation on a resistive load, measured on a wide-band power analyser with a basic accuracy of ±0.03%."

**★ 7. Passive-cooling thermal results (pp. 150–151, 112, 134).** HB-MLI: approximately 46 °C maximum after 15 minutes at 800 W single phase, natural convection only, coolest stage being the 100 kHz low-voltage level. MS2: below 47 °C at 450 W, passively cooled.
(a) Approach RQ5/WP2 thermal plausibility (low device losses are what make per-slot ICs inside a 120–150 °C winding thinkable); Capability Module 1; Vision cascade paragraphs as implicit support for "no added filtering or forced cooling".
(b) Corroboration.
(c) Fragment: "Both converters run cool enough for passive cooling: the inverter reached approximately 46 °C at 800 W and the pack-level converter 47 °C at 450 W, in both cases under natural convection alone, with the 100 kHz low-voltage stage the coolest in the stack."

**★ 8. The stated gap: reduced modulation index, external drive, per-slot operation untouched (pp. 168, 178–179).** The machine tests ran at reduced modulation index (120 V peak against a 400 V machine); the 6 A supplies "prevented the characterization of the system at its maximum theoretical thermal and electrical limits"; the converter remained an external terminal-connected drive; future work stops at 800 V EV and kV grid scaling. Nothing in the thesis integrates the converter into the winding.
(a) Approach "Building on previous work" (the lineage-table gap column "Terminal-connected only, not per-slot bilateral") and Vision "Novelty" defence: the group's own prior work authenticates the gap this programme fills, so the proposal extends rather than repeats it.
(b) Defensive/anchor for the novelty claim.
(c) Fragment: "That demonstration remained a terminal-connected drive at reduced modulation index; converter-in-winding operation, the subject of this programme, is untouched by it and is listed in the underpinning doctoral work only as an open direction."

**9. Magnetising-inductance adiabatic ZVS with closed-form dead-times (pp. 62–65, 92–101, 122–124).** ZVS/ZCS by resonating device capacitances against magnetising (not leakage) inductance, with closed-form dead-time equations (Eqs. 3.1–3.28, 3.33–3.44), "effectively decoupling the requirements for balancing accuracy from the requirements for high efficiency" (p. 64).
(a) Approach WP2/T2.1 (the ZVS-envelope mapping method exists and is validated); RQ2/H2 background.
(b) Background/corroboration; the design equations are the methodological inheritance WP2 adapts to a winding source.

**10. Third-harmonic injection and control implementation detail (pp. 141–144, 157–161, 165–166).** Cascaded dq0 dual-loop PI plus PLL on the CPU, FPGA modulation via HDL Coder/Vivado on an Imperix B-Box, THI (V3 = Vm/6) giving the 2/sqrt(3), approximately 15.5%, bus-utilisation boost and 240 V peak line-to-line from a 240 V staircase.
(a) Approach WP2/WP3 methodology credibility (the group already runs exactly the CPU/FPGA split and closed-loop machine control the programme needs) and Capability Module 1 texture.
(b) Background.

**11. Waveform quality at 800 W (pp. 166–167).** Filtered phase-voltage THD 1.16%, line-to-line 1.10%, phase current 1.17%, linked in the thesis to reduced torque ripple and IEEE 519 compliance.
(a) Approach WP4 torque-ripple test rationale; Vision cascade ("torque ripple falls without added filtering").
(b) Corroboration; USE ONLY the Chapter 5 figures with pages, never the Abstract/Chapter 6 variants (see Traps).

**12. The 52-prototype planar magnetics study (pp. 65–84).** Quantified R_AC/R_DC and inductance trade-offs for planar Litz versus solid, multi-track and twisted structures at 50–800 kHz; interleaving cuts leakage 805 nH to 167 nH (up to 26 times); optimal transposition count is not the maximum.
(a) Approach WP1 (validated multi-winding electromagnetic design methodology in the team) and A1 corroboration.
(b) Background/corroboration.

**13. MFWE headline results (pp. 126–133).** 98.94% peak (S2L2), 12 A from a single tap at 97.06%, sub-1% SOC convergence within 60 minutes.
(a) Capability Module 1 and the A4 paper's numbers (they match: 98.94%, 60 minutes); Approach "Building on previous work" only in passing.
(b) Corroboration.

**14. Hybrid-frequency principle (Abstract p. ix; pp. 139, 142).** "By confining high-frequency PWM to the lowest voltage stage while operating high-voltage stages at the fundamental frequency, the topology minimizes switching losses without compromising waveform quality"; one control signal per level.
(a) Vision and Approach wherever the binary-tree family is characterised in a sentence; explains why the family's efficiency and thermal numbers arise.
(b) Background (quotable, anonymised).

### Traps

- **Do not inflate the machine test beyond its conditions.** The 400 V machine was driven at reduced modulation index (120 V peak phase), at 150–500 rpm only, well below its 4 kW rating, and behind an LC filter as an external terminal-connected drive, with high-speed behaviour bounded by 6 A supplies. Never write "drove a 4 kW machine" or imply full-voltage, full-power or high-speed operation; the safe formula is item 1(c). Equally, do not present the 99.46% efficiency as a three-phase or machine-load figure: it is single-phase, resistive load, 1.2 kW maximum tested (thesis pp. 148, 178 say so explicitly).
- **Two internal inconsistencies in the thesis must not be quoted without resolution.** (i) Magnetising inductance: p. 104 quotes an optimised L_m of 1638 uH with 3.5 us dead-time, while Table 3.1 (p. 105) lists L_mp = 25.4 uH and L_mg = 4.7 uH. Do not cite any MS2 magnetising-inductance value until the PI resolves which is correct. (ii) THD: Chapter 5 measures 1.16% (phase), 1.10% (line-to-line), 1.17% (current) at 800 W (pp. 166–167), but the Abstract (p. ix) says 1.04% and Chapter 6 (p. 174) says 2.15% line-to-line and 1.04% current. If a THD number is needed, use the Chapter 5 measured values with their page citation and flag the discrepancy to the PI; never mix the sets.
- **Anonymisation.** No proposal body text may name the thesis author; Capability Module 1 and "Building on previous work" already use the anonymised formula. The full citation goes only in the reference list (Master Handover S7c), and the [20]/[6] key mismatch between Vision and Approach must be reconciled at final numbering (Master Handover S9/S11).
- **Battery simulators, not cells.** All balancing validation used Keithley simulators (pp. 113–115, 131–133); do not describe MS2/MFWE results as validated "on battery packs".

---
*Internal digest for the EPSRC evidence dossier. All figures transcribed from the thesis as printed; discrepancies noted inline (Table 3.1 vs p. 104 magnetising inductance; Ch. 5 vs Abstract/Ch. 6 THD figures). Never quote un-paginated numbers from this digest without checking the cited page.*


<!-- ==================== FILE: evidence/06_Edwards_transfer_viva_digest.md ==================== -->

# Digest 06 — Edwards Transfer Viva Report (2nd draft, May 2026)

## 1. Identity and status

- **Title (as printed):** "Optimised Efficiency and Compact Integration of Drive Unit for Ultra-High-Speed Electric Motors"
- **Author:** Zachary Edwards, University College London, Department of Mechanical Engineering
- **Document type (as printed):** "MPhil to DPhil Transfer Viva" report; file is the second draft dated 26-05 (May 2026). 50 pages including references. Project end date stated as 31 October 2028 (p. 47).
- **File:** `/home/user/proposal/Transfer Viva 2nd draft 26-05.pdf`

**STATUS: NOT CITABLE.** Unpublished, unexamined student transfer report in draft form. It must never appear in the proposal's reference list and no claim may be sourced to it. Its value is internal only: the team's map of the integrated-motor-drive (IMD) landscape and the only end-to-end account of DCAT-based IMD design. Every claim the proposal needs is either traceable to a published source (Section 3) or is unpublished original work that cannot be cited at all.

## 2. Section-by-section walk

### Abstract (p. 2)

Power electronics for a **20 kW IMD for longer-range electric aircraft propulsion**, with **partial discharge (PD) mitigation** as the central reliability concern: integrate electronics within the machine to cut cable lengths and parasitics; split the DC bus into lower voltage levels feeding a modular multilevel DC/AC stage; prioritise scalability; explore packaging MLI topologies as integrated circuits (ICs).

### 1. Introduction and Project Overview (pp. 4–5)

Decarbonisation framing with quantified claims and stated provenance:

- Paris Agreement: 43% CO₂e cut by 2030, net zero 2050, 1.5 °C — **UN web page [1] (2025)**.
- EVs: net reduction of ~**80 Mt** GHG in 2022 alone — **IEA Global EV Outlook [2] (2023)**.
- **Aviation CO₂e: 882 Mt in 2024**, international-flight emissions more than doubled since 1990 — a **Statista topic page [3]** (M. Rathore, 17 Dec 2025). Weak provenance; the proposal should use ICCT/IATA/IEA primary data.
- Electric aircraft: **49–88% CO₂e reduction** vs conventional and **cruise efficiencies up to three times higher** — **ICCT report, Mukhopadhaya & Graver 2022 [4]**.
- **ARPA-E targets: minimum 12 kW/kg power density and 93% cruise efficiency** for a narrow-body aircraft to complete a five-hour flight — **ARPA-E FOA document, 16 Dec 2019 [5]**.
- Sets the 20 kW target with scalability emphasised. Figure 1.1: powertrain [37], Joby eVTOL [44]. (Minor slip: p. 5 text cites "Figure 1.3" for the conventional-vs-integrated layout; the figure is captioned 1.2.)

### 2.1 Electric Aviation Context and Design Trends (p. 6)

Distributed Electric Propulsion (DEP) as the defining trend; eVTOL taxonomy (wingless vs powered-lift; the latter split into vectored/independent/combined thrust). **eVTOL design-survey statistics:** of **120 eVTOL concepts (2014–2022)**, **powered-lift accounts for 57% of designs, within which vectored thrust comprises 53%** — **Ugwueze et al., AIAA SciTech 2023 [6]**. Inference: unit power rating is secondary to architectural scalability.

### 2.2 Partial Discharge in Aerospace Electric Propulsion (pp. 6–7)

V_spike = L_parasitic·dI/dt (Eq. 2.2.1); two-level inverters combine large ΔI with small Δt, hence large spikes. PD defined via partial discharge inception voltage (PDIV); lower air dielectric strength at altitude lowers PDIV — **Madonna et al., IEEE Trans. Ind. Appl. 2021 [7]**.

### 2.3 Integrated Motor Drives for Aerospace Applications (pp. 7–13)

**2.3.1 Motivation (p. 7).** The headline quantified claims, with provenance and age flagged:

- Eliminating separate housings and shielded inverter–machine cables **reduces volume by 10–20%** and **installation and manufacturing costs by 30–40%** — cited to **[8] Lee, Li, Han, Sarlioglu, Minav & Pietola, IEEE Trans. Transportation Electrification, 2018** (a review on IMDs/WBG for electro-hydrostatic actuators; the figures are second-hand survey numbers, not measurements from that paper).
- "**These changes can boost the system-level efficiency by 30% or more**" — printed **without its own citation**, following the [8]-cited sentence. The weakest quantified claim in the report and physically dubious as stated; do not repeat anywhere without an independent primary source.
- Phase-lead integration and modularisation improve fault tolerance — [9] Jahns & Sarlioglu, IEEE Power Electronics Magazine, Sept 2020. Improved EMC from removing interconnects — [8].

**2.3.2 Challenges (pp. 7–8).** Thermal proximity of inverter and machine [10]; and the **7.5 kW thermal barrier**: "[11] even suggesting that in IMDs above a 7.5 kW output … heating effects build up significantly and designs with increased complexity are required" — **[11] is F. J. Bartos, Control Engineering, 1 Dec 2000**, i.e. a **25-year-old trade-magazine article**, not peer-reviewed. The proposal must not lean on this figure except as historical context, and never via this report.

**2.3.3 Integration Configurations (pp. 8–9).** The IMD taxonomy. Figure 2.1 (from [8]): **(a) radial housing-mounted, (b) radial stator-mounted, (c) axial housing-mounted, (d) axial stator-mounted (endplate)**. Radial mounting suits high-speed machines, axial suits high-torque (stack-length/stator-diameter ratio, per [8]); stator-mounted variants are "purer" integration (interconnects fully eradicated) but complicate cooling; housing-mounted variants use the housing as a thermal barrier, easing cooling at the cost of volume. Figure 2.2 adds real examples: **(a) single-location radial mounting by Danfoss [38]** (VLT DriveMotor FCM 300), **(b) distributed-electronics radial by H3X [39]**, **(c) endplate integration from [14]**, **(d) the tilt-rotor motor system of the Archer Midnight eVTOL [43]**. Aerospace argument: single-location radial's non-axisymmetric geometry adds parasitic drag and interferes with tilt mechanisms, so **distributed radial or endplate mounting is preferred**; endplate integration needs a co-designed endplate and restricts end-winding ventilation but does not grow the diameter.

**2.3.4 Integrated Modular Motor Drives (pp. 10–11).** IMMD: basic module = stator pole-piece with concentrated coil and dedicated power converter; modules held by a bearing housing, capped by a redesigned endplate — **Brown, Jahns & Lorenz, IEEE IAS Annual Meeting 2007 [12]**. Modules termed **'Smart Stator Teeth' (SST)** in **Brockerhoff et al., IEEE EDPC 2014 [13]**, each connected to a central control unit, forming a multiphase machine with integrated electronics: phase-number flexibility, redundancy, fault management, scalability. Both [12] and [13] flag **DC bus capacitor size as the critical issue**: electrolytics are thermally excluded, and capacitors that fit cannot handle two-level-inverter DC-link ripple current.

**2.3.5 Wide Bandgap Devices (p. 11).** (Heading misprinted "Wind Bandgap Devices".) **SiC and GaN: practical temperature limit ~600 °C vs 225 °C for Si**; SiC has higher thermal conductivity and suits >1000 V; choice application-dependent — all cited to **[10] Abebe et al., IET Electric Power Applications 2016**.

**2.3.6 Existing IMD Implementations (pp. 11–13).** **[14]** Wheeler et al. (EPE 2005) — fully integrated 30 kW matrix-converter drive, endplate-mounted, finned endplate + shaft fan; **[15]** Hilpert et al. (EDPC 2014) — endplate integration, liquid cooling, 'inverter building blocks' (one half-bridge each) on direct-cooled aluminium baseplates; **[16]** Chen et al. (IEEE TTE) — radial, WBG current-source inverter replacing DC-link capacitors with inductors, shared water jacket in a hexagonal stator housing; **[17]/[18]** Wang et al. (IEEE JESTPE 2025) and Swanke et al. (IEMDC 2021) — the aerospace flagship: **2 kV, 1 MW, 20,000 rpm IMMD** with a 200 kW risk-retirement build, radial submodules of paired SiC H-bridges, 9 cold plates for 18 power modules, flooded slots, and explicit PD countermeasures (extra insulation at PD-prone areas, rounded edges, optimised gaps). Summary (p. 13): aerospace IMD literature is thin; thermal management is inseparable from integration strategy; no consensus inverter topology; WBG generally adopted; high power needs liquid + air cooling.

### 2.4 Electric Machine Considerations (pp. 13–15)

Machine comparison from **[19] El Hajji et al., *Aerospace* 2024 (1 MW S-PMSM case study)**: PMSM best overall; WFSM/IM magnet-free but lossier; HTSM cryogenics too complex; SRM robust but less efficient, larger, higher torque ripple. **Slot/pole vs speed weight trade-off, also [19]:** **12/10** — weight falls substantially up to **10,000 rpm** then plateaus; **24/20** — keeps improving to **15,000 rpm**; **36/30** — significant gains only up to **5,000 rpm**. Decision: PMSM, preliminary target **5,000–15,000 rpm**, finalised with slot-pole and power-electronics choices.

### 2.5 Advanced Inverter Topologies (pp. 15–18)

**2.5.1 Motivation for MLIs (pp. 15–16).** Second headline claim: "typically, about **40% of the volume of the motor drive constitutes of the capacitors**, rendering compact integrated drives above 7.5 kW unfeasible within the original motor envelope **[14]**" — the 40% figure is thus sourced to the **2005 Wheeler paper**, twenty years old; the 7.5 kW envelope statement here is also pinned to [14], while §2.3.2 pinned a similar 7.5 kW threshold to the 2000 trade article [11]. Note both the age and the double attribution. MLIs cut DC-link capacitor needs and THD. **THD comparison from [20] (Paterakis, Marouchos & Darwish, UPEC 2017): 13-level MLI 5.285% THD vs 73.98% for a 3-level PWM inverter.** Reduced voltage steps also shrink dv/dt spikes, cutting PD risk. Trade-offs: device count, control complexity, capacitor balancing.

**2.5.2 MLI Control and Topologies (pp. 16–18).** Survey keyed to **[21] Poorfakhraei, Narimani & Emadi, IEEE Open Journal of Power Electronics 2021**: NPC (compact, poor scalability, unequal switch loss), ANPC (equalised losses, complex control), Flying Capacitor (cost-scalable but bulky, needs balancing and many sensors), NNPC (compromise, still capacitor-bound), CHB (modular and scalable but needs isolated DC sources), MMC (reliable/modular/scalable but capacitor-heavy with pre-charge circuits), T-type (simple but high switch stress, unsuited to high-voltage traction). Then the **generalised MLI [22] (Peng, IEEE Trans. Ind. Appl. 2001)** — self-balancing via redundant states, but very high component count. Pivot to the core idea: **[23] — the DCAT (DC-autotransformer)**: DC bus divided by a DCAT, multilevel waveform synthesised by a voltage tap selector; H-bridge modules paralleled with capacitors defining intermediate levels, magnetically coupled via a multi-winding transformer that forces balancing currents; fewer, smaller capacitors; drawbacks are the added voltage-splitting stage and the non-trivial multi-winding HF transformer. Finally, **open-end-winding machines [24]**: no capacitor balancing, added redundancy, separate supplies per inverter, level scaling beyond a single inverter — at the price of control complexity.

### 2.6 IC Implementation (pp. 19–21)

**[25] Farhat & Baghdadi (IEEE Trans. Power Electronics, 2026, pp. 1–13)** — on-chip binary-tree multilevel converter in a **130 nm Bipolar-CMOS-DMOS** process, limited to **8 levels** by breakdown voltage, die on daughterboard with **33 µm Al bond wires**, prototype **3.530 mm × 4.297 mm**, reliable operation only to **2 A**; **[26] Weiss et al. (IEEE CSICS 2015)** — monolithic single-phase diode-clamped converter in AlGaN/GaN-on-Si, chip **2 × 3 mm²**, max **5 A**; **[27] Li et al. (IEEE EDL 2017)** — 200 V p-GaN HEMTs on GaN-on-SOI, cited for fabrication/substrate-coupling issues. Scaling routes: higher-voltage processes, wider devices, or series/parallel chip stacking at board level [25]. **Defects:** the p. 20 figure is numbered **"Figure 2.12"**, duplicating the DCAT figure on p. 19; its caption attributes the binary-tree topology/chip to **[27]** and layout (c) to **[28]**, while the text attributes them to [25]/[27] and [26] — and [28] is actually the RS wire datasheet. The cross-references are internally inconsistent.

### 2.7 Summary and Identified Research Gaps (p. 21)

Integration reduces parasitics → PD mitigation + power density; DEP emphasises scalability; radial vs endplate mounting each need tailored cooling; IMMDs add phase redundancy; MLIs cut voltage steps; open-ended-winding dual inverters enable level scaling under space constraints; monolithic integration aids feasibility.

### 3.1 Battery-to-IMD Connection study (pp. 22–25)

Original (unpublished) analysis. Capacitor sizing is driven by voltage ripple / 'neutral point drift' (PSIM demo, Figure 3.1: binary inverter with ideal 100 V sources vs four 1 mF capacitors on a 400 V bus). Three ripple-avoidance options (Figure 3.2): (a) direct multi-wire connection to intra-battery terminals, (b) 2 wires + DCAT voltage-splitting stage, (c) CHB — rejected for its isolated-source requirement.

- **2-wire configuration (p. 23):** modelled on the **AS22759/34 aerospace wire** (RS datasheet [28]); gauge sweep with **J_max = 3 A/mm²** and ≤1% power loss; for a **20 kW, 400 V** system: **one pair of AWG 8 wires**.
- **Binary configuration (p. 24):** N-level MLI fed by **(N+1) wires** (incl. ground); per-wire currents from an rms band-splitting algorithm (Figure 3.3, 4- and 8-level cases); gauges assigned per wire to equalise total loss with the 2-wire case, then weight/area compared.
- **Table 3.1 (p. 24)**, as printed:

| Levels | Power loss (W/m) 2-wire | Binary | Weight (kg/m) 2-wire | Binary | Total area (mm²) 2-wire | Binary |
|---|---|---|---|---|---|---|
| 4 | 5.74 | 5.70 | 0.08 | 0.03 | 20.06 | 12.36 |
| 8 | 5.74 | 5.58 | 0.08 | 0.05 | 20.06 | 21.33 |
| 16 | 5.74 | 5.56 | 0.08 | 0.11 | 20.06 | 33.51 |
| 32 | 5.74 | 5.41 | 0.08 | 0.22 | 20.06 | 68.04 |

- **Conclusion (p. 25):** a 4-level system could justify multi-wire (lighter, smaller), but the advantage vanishes and reverses with level count; sweeps up to **500 kW** (Figure 3.4) show binary wiring mass/area growing with levels at high power — **the binary battery-tap approach is not scalable**; 2-wire + DCAT is adopted.

### 3.2 DC-Autotransformer Based Voltage Division (pp. 25–44)

PSIM shows the DCAT tightens capacitor voltage profiles and improves output quality (Figure 3.5, p. 25). Design physics follows: magnetising inductance via core reluctance (pp. 26–27, Erickson & Maksimovic [29]); the case for **copper foil windings** (skin/proximity/eddy suppression, thermal spreading, pp. 27–28); core losses, ferrite **B_sat 0.25–0.5 T** (p. 28); leakage inductance and **interleaving** (pp. 28–29, [30] Barrios et al.); parasitic inductance minimisation (p. 29); **adiabatic (soft) switching** via the LC tank of MOSFET parasitic capacitances and magnetising inductance (pp. 29–30, [31]).

**DCAT literature review (pp. 30–33):** **[31] Kolahian, Grimm, Bucknall & Baghdadi (TechRxiv preprint, 2025)** — 8 balanced 50 V levels from a 32-board PCB stack, central gate H-bridge distributing signals via internal gate magnetics; derivation of the energy-exchange interval **t_f** (all-switches-off resonant transfer between L_m^p and C_eq^p = C_ds·N_s·N_L) and the gate-circuit compensation interval **t_z** (t_f = t_f^g + t_z, clamp states holding V_TG at zero). **[32] Zhao et al. (IEEE TTE 2022)** — 100 kW matrix-core transformer for more-electric-aircraft distribution: multiple parallel cores, symmetric circular-friendly layout, good natural-convection heat paths.

**Proposed high-power DCAT (pp. 33–35):** hybrid of [31] and [32]: copper-foil windings coupled by ferrite cores each built from 4 custom-cut slabs in a circular array; PCB modules with H-bridges between adjacent cores; MCU generates 4 gate signals, per-PCB gate H-bridge + buffer, gate transformer distributing isolated gate drive. Parameters defined in Table 3.2 (p. 35): N_L, N_c, N_s; power-core geometry a, b, H_core, W_core; gate core A_e^g, l_e^g, l_g, N_turns; timings t_f, t_z.

**Parameter calculation and algorithm (pp. 35–41):** closed-form chain from the 50 A rating (20 kW / 400 V) with **J_max = 5 A/mm² in the foils**: foil-stack geometry → core reluctance → L_m^p → t_f → B_pk; gate side from EE-core datasheet values → L_m^g → t_z → gate-wire rms current and AWG fit within the core window. Python search (flowchart, Figure 3.17): H-bridges per module divisible by 4; a swept 10–20 mm; **b fixed at 20 mm** (largest Kemet FPL ferrite slab on the market [33]); N_s ∈ {1, 2}; l_g in 50 µm multiples; **TDK EE-core catalogue [34]**; **constraints: t_f ≥ 500 ns** (so t_f > t_d incl. gate-driver delays), **B_sat = 0.35 T** with 5% loss allowance, t_z > 0, gate wires within rated current, **outer diameter ≤ 300 mm** (market-available copper sheet); slack diameter fed back into W_foil. (Defects: p. 40 cites "**[69]**" for the AWG table — the reference list stops at [44]; presumably [42] was meant. Figure 3.18's caption draws the dotted limit at **D_o = 305 mm** while the text says 300 mm.)

**Chosen design (pp. 41–42):** N_L = 36 is the largest level count under the diameter limit; of the 36-level candidates, the one with the smallest gate core is selected. **Table 3.3 (p. 42), as printed:** N_L 36; N_c 9; N_s 2; power ferrite core a = 10 mm, b = 20 mm, H_core = 14.7 mm, W_core = 46 mm; **gate core geometry E20/10/6**, l_g = "300 μs" (obvious unit misprint for µm), N_turns = 6; timings **t_f = 868 ns, t_z = 384 ns**. Stated magnetising inductances: **L_m^g = 453 µH, L_m^p = 25.2 µH**. PSIM confirms adiabatic switching (Figure 3.19).

**Practical design and the two IMD configurations (pp. 42–44):** KiCad PCB of a single module, replicated circularly into the full 36-level structure (Figures 3.20–3.21). Cooling options: water jackets, or a **customised annular oil bath** (more uniform cooling, closer PCB-foil connection, lower parasitics). The two proposed IMD architectures (Figure 3.22):

- **Configuration 1 — single DCAT, singly-excited winding:** one DCAT feeds an inverter stage in which **each inverter module supplies one slot of the machine**; balanced split levels delivered per slot; level allocation flexible with phase count and slots-per-pole-per-phase (printed "SPPR").
- **Configuration 2 — dual DCAT, open-ended winding:** DCAT duplicated on the opposite side of the machine, battery voltage halved to each end; **levels double from 36 to 72** as the winding potential is controlled from both ends; extra redundancy; challenges are the shaft passing through the DCAT structure and far more complex control. Feasibility to be judged after a single-DCAT prototype.

**Defect — figure-label swap:** the text describes Figure 3.22**a** as the single-DCAT/per-slot configuration and 3.22**b** as the dual-DCAT open-ended-winding one, but the printed caption reads "(a) Open-Ended winding and dual-inverter setup (b) Singly excited winding with single inverter" — caption and text (a)/(b) assignments are swapped. Reuse must follow the text, not the caption.

### 4. Relevant Experimental Work (pp. 45–46)

**4.1 Current sensor:** shunt-based Ultrafast Current Shunt (UFCS) per **[35] Shillaber et al. (IEEE TPEL 2022)** — shunt array, RL low-pass, two amplifier stages; board assembled with an embedded half-bridge for insertion-inductance-free testing; **experiments not yet run**. **4.2 Double pulse test:** DPT circuit per **[36]**, designed to **50 A / 400 V**; PCB assembled, external inductor, setup photographed.

### 5. Future Work (p. 47)

Plan to 31 October 2028: May–Sept 2026 voltage splitter (analysis, PCB, custom ferrites, testing); Oct 2026–Sept 2027 3-phase multilevel inverter; Oct 2027–Mar 2028 monolithic integration **or** full IMD integration; Apr–Oct 2028 thesis. Candid admission: "**there is a lack of quantitative metrics to target**; this project focuses on the feasibility of system-level architectures".

### 6. References (pp. 48–50) — quality issues

44 entries, [1]–[44]. Systematic problem: **nearly all journal entries omit volume and issue numbers** (only [27] carries "vol. 38, no. 7"); several conference entries lack pages or locations. Specific defects, as printed:

- **[23] is malformed:** "F. Grimm, J. Wood and M. Baghdadi, 'A DC-Autotransformer based Multilevel Inverter for Automotive Applications,' pp. Grimm, Ferdinand; Wood, John; Baghdadi, Mehdi, 2020." — author names duplicated into the page field, **no venue given**. As the foundational DCAT citation, its correct bibliographic record must be established independently before the proposal cites it.
- **[16]** title reads "…Current-Source Inverter **or** EV Traction Applications" (for "for") and is dated **2026** — year needs verification.
- **[36]** title truncated: "A tutorial on double pulse test of silicon and silicon" (presumably "…silicon carbide").
- **[3]** (Statista) and [39] (bare H3X homepage) are weak grey-web citations; [2] carries a `utm_source=chatgpt.com` tracking parameter.
- Dangling in-text citation **[69]** on p. 40 with no corresponding entry.
- [31] is a **TechRxiv preprint** (not peer-reviewed); [25] listed pp. 1–13, apparently early access.

## 3. Published sources it relies on (citable substitutes)

Cite these directly, never the transfer report. Details as printed (volume/issue data mostly missing — verify before use):

**Peer-reviewed journals / magazines**
- [7] Madonna et al. — "Electrical Machines for the More Electric Aircraft: Partial Discharges Investigation," IEEE Trans. Ind. Appl., pp. 1389–1398, 2021. *(PD/PDIV at altitude.)*
- [8] Lee, Li, Han, Sarlioglu, Minav & Pietola — "A Review of Integrated Motor Drive and Wide-Bandgap Power Electronics for High-Performance Electro-Hydrostatic Actuators," IEEE Trans. Transp. Electrif., pp. 684–693, 2018. *(IMD taxonomy; 10–20% volume; 30–40% cost; EMC.)*
- [9] Jahns & Sarlioglu — "The Incredible Shrinking Motor Drive," IEEE Power Electronics Magazine, pp. 18–27, Sept 2020.
- [10] Abebe et al. — "Integrated motor drives: state of the art and future trends," IET Electric Power Applications, pp. 757–771, 2016. *(Challenges; SiC/GaN 600 °C vs Si 225 °C.)*
- [16] Chen et al. — "Power-Dense Integrated Motor Drive Using a WBG-Enabled Current-Source Inverter [f]or EV Traction Applications," IEEE Trans. Transp. Electrif., pp. 542–555, printed 2026 (verify).
- [17] Wang, Jahns, McCluskey, Kizito, Sarlioglu et al. — "2-kV 1-MW 20 000-r/min Integrated Modular Motor Drive for Electrified Aircraft Propulsion," IEEE JESTPE, pp. 394–407, 2025.
- [19] El Hajji et al. — "Optimal Design of High Specific Power Electric Machines for Fully Electric Regional Aircraft: A Case Study of 1MW S-PMSM," Aerospace, pp. 1–12, 2024. *(Machine comparison; slot/pole vs speed.)*
- [21] Poorfakhraei, Narimani & Emadi — "A Review of Multilevel Inverter Topologies in Electric Vehicles…," IEEE Open Journal of Power Electronics, pp. 155–170, 2021.
- [22] Peng — "A Generalized Multilevel Inverter Topology with Self Voltage Balancing," IEEE Trans. Ind. Appl., pp. 611–618, 2001.
- [24] Aihsan et al. — IJPEDS, pp. 1270–1279, 2023. *(Open-end winding.)*
- [25] Farhat & Baghdadi — "On-Chip Design and Implementation of a Battery-Cell-Level Binary-Tree Multilevel Converter," IEEE Trans. Power Electron., pp. 1–13, 2026. *(Team's own published on-chip work — copy in repo.)*
- [27] Li et al. — "200 V Enhancement-Mode p-GaN HEMTs Fabricated on 200 mm GaN-on-SOI…," IEEE Electron Device Letters, vol. 38, no. 7, pp. 918–921, 2017.
- [30] Barrios et al. — "High-Frequency Power Transformers With Foil Windings…," IEEE Trans. Power Electron., pp. 5712–5723, 2015.
- [32] Zhao et al. — "Design and Demonstration of a 100 kW High-Frequency Matrix Core Transformer for More Electric Aircraft Power Distribution," IEEE Trans. Transp. Electrif., pp. 4279–4290, 2022.
- [35] Shillaber et al. — "Ultrafast Current Shunt (UFCS)…," IEEE Trans. Power Electron., pp. 15493–15504, 2022.
- [41] Wang et al. — "Review of High-Power-Density and Fault-Tolerant Design of Propulsion Motors for Electric Aircraft," Energies, pp. 1–31, 2023.

**Conference papers**
- [6] Ugwueze, Statheros, Bromfield & Horri — "Trends in eVTOL Aircraft Development…," AIAA SciTech, 2023. *(120-concept survey.)*
- [12] Brown, Jahns & Lorenz — IEEE IAS Annual Meeting, pp. 1322–1328, 2007. *(IMMD.)*
- [13] Brockerhoff et al. — IEEE EDPC, pp. 1–6, 2014. *(Smart Stator Teeth.)*
- [14] Wheeler et al. — "A Fully Integrated 30kW Motor Drive Using Matrix Converter Technology," EPE 2005. *(40%-capacitor-volume and motor-envelope claims.)*
- [15] Hilpert, Brinkfeldt & Arenz — IEEE EDPC, pp. 1–8, 2014.
- [18] Swanke et al. — IEEE IEMDC, pp. 1–8, 2021.
- [20] Paterakis, Marouchos & Darwish — UPEC 2017. *(13-level vs 3-level THD.)*
- [26] Weiss et al. — IEEE CSICS, New Orleans, 2015.
- [36] Masoud, Issa & Yates — IEEE WEMDCD, 2023.
- [40] Tallerico, Chapman & Smith — AIAA AVIATION 2023 Forum, San Diego, 2023.

**Book:** [29] Erickson & Maksimovic, *Fundamentals of Power Electronics*, Springer Nature, Cham, 2020.

**Preprint (cite with care):** [31] Kolahian, Grimm, Bucknall & Baghdadi — "Multiport DC Solid State Transformer with Enhanced Power Efficiency: A Modular Architecture," TechRxiv, pp. 1–10, 2025.

**Needs bibliographic repair before any use:** [23] Grimm, Wood & Baghdadi — "A DC-Autotransformer based Multilevel Inverter for Automotive Applications," 2020 (venue missing in the report).

**Grey/web sources (prefer primaries):** [1] UN net-zero page; [2] IEA Global EV Outlook 2023; [3] Statista aviation-emissions page; [4] ICCT Mukhopadhaya & Graver 2022 (solid report); [5] ARPA-E FOA (16 Dec 2019); [11] Bartos, Control Engineering, 2000; [28] RS AS22759/34 datasheet; [33] Kemet FPL ferrite tiles; [34] TDK EPCOS ferrite data book 2013; [37] Embry-Riddle textbook chapter; [38] Danfoss VLT DriveMotor FCM 300; [39] H3X website; [42] Meters UK AWG table; [43] Archer aircraft page; [44] Joby Aviation news.

## PROPOSAL USE MAP (detailed)

**Ground rule.** The transfer viva is NOT citable. Every row below routes its fact to a published substitute. The three load-bearing substitutes are fully verified — complete bibliographic records confirmed in `drafts/06_References.md` (residual check 3), ready to insert at the tail of Part 1 of that list:

- **[IMD-A] Abebe 2016** — R. Abebe, G. Vakil, G. Lo Calzo, T. Cox, S. Lambert, M. Johnson, C. Gerada, and B. Mecrow, "Integrated motor drives: state of the art and future trends," *IET Electr. Power Appl.*, vol. 10, no. 8, pp. 757–771, Sep. 2016. DOI: 10.1049/iet-epa.2015.0506. *(The canonical IMD state-of-the-art review; recommended primary for the partition claim.)*
- **[IMD-B] Lee 2018** — W. Lee, S. Li, D. Han, B. Sarlioglu, T. A. Minav, and M. Pietola, "A Review of Integrated Motor Drive and Wide-Bandgap Power Electronics for High-Performance Electro-Hydrostatic Actuators," *IEEE Trans. Transp. Electrific.*, vol. 4, no. 3, pp. 684–693, Sep. 2018. DOI: 10.1109/TTE.2018.2853994. *(Source of the 10–20% volume / 30–40% cost figures and of the four-way mounting taxonomy.)*
- **[IMD-C] Jahns 2020** — T. M. Jahns and B. Sarlioglu, "The Incredible Shrinking Motor Drive: Accelerating the Transition to Integrated Motor Drives," *IEEE Power Electron. Mag.*, vol. 7, no. 3, pp. 18–27, Sep. 2020. DOI: 10.1109/MPEL.2020.3011275. *(Field-trajectory and modularisation/fault-tolerance source.)*

None of the three yet carries a number in `drafts/06_References.md` Part 1. Fragments below use the [IMD-A/B/C] placeholders; replace with final keys on insertion, then log the assignment in the renumbering map.

**Proposal locations served.** The digest's proposal value concentrates on the *IMD-shortens-vs-dissolves* differentiation, which lives in exactly three places: (i) Vision **"Opening: stand beside the expert"** (VIS-OPEN-v7, `drafts/02_Vision_ArcRevision.md` — the state-of-the-art paragraph, currently citing only the general MEA reviews [15,16]); (ii) Vision **"Crossing the line: the 50 V claim"** (VIS-CROSS-v7 — the sentence "an integrated motor drive relocates a functionally intact inverter onto the housing and still meets the winding at full-voltage terminals"); (iii) Approach **"Building on previous work"**, third paragraph (`drafts/03_Approach.md` — "IMD *shortens* the converter–machine partition; this proposal *dissolves* it"), whose `[PI TO CONFIRM: cite a published IMD state-of-the-art review here]` is the one outstanding citation slot this map closes.

### Fact-by-fact rows (★ = the six highest-value items)

**★ ROW 1 — The partition claim: an IMD relocates a functionally intact inverter; the converter remains an electrically distinct unit meeting the winding at full-bus-voltage terminals.**
- (a) *Location:* Vision "Crossing" (the relocates-vs-dissolves sentence); Approach "Building on previous work" ¶3 — this row fills its open `[PI TO CONFIRM]` slot.
- (b) *Cite:* **[IMD-A] Abebe 2016** (recommendation in `drafts/06_References.md`); optionally reinforced by [IMD-C].
- (c) *Fragment:* "Integrated motor drives mount a functionally complete inverter onto or into the machine, shortening cables and pooling cooling, while the converter remains an electrically distinct unit connected to the winding at full-bus-voltage terminals [IMD-A]. IMD *shortens* the converter–machine partition; this proposal *dissolves* it."

**★ ROW 2 — Field trajectory: the converter has moved progressively closer to the machine; integration is the field's direction of travel.**
- (a) *Location:* Vision "Opening" ¶1 ("Integrated motor drives have moved the inverter out of the equipment bay and onto the machine housing…").
- (b) *Cite:* **[IMD-C] Jahns 2020** — a magazine review titled for exactly this trajectory; add [IMD-A] for the survey backbone.
- (c) *Fragment:* "Integrated motor drives have moved the inverter out of the equipment bay and onto the machine housing, shortening cables and pooling two thermal systems into one [IMD-A, IMD-C]."

**★ ROW 3 — Quantified IMD benefits: 10–20% volume reduction and 30–40% installation/manufacturing cost reduction from eliminating separate housings and shielded cables.**
- (a) *Location:* Vision "Opening" ¶1 (if the state-of-the-art sentence is to be quantified); Approach "Building on previous work" ¶3 (quantifying what *shortening* buys — setting up why *dissolving* must be argued on different grounds).
- (b) *Cite:* **[IMD-B] Lee 2018** — but these are second-hand survey numbers inside a review, so hedge with "reported".
- (c) *Fragment:* "Mounting the inverter on the machine is reported to save 10–20% of system volume and 30–40% of installation and manufacturing cost [IMD-B] — gains that flow from shortening the partition, not from removing it; the winding still sees the full bus voltage."

**★ ROW 4 — Modularisation and phase-lead integration improve fault tolerance — at the price of duplicated converter channels.**
- (a) *Location:* Vision "Opening" ¶1 (multiphase sentence) and "The unseen line" third point / "Cascade" (redundancy-without-duplication argument).
- (b) *Cite:* **[IMD-C] Jahns 2020** (for the benefit); the duplication-cost framing is the proposal's own argument and needs no citation.
- (c) *Fragment:* "Modular, phase-lead-integrated drives improve fault tolerance by construction [IMD-C]; conventional multiphase machines buy the same softening by duplicating inverter channels, gate drives, isolated supplies and protection."

**★ ROW 5 — Wide-bandgap devices in integrated drives: SiC/GaN practical limits (~600 °C vs ~225 °C for Si), higher switching frequency, application-dependent choice.**
- (a) *Location:* Vision "Opening" ¶1 ("Wide-bandgap devices have raised switching frequency and efficiency together…").
- (b) *Cite:* **[IMD-A] Abebe 2016** — the report's own source for these figures.
- (c) *Fragment:* "Wide-bandgap devices have raised switching frequency and efficiency together and collapsed passive volume in ways silicon never permitted [IMD-A]." *(Quote the 600 °C / 225 °C figures only if needed, and only to [IMD-A].)*

**★ ROW 6 — IMMD/per-tooth converters are the field's closest approach to dissolution — and still retain a shared DC link and terminal-fed sections.**
- (a) *Location:* Approach "Building on previous work" ¶3 — the pre-emptive answer to a reviewer's "per-slot drive already exists (IMMD/Smart Stator Teeth)" objection; optionally one clause in Vision "Crossing".
- (b) *Cite:* Brown, Jahns & Lorenz, IEEE IAS Annual Meeting 2007, pp. 1322–1328 (IMMD) and Brockerhoff et al., IEEE EDPC 2014 (SST) — **from the digest inventory, bibliographic details NOT yet independently verified; verify before insertion.** [IMD-C] also surveys IMMD and is the verified fallback if only one entry is affordable.
- (c) *Fragment:* "Even the most granular published integration — integrated modular motor drives with per-tooth converter modules [Brown 2007; Brockerhoff 2014] — feeds every module from a common DC link whose capacitors the same literature identifies as the binding constraint, and each winding section still meets its converter at terminals rated for the link voltage. No prior architecture removes the terminal itself."

**ROW 7 — IMD mounting taxonomy: radial/axial × housing/stator-mounted; radial suits high-speed machines; stator-mounted variants are 'purer' but complicate cooling.**
- (a) *Location:* Approach "Building on previous work" ¶3, only if the differentiation needs taxonomy depth (one clause at most — the proposal must not read as an IMD survey).
- (b) *Cite:* **[IMD-B] Lee 2018** (the taxonomy figure's source); [IMD-A] equivalently.
- (c) *Fragment:* "Whether housing- or stator-mounted, radial or axial [IMD-B], every configuration relocates the same electrically intact converter."

**ROW 8 — EMC/parasitics improve when inverter–machine interconnects are removed.**
- (a) *Location:* Vision "Opening" ¶1 ("shrinking electromagnetic-interference filtering"); Vision "The unseen line" first point (dV/dt at the terminals).
- (b) *Cite:* **[IMD-B] Lee 2018**.
- (c) *Fragment:* "Integration shortens or removes the shielded feeder whose parasitics convert fast switching edges into terminal overvoltage [IMD-B]."

**ROW 9 — Aerospace is already pushing IMD integration to megawatt scale (2 kV, 1 MW, 20,000 rpm IMMD with explicit PD countermeasures).**
- (a) *Location:* Vision "Opening" ¶1 or "Timeliness" (evidence the field is investing in integration yet retaining the partition); Approach "Building on previous work" ¶3 as the state-of-the-art bound.
- (b) *Cite:* Wang et al., IEEE JESTPE 2025, pp. 394–407 (and Swanke et al., IEMDC 2021) — **digest inventory; verify volume/issue before use.**
- (c) *Fragment:* "The most aggressive aerospace integration to date — a 2 kV, 1 MW, 20,000 rpm integrated modular motor drive [Wang 2025] — mitigates partial discharge with added insulation and geometry control at PD-prone regions; the bus voltage still reaches the winding."

**ROW 10 — Integration motivated by PD: shorter interconnects reduce the parasitics that create terminal overvoltage and PD risk.**
- (a) *Location:* Vision "The unseen line" first point; Vision Openings A–C.
- (b) *Cite:* the proposal's **existing PD anchors** — Lusuardi et al., IEEE Access 2021 (current [13] in `drafts/06_References.md`) and, if a second is wanted, Madonna et al., IEEE Trans. Ind. Appl., vol. 57, no. 2, pp. 1389–1398, 2021 (verified in the [14] note there). Do **not** import PD sourcing via this report.
- (c) *Fragment:* none needed — the Vision's PD text is already drafted and anchored; this row exists to block accidental re-sourcing.

### Trap rows — claims that must NEVER be sourced to this report

| # | Tempting claim (as printed in the viva) | Why it is a trap | Required action |
|---|---|---|---|
| T1 | "System-level efficiency boost of 30% or more" from integration | Printed with **no citation at all** in the viva; physically dubious | **Never use anywhere** unless an independent primary source is found; no substitute exists |
| T2 | 10–20% volume, 30–40% installation/manufacturing cost savings | Real source is [IMD-B] Lee 2018 — itself a review carrying second-hand numbers | Cite [IMD-B] with "reported"; never the viva (see ★ ROW 3) |
| T3 | DC-link capacitors ≈ 40% of drive volume; >7.5 kW unfeasible in the motor envelope | Sourced to Wheeler et al., EPE **2005** — twenty years old | If used, cite Wheeler 2005 and flag the vintage explicitly |
| T4 | 7.5 kW "thermal barrier" for IMDs | Bartos, *Control Engineering*, **2000** — 25-year-old trade article, not peer-reviewed | Avoid as evidence entirely; historical colour only |
| T5 | ARPA-E targets: 12 kW/kg, 93% cruise efficiency | Viva cites the FOA second-hand | Retrieve and cite the ARPA-E FOA (16 Dec 2019) directly |
| T6 | Aviation CO₂e 882 Mt (2024); doubled since 1990 | Viva's source is a Statista topic page | Replace with ICCT/IATA/IEA primary data |
| T7 | Electric aircraft 49–88% CO₂e reduction; 3× cruise efficiency | Second-hand via viva | Cite ICCT (Mukhopadhaya & Graver 2022) directly |
| T8 | eVTOL survey: 120 concepts, 57% powered-lift, 53% vectored thrust | Second-hand via viva | Cite Ugwueze et al., AIAA SciTech 2023 |
| T9 | THD 5.285% (13-level) vs 73.98% (3-level) | Second-hand via viva | Cite Paterakis, Marouchos & Darwish, UPEC 2017 |
| T10 | SiC/GaN ~600 °C vs Si ~225 °C limits | Second-hand via viva | Cite [IMD-A] Abebe 2016 (see ★ ROW 5) |
| T11 | Slot/pole weight-vs-speed plateaus (12/10 @ 10 krpm; 24/20 @ 15 krpm; 36/30 @ 5 krpm) | Second-hand via viva | Cite El Hajji et al., *Aerospace* 2024 |
| T12 | Foundational DCAT citation (Grimm, Wood & Baghdadi 2020) | The viva's entry [23] is **malformed** (authors duplicated into page field, no venue) | Establish the correct record independently before citing; the proposal's DCAT anchor is already Wood et al., PCIM 2016 ([3] in `drafts/06_References.md`) |
| T13 | Multiport DC solid-state transformer results (Kolahian et al. 2025) | TechRxiv **preprint**, not peer-reviewed | Cite only with explicit preprint labelling, if at all |
| T14 | Battery-tap wiring study: Table 3.1, non-scalability conclusion, 2-wire+DCAT decision | Edwards' **unpublished original work** | Uncitable anywhere; describable only as the team's unpublished preliminary work, unreferenced |
| T15 | DCAT design algorithm and parameters (36 levels, 9 cores, E20/10/6, t_f = 868 ns, t_z = 384 ns, L_m^p = 25.2 µH, L_m^g = 453 µH, ≤300 mm) | Unpublished original work | Same as T14 |
| T16 | The two IMD configurations (per-slot Configuration 1; dual-DCAT open-end 36→72 levels) and the annular-oil-bath cooling concept | Unpublished original work — and Configuration 1 superficially resembles this proposal's per-slot architecture | Never cite; never present as established. The proposal's per-slot claim rests on its own published silicon [1]–[3] in `drafts/06_References.md`, not on Edwards' concept figures |
| T17 | UFCS current-sensor and double-pulse-test hardware status | Unpublished, experiments not yet run | Uncitable; internal knowledge only |

### Internal-use cautions (when mining the viva for anything else)

Figure 3.22's (a)/(b) caption is swapped against the text (follow the text); "Figure 2.12" is duplicated on pp. 19–20 with crossed [25]/[26]/[27]/[28] attributions; in-text "[69]" dangles (list ends at [44]); the gate-core airgap "300 μs" is a unit misprint for µm; the diameter limit is 300 mm in text vs 305 mm in Figure 3.18's caption; nearly all journal entries omit volume/issue. Treat every figure, number and reference as unverified until checked against the body text and the primary source.


<!-- ==================== FILE: evidence/07_2026_preprints_digest.md ==================== -->

# Evidence Digest 07 — Two March 2026 Preprints (Farhat, UCL/QUB)

Internal dossier document for the EPSRC proposal. Page-by-page digests of two single-author preprints derived from Qassam Farhat's 2025 UCL PhD thesis. Extraction: pdftotext (A); 300-dpi OCR plus visual inspection (B, image-only PDF). Page numbers are the printed manuscript pages.

---

# PART A — Hybrid BTMLC Preprint

**File:** `/home/user/proposal/Farhat_Hybrid_BTMLC_9_March_2026_engarxiv.pdf` (26 pp., US letter)

## A1. Identity (exactly as printed)

- **Title:** "A Scalable Hybrid Multilevel Power Converter Using Low-Voltage On-Chip Power Modules" (title page set in small caps).
- **Author:** Qassam Farhat (sole author, with ORCID icon), University College London, Gower St, London WC1E 6BT, UK; e-mails `qassamfarhat@gmail.com`, `qassam.farhat.21@ucl.ac.uk`.
- **Venue marking:** "A PREPRINT" beneath the title; running header "FARHAT: A SCALABLE HYBRID MULTILEVEL POWER CONVERTER… A PREPRINT".
- **Date printed:** March 9, 2026 (PDF metadata creation 9 March 2026; produced with LaTeX/pdfTeX).
- **DOI:** **Confirmed — no DOI is printed anywhere in the document.** No engrXiv branding appears on the pages either; only the filename indicates engrXiv hosting. No licence statement is printed.
- **Footnotes (p. 1):** (\*) "This manuscript is based on a chapter of the author's PhD thesis submitted to University College London in 2025." (†) "Current affiliation: The School of Electronics, Electrical Engineering and Computer Science, Queen's University Belfast, Belfast, UK. E-mail: q.farhat@qub.ac.uk".
- **Keywords:** Multilevel converters; Integrated power ICs; Cell-level power conversion; Hybrid IC–discrete architecture; Electric vehicle power electronics; bond-on-active-circuit; BCD technology.

## A2. Significance for the proposal

The strongest single evidence that the BTMLC platform scales beyond the single-chip voltage limit towards machine-relevant per-slot voltage/current levels. All previously extracted claims are **verified and completed**: two stacked eight-tap BTMLC ICs, outputs multiplexed by an off-chip half-bridge of 50 V power MOSFETs, synthesise sixteen-step half-sine waveforms (3.3 V per step, references to 49.5 V), delivering up to 6 A into resistive loads; peak efficiency 98.5% (98.5–85% across taps, 2–6 A); path resistance 60–85 mΩ; NLC with dynamic frequency (10 Hz ↔ 1 kHz / 500 Hz) and arbitrary magnitude variation (3.3 ↔ 23.1 V single chip; 3.3 ↔ 49.5 V stacked) demonstrated. The hybrid IC–discrete partition is explicitly the scaling route, "supporting unified power-processing functions including motor driving, charging, and cell balancing" (p. 3).

## A3. Page-by-page walk

- **p. 1** — Title, abstract, keywords; thesis/QUB footnotes. Headline numbers: eight-battery-tap BTMLC; 130-nm BCD, LDMOS devices; 20.52 mm² prototype; two stacked modules + off-chip half-bridge; up to 6 A; 98.5% peak efficiency.
- **p. 2** — Motivation and survey: MLC benefits (low-voltage devices, reduced per-switch stress, EMI, THD, "lower stress on machine insulation systems"); FC/NPC/P2/CBSC families; battery-integrated MLC (BIMI, BI-MMC, BM3) complexity; GaN monolithic limits; BCD as the mature integration platform.
- **pp. 3–4** — Fig. 1 (MLC architecture overview). Five contributions: hybrid IC–discrete architecture "supporting unified power-processing functions including motor driving, charging, and cell balancing"; stacked 50 V half-sine synthesis under variable voltage/frequency with R_on, efficiency, heat and thermal-resistance measurements; new BTMLC implementation with battery-fed driver-rail generators; LDMOS switches with "at least 6 A continuous current capability"; reliable bond-on-active-circuit (BOAC) wire bonding in low-k silicon. Section 2 reviews topology-derivation methods (horizontal/vertical conformation, tree-type ANPC: (n+1) levels from 2n switches, no flying capacitors).
- **p. 5** — Hybrid Si–SiC precedents; level-generator/level-selector abstraction. Section 3: voltage/frequency stress partitioned between a high-frequency low-voltage IC domain and a lower-frequency higher-voltage discrete domain. **Key scaling statement:** breakdown voltage of the technology constrains a module to eight taps; higher voltages via SOI-class processes or **board-level stacking**; two tap-of-eight (TO8) modules + discrete stage = sixteen-tap converter (Fig. 3).
- **pp. 6–7** — Fig. 2 (hybrid concept; lateral on-chip vs vertical off-chip devices). BTMLC theory: inputs B1–B7 at V_cell; three switching levels; n = 2^k taps (Eq. 1), k = 3 → eight levels 0–7·V_cell; N_sw = 2n − 2 (Eq. 2); V_blk,j = V_cell·2^(j−1) (Eq. 3); f_sw,j ∝ 1/2^(j−1) (Eq. 4) — lowest-voltage switches switch fastest; optional fundamental-frequency H-bridge for bipolar AC; conduction-loss model (Eq. 5).
- **p. 8** — Loss evaluation at I_rms = 5 A, f_out = 10 kHz, switches rated 5/10/16 V (Levels I/II/III): total ≈ 0.7 W; 6.5% switching, 42.6% channel conduction, 50.9% metallisation conduction; for a 16-tap stack, switching share rises to ≈ 21.7%. Section 5: NDMOS power stages; on-chip level shifting, dead-time, gate drive; driver rails derived internally (no auxiliary DC–DC); isolation-junction breakdown sets the ceiling.
- **pp. 9–10** — Fig. 5 (full eight-tap circuit; LS1–LS3, DT blocks). Stacked static-V_SSH level shifters (inputs V_CNT1–3) for low-side; floating cross-coupled shifters (Fig. 6) elsewhere; NAND-based dead-time generator. Level I: four 5 V NDMOS half-bridges; push–pull driver-rail circuits hold high-side V_GS at one cell voltage; thresholds 0.9–1.3 V, so any cell above 2.5 V suffices.
- **p. 11** — Level II (M9–M12, 10 V) reuses Level-I rails for low-side, dedicated push–pull rails for high-side; Level III (M13–M14, 16 V) rail generator withstands four cell voltages with auxiliary V_X stage. No high-voltage resistors/Zeners — portable across technologies.
- **p. 12** — Simulations (Cadence Spectre, post-layout) under nearest-level control (NLC): staircase synthesis into 4 Ω; 3.6 V per level gives low THD without PWM. Section 7 opens: 130-nm BCD fabrication, all-N-type switches.
- **pp. 13–14** — BOAC pads over active regions; die 20.52 mm² (5474 µm × 3750 µm, Fig. 13); three-stage validation plan (JLCC-84 package; custom wire-bonded board; two-chip stack). Test bench: B-Box RCP controller, multi-channel supplies; extra supply gives V_cell,8 for stacked mode.
- **p. 15** — No-load staircases at 10 Hz and 5 kHz (Fig. 14); switching-order overshoot on V_cell,4→V_cell,3 and ~100 ns dip on the reverse transition. Loaded tests (0.1/0.33/10/22 µF tap decoupling, taps 3.3–3.4 V): JLCC limited to ≈ 2.5 A, near the fusing limit of three 25 µm gold bond wires.
- **p. 16** — Table 1 (DC tap-selector, ≈ 2 A, 3.3–23.1 V in): R_path ≈ 0.385–0.409 Ω (JLCC); input/output current difference ≤ ~10 mA (level-shifter consumption). Thermal: 66 °C at 2 A DC; ≈ 46 °C under NLC operation.
- **p. 17** — Gate-drive measurements: dead-times ≈ 80–85 ns (Levels I–II), ≈ 250 ns (Level III); V_GS rise/fall ≈ 60/30 ns, 190/35 ns, 350/50 ns respectively; V_DS within 3.3/6.6/13.2 V ratings. Section 7.2: ENIG PCB; 10–12 aluminium 33 µm bonds per pad, double-sided output bonding; BOAC robustness confirmed with flat-wedge bonding.
- **pp. 18–19** — Fig. 19: fourteen node/gate waveforms during 5 kHz NLC half-sine synthesis (Level-I outputs swing 13.2↔16.5 V, 19.9↔23.1 V). Daughterboards on 50-contact card-edge sockets; motherboard hosts the external half-bridge. **Path resistance with optimised packaging: 60–85 mΩ across all taps at 2–6 A DC**, tap spread ≈ 20–25 mΩ within measurement uncertainty (Fig. 22).
- **p. 20** — Fig. 21: stacked-IC bench schematic — two BTMLC ICs across seventeen rails (Keithley 2281S), off-chip half-bridge M1/M2, B-Box control, FLIR thermal camera.
- **p. 21** — Efficiency (Eq. 6, per-tap DC 2–6 A): **98.5% down to 85%** (Fig. 23); higher taps more efficient (fixed conduction loss vs larger P_out); further gains expected without edge-connector sockets.
- **p. 22** — Single-module NLC dynamics (Fig. 24): 4 Ω at 10 Hz and 2 kHz; dynamic frequency 10 Hz↔1 kHz; arbitrary reference steps 3.3 V↔23.1 V — robust throughout. **Stacked demonstration:** sixteen taps multiplexed by 50 V power MOSFETs (stage "not optimised for low on-state resistance or compactness"); 8 Ω load; sixteen 3.3 V steps forming smooth half-sines; reference stepped 3.3 V↔49.5 V with stable response.
- **p. 23** — Fig. 25 (stacked waveforms: 10 Hz, 500 Hz, dynamic 10 Hz↔500 Hz, 49.5 V steps). Thermal-resistance estimate at 6 A, highest tap: R_path = 82 mΩ → P_cond = 2.952 W; ΔV = 0.492 V; T_chip = 102 °C vs T_pcb = 28 °C; **θ_eff ≈ 25.1 °C/W**, no external cooling.
- **p. 24** — Fig. 26 heat map. Heat extraction limited by die attach/copper area/vertical spreading; improved thermal coupling flagged for future prototypes. Conclusion begins.
- **pp. 25–26** — Conclusion: BTMLC as "a promising building block for future high-voltage converters, battery-integrated power electronics, and compact motor drive systems." Acknowledgements: **EPSRC PhD studentship at UCL, Grant No. EP/T517793/1 (Project Reference 2600345)**; Silicon Contact Ltd (first two years); Dr Mehdi Baghdadi (supervision); Prof Andreas Demosthenous and Prof Richard McMahon (feedback); Pouya Kolahian (experiments); Dr Ahmad Elkhateb (writing). References [1]–[30], incl. [23] Farhat & Baghdadi, BTMLC IC, Authorea Preprints 2025, and [24] Farhat & Baghdadi, multiple-output level shifters, Authorea Preprints 2026.

## A4. Quotable passages (with pages)

- p. 1 (footnote): "This manuscript is based on a chapter of the author's PhD thesis submitted to University College London in 2025."
- p. 1 (abstract): "Measurements confirm variable-frequency and variable-magnitude waveform synthesis while delivering up to 6 A to a resistive load with a peak efficiency of 98.5%."
- p. 3: "…supporting unified power-processing functions including motor driving, charging, and cell balancing."
- p. 5: "The voltage capability of a single BTMLC module is ultimately limited by the breakdown voltage of the chosen semiconductor technology… Higher system voltages can therefore be achieved either by adopting technologies with greater breakdown capability (e.g., silicon-on-insulator (SOI)-based processes) or by stacking multiple BTMLC modules at the board level."
- p. 5: "This stacking principle provides a scalable pathway for constructing higher-voltage and higher-power systems while maintaining compatibility with mainstream low-voltage IC technologies."
- p. 22: "…the stacked configuration synthesises voltage waveforms with sixteen discrete steps of 3.3 V resolution, producing smooth half-sine waveforms while simultaneously delivering current to the load at varying frequencies and voltage levels."
- p. 25: "The BTMLC module therefore represents a promising building block for future high-voltage converters, battery-integrated power electronics, and compact motor drive systems."

## A5. Limitations / future work (as stated)

- Off-chip 50 V stage "not optimised for low on-state resistance or compactness" (p. 22); it validates feasibility only.
- Edge-connector sockets add series resistance; direct daughterboard interfacing expected to raise efficiency further (p. 21).
- Thermal path is the dominant constraint: θ_eff ≈ 25.1 °C/W with no external cooling; improved die attach/heat spreading flagged for subsequent prototypes (pp. 23–24).
- Eight-tap ceiling per chip from junction-isolation breakdown; SOI processes named as the on-chip scaling route (p. 5).
- JLCC packaging limited to ≈ 2.5 A by three 25 µm gold bond wires; internal pads for extra bonds/stud bumping included but "not explored in this work" (p. 15).
- Full three-phase machine drive and bipolar (H-bridge) operation are described conceptually (p. 7) but not demonstrated; demonstrations are half-sine into resistive loads.

*(Proposal mapping for Part A consolidated into "PROPOSAL USE MAP (detailed)" at the end of this document.)*

---

# PART B — On-Chip Active Battery Balancer Preprint

**File:** `/home/user/proposal/View of On-chip Scalable High-speed Active Battery Balancer.pdf` (34 pp., image-only PDF)

## B1. Identity (exactly as printed)

- **Title:** "On-Chip Scalable High-Speed Active Battery Balancers" (plural "Balancers" as printed; the filename uses the singular).
- **Author:** Qassam Farhat (sole author, ORCID icon), University College London, Gower St, London WC1E 6BT, UK; same two e-mails as Part A.
- **Venue marking:** "A PREPRINT"; running header "FARHAT: ON-CHIP SCALABLE HIGH-SPEED ACTIVE BATTERY BALANCERS — A PREPRINT".
- **Date printed:** March 7, 2026.
- **DOI:** **Confirmed — no DOI printed anywhere**; no server branding on any page. The PDF is a Chrome-printed "View of…" capture (Skia/PDF metadata, captured 11 July 2026) of the hosted preprint view. (Part A's file metadata carries *this* paper's title — both PDFs came from the same LaTeX pipeline in the same session.)
- **Footnotes (p. 1):** identical thesis statement — "This manuscript is based on a chapter of the author's PhD thesis submitted to University College London in 2025." — and the same QUB affiliation footnote.
- **Keywords:** Integrated battery balancer; Active battery balancing; Battery management systems (BMS); Switched-capacitor converters; On-chip gate drivers; BCD technology.

## B2. Significance for the proposal

Evidences breadth of on-chip integration capability in the **same 130-nm BCD process family** as the BTMLC: a second fabricated, measured IC (3.4 mm², 5 V lateral LDMOS) — four stacked half-bridge submodules with fully integrated dead-time generation, multiple-output level shifting and gate driving — operating 1 kHz–5 MHz over 2.4–4.3 V and delivering up to 2.5 A average balancing current in dual-IC complementary mode. With Part A it shows the complete battery-facing suite (conversion + balancing) on one process platform, reusing identical level-shifter/dead-time IP ([31]/[32], the same Authorea preprints cited in Part A) — a coherent, reusable circuit-IP lineage.

## B3. Page-by-page walk

- **p. 1** — Title, abstract, keywords; thesis footnote. Headline numbers: 3.4 mm² die, 130-nm BCD, 5-V lateral switches; four cells natively, extendable; single open-loop control signal, sensor-less; star capacitor network; full-bridge via a second chip; 1 kHz–5 MHz; 2.4–4.3 V; up to 2.5 A average balancing current.
- **pp. 2–3** — Survey of switched-capacitor balancer families (STSC, DTSC, SSC, Chain-SC, SP-SC, Star-SC, delta, mesh, CS-SC; Table 1 gives component counts and ratings vs cell count n); a 100-cell CS-SC would need 400 switches; discrete implementations limited to tens of kHz by parasitics. Prior ICs: [5] 180-nm BCD 18-cell BMIC, *passive* only (25 Ω switches, ≈ 5 mA); [19] 7-cell IC, 100 mA, 50 V P-channel + external transformer; commercial TLE9012DQU (12 cells, 200 mA passive) and TI BQ76PL455A-Q1 needing external EMB1428Q/EMB1499Q for active balancing. Four contributions: flexible stacked half-bridge IC compatible with single-/double-tier, mesh, delta and star networks; parasitic-aware layout and BOAC bonding; dual-chip complementary validation; generalised analytical model linking imbalance dynamics to transistor sizing.
- **pp. 4–7** — Fig. 1: stacked half-bridge submodules, complementary variant, six compatible capacitor networks; two-phase operation from a single 0.5-duty PWM (high-side in State 1, low-side in State 2); star network chosen (any-cell-to-any-cell transfer, fewer capacitors than mesh/delta). Section 2.1 generalised dynamic analysis: lumped model with battery resistance and port inductances (Fig. 2); KVL/KCL with charge conservation on the floating star node; first-order response τ = R_e·C_e; closed-form periodic capacitor voltages/currents (Eqs. 1–14); battery currents and average/RMS expressions (Eqs. 15–17); full-bridge extension (Eq. 18) gives continuous cell current and higher average-to-RMS ratio.
- **p. 8** — Losses: dynamic loss P_dyn = 2nf(C_gs·ΔV_gs² + C_gd·ΔV_gd² + C_ds·ΔV_ds²) (Eq. 19); conduction from mean-square capacitor currents (Eqs. 20–22); per-width device scaling (Eqs. 24–27); **optimal switch width** from d(P_switch)/dW = 0 (Eq. 30); performance-first vs area/cost-first sizing routes.
- **pp. 9–10** — IC technologies: DEMOS vs LDMOS; NBL junction isolation and parasitic diodes; DTI; SOI pros (stacking, latch-up immunity, below-ground capability) and cons (cost, BOX thermal resistance). **Design choice:** 130-nm BCD, 5 V devices, substrate isolation "enabling operation with battery stacks of approximately eight to ten Li-ion cells"; four-cell prototype fabricated for cost; extension via on-chip scaling to breakdown, SOI, or board-level IC stacking.
- **pp. 10–12** — Circuit implementation (Fig. 6): four stacked half-bridges HBC1–HBC4; RC dead-time generator; multiple-output stacked-NDMOS level shifter [31]; symmetric cross-coupled LS blocks for delay matching [33]; high-side drivers supplied by the next-higher cell (no external supplies mid-stack); top-most high-side needs only a ≈ 1 nF bootstrap capacitor; Fig. 7: dual-IC full-bridge.
- **pp. 12–16** — Simulations. System level (cells 4.3/4.0/3.1/2.8 V, f = 4 kHz, R_e = 0.2 Ω, C_e = 200 µF): analytical laws verified; full-bridge roughly doubles current; sweeps C_e = 25–400 µF (Fig. 9); parasitic study with 20 nH ports, 10 mΩ battery resistance — negligible in SSL, significant in FSL, full-bridge more robust (Fig. 10). Loss breakdown at 1 MHz, switch width ≈ 64 mm: P_tot = 3.851/5.651/0.151 W for three imbalance scenarios, dynamic loss small (Fig. 11). Post-layout: level-shifter delay 290 ps → 365 ps with parasitics; ≈ 18 mA during transitions; dead-time ≈ 20 ns; imbalance-corner delays 240–300 ps; PVT corners −20 °C/80 °C (dead-time widens SS, shrinks FF; ≈ 1 mA worst-case cross-conduction); Monte Carlo at 2.5 V cells: dead-times ≈ 26.0/28.4 ns, relative shift ≈ 2.4 ns, σ ≤ 0.021 ns. Sub-0.5 ns delays preclude harmful inter-node transients.
- **pp. 16–20** — Experimental set-up: 5 V N/P LDMOS; **3.4 mm² die**; circuit-under-pad (CUP) and BOAC pads; 6–8 aluminium 33 µm bonds per pad (Table 2); daughterboard (0.1 µF + 2×22 µF) on 50-contact card-edge connector; motherboard 4×22 µF; FPGA + B-Box control, 1 kHz–5 MHz; four Keithley 2281S-20-6 emulators (2.4–4.3 V, 3.7 V Li-ion model); balancing capacitors 2×100 µF 16 V MLCC per node (self-resonance 200–250 kHz, ESR ≈ 10 mΩ).
- **pp. 18–22** — Balanced-condition tests: IC bias ≈ 18 mA; node/capacitor/bus voltages and adjacent-node differentials at 2.5 V and 4.2/4.3 V, 1 kHz and 1 MHz (Figs 19–22): clean edges, no over-voltage transients; validates BOAC/CUP, LDMOS dynamics to 1 MHz across the Li-ion window, and internal driver-rail generation.
- **pp. 22–27** — Single-IC imbalance: average current vs imbalance for 8–500 kHz (Fig. 23) — top cell 4.2 V vs 3.3 V others gives ≈ 0.5 A at 8 kHz rising to ≈ 1.25 A at 250–500 kHz, rolling off beyond ~125–250 kHz from parasitic inductance. Average/RMS convergence ≈ 60 kHz (terminal cells), ≈ 30 kHz (middle cells) (Fig. 24); SSL→FSL transition beyond ≈ 32 kHz (Fig. 25); sweeps to 5 MHz show the inductance limit, ~500 kHz optimal for the chosen capacitance (Fig. 26); input filter (≈ 140 µF + ≈ 1 µH cable inductance) noted. SOC balancing of 500 mAh emulated cells at 250 kHz to ≤ 1% ΔSOC across three scenarios (Fig. 28); chip ≈ 65 °C at maximum imbalance, no cooling (Fig. 29).
- **pp. 27–31** — Complementary dual-IC balancer (Figs 30–36): currents nearly doubled and more linear, **reaching ≈ 2.5 A** at only 32–64 kHz (vs 250–500 kHz single-IC), permitting smaller capacitors; average/RMS ratio approaches unity above ≈ 20 kHz; measured transfer efficiency rises with frequency, plateauing above ≈ 30 kHz at ≈ 71–73% (Fig. 35, one cell 4.3 V vs 3.3 V); eight SOC scenarios balanced at 32 kHz to 1–1.8% ΔSOC with reduced cell-location dependency, consistent with discrete realisations [16], [34].
- **pp. 31–32** — Comparison Table 3 (vs TI ICs, JK 16S-15P/20P, Daly BMS, EK-C14S5A, MP2643): proposed = 1.3–2.5 A, 4 cells, 2.4–4.3 V, 18 mA active current, on-chip; only MP2643 is also on-chip but is limited to 2 cells, adjacent-only transfer. Scalability: up to eight cells on-chip; current scalable via LDMOS width; "the chip area was primarily constrained by cost considerations rather than fundamental performance limits."
- **p. 32** — Conclusion (modular, stackable, open-loop, sensor-less; packaging/parasitic co-design as enabler; 2.4–4.3 V chemistry compatibility). Acknowledgements: **EPSRC studentship, Grant No. EP/T517793/1 (Project Reference 2600345)**; Dr Mehdi Baghdadi (supervision); Mehdi Zarei Tazehkand (experimental discussions); Dr Ahmad Elkhateb (manuscript support).
- **pp. 32–34** — References [1]–[34], including [16] Tazehkand & Baghdadi, IEEE TPEL 2025, and the companion Authorea preprints [31] (level shifters, Feb. 2026) and [32] (BTMLC, Oct. 2025).

## B4. Quotable passages (with pages)

- p. 1 (footnote): "This manuscript is based on a chapter of the author's PhD thesis submitted to University College London in 2025."
- p. 1 (abstract): "Experimental results demonstrate robust operation over a wide range of conditions, with switching frequencies from 1 kHz to 5 MHz and cell voltages from 2.4 V to 4.3 V… an average balancing current of up to 2.5 A."
- p. 10: "…the circuit was designed and implemented in a 130-nm BCD process using 5-V devices with substrate isolation, enabling operation with battery stacks of approximately eight to ten Li-ion cells."
- p. 10: "On-chip expansion is possible up to the breakdown limits of the isolation structure, or by adopting an SOI-based process to support higher stack voltages. Alternatively, multiple ICs can be stacked at the board level to accommodate longer battery strings."
- p. 31: "In the present prototype, the chip area was primarily constrained by cost considerations rather than fundamental performance limits."
- p. 32: "…integrated, modular battery balancing circuits can provide compact, scalable, and efficient cell equalisation both as stand-alone modules and when combined in complementary configurations."

## B5. Limitations / future work (as stated)

- Prototype limited to four cells (cost/validation), though the architecture is stated to support eight cells on-chip and eight-to-ten Li-ion cells within the 5 V-device isolation limit (pp. 10, 31).
- Balancing current above ≈ 125–500 kHz limited by parasitic inductances of interconnects and capacitor ESL (pp. 22–26); packaging/interconnect optimisation identified as the route to further gains (p. 32).
- Capacitive-transfer efficiency plateaus at ≈ 71–73% (Fig. 35, p. 30) — inherent to switched-capacitor equalisation under the chosen test differential; not compared against inductive alternatives.
- Active-mode consumption (≈ 18 mA) reducible "through design" — deferred (p. 31).
- Full-bridge mode doubles hardware (two ICs); validation used battery emulators (Keithley 2281S), not physical cells; chip self-heating to ≈ 65 °C without cooling (pp. 26–27).

*(Proposal mapping for Part B consolidated into "PROPOSAL USE MAP (detailed)" at the end of this document.)*

---

## Cross-cutting notes for the lineage argument

1. Both preprints carry the identical printed statement that they derive from a chapter of the author's 2025 UCL PhD thesis, and both acknowledge the same EPSRC studentship **EP/T517793/1 (Project Reference 2600345)** — a direct, citable EPSRC lineage.
2. Both cite the same two companion Authorea preprints (BTMLC IC, Oct. 2025; multiple-output level shifters, Feb. 2026), establishing a four-output publication chain from one thesis on one process platform.
3. Neither document prints a DOI — cite by title/date/hosting, and check engrXiv for assigned DOIs before submission.
4. Machine-load applicability is asserted (motor driving, machine insulation stress, "compact motor drive systems" — Part A, pp. 2, 3, 25) but all delivered-power demonstrations are into resistive loads; the proposal should present inductive/machine loading as the next step the new work funds.

---

## PROPOSAL USE MAP (detailed)

Fact-by-fact mapping into the proposal set: drafts/02_Vision_ArcRevision.md (Vision parts), drafts/03_Approach.md (RQ1–RQ5, WP1–WP4, Building on previous work), and EPSRC_Master_Handover.md S5/S6 plus the R4RI Capability section (Capability Module 2, prior-investment evidence). Conventions for every fragment below: UK English; no em dashes; the author and thesis are anonymised as "the group's work" or "the group's doctoral work" in body text; no DOI is asserted, citation is by title, date and hosting [PI TO CONFIRM: engrXiv DOI check]. The SIX highest-value items are marked ★.

**Citation strings (reference list only, never body text):**
- Part A: "A Scalable Hybrid Multilevel Power Converter Using Low-Voltage On-Chip Power Modules", preprint, 9 March 2026, hosted on engrXiv [PI TO CONFIRM: engrXiv DOI check; no DOI or server branding is printed in the PDF].
- Part B: "On-Chip Scalable High-Speed Active Battery Balancers", preprint, 7 March 2026, hosted preprint (PDF is a captured hosting view) [PI TO CONFIRM: hosting venue and any assigned DOI].

### ★ 1. Stacked two-IC sixteen-step demonstration (Part A, pp. 20–23)
- **Fact.** Two eight-tap BTMLC ICs plus an off-chip half-bridge of 50 V MOSFETs synthesise sixteen-step half-sine waveforms (3.3 V per step, references to 49.5 V), delivering up to 6 A into resistive loads; per-tap DC efficiency 98.5% peak, 85% worst tap.
- **(a) Location.** The single strongest support for Vision "Crossing the line: the 50 V claim" (VIS-CROSS-v7 buildability paragraph) and for the Approach "Building on previous work" lineage: it shows the platform scales toward per-slot voltage and current levels. Directly replaces the placeholder at drafts/03_Approach.md line 65 ("[PI TO CONFIRM: preprint citation — candidate entry in References]"). Also feeds handover S6 WP2 feasibility and the standard risk table (discrete plus IC hybrid partition already demonstrated).
- **(b) Usage mode.** Quantitative evidence claim plus reference-list citation; the numbers 49.5 V, 6 A, sixteen steps, 98.5% are the load-bearing figures.
- **(c) Fragment.** "The platform scales towards per-slot voltage and current levels: in the group's work, two stacked converter ICs and an off-chip half-bridge synthesise sixteen-step waveforms of approximately 49.5 V at up to 6 A into resistive loads, with per-tap efficiencies of 98.5% down to 85%."

### ★ 2. Printed stacking-scalability argument (Part A, p. 5)
- **Fact.** The eight-tap ceiling per chip is set by technology breakdown; higher voltage is reached by SOI-class processes or by board-level stacking, stated as "a scalable pathway for constructing higher-voltage and higher-power systems while maintaining compatibility with mainstream low-voltage IC technologies".
- **(a) Location.** Vision "Crossing the line" and the Building-on-previous-work scaling narrative: this is the printed, citable version of exactly the scaling story the proposal extends from battery strings to stator slots. Also usable in Novelty (handover S5b) to show the scaling route is published, while its machine application is not.
- **(b) Usage mode.** Direct quotation or close paraphrase with citation; anchors the claim that scaling is a demonstrated property of the platform, not a hope.
- **(c) Fragment.** "The group's work has shown that stacking low-voltage converter ICs at board level provides a scalable pathway to higher-voltage systems while retaining mainstream low-voltage IC technology; this programme carries that pathway into the stator, where each slot section requires only tens of volts."

### ★ 3. Motor-drive positioning statements (Part A, pp. 3, 25)
- **Fact.** The architecture is printed as "supporting unified power-processing functions including motor driving, charging, and cell balancing" (p. 3) and as "a promising building block for future high-voltage converters, battery-integrated power electronics, and compact motor drive systems" (p. 25).
- **(a) Location.** Vision "Crossing the line" (the platform was built with machine drive in view) and the Approach differentiation paragraph; also the intellectual-lineage table (handover S7d).
- **(b) Usage mode.** Short quotation as intent evidence; must be paired with the honesty caveat that machine loading is asserted, not demonstrated (see Traps).
- **(c) Fragment.** "The converter platform was published with motor driving explicitly among its unified power-processing functions; what remains undemonstrated, and what this programme establishes, is its operation from a machine winding rather than a battery string."

### ★ 4. EP/T517793/1 acknowledgements in both preprints (Part A pp. 25–26; Part B p. 32)
- **Fact.** Both preprints print the acknowledgement of an EPSRC PhD studentship, Grant No. EP/T517793/1 (Project Reference 2600345), and both carry the printed footnote that they derive from a chapter of a 2025 UCL PhD thesis.
- **(a) Location.** Capability Module 2 (the R4RI track-record section, handover S10 territory): printed, citable evidence that prior EPSRC investment matured into the enabling IC platform, closing the loop for the return-on-public-investment argument in "Scope and Funding Rationale" (S5b).
- **(b) Usage mode.** Track-record statement with grant number; the Capability section is where naming the grant is appropriate. In the anonymised body, use only "the group's doctoral work".
- **(c) Fragment.** "The enabling integrated-circuit platform was developed under prior EPSRC investment: the 2026 preprints recording the stacked converter and the on-chip balancer both carry printed acknowledgement of EPSRC studentship EP/T517793/1 (Project Reference 2600345). This proposal converts that investment into a new class of machine drive."

### ★ 5. Measured thermal behaviour without cooling (Part A, p. 23; Part B, pp. 26–27)
- **Fact.** At 6 A on the highest tap: R_path = 82 mΩ, P_cond = 2.952 W, chip at 102 °C against a 28 °C board, effective thermal resistance approximately 25.1 °C/W with no external cooling; die attach and heat spreading flagged for improvement. The balancer chip reached approximately 65 °C at maximum imbalance, also uncooled.
- **(a) Location.** RQ5 and WP2 (thermal network and packaging specification) in 03_Approach.md; the risk-table row "IC junction temperature exceeds limit".
- **(b) Usage mode.** Quantitative baseline: the group's own measured thermal figures motivate RQ5 (an uncooled bench chip already reaches 102 °C, so a 120–150 °C winding environment is a genuine research question, not a detail) and give WP2 a validated starting point.
- **(c) Fragment.** "Measured thermal data from the group's work, an effective junction-to-board thermal resistance of approximately 25 °C per watt with chip temperatures reaching 102 °C at 6 A without external cooling, define the starting point for RQ5: per-slot modules must reject comparable losses into a winding environment at 120 to 150 degrees Celsius."

### 6. Path resistance and efficiency envelope (Part A, pp. 18–21)
- **Fact.** Optimised packaging gives 60–85 mΩ path resistance across all taps at 2–6 A DC; efficiency 98.5% to 85% per tap; edge-connector sockets identified as removable loss.
- **(a) Location.** WP2 (SPICE modelling under winding-source conditions needs measured device and path parameters) and Feasibility.
- **(b) Usage mode.** Design-input numbers; supporting evidence that per-slot conduction loss is compatible with the efficiency claims of the Vision cascade.
- **(c) Fragment.** "Measured path resistances of 60 to 85 milliohms per tap at 2 to 6 A in the group's work bound the conduction loss of a per-slot module and seed the WP2 circuit models with silicon-validated parameters."

### 7. Dynamic frequency and magnitude agility (Part A, p. 22)
- **Fact.** NLC operation with dynamic frequency changes (10 Hz to 1 kHz single module; 10 Hz to 500 Hz stacked) and arbitrary reference steps (3.3 V to 23.1 V single; 3.3 V to 49.5 V stacked) with stable response throughout.
- **(a) Location.** RQ4/WP3 (reconfigurable field control) feasibility: per-slot waveform agility is the actuator capability that software-defined pole reconfiguration assumes.
- **(b) Usage mode.** Feasibility evidence, one sentence.
- **(c) Fragment.** "The converter platform has demonstrated stable synthesis under step changes of both frequency and magnitude, from 10 Hz to 1 kHz and from 3.3 V to 49.5 V, which is precisely the waveform agility that per-slot spatial field reconfiguration requires of its actuators."

### ★ 8. Second IC: the on-chip active balancer (Part B, throughout)
- **Fact.** A second fabricated and measured IC (3.4 mm², same 130-nm BCD family, 5 V LDMOS): four stacked half-bridges with fully integrated dead-time, multiple-output level shifting and gate driving; 1 kHz to 5 MHz; 2.4 to 4.3 V; up to 2.5 A average balancing current in dual-IC complementary mode; emulated cells balanced to about 1% SOC difference.
- **(a) Location.** Capability Module 2 and Building on previous work: proves the group's on-chip integration capability is a repeatable platform (two distinct fabricated ICs, shared IP), not a single device. Also supports "Research environment and facilities" ("IC design flows developed for the group's prior chip work transfer directly into WP2").
- **(b) Usage mode.** Breadth-of-capability evidence; one to two sentences plus reference.
- **(c) Fragment.** "The same 130 nm BCD platform has produced a second fabricated and measured IC, an on-chip active battery balancer operating from 1 kHz to 5 MHz and delivering up to 2.5 A of balancing current, demonstrating that the group's floating-domain gate-drive, level-shifting and dead-time IP is a reusable design platform rather than a single device."

### 9. Shared IP chain and thesis lineage (Part A pp. 25–26 refs [23]/[24]; Part B refs [31]/[32]; both p. 1 footnotes)
- **Fact.** Both preprints derive from the same 2025 thesis, cite the same two companion Authorea preprints (BTMLC IC, Oct. 2025; multiple-output level shifters, Feb. 2026), and reuse identical level-shifter and dead-time circuit IP.
- **(a) Location.** The intellectual-lineage table (handover S7d) and the Building-on-previous-work table in 03_Approach.md; strengthens the "every constituent capability has a prior demonstration within the group" sentence in Novelty (S5b).
- **(b) Usage mode.** Structural evidence for the lineage argument; the four-output publication chain from one thesis on one process shows sustained, coherent capability.
- **(c) Fragment.** "Across four related outputs from the group's doctoral work, converter IC, level shifters, stacked converter and balancer, the same floating-domain circuit IP recurs on one process platform, evidencing a coherent and transferable design capability rather than isolated results."

### 10. Stated limitations as the funded gap (Part A §A5; Part B §B5)
- **Fact.** All delivered-power demonstrations are into resistive loads; the off-chip 50 V stage is "not optimised for low on-state resistance or compactness"; three-phase machine drive and bipolar operation are conceptual only; balancer validation used battery emulators.
- **(a) Location.** RQ2 gap statement and the "Remaining gap" column of the Building-on-previous-work table ("Battery-cell resistive loads only"); also Feasibility (honest framing pre-empts reviewer challenge).
- **(b) Usage mode.** Deliberate self-limitation: state the resistive-load boundary explicitly and define the programme as the work that crosses it.
- **(c) Fragment.** "Every delivered-power demonstration of the platform to date is into resistive loads. Operation from an inductive winding section with back-EMF, under the coupled conditions of a shared magnetic core, is exactly the boundary of knowledge that RQ2 and WP2 are designed to cross."

### Traps

1. **Do not present resistive-load demonstrations as machine-validated.** Every delivered-power result in both preprints is into resistive loads (4 Ω and 8 Ω benches); motor driving is asserted intent, not a demonstration. Phrase the stacked result as a converter-platform result whose machine-source extension is what the programme funds; any wording implying the platform "drives machines" overclaims and hands reviewers an easy objection.
2. **Do not assert a DOI.** Neither PDF prints a DOI, and neither carries server branding on its pages; engrXiv hosting for Part A is inferred from the filename only, and Part B is a captured hosting view. Cite by title, date and hosting, keep the [PI TO CONFIRM: engrXiv DOI check] flag live, and resolve it before submission; an invented or wrong DOI in an EPSRC reference list is a credibility wound.
3. **Efficiency framing.** 98.5% is the peak per-tap DC efficiency at 2 to 6 A, falling to 85%; it is not a system efficiency for the 49.5 V stacked waveform synthesis. Never attach 98.5% directly to the sixteen-step demonstration.
4. **Die-area consistency.** The Vision text cites a 15.2 mm² die [1]; this preprint's die is 20.52 mm² (5474 by 3750 micrometres). These figures refer to different prototypes or accounting; reconcile before both appear in the same document [PI TO CONFIRM: which die area belongs to which IC].
5. **Current-rating context.** "Up to 6 A" holds for the optimised wire-bonded board; JLCC-packaged parts were limited to about 2.5 A by bond-wire fusing. Quote 6 A only with the stacked or optimised-board context.
6. **Anonymisation discipline.** Both preprints are single-author with printed personal e-mails and a QUB affiliation footnote. Body text must say "the group's work" or "the group's doctoral work"; grant number EP/T517793/1 belongs in the Capability section, not in anonymised Vision or Approach body text.
7. **Balancer validation medium.** Part B used Keithley battery emulators, not physical cells; write "emulated cells" wherever balancing performance is quoted.


<!-- ==================== FILE: evidence/08_SkyDrive_appendices_digest.md ==================== -->

# 08 — SkyDrive Programme Appendices: Technical Digest

## Framing rule (read first)

**SkyDrive is a separate Innovate-UK-class (ATI) programme, not the EPSRC research target.** It is a 100 kW, 18,000 RPM, 1 kV-class integrated electric propulsion programme (TRL 3–6) delivered by a consortium of iNetic (lead), UCL and ARC Aerosystems, with Eaton participating as a **non-funded Tier-1 adviser**. For the EPSRC proposal, SkyDrive is **context only**: translation environment, industrial-engagement evidence, and impact-narrative background. It must **never** be presented as the research target, its specifications must not become EPSRC deliverables, and its market/benefit claims must not be restated as the applicants' own. All figures below are **SkyDrive's claims as written in its appendices**; stated sources are recorded, as is their absence.

Source files (all in `/home/user/proposal/`): `10192096 - SkyDrive - Appendix - Q7 Business Opportunity.docx`, `SkyDrive_Q9.docx`, `SkyDrive_Q12_Technical_Approach_FINAL (1).docx`, `10192096 SkyDrive - Risk Register - Appendix Q13.docx`, `good photos for Question 10.docx`.

---

## 1. Q7 — Business Opportunity

### 1.1 Quantified market and policy figures, with stated sources

| Figure (as stated in Q7) | Source stated in the document |
|---|---|
| UK passenger demand forecast to reach **435 million by 2050** | None cited in text ("UK passenger demand is forecast to reach…") |
| Global demand exceeds **38,000 new aircraft** valued at approximately **£4.65 trillion** over the next two decades | None cited in text |
| UK aerospace sector contributes over **£35 billion annually** to the economy | None cited in text |
| More than **120,000 high-value jobs** across nearly **3,000 supply-chain companies** | None cited in text |
| **ATI and industry co-investment of £1.37 billion between 2022 and 2025**, expected to unlock over **£20 billion of private investment by 2040** | Attributed to ATI/industry co-investment context; no document citation |
| Propulsion power-density requirements of approximately **1.5 kW/kg by 2026**, increasing toward **3.5 kW/kg by 2050**, alongside fault tolerance and high-voltage operation in the **1 kV class** | Attributed only to "Industry targets" |
| Harbour Air retrofit comparison: **~1.0 kW/kg (battery-only)**, 30–60 min range vs SkyDrive target **2.0–2.5 kW/kg**, >2 h with fuel cell | Comparison table (Figure 5 in Q7); no external citation |

**Caveat:** our separate verification found the **ATI provenance of the 1.5 → 3.5 kW/kg targets uncertain** — not traceable to a published ATI document. Any EPSRC mention of sector power-density trajectories must cite an independently verified source or be flagged [PI TO CONFIRM]; likewise all unsourced macro figures above.

Policy alignment claimed: Aerospace Growth Partnership "Net Zero Aviation by 2050"; Jet Zero and Destination Net Zero strategies; emerging CAA/EASA certification frameworks.

### 1.2 Deployment phasing

Four-phase customer-led pathway with ARC Aero Systems as launch customer:

1. **Phase 1** — non-primary propulsion on **Pegasus** (§7.2: the **Pegasus III hybrid gyrocopter**, SkyDrive as a **jump take-off propulsion module**, certifiable as an aircraft component with early in-flight data capture).
2. **Phase 2** — production ramp and data-driven certification maturity.
3. **Phase 3** — primary propulsion integration on the **Linx P9** (nine-seat platform).
4. **Phase 4** — replication across other OEM platforms.

ARC has confirmed willingness to support post-project TRL 7–9 progression (ground test rigs, air vehicles, potential joint commercial structures).

### 1.3 Customer-pull companies named

- **ARC Aero Systems** — committed launch customer (Pegasus III, then Linx P9).
- **Eaton** — Tier-1 aerospace supplier "actively supporting system architecture, certification strategy, and industrialisation planning" (unfunded).
- Wider engagement claimed with **Boeing, Rolls-Royce Electrical, Ontic, Beyond Gravity, and Vertical Aerospace** — described as confirming demand; no commitments quantified.

### 1.4 Technical differentiation claims (context for the machine class)

Multi-phase HV motor at **1 kV and 18,000 rpm**; modular multilevel inverter (PD mitigation, EMI reduction, fault reconfiguration); integrated battery/hydrogen-fuel-cell balancing converter; advanced thermal management; fully integrated motor–inverter–energy-management package for joint certification; modular 100 kW unit scalable "toward megawatt class".

### 1.5 Revenue model

- **SkyDrive IM** (integrated motor drive): ~**£35k**/unit; **200 units by 2031**, **>1,000 by 2035**; licensable at component level.
- **SkyDrive HPro** (hybrid, battery/fuel-cell balancing): ~**£80k**/unit.
- **SkyDrive Services**: recurring revenue at ~**20% of total product revenue**.
- ARC forecasts deliveries from year three post-development, **~50 aircraft/year by year five**, each embedding a SkyDrive package.
- By **2040**: exports **>£200m/year**, **>70% international**, **>500 direct high-skill UK jobs**.
- Manufacturing: **iNetic's AS9100-certified facilities**; Eaton industrialisation and market-access experience.

---

## 2. Q9 — Innovation Content

Q9 is a technology-by-technology table (challenge / SoA / innovation beyond SoA); all streams **TRL 3 → 6** except AI control (TRL 4 → 6).

1. **Ultra power-dense electric motor.** SoA cited: Siemens ~5 kW/kg @ 11 krpm; Honeywell ~8 kW/kg @ 19 krpm; NASA ~10–13 kW/kg @ 20 krpm; EMRAX ~10 kW/kg. Claim: **~13 kW/kg at 100 kW, 1 kV, 18,000 rpm, 95–98% efficiency**; AM housings (+30% thermal conductivity, −25% temperature); hollow conductors at **25 A/mm²**, direct liquid cooling; spray cooling; amorphous laminations (−30% losses); carbon-fibre sleeves (**>3 GPa**); **~24% higher density**, up to **47 kg mass saving**, **10–15% more range**.
2. **Multiphase reliability/redundancy.** Six-phase and dual three-phase machines with integrated multilevel fault-tolerant inverters; torque ripple −50–80%; common-mode voltage −40–60%; life +>30%; operation continues under partial winding/phase loss. KPI: "100% improvement in fault tolerance vs SoA".
3. **Altitude-resilient multilevel drive for partial-discharge (PD) mitigation.** SoA limited to <800 V, thick insulation, bulky filters. Claim: stepped waveforms cut dv/dt ~50%, overshoot >90%; insulation life **2–3×**; reliable **1 kV operation at altitude**.
4. **Power-on-Chip converter with integrated cooling.** SoA (Evolito, Helix UK): SiC modules, cold plates, ~50–100 W/cm². Claim: WBG switches, drivers and passives on hybrid substrates; AM microchannels **>1,000 W/cm²**; 2× power density; hardware weight −50–75%; component count −up to 50%.
5. **Streamlined propulsion integration.** Motor, inverter and cooling in a single modular housing; cabling mass −20–40%; propulsion mass −≥10%; validated on ARC's jump take-off (**eJTO**) platform.
6. **AI-powered fault-tolerant control and validation.** FPGA closed-loop control with AI-driven digital twins for fault prediction/reconfiguration; validated on the ARC eJTO platform (altitude, pressure, dynamic load).

**KPI list (Q9 §9.2):** ≥10% propulsion mass reduction; **13 kW/kg motor** power density; 100% fault-tolerance improvement; 50–70% EMI reduction; ≥25% lower temperature; up to 50% power-electronics compactness gain; **16 kW/kg integrated system** power density; TRL 3→6 validation with digital twin; +10–15% range/payload.

**Baseline spec (§9.3):** continuous **100 kW**, **1 kV**, **18,000 rpm**, multilevel inverter, embedded cooling; requirements derived from ARC's **"LINX P3"** platform (Q7/Q12 say **Linx P9** — an internal naming inconsistency; do not propagate either into EPSRC text unchecked). Partner-led sections: iNetic — multiphase machine (Vacoflux SiCo and Metglas amorphous laminations, T1000G carbon-fibre sleeves, hollow conductors, spray cooling, planetary gearbox); UCL — power electronics (control-integrated chip sequencing cascaded H-bridge cells: stepped low-dv/dt synthesis instead of HV PWM; microchannel-cooled substrates, dielectric coolant); ARC — eJTO testing (fault injection, thermal, EMI, digital-twin correlation, TRL 4→6).

**Note:** Q9's 13/16 kW/kg claims sit differently from Q12's stated targets (system >1.5 kW/kg, active-material >15 kW/kg) — quote whichever document is being referenced, never blend them.

---

## 3. Q12 — Technical Approach

### 3.1 Concept and specifications

Integrated **100 kW-class** HV propulsion subsystem: **six-phase motor at 1 kV and 18,000 rpm**, fault-tolerant **multilevel inverter**, **high-speed step-down gearbox**, integrated control and thermal management, co-designed as a single jointly certifiable subsystem. Energy storage is explicitly **out of scope (bought in)**. Targets: continuous high power; **system power density >1.5 kW/kg** for the integrated motor + inverter (**active-material >15 kW/kg**); **efficiency >97%**; defined fault tolerance; compliance-aligned validation evidence. TRL 3 → 6 via laboratory validation, HIL, environmental stress testing and integrated operation on ARC's **flight-representative Pegasus platform**, progressing to the **nine-seat Linx P9**; MW-class scaling identified (insulation coordination, multi-module thermal balancing, parallel-inverter control).

### 3.2 Partner roles — exact wording

- Consortium sentence: "**iNetic leads motor design, gearbox integration and aerospace-grade manufacturing; UCL contributes multilevel power electronics, control architecture and electro-thermal modelling; ARC provides system integration and flight-representative validation; and Eaton participates as a non-funded Tier-1 adviser on certification, industrialisation readiness and system safety.**"
- Eaton, on the WP diagram: "**Eaton advising across all of them**" (i.e. across WP0–WP4).
- iNetic dynamometer — the only explicit Q12 mention is the build-stream photo caption: "**(left) iNetic six-phase motor and dynamometer rig; (centre) UCL multilevel power-electronics drive; (right) ARC flight-representative platform. Placeholders to be replaced with consortium images.**" (Q9 §9.6 also refers to "subsystem verification on dynamometers"; Q13 T1 to tuning models "with dyno telemetry after each build".)
- **UCL APL facilities: not mentioned anywhere in Q12** (nor in the other appendices as extracted). Any EPSRC statement about UCL's Advanced Propulsion Lab must be evidenced from elsewhere, not from SkyDrive documents.

### 3.3 Work-package structure

- **WP0 Project Management (iNetic)** — iNetic PM, Principal Investigator holds technical leadership; **xRL and PROLaunch** life-cycle tools; weekly/monthly/quarterly reviews; quarterly reports to the monitoring officer.
- **WP1 Six-Phase Motor Engineering (iNetic)** — WP1.1 electromagnetic/mechanical multi-physics optimisation at 18,000 rpm; WP1.2 integrated cooling; WP1.3 high-speed step-down gearbox; WP1.4 hardware integration and bench test. Deliverable: validated motor + cooling + gearbox assembly; defines the torque–speed envelope and motor interface for WP2/WP3.
- **WP2 Fault-Tolerant Power-Electronics Drive (UCL)** — WP2.1 topology definition (candidates: **neutral-point-clamped, flying-capacitor** for >1 kV, reduced dv/dt and common-mode stress) plus six-phase modulation/digital control with balanced power sharing under single-phase or device failure; WP2.2 electro-thermal design and cooling; WP2.3 hardware build and readiness verification (electrical, thermal, EMI). Deliverable: fabricated, readiness-verified drive unit.
- **WP3 System Integration and Experimental Validation (ARC Aerosystems)** — integrates motor-gearbox and drive; validates under aerospace-representative duty cycles: fault injection (graceful degradation under phase/device loss), thermal endurance, altitude-representative cycles, EMI characterisation; produces the TRL6 airworthiness-aligned evidence package.
- **WP4 Exploitation and Dissemination (iNetic)** — industrialisation/feasibility assessment, exploitation strategy, IP-protection framework, publications, industry engagement.

### 3.4 Timeline and milestones

**36 months**; motor and power electronics in parallel for two years; integration from mid-point; exploitation in the final year; **TRL6 by ~2029**. Milestones: **M1** requirements/baselines frozen (M6); **M2** detailed designs verified by analysis, TRL 4–5 (M12); **M3** hardware manufactured and bench-tested (M20); **M4** subsystem assembled (M30); **M5** validated on the SkyDrive platform, TRL6 (M36).

**Cross-reference note:** Q12's preamble points to "Risks appendix (Q14)" and "Innovation appendix (Q13)", but the actual files are Q13 (risks) and Q9 (innovation) — drafting drift; cite files by filename, not internal cross-reference.

---

## 4. Q13 — Risk Register

**Format:** Risk = Likelihood (1–5) × Impact (1–5); bands **1–8 Low, 9–15 Medium, 16–25 High**; each risk scored **pre- and post-control** with cause, impact, mitigation and WP/owner. Categories: Technical T1–T33, Commercial C34–C40, Managerial M41–M50, Environmental E51–E53, Social S54–S55. Scores shown pre → post (L×I=S).

| ID | Risk (abridged) | Pre | Post | Mitigation (abridged) | Owner/WP |
|---|---|---|---|---|---|
| T1 | EM/thermal/PD model uncertainty: 1 kV, 18,000 RPM motor, reduced pressure, spray cooling | 3×4=12 | 2×3=6 | Correlate FEM vs Epstein/BH and reduced-pressure PD coupons; tune with dyno telemetry; ±5% torque / ±5 °C gate criteria | WP1&2, iNetic/UCL |
| T2 | Incomplete system requirements (duty cycle, DC-link, EMI/EMC, interfaces) | 3×3=9 | 1×3=3 | Freeze SRS/ICD via OEM/regulator workshops; CCB change control | WP1, iNetic |
| T3 | Inverter fails fault-ride-through/redundancy at 1 kV with SiC | 4×4=16 | 2×3=6 | Two topologies to PDR; HIL fault-injection down-select; per-leg isolation; limp-home mode | WP1, iNetic |
| T4 | AM cooling channels / hollow conductors fail yield/accuracy | 4×4=16 | 2×2=4 | DFAM trials, CT-scanned coupons; brazed-insert fallback if yield <90% | WP1, iNetic |
| T5 | Vacoflux laminations, carbon sleeves, HV insulation delays | 3×4=12 | 2×3=6 | Long-lead POs at PDR; dual-source; safety stock | WP1, iNetic |
| T6 | Component delay due to licence requirements | 4×5=20 | 3×4=12 | Order via licence-holding supplier; documentation provided | WP2, iNetic |
| T7 | Aerospace-grade SiC/GaN allocation limits | 2×3=6 | 1×2=2 | Pin-compatible second sources; derating; post-PDR buys | WP2, iNetic |
| T8 | Supplier/logistics slips stall assembly | 3×4=12 | 2×2=4 | Early orders; weekly expediting; pre-qualified alternates | WP3, iNetic/UCL |
| T9 | Weight/efficiency miss benchmarks and business case | 3×3=9 | 2×2=4 | Re-optimise with dyno data/BoM; gearbox/cooling as levers | WP1&2, iNetic/UCL |
| T10 | Incorrect/unclear drawings | 4×4=16 | 2×3=6 | Clarification with stakeholders | WP1&2, iNetic/UCL |
| T11 | Delivery delays (lead times underestimated) | 4×5=20 | 2×3=6 | Early ordering; dual-source | WP2, iNetic |
| T12 | Out-of-spec components / quality issues | 4×4=16 | 2×3=6 | Incoming QC; supplier QA agreement | WP3, iNetic |
| T13 | Performance/economics not commercially competitive | 2×3=6 | 2×2=4 | Re-optimise topology; define further optimisation work | WP1, iNetic |
| T14 | SkyDrive/test facilities damaged in testing | 1×4=4 | 1×2=2 | Instrumentation and protection; destructive tests last | WP3, iNetic/ARC |
| T15 | Rotor hoop-stress failure / burst at 18,000 rpm | 3×5=15 | 2×3=6 | FEA (stress/modal/fatigue); retaining sleeves; staged spin tests | WP3, iNetic |
| T16 | Coil-winding errors | 3×4=12 | 2×2=4 | Checked coil calculator; winding plan; validated temperature rating | WP3, iNetic |
| T17 | Component overheating (poor thermal design) | 3×4=12 | 2×2=4 | Thermal simulation; derating; certified materials | WP1, UCL |
| T18 | Incomplete/non-intuitive assembly SOPs | 3×3=9 | 1×2=2 | Visual SOPs; supervised pilot build with hold points | WP3, iNetic |
| T19 | Motor/powertrain fails final testing (design flaw) | 3×4=12 | 2×3=6 | Simulation; DVP; sub-assembly testing | WP3, iNetic |
| T20 | Test rig not ready | 2×4=8 | 2×2=4 | Parallel planning; early rig preparation | WP3, iNetic/ARC |
| T21 | Inadequate tooling (no early jig plan) | 2×4=8 | 1×2=2 | Fixture planning in early design | WP1, iNetic/UCL |
| T22 | Inadequate heat transfer (microchannel/oil spray) under dynamic load | 2×4=8 | 1×3=4 | CFD; HIL bench test; redundant cooling path (hollow windings) | WP2, UCL |
| T23 | Thermal management under real operating conditions | 3×4=12 | 2×3=6 | Flight-like simulation/test; liquid cooling if needed | All, iNetic/UCL |
| T24 | Power density vs reliability trade-off | 4×4=16 | 2×3=6 | Conservative margins; accelerated life test; FMEA | WP1&3, iNetic |
| T25 | NVH from EM forces/assembly | 3×3=9 | 2×2=4 | FEA; NVH testing; precision balancing | WP1, iNetic |
| T26 | Precision tolerances not consistently achievable | 4×4=16 | 2×3=6 | Supplier selection; CMM validation; pilot production | WP3, iNetic |
| T27 | Control tuning / DO-178C software certification delays | 3×5=15 | 2×3=6 | Experienced control partners; modular software architecture | WP3, iNetic |
| T28 | Test environment cannot replicate altitude/vibration/cooling | 3×4=12 | 2×2=4 | HIL setups; vibration tables; altitude chambers | WP4*, iNetic |
| T29 | Battery/power-source compatibility mismatch | 3×4=12 | 2×2=4 | Early power requirements; involve battery partners | WP1, iNetic |
| T30 | Integration interface mismatches (mechanical/software) | 4×5=20 | 3×4=12 | WP1 interface definition with ARC; staged test plan | WP3, iNetic |
| T31 | Inverter/motor subsystem underperformance | 4×4=16 | 3×3=9 | Iterative hardware test; WP1-validated alternatives | WP1&4*, UCL |
| T32 | Thermal management failures in prototypes | 3×4=12 | 2×3=6 | System thermal modelling; phased validation | WP4*, UCL |
| T33 | Assembly errors / lack of rotor-specific skill | 3×4=12 | 1×3=3 | Training; work instructions; supervision | WP3, iNetic |
| C34 | Failure to meet specs (delays/rework) | 4×5=20 | 2×3=6 | Schedule buffer | All, iNetic |
| C35 | Cost overrun | 3×3=9 | 2×2=4 | Cost tracking; contingency; fixed-price deals | WP2, iNetic |
| C36 | Customer concentration risk | 3×4=12 | 2×3=6 | Diversify customers, incl. buses | All, iNetic |
| C37 | IP infringement / insufficient protection | 3×4=12 | 2×3=6 | Early patents; NDAs; monitoring | All, iNetic |
| C38 | Misalignment with customer roadmaps | 3×4=12 | 2×2=4 | Co-develop with anchor customers; modularity | All, iNetic |
| C39 | Geopolitical/trade risks | 3×4=12 | 2×3=6 | Multiple suppliers; UK/EU/US routes | All, iNetic |
| C40 | Late customer requirement changes | 3×4=12 | 2×2=4 | Design lock at order; change control | WP1 |
| M41 | Resource constraints / skills gaps | 4×5=20 | 3×3=9 | Workforce planning; cross-training; subcontractors | All, iNetic |
| M42 | Key staff attrition | 3×4=12 | 2×3=6 | Retention bonuses; cross-training | All |
| M43 | Communication breakdown | 3×4=12 | 2×2=4 | Reviews; collaborative tools; dashboard | All, iNetic |
| M44 | Inadequate risk-management culture | 4×4=16 | 2×3=6 | Register; scheduled reviews; escalation matrix | All, iNetic |
| M45 | Delayed decision-making | 3×4=12 | 2×3=6 | Authority matrix; time-boxed decisions | All, iNetic |
| M46 | Weak project governance | 4×4=16 | 2×3=6 | RACI; governance board; tracking | All, iNetic |
| M47 | Inconsistent stakeholder engagement | 3×4=12 | 2×3=6 | Stakeholder map; quarterly briefings | All, iNetic |
| M48 | Timeline slippage | 3×3=9 | 2×2=4 | Milestone buffers; weekly stand-ups | All |
| M49 | Budget overrun (subcontractor delays) | 2×4=8 | 1×3=3 | Fixed-price contracts; contingency fund | All |
| M50 | Data/documentation loss or miscommunication | 3×3=9 | 1×2=2 | Central document control | WP3 |
| E51 | Rare-earth magnet supply/sustainability (NdFeB, e.g. N48UH) | 4×5=20 | 3×3=9 | ISO 14001 suppliers; recycled magnets; disclosure | (no owner listed) |
| E52 | Energy savings not achieved | 3×3=9 | 2×2=4 | Energy monitoring; AI tweaks | WP3 |
| E53 | Scrap rate exceeds target | 2×4=8 | 1×3=3 | Lean kitting; error-proofing | WP3 |
| S54 | Skills gap in digital manufacturing | 2×3=6 | 1×2=2 | STEM workshops | WP3, iNetic |
| S55 | H&S incident during assembly | 2×5=10 | 1×2=2 | Document/version control (as written) | WP3, iNetic |

\*T28/T31/T32 cite "WP4/Testing" although Q12 defines WP4 as exploitation — another register/WP-structure inconsistency. **These risks inform, but are not copied into, the EPSRC risk table** — EPSRC risks must be research risks owned by the EPSRC team.

---

## 5. "good photos for Question 10.docx"

Despite the filename, this is a full **Q10/benefits appendix draft** (internally numbered §7.1–7.6) containing **six embedded PNG images** (`word/media/image1.png`–`image6.png`) and these table/figure captions:

- **Table 1.** "Benefits at a glance, with the source of each in this appendix" (30–80 vs 150–200 gCO₂/pax-km; >400,000 tCO₂/yr abated by 2040, ~900 t per 100 kW unit; ~1,220 UK jobs, £268m revenue by 2040; sovereign capability at TRL6 by ~2029).
- **Figure 1.** "Line of sight from validated component performance, through the efficiency and mass levers, to aircraft-level and fleet benefit."
- **Figure 2.** "Aircraft CO₂ intensity, electric and hybrid versus conventional, across the classes SkyDrive's propulsion addresses."
- **Figure 3.** "Post-project industrialisation and certification investment, 2029 to 2032 (£37m total), by category and year."
- **Figure 4.** "Projected UK employment and revenue growth to 2040, consistent with the bid's established figures."
- **Figure 5.** "SkyDrive commercialisation roadmap, from TRL6 validation on the Pegasus platform to higher-power derivatives."

Notable body figures (SkyDrive's claims): ~£1.9m programme over three years; ~£0.42m industrial match; ATI contribution ~£1.50m; £37m industrialisation 2029–2032; direct employment ~450 by 2040 (iNetic ~280, ARC ~150, UCL ~20), **ONS multiplier 1.72** → ~1,220 total; revenue ~£130m by 2036, ~£268m by 2040 (~£200m/yr export); "every £1 of aerospace R&D leverages ~£14" (attributed to ATI); three patent families; **five PhD completions and UCL-led publications**; Eaton in **SAE AE-7/AE-10** standards work; noise −10–15 dB; ATI 2026 strategy alignment (double UK share by 2035; propulsion >US$17bn/yr by 2050; >65,000 deliveries to 2050, ~70% single-aisle).

---

## PROPOSAL USE MAP (detailed)

Standing rule restated: SkyDrive is **context only** — a separate higher-TRL programme cited as translation environment, industrial-engagement evidence and impact background. Citing it **implies no commitment** to the EPSRC proposal by any SkyDrive party, and **every figure drawn from it carries [PI TO CONFIRM] as another programme's claim**. Fact-by-fact map below; the five highest-value items are marked ★.

### ★ 1. SkyDrive programme identity — the translation environment

- **Fact:** ATI project 10192096; iNetic (lead) + UCL + ARC Aerosystems, Eaton as non-funded adviser; 100 kW-class, 1 kV, 18,000 RPM integrated propulsion; TRL 3–6, TRL6 by ~2029 (Q7, Q12).
- **(a) Proposal location:** Capability R4RI (`/home/user/proposal/drafts/05_Capability_R4RI.md`) Module 2 "Development of others / working relationships" (Variant A ¶2 of that module; Variant B, PI block) and Module 4 "Broader users and societal benefit" (both variants) — already deployed there; Approach section "Maximising translation of outputs into outcomes and impact" (handover S6 sub-heading list).
- **(b) Usage mode:** cite as evidence of an active, delivery-based industrial relationship and the environment into which TRL 1–3 outputs feed. Mandatory caveat wording: a **separate higher-TRL programme**, separately funded (ATI/Innovate-UK-class) with independent objectives; citing it **implies no commitment** to the present proposal; the 100 kW / 18,000 RPM / 1 kV figures describe *that* programme's target class, never this one's, and each is **[PI TO CONFIRM] as another programme's claim**.
- **(c) Fragment:** "The ATI-funded SkyDrive programme (project 10192096) — a separate, higher-TRL (TRL 3–6) collaborative programme in which the applicant group develops 100 kW-class integrated aerospace propulsion with iNetic and ARC Aerosystems [PI TO CONFIRM: figures are that programme's claims] — evidences the working industrial translation environment into which this programme's TRL 1–3 outputs feed; it is separately funded with independent objectives and implies no commitment to the present proposal."

### ★ 2. Eaton's role — verbatim adviser wording (Q12)

- **Fact (verbatim):** "Eaton participates as a non-funded Tier-1 adviser on certification, industrialisation readiness and system safety"; WP diagram: "Eaton advising across all of them" (WP0–WP4).
- **(a) Proposal location:** Partner contributions (`/home/user/proposal/drafts/09_Partner_Contributions.md`), "Why Eaton is the right partner" — the verbatim quote is already embedded there; secondarily Vision "Impact and Beneficiaries" (handover S5b names Eaton [PI TO CONFIRM]).
- **(b) Usage mode:** quote verbatim, attributed to "the SkyDrive technical-approach documentation". Mandatory caveat wording (as already written in drafts/09): "That engagement concerns a **separate, higher-TRL** collaborative programme; it is cited here solely as evidence of an established working relationship … and **implies no commitment** to the present proposal." Eaton is stated non-funded — never imply funding; the EPSRC letter of support is a separate, unsecured item (handover checklist item 7, **[PI TO CONFIRM]**).
- **(c) Fragment:** "Eaton participates in the group's SkyDrive integrated-propulsion programme as a 'non-funded Tier-1 adviser on certification, industrialisation readiness and system safety', advising across all of that programme's work packages (SkyDrive technical-approach documentation). That engagement concerns a separate, higher-TRL programme and implies no commitment to the present proposal."

### ★ 3. Eaton's active support and standards roles (Q7, Q10 doc)

- **Fact (verbatim):** Eaton "actively supporting system architecture, certification strategy, and industrialisation planning" (Q7); Eaton participation in **SAE AE-7/AE-10** aerospace-electrification standards work (Q10 doc).
- **(a) Proposal location:** drafts/09 — Eaton narrative paragraph and letters-guidance item 3 "strategic fit" (feeds what the letter should say); Approach "Maximising translation" (standards route for outputs).
- **(b) Usage mode:** as depth-of-relationship and standards-pathway evidence only, same mandatory caveats: **separate higher-TRL programme**, **implies no commitment**, non-funded, letter **[PI TO CONFIRM]**; SAE roles are SkyDrive-document claims — **[PI TO CONFIRM] as another programme's claim** before naming committees in EPSRC text.
- **(c) Fragment:** "Eaton's engagement in the adjacent SkyDrive programme extends to certification strategy and industrialisation planning and to SAE AE-7/AE-10 standards activity [PI TO CONFIRM: stated in SkyDrive documentation], giving the proposed advisory role a standards route through which per-slot drive findings could inform emerging aerospace electrification practice — subject to Eaton's separate written confirmation for this proposal."

### ★ 4. Staged flight-validation and TRL 4–9 pathway (Q7 §1.2, Q12)

- **Fact:** four-phase deployment (Pegasus III jump take-off module → production ramp → Linx P9 primary propulsion → OEM replication); ARC's flight-representative Pegasus platform; ARC-confirmed willingness to support post-project TRL 7–9.
- **(a) Proposal location:** Approach "Maximising translation of outputs into outcomes and impact"; supports the settled Vision "Scope and Funding Rationale" hand-off sentence ("validated TRL-3 framework hands to Eaton and Airbus for follow-on Innovate UK or ATI development at TRL 4–6", handover S5b); drafts/09 letters-guidance item 4 (follow-on evaluation).
- **(b) Usage mode:** evidence that a concrete, staged TRL 4–9 route *exists* in the group's industrial orbit — not that this proposal's outputs are on it. Mandatory caveats: **separate higher-TRL programme**; the pathway and ARC's willingness are SkyDrive commitments to SkyDrive, **imply no commitment** here; platform names and dates **[PI TO CONFIRM] as another programme's claims** (note internal LINX P3 / Linx P9 inconsistency).
- **(c) Fragment:** "A staged route from bench validation to flight already operates around the applicant group: the separate SkyDrive programme progresses through ground rigs to flight-representative platform validation with ARC Aerosystems [PI TO CONFIRM: that programme's stated pathway]. This demonstrates the maturity of the translation environment awaiting this programme's TRL 1–3 outputs; it implies no commitment of that programme or its partners to the present proposal."

### ★ 5. Q13 risk themes — corroboration that the EPSRC problem set is industry-real

- **Fact:** SkyDrive's own register scores PD/insulation model uncertainty at 1 kV and reduced pressure (T1), inverter fault-ride-through at 1 kV (T3), rotor containment at 18 krpm (T15), SiC/GaN supply (T6/T7), interface freeze (T2/T30) — with L×I pre/post-control discipline.
- **(a) Proposal location:** Approach "Feasibility and risk management" (theme selection only — the agreed EPSRC risk table in handover S6 stands); optionally one clause in the Vision problem framing (PD at altitude as a live industrial concern).
- **(b) Usage mode:** themes only — evidence that PD at altitude, graceful fault degradation and thermal integration are what an active industrial programme worries about, so the TRL 1–3 research targets real constraints. Mandatory caveats: **separate higher-TRL programme**; no SkyDrive rows, scores or owners copied — EPSRC risks are research risks owned by the EPSRC team; any cited detail **[PI TO CONFIRM] as another programme's claim** and **implies no commitment**.
- **(c) Fragment:** "That partial discharge at altitude, fault-tolerant degradation and electronics-in-winding thermal management dominate the risk registers of active industrial propulsion programmes [PI TO CONFIRM: e.g. the separate ATI-funded SkyDrive programme] confirms that the constraints this programme removes at TRL 1–3 are the ones industry meets at TRL 3–6."

### 6. iNetic AS9100 facilities and dynamometer rig; ARC test environment (Q7 §1.5, Q12 caption, Q9 §9.6, Q13 T1)

- **(a) Proposal location:** Approach "Maximising translation" (downstream infrastructure); NOT "Research environment and facilities", which must describe facilities this programme will actually use.
- **(b) Usage mode:** partner-side infrastructure that *follow-on* (TRL 4–6) work could exploit — never facilities available to, or relied on by, this proposal; access **[PI TO CONFIRM]**; **separate higher-TRL programme**, **implies no commitment**; AS9100 status is a SkyDrive-document claim, **[PI TO CONFIRM] as another programme's claim**.
- **(c) Fragment:** "Downstream industrialisation infrastructure — iNetic's AS9100-certified manufacturing and dynamometer facilities and ARC's flight-representative test environment [PI TO CONFIRM: as described in SkyDrive documentation] — already exists within the group's industrial network for any follow-on TRL 4–6 programme; none is required by, or committed to, the present TRL 1–3 research."

### 7. Sector and policy framing figures (Q7 §1.1)

- **Facts:** 435M passengers by 2050; 38,000 aircraft / £4.65tn; £35bn sector; 120,000 jobs / 3,000 companies; ATI £1.37bn / £20bn; 1.5→3.5 kW/kg trajectory; Jet Zero / AGP alignment.
- **(a) Proposal location:** Vision "Timeliness" and "Impact and Beneficiaries" background only (handover S5b already carries its own [PI TO CONFIRM]-flagged figures — prefer those).
- **(b) Usage mode:** scene-setting at most, attributed as "figures stated in the ATI-funded SkyDrive documentation"; every one is **[PI TO CONFIRM] as another programme's claim** — mostly uncited in source, and the 1.5→3.5 kW/kg ATI provenance is independently unverified. Strongly prefer substituting ADS / ATI publications / DfT Jet Zero citations. **Separate higher-TRL programme**; use **implies no commitment**.
- **(c) Fragment:** "[PI TO CONFIRM — substitute an independently cited source before use: sector figures currently traceable only to another programme's (SkyDrive's) uncited claims.]"

### 8. SkyDrive commercial and benefits figures (Q7 §1.5, Q10 doc)

- **Facts:** unit prices, volumes, £268m/£200m revenue, ~1,220 jobs, tCO₂ abatement, £37m industrialisation, "£1 leverages ~£14", five PhDs, patent families.
- **(a) Proposal location:** none. **(b) Usage mode:** do not use — these are SkyDrive's benefit claims and would read as the applicants' own impact projections; if a reviewer-facing sentence ever needs them, full attribution + **[PI TO CONFIRM] as another programme's claim** + **separate higher-TRL programme** + **implies no commitment**. **(c) Fragment:** none provided deliberately.

### 9. Wider customer-pull names (Q7 §1.3: Boeing, Rolls-Royce Electrical, Ontic, Beyond Gravity, Vertical Aerospace)

- **(a) Proposal location:** none at present. **(b) Usage mode:** avoid — engagement is claimed by SkyDrive, unquantified, and naming these firms in EPSRC text would imply relationships this team has not evidenced; **implies no commitment**, **[PI TO CONFIRM]** in full if ever used. **(c) Fragment:** none.

### Traps — numbers and claims that must NEVER appear as EPSRC research targets

The EPSRC programme's own confirmed parameters (handover S3) are 270 V bus, 20–50 V per slot section, 6,000–10,000 RPM, 5–50 kW per-motor class, TRL 1–3. The following SkyDrive numbers must never migrate into EPSRC objectives, KPIs, milestones, specs or the Gantt — only into attributed context sentences per items 1–7:

- **100 kW** (continuous rating), and "modular toward megawatt class".
- **18,000 RPM** (and the 18 krpm rotor/containment context) — the EPSRC machine is 6,000–10,000 RPM.
- **1 kV** (and "1 kV class" operation at altitude) — the EPSRC platform context is 270 V DC.
- **All kW/kg power-density targets:** 13 kW/kg motor and 16 kW/kg system (Q9), >1.5 kW/kg system and >15 kW/kg active-material (Q12), the 1.5→3.5 kW/kg sector trajectory (Q7), and 2.0–2.5 kW/kg (Harbour Air comparison). Note Q9 vs Q12 are mutually inconsistent — never blend, never adopt.
- Supporting SkyDrive spec numbers: 95–98% / >97% efficiency, 25 A/mm², >3 GPa sleeves, torque-ripple/EMI/mass-percentage KPIs, TRL6 by ~2029, and all revenue/jobs/CO₂ forecasts.
- **UCL APL cannot be evidenced from here:** the UCL Advanced Propulsion Laboratory appears **nowhere** in these SkyDrive documents (§3.2), so they **cannot resolve the open dynamometer/facilities flag** (handover S6: "APL facility specifics with distinctive numbers" still needed from the PI). The only dynamometer mentioned is **iNetic's** rig. Caution: `drafts/09_Partner_Contributions.md` currently states Eaton participates in SkyDrive "at the UCL Advanced Propulsion Laboratory" — that location claim is not supported by any SkyDrive appendix and needs independent evidence or removal [PI TO CONFIRM].

**Blanket rule (unchanged):** every SkyDrive-derived number or claim in EPSRC text carries explicit attribution to SkyDrive and a **[PI TO CONFIRM]** flag until verified or substituted with an independent source.


<!-- ==================== FILE: evidence/11_open_end_winding_research.md ==================== -->

# Digest 11 — Open-End Winding (OEW) Machine Drives: Landscape, Challenges, and Positioning

> **Status:** Web-verified evidence base compiled 1 August 2026. Every factual claim below was cross-checked across at least two independent search results (IEEE Xplore metadata, IET Digital Library, publisher pages, Nottingham ePrints, secondary reviews). Items that could not be confirmed in two independent places are marked **NOT VERIFIED**. This digest exists because the proposed per-slot bilateral drive feeds every slot section from both conductor ends, and drives-expert reviewers will read that as an OEW-family idea; the proposal must show it knows this literature and can differentiate against it precisely.

---

## 1. The OEW landscape, accurately

**The core concept.** In a conventional drive the three stator phase windings are star- (or delta-) connected and fed from one end by a single inverter. In an open-end winding drive the star point is opened so that **both ends of every phase winding are accessible**, and a second inverter is connected at the formerly-neutral end. The two inverters apply voltage differentially across each winding; the winding voltage is the *difference* of the two inverter pole voltages. Two ordinary two-level inverters, each on a DC link of half the voltage a single-inverter drive would need, then synthesise across the winding a voltage waveform equivalent to that of a **three-level inverter**: the dual two-level OEW drive produces voltage space-vector locations identical to a conventional three-level NPC inverter, with 64 switching-state combinations distributed over 19 vector locations (versus 27 combinations in a three-level NPC), giving large switching-state redundancy. Higher-level bridges at each end compound multiplicatively (two three-level bridges give five-level-equivalent operation, etc.).

**Origins.** The canonical early reference is confirmed as **H. Stemmler and P. Guggenbach, "Configurations of high-power voltage source inverter drives," EPE'93 (5th European Conference on Power Electronics and Applications), Brighton, UK, September 1993** (commonly cited as vol. 5, pp. 7–14). Multiple independent sources, including a 2025 *Applied Sciences* review of dual two-level OEW configurations and the IET dual-inverter papers, attribute the first presentation of the dual-inverter OEW connection to this paper. The attribution in the task brief is therefore correct as stated. Note it is a pre-digital-era conference paper: no DOI exists, and the page/volume details circulate through secondary citation rather than a publisher record (details beyond title/venue/year: **NOT VERIFIED** at first hand).

**Major variants** (all confirmed across multiple sources):

1. **Isolated DC buses.** Each inverter has its own galvanically isolated supply (two rectifier-transformer secondaries, or two batteries). This breaks the zero-sequence current path entirely, at the cost of an isolation transformer or a second source. The classic high-power configuration, and the configuration used by Welchko for hybrid-vehicle energy management (Section 3).
2. **Common (single) DC bus.** Both inverters share one supply, eliminating the transformer, but creating a closed path for zero-sequence current through the windings (Section 2). Somasekhar, Gopakumar and Baiju's 2004 IEE Proceedings paper is the reference single-supply scheme with improved DC-bus utilisation; later work (e.g. the Nottingham "dual inverter without an isolation transformer" papers) attacks the same problem by modulation.
3. **Floating-capacitor (floating-bridge) second inverter.** Only the primary inverter has a DC source; the second inverter's DC link is a capacitor with no supply, charged and regulated (typically at half the main DC-link voltage) using the redundant switching states. The floating bridge supplies mainly reactive power, so it can (a) compensate the machine's reactive power so the main inverter operates near unity power factor and fully exploits its current rating, and (b) boost the effective machine terminal voltage, extending the constant-power speed range. Reference implementation: Chowdhury, Wheeler, Patel and Gerada, IEEE TIE 2016 (University of Nottingham PEMC group). Variants regulate the floating link at variable voltage ratios or combine it with overmodulation of the primary inverter.

**Recognised benefits** (each confirmed in at least two sources):
- **Multilevel-equivalent voltage from standard two-level modules**: three-level performance without NPC clamping diodes and, critically, **no neutral-point capacitor-balancing problem**, since there is no midpoint-tapped DC link.
- **Halved DC-link voltage per inverter** for a given machine voltage, or conversely near-doubled machine voltage from a fixed low-voltage source; this is the basis of the extended constant-power speed range claims in EV work.
- **Switching-state redundancy** (64 states/19 locations) exploitable for zero-sequence suppression, common-mode voltage elimination, floating-capacitor regulation, or loss balancing.
- **Fault tolerance / limp-home**: if one inverter fails, its terminals can be shorted (by its own devices or a crowbar) to re-form a star point, and the machine continues on the healthy inverter at reduced voltage. Fault-tolerant OEW topologies are an active literature of their own (e.g. Kedika et al., *Int. Trans. Electr. Energy Syst.*, 2021).
- **No neutral point in the machine**, and full independent access to each phase winding, enabling independent phase control and functions such as energy transfer between two sources through the machine.

---

## 2. The recognised challenges, with numbers where verifiable

1. **Zero-sequence / circulating current (common-bus configurations).** With a single DC supply, the two inverters plus the three windings form a closed loop for zero-sequence current, driven by the instantaneous common-mode (triplen-harmonic) voltage difference between the two inverters. The circulating current adds no torque, distorts the phase currents, and produces extra copper and device losses. Confirmed remedies: (a) galvanic isolation (transformer or separate sources); (b) SVPWM restricted to the switching-state combinations that generate no triplen voltage (the decoupled/zero-sequence-free SVPWM family, e.g. "A space-vector modulation scheme for a dual two-level inverter fed open-end winding induction motor drive for the elimination of zero-sequence currents"); (c) closed-loop suppression with resonant or predictive controllers. Every one of these either costs hardware (transformer), restricts the usable vector set (reducing the effective modulation range or the redundancy available for other purposes), or adds control complexity.
2. **Common-mode voltage.** Dual-inverter PWM generates common-mode voltage at the machine terminals exactly as single inverters do (bearing currents, EMI). The OEW redundancy allows complete elimination of alternating common-mode voltage by using only vector combinations of equal common-mode potential (Baiju, Mohapatra, Kanchan and Gopakumar, IEEE TPEL, vol. 19, no. 3, pp. 794–805, May 2004), but again by sacrificing part of the vector set; with isolated half-voltage supplies this scheme retains three-level-equivalent operation.
3. **Doubled converter infrastructure.** A dual two-level OEW drive uses **12 controlled switches, 12 gate drivers, and two DC links (or one link plus an isolation transformer, or one link plus a floating capacitor bank)** against 6 switches and one link for the standard drive. Each device is rated for half the voltage, so total installed silicon VA is comparable, but the gate-drive, isolation, sensing and protection infrastructure doubles, and both three-phase cable ends must be brought out of the machine (six machine leads instead of three). The more-electric-aircraft starter-generator literature explicitly counts this cost: reconnecting the three phases through a dual inverter "requires all phases to be opened between inverter legs, resulting in 12 IGBTs, which complicates the overall power electronic converter interface" (High-Power Machines and Starter-Generator Topologies for More Electric Aircraft: A Technology Outlook, 2020).
4. **Modulation and control complexity.** Coordinating two inverters (synchronisation, dead-time interaction across 64 states, vector-subset selection under the constraints of items 1 and 2, floating-capacitor charge regulation in variant 3) makes the modulator markedly more complex than a standard SVPWM, and the constraints interact: states reserved for capacitor regulation cannot simultaneously be reserved for zero-sequence elimination.

**Numbers worth quoting** (verified): 64 switching combinations over 19 space-vector locations; three-level-equivalent voltage from two two-level bridges at half DC-link voltage each; 12 switches and 12 gate drives versus 6; floating-capacitor link regulated at half the main DC-link voltage in the Nottingham TIE 2016 scheme. A frequently repeated claim that cascaded OEW operation raises high-speed power density of an induction machine by ~73% and IPM high-speed power by up to 300% appears in secondary summaries of the Welchko–Nagashima line of work but was not traceable to a verifiable primary source in this search: **NOT VERIFIED, do not use**.

---

## 3. OEW in aerospace and EV/traction applications

- **Hybrid/electric vehicles (General Motors line).** B. A. Welchko's IECON 2005 paper (GM Advanced Technology Center) proposes the "double-ended inverter system": two electrically isolated inverters, one per winding end, each fed from a different energy source, controlling simultaneously the motor power and the energy flow *between the two sources through the machine windings*, removing the DC/DC converter otherwise needed for the second source. Proposed control modes include unity-power-factor and optimum-inverter-utilisation control. GM also patented unified power control of double-ended inverter drives for hybrid vehicles (US 7,154,237 B2). This is the strongest evidence that OEW was seriously engineered for traction, not only studied academically.
- **EV wide-speed-range work.** Isolated-dual-inverter flux-weakening control (Kwak and Sul line) and switchable winding-mode OW-PMSM dual-inverter drives for EVs (e.g. *Energies*, vol. 10, no. 5, 616, 2017) target extended constant-power speed range from low battery voltage. A 2025 US patent (12,267,032, "Dual inverter open winding machine for vehicle with electric power takeoff") shows continuing industrial interest.
- **More-electric aircraft.** Y. Jia, U. R. Prasanna and K. Rajashekara, IECON 2014, propose an OEW induction generation system for frequency-insensitive AC loads in more-electric aircraft, using the dual-converter access to serve DC-link loads and AC loads simultaneously; a follow-up (IEEE IECAT/conference 2019, IEEE Xplore 8707679) adds simultaneous DC-link and AC load supply with voltage regulation. The Nottingham floating-bridge work (Chowdhury et al.) sits in a group whose stated application space is aerospace and transport drives. MEA starter-generator surveys discuss OEW-style dual-inverter reconnection for DC excitation in generator mode and count its 12-IGBT cost against it. Overall: aerospace OEW work exists but is sparse and subsystem-level; no flight-hardware OEW propulsion drive was found. That scarcity is usable context, not a gap the proposal claims to fill.

---

## 4. Verified reference candidates

1. **H. Stemmler and P. Guggenbach, "Configurations of high-power voltage source inverter drives," in *Proc. 5th Eur. Conf. Power Electronics and Applications (EPE'93)*, Brighton, U.K., Sep. 1993, vol. 5, pp. 7–14.** No DOI (pre-digital conference; volume/pages carried by secondary citation, **page numbers NOT VERIFIED at first hand**). Supports: the canonical origin of the dual-inverter OEW concept.
2. **V. T. Somasekhar, K. Gopakumar, and M. R. Baiju, "Dual two-level inverter scheme for an open-end winding induction motor drive with a single DC power supply and improved DC bus utilisation," *IEE Proc. Electr. Power Appl.*, vol. 151, no. 2, pp. 230–238, Mar. 2004, doi: 10.1049/ip-epa:20040023.** Supports: single-supply variant, three-level equivalence, 64-states/19-locations redundancy, DC-bus utilisation.
3. **M. R. Baiju, K. K. Mohapatra, R. S. Kanchan, and K. Gopakumar, "A dual two-level inverter scheme with common mode voltage elimination for an induction motor drive," *IEEE Trans. Power Electron.*, vol. 19, no. 3, pp. 794–805, May 2004, doi: 10.1109/TPEL.2004.826514.** Supports: common-mode voltage as a recognised OEW challenge and the redundancy-based elimination remedy.
4. **B. A. Welchko, "A double-ended inverter system for the combined propulsion and energy management functions in hybrid vehicles with energy storage," in *Proc. 31st Annu. Conf. IEEE Ind. Electron. Soc. (IECON 2005)*, Raleigh, NC, USA, Nov. 2005, pp. 1401–1406, doi: 10.1109/IECON.2005.1569110.** Supports: industrial traction application of OEW; energy transfer between isolated sources through the machine.
5. **S. Chowdhury, P. W. Wheeler, C. Patel, and C. Gerada, "A multilevel converter with a floating bridge for open-end winding motor drive applications," *IEEE Trans. Ind. Electron.*, vol. 63, no. 9, pp. 5366–5375, Sep. 2016, doi: 10.1109/TIE.2016.2561265.** Supports: floating-capacitor variant, reactive-power/boost function, half-DC-link capacitor regulation via redundant states.
6. **Y. Jia, U. R. Prasanna, and K. Rajashekara, "An open-end winding induction generation system for frequency insensitive AC loads in more electric aircraft," in *Proc. 40th Annu. Conf. IEEE Ind. Electron. Soc. (IECON 2014)*, Dallas, TX, USA, Oct.–Nov. 2014 (IEEE Xplore 7048533; DOI presumed 10.1109/IECON.2014.7048533, **DOI NOT VERIFIED**).** Supports: OEW in the more-electric-aircraft context.

*Secondary survey, useful for a single landscape citation if a recent review is wanted:* "Overview of Dual Two-Level Inverter Configurations for Open-End Winding Machines: Enhancing Power Quality and Efficiency," *Appl. Sci.*, vol. 15, no. 10, art. 5611, 2025, doi: 10.3390/app15105611 (author list **NOT VERIFIED** in this search; confirm before citing).

---

## 5. PROPOSAL USE MAP

**Vision, "Opening: stand beside the expert."** Acknowledge OEW as a known, thirty-year-old partition-era technique so the expert reviewer sees the landscape is understood before the new claim is made. Ready fragment (proposal register, UK English, no em dashes, no metaphor):
> "Opening both ends of the stator winding is itself a classical idea: since Stemmler and Guggenbach's 1993 dual-inverter configuration, open-end winding drives have used two standard inverters, one at each winding terminal, to synthesise multilevel voltage, improve DC-bus utilisation and provide a limp-home path. That literature, however, retains the fundamental partition: two lumped, machine-rated converters stand outside the machine, and cables still carry bus-scale switched voltage to the winding."

**Vision, "Crossing the line" (differentiation).** The load-bearing distinction, stated so a drives expert cannot mistake the proposal for an OEW rediscovery. Three verified axes: (i) *granularity*: OEW splits the converter in two; per-slot bilateral drive distributes it to every slot section, with one IC pair per slot; (ii) *voltage scale*: in OEW each winding still sees the difference of two bus-scale pole voltages, and each inverter still blocks half the full DC-link voltage, whereas per-slot drive confines each converter and each conductor section to slot-scale voltage; (iii) *infrastructure*: OEW's recognised costs (doubled gate-drive and isolation infrastructure, six machine leads, zero-sequence paths on a common bus, coordination of 64 switching states) are exactly the costs that grow unmanageably with further subdivision using discrete converters, which is the IC-necessity argument (evidence chain 2, Farhat digest 03) applied at the system level. Ready fragment:
> "Open-end winding drives cross half of the boundary: they reach the second terminal of the winding, but with another lumped, machine-rated inverter. The winding still experiences bus-scale voltage, the two converters still require full gate-drive and isolation infrastructures, and a common supply introduces a zero-sequence circulating path that must be suppressed by transformer isolation or by restricting the modulation set. The programme proposed here distributes both the converter and the voltage: every slot section is driven bilaterally by its own integrated converter pair at slot-scale voltage, with the supply distributed magnetically rather than by a shared switched bus, so the circulating-current path, the cable-borne dv/dt and the per-channel isolation infrastructure of the dual-inverter approach do not arise."
(Confirm against WP1/WP3 drafts that the "magnetic bus distribution" wording matches the proposal's own term for the DCAT-mode supply before reuse; the OEW contrast itself is fully supported by this digest.)

**Approach, WP1 (winding design context).** OEW legitimises open-ended conductors as sound machine-design practice (both ends brought out, no star point, per-phase independence, fault reconfiguration by re-forming the star point), so WP1 can cite it as precedent that opening the winding is electromagnetically benign, then state what per-slot sectioning adds beyond it. One line for WP1: "Open-end winding practice since 1993 establishes that machines operate correctly with both winding terminals driven; WP1 extends terminal access from the phase level to the slot-section level and co-designs the winding for slot-scale voltage rather than bus-scale insulation." Also reusable in WP1 risk discussion: the OEW fault-tolerance mechanism (short one end to re-form a star point) has a per-slot analogue worth one sentence in the fault-management task.

**Where NOT to use.** Do not claim OEW is obscure (it has a 2025 review journal literature); do not use the unverified 73%/300% power-density figures; do not cite the Stemmler page numbers as authoritative without first-hand confirmation; do not imply aerospace OEW is nonexistent, only that it remains subsystem-level and sparse.

---

*Compiled from: IET Digital Library (doi 10.1049/ip-epa:20040023, 10.1049/ip-epa:20020127), IEEE Xplore records 7463475, 1569110, 7048533, 8707679, 7104364, Nottingham ePrints/Worktribe (Chowdhury thesis and TIE paper), Scilit/Semantic Scholar records for TPEL 10.1109/TPEL.2004.826514, Taylor & Francis EPE Journal 10.1080/09398368.2002.11463495, MDPI Appl. Sci. 10.3390/app15105611, Google Patents US7154237B2, USPTO 12,267,032, and cross-checking ResearchGate metadata pages. All claims cross-checked in at least two of these; single-source items are marked NOT VERIFIED.*


<!-- ==================== FILE: evidence/12_gearbox_burden_research.md ==================== -->

# 12. Gearbox/Transmission Burden in Electric Drivetrains — Evidence Base

**Purpose.** Substantiate the Vision claims that the gearbox is (a) a concentrated mechanical failure mode treated exceptionally by airworthiness law, (b) a mass, loss, thermal and maintenance burden that does no electromagnetic work, and (c) being designed out by the eVTOL industry, which the software-defined pole count claim completes. Web-search based; page fetches blocked, so facts were cross-checked across independent results. Items the PI must verify against primary text are flagged.

---

## 1. Reliability evidence: airworthiness treatment and documented failures

### 1.1 The loss-of-lubrication requirement (the regulator's own verdict on gearboxes)

- **14 CFR (FAR) 29.927(c)(1)** — verified at ecfr.gov: for **Category A** rotorcraft, "unless such failures are extremely remote, it must be shown by test that any failure which results in loss of lubricant in any normal use lubrication system will not prevent continued safe operation, although not necessarily without damage, at a torque and rotational speed prescribed by the applicant for continued flight, **for at least 30 minutes** after perception by the flightcrew of the lubrication system failure or loss of lubricant." [PI TO CONFIRM exact current wording at ecfr.gov before quoting verbatim.]
- **CS-29 Amendment 7 (EASA, July 2019)**, following NPA 2017-07, **removed the "extremely remote" escape clause** and rewrote CS 29.927(c)(1) as an objective requirement: "Confidence shall be established that the rotor drive system has an in-flight operational endurance capability of at least 30 minutes following a failure of any one pressurised normal-use lubrication system." Search results consistently report the associated AMC sets a minimum demonstrated capability of **36 minutes (a 20% margin)** [PI TO CONFIRM against AMC 29.927(c) in Easy Access Rules for CS-29].
- Argument value: no other component of an electric drivetrain has a bespoke certification rule whose premise is "assume the lubricant is gone; prove the crew has half an hour to land". The rule exists because gearbox lubrication failure is a recognised catastrophic-failure pathway.

### 1.2 Mandated monitoring: chip detectors

- **14 CFR 29.1337(e)** (verified via eCFR/Cornell LII): rotor drive system transmissions and gearboxes utilising ferromagnetic materials **must be equipped with chip detectors** signalling the indicator required by 29.1305(a)(22), with an in-flight crew check of each detector circuit. A whole instrumentation subsystem exists solely to watch the gearbox shed metal.
- EASA opened rulemaking task **RMT.0725 / NPA 2021-01 (rotorcraft chip detection systems)** explicitly because in-service experience showed chip detection systems failing to indicate gearbox degradation even when particles had been present for some time before failure.

### 1.3 Documented transmission-failure accidents (as categories, not sensationalised)

- **G-REDL, AS332 L2 Super Puma, 1 April 2009, North Sea (AAIB Aircraft Accident Report 2/2011).** Catastrophic main rotor gearbox failure from **fatigue fracture of a second-stage planet gear in the epicyclic module**; main rotor separated in flight; 16 fatalities. A magnetic particle had been found on the epicyclic chip detector 36 flying hours before the accident but was not recognised as degradation of the gear that failed; the crew's first cockpit indication was a fall in gearbox oil pressure roughly 20 seconds before rotor separation. Demonstrates both the concentrated failure mode and the limits of the mandated monitoring.
- **LN-OJF, EC225 LP (H225), 29 April 2016, Turøy, Norway (Accident Investigation Board Norway, Report 2018/04).** **Fatigue fracture in one of the eight second-stage planet gears** of the main gearbox epicyclic module; crack initiated at a surface micro-pit and propagated subsurface, **undetected by any monitoring**, to catastrophic failure; main rotor detached without warning; 13 fatalities. The investigation also found the planet gears rarely reached their intended operational time limit before being scrapped at inspection (reported: no FAG-supplied second-stage planet gears reached the 4,400 h limit; only about 10% of the alternative supplier's did) [PI TO CONFIRM figures against NSIA Report 2018/04].
- **G-REDW (10 May 2012) and G-CHCN (22 October 2012), EC225 LP, North Sea ditchings (AAIB Report 2/2014).** Circumferential **fatigue cracking of the welded bevel-gear vertical shaft** that drives the main gearbox oil pumps caused loss of oil pressure in both events; after emergency-lubrication warnings the crews ditched. Controlled ditchings, no fatalities; valuable as a documented category: the **lubrication system itself is a single-point dependency** of the transmission.
- CS-29 Amendment 7 is widely reported as a direct regulatory response to this accident sequence (EASA "Rotorcraft gearbox loss of lubrication" material; Gear Solutions "Rotorcraft gearbox regulations: LOL").

### 1.4 Wind-turbine gearboxes: the industrial reliability analogue

- **NREL Gearbox Reliability Collaborative (GRC)**, launched 2007 specifically because fleet gearboxes were failing well short of design life; the **Gearbox Reliability Database (GRD)** (from 2009) categorises failure modes. Citable summary: S. Sheng, *Report on Wind Turbine Subsystem Reliability — A Survey of Various Databases*, NREL/PR-5000-59111 (2013): across surveyed databases, **gearboxes caused the longest downtime per failure of any turbine subsystem**.
- GRD damage distribution (2014 release, data.openei.org): gearbox failures are dominated by bearings rather than gear teeth; the **high-speed-shaft bearing accounts for about 48% of failures**, and planetary-bearing failures (about 6.6%) require gearbox removal by crane, driving extreme cost and downtime. [PI TO CONFIRM percentages against the OEDI dataset documentation.]
- **Carroll, McDonald and McMillan (2016)**, *Wind Energy* 19:1107-1119, doi:10.1002/we.1887: field failure-rate, repair-time and unscheduled O&M cost data for approximately 350 offshore turbines; gearbox major replacements are among the highest-cost, longest-duration corrective actions. Companion paper (Carroll et al. 2017, doi:10.1002/we.2011) compares O&M cost across drivetrain configurations including direct drive.
- The wind industry's response is instructive: **direct-drive generators were adopted at multi-megawatt scale specifically to remove the gearbox as a reliability and O&M liability** (Polinder et al. 2006, below).

---

## 2. Mass, losses, thermal and lubrication burden

### 2.1 Losses and the thermal chain they create

- **Per-mesh efficiency:** standard gear references give parallel-axis (spur/helical) gear meshes **98.0-99.5% efficiency per mesh**, i.e. roughly **0.5-2% of transmitted power lost per stage**, with ~1% per mesh a common engineering estimate (KHK gear technical reference; RoyMech gear efficiency tables). Losses compound multiplicatively across stages. [Use "approximately 0.5-1% per gear stage" with these secondary sources; NOT VERIFIED against a single archival aerospace paper.]
- **Aerospace-quality measurement:** Handschuh and Kilmain, *Efficiency of High-Speed Helical Gear Trains*, NASA/TM-2003-212222 (also DTIC ADA414211), tested an aerospace-quality helical gear train to 5,000 hp and 15,000 rpm, quantifying load- and speed-dependent losses and the thermal behaviour they drive.
- **System level:** NASA's drive-train technology summaries state complete helicopter transmissions are "typically above 95 percent" efficient across 300-3,000 hp (NASA NTRS 19840022225 and related overviews). Inverted: **several percent of megawatt-class shaft power becomes heat in the oil**, which is why the oil system exists.
- **The chain the loss buys:** because that heat must be removed and the meshes and bearings continuously lubricated, the gearbox carries pressurised oil pumps, oil coolers and blowers, filters, oil temperature and pressure sensing, chip detectors (regulatory, 29.1337(e)), emergency lubrication provisions (29.927 compliance), and scheduled oil sampling, inspection and overhaul. Each element is mass and maintenance that performs no electromagnetic work, and 1.3 above shows the lubrication system is itself a documented failure origin.

### 2.2 Mass share

- Widely cited figure (CompositesWorld, reporting on helicopter transmission technology): a helicopter's drive system (engine plus shafts plus geared transmission) is **10-15% of empty weight**. Drive-system design literature (e.g. Bellocchio, *Drive System Design Methodology for a Single Main Rotor Heavy Lift Helicopter*, Georgia Tech MSc thesis, 2005) treats the main gearbox as the dominant drive-system mass item. [PI TO CONFIRM a primary-source fraction; the 10-15% figure as found bundles the engine. Safer phrasing: "the transmission is one of the largest single mass items in a rotorcraft, with the drive system contributing of order ten percent of empty weight".]
- **Sizing driver:** gearbox mass scales with rated torque, not power; helicopter transmission design texts (NASA overview NTRS 19830011853; split-torque literature quoting 15% mass savings from load-path changes alone) confirm torque capacity is the sizing quantity. This is the citable basis for "sized by peak torque".
- eVTOL/geared-turbofan specific mass fractions: no published per-aircraft gearbox mass figures found for announced eVTOLs. NOT VERIFIED; avoid quantitative claims there.

---

## 3. The direct-drive trend in eVTOL/AAM

- **Joby Aviation (S4):** six **direct-drive** outer-rotor radial-flux motors. IEEE Spectrum ("Joby's Quiet, Direct-Drive Electric Motor Could Reshape Urban Flight") reports Joby **iterated through several generations of geared motors before abandoning the gearbox**, citing reliability, noise and maintenance; the direct-drive motor uses large diameter for torque density.
- **Beta Technologies:** motors are **direct-drive and air-cooled**, with the design philosophy stated publicly as "the least complexity, removing things that fail" (beta.team/motor; Aviation Week coverage). Beta supplies its direct-drive pusher motor to Eve Air Mobility, extending the pattern across developers.
- **Counterexample proving the trade is live:** Archer's Midnight uses motors at approximately 12,000 rpm through a **planetary gearbox** driving each propeller, accepting gearbox burden to keep motor torque (hence mass) down. This is exactly the torque-density versus mechanical-complexity trade the proposal's software-defined pole count dissolves: reconfigurable pole count lets one machine deliver high-pole high-torque behaviour at low speed without a fixed-ratio mechanical stage.
- **Trade-study literature:** Polinder, van der Pijl, de Vilder and Tavner, "Comparison of Direct-Drive and Geared Generator Concepts for Wind Turbines", *IEEE Trans. Energy Conversion* 21(3):725-733, 2006, doi:10.1109/TEC.2006.875476, is the canonical geared-versus-direct-drive electromechanical trade study (cost, mass, energy yield across five drivetrain concepts). For aerospace: NASA RVLT reference eVTOL designs explicitly assume a gearbox to decouple motor speed from rotor tip speed for noise (NASA Reference Motor Designs for eVTOL, AIAA 2021-3279, doi:10.2514/6.2021-3279), and NASA is developing **magnetic gearing** to eliminate contacting gear teeth (Asnani, NASA Glenn, NTRS 20180004692) — independent evidence that the mechanical gearbox is regarded as a liability worth an entire research programme to remove.

---

## 4. Verified reference candidates

1. **14 CFR 29.927 (FAR/CS-29), "Additional tests"** — 30-minute loss-of-lubrication endurance for Category A rotor drive systems; CS-29 Amdt 7 (2019) made the test effectively mandatory. ecfr.gov / EASA Easy Access Rules. VERIFIED (provision exists; quote wording to be checked by PI).
2. **AAIB Aircraft Accident Report 2/2011 (G-REDL, AS332 L2)** — main rotor separation from second-stage planet gear fatigue in the epicyclic module; 16 fatalities. VERIFIED (gov.uk/FAA mirrors).
3. **Accident Investigation Board Norway Report 2018/04 (LN-OJF, EC225 LP, Turøy)** — undetected subsurface planet-gear fatigue; main rotor detachment; 13 fatalities. VERIFIED (nsia.no).
4. **S. Sheng, *Report on Wind Turbine Subsystem Reliability — A Survey of Various Databases*, NREL/PR-5000-59111, 2013** — gearboxes caused the longest downtime per failure of any subsystem. VERIFIED (nrel.gov docs).
5. **J. Carroll, A. McDonald, D. McMillan, "Failure rate, repair time and unscheduled O&M cost analysis of offshore wind turbines", *Wind Energy* 19:1107-1119, 2016, doi:10.1002/we.1887.** VERIFIED.
6. **H. Polinder et al., "Comparison of Direct-Drive and Geared Generator Concepts for Wind Turbines", *IEEE Trans. Energy Conversion* 21(3):725-733, 2006, doi:10.1109/TEC.2006.875476.** VERIFIED.
   - Supporting: Handschuh and Kilmain, NASA/TM-2003-212222 (helical gear train efficiency, VERIFIED to exist); AAIB AAR 2/2014 (G-REDW/G-CHCN lubrication-shaft failures, VERIFIED); NASA AIAA 2021-3279 (RVLT motor designs, VERIFIED).

---

## 5. PROPOSAL USE MAP

| Fact | Lands in |
|---|---|
| 29.927 30-minute run-dry rule; CS-29 Amdt 7 tightening | Vision, "The unseen line" gearbox passage (the regulator already treats the gearbox as the exceptional failure mode) |
| G-REDL and LN-OJF planet-gear fatigue accidents; chip-detector limits (29.1337(e), RMT.0725) | Vision gearbox passage and risk framing ("concentrated mechanical failure mode", "inspection-scheduled") |
| G-REDW/G-CHCN oil-pump shaft failures | Risk framing: the lubrication system is itself a failure origin |
| NREL GRD/59111 + Carroll 2016 | Vision gearbox passage, industrial analogue sentence; also Impact (O&M cost logic) |
| Per-stage 0.5-1% loss; >95% overall transmission efficiency; oil system chain | "Mass that does no electromagnetic work" and thermal burden sentences |
| Drive system of order 10% of empty weight; torque-sized | "Sized by peak torque" claim |
| Joby and Beta direct drive; Archer geared counterexample; Polinder trade study; NASA magnetic gearing | "The cascade" gearbox-elimination claim and timeliness (industry is already paying to remove the gearbox; software pole count removes the reason it exists) |

### Ready-to-use fragments (UK English, no em dashes)

- **Vision, "The unseen line":** "Airworthiness law already singles the gearbox out: certification of large rotorcraft requires demonstration that the drive system survives at least 30 minutes after total loss of lubrication (CS-29/FAR 29.927), a requirement EASA tightened in 2019 after main gearbox planet-gear fatigue failures caused the loss of two North Sea helicopters with 29 lives (AAIB AAR 2/2011; AIBN Report 2018/04). No other drivetrain component carries a certification rule whose premise is its own lubrication failing in flight. [PI TO CONFIRM exact regulatory wording]"
- **Vision, burden sentence:** "Each gear stage dissipates of the order of 0.5 to 1% of transmitted power as heat in the oil, so the transmission arrives with pumps, coolers, filters, chip detectors and scheduled inspection as compulsory companions; mandated chip detection (FAR 29.1337(e)) monitors the gearbox precisely because its dominant failure modes begin as wear debris, yet in both fatal Super Puma accidents the monitoring did not prevent catastrophic planet-gear failure."
- **Industrial analogue:** "The same lesson has been paid for at industrial scale: across wind-turbine reliability databases the gearbox causes the longest downtime per failure of any subsystem (Sheng, NREL/PR-5000-59111; Carroll et al., Wind Energy 2016), and the industry's response was to remove it, with direct-drive architectures adopted at multi-megawatt scale (Polinder et al., IEEE Trans. Energy Conversion 2006)."
- **"The cascade", elimination claim:** "The leading eVTOL developers have reached the same conclusion where they can: Joby abandoned several generations of geared motors for direct drive, and Beta's flight motors are direct drive and air cooled, with the stated philosophy of removing things that fail. Where developers retain a gearbox, as Archer does, it is to buy torque density by spinning the motor faster. A machine whose pole count is a software parameter dissolves that trade: high-pole operation provides gear-like torque multiplication electromagnetically, with no oil, no meshes and no scheduled disassembly."
- **Risk framing:** "The gearbox is sized by peak torque rather than power, is wear limited, and concentrates the drivetrain's mechanical risk in a single oil-dependent assembly; eliminating it converts a concentrated mechanical failure mode into distributed, gracefully degrading electronics."

**Key caveats for the PI.** (1) The 36-minute AMC figure, the GRD percentages, the LN-OJF gear-life statistics and the 10-15% drive-system mass fraction were found in secondary reporting; confirm against primary documents before print. (2) The 10-15% figure includes the engine; do not attribute it to the gearbox alone. (3) Do not imply eVTOL accidents from gearbox failure; the rotorcraft accidents cited are conventional turbine helicopters.

**Primary source URLs.** [29.927 (eCFR)](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-29/subpart-E/subject-group-ECFRc74ea0c244f5fca/section-29.927) | [CS-29 Easy Access Rules](https://www.easa.europa.eu/en/document-library/easy-access-rules/online-publications/easy-access-rules-large-rotorcraft-cs-29) | [EASA NPA 2017-07](https://www.easa.europa.eu/en/document-library/notices-of-proposed-amendment/npa-2017-07) | [AAIB G-REDL AAR 2/2011 (FAA mirror)](https://www.faa.gov/sites/faa.gov/files/2023-04/2-2011_G-REDL.pdf) | [NSIA Report 2018/04](https://nsia.no/Aviation/Aviation/Published-reports/2018-04) | [AAIB AAR 2/2014 summary](https://www.gov.uk/aaib-reports/aar-2-2014-ec225-lp-super-puma-g-redw-and-g-chcn-10-may-2012) | [NREL 59111](https://docs.nrel.gov/docs/fy13osti/59111.pdf) | [GRD damage distribution (OEDI)](https://data.openei.org/submissions/467) | [Carroll 2016 doi:10.1002/we.1887](https://doi.org/10.1002/we.1887) | [Polinder 2006 doi:10.1109/TEC.2006.875476](https://doi.org/10.1109/TEC.2006.875476) | [Handschuh & Kilmain NASA/TM-2003-212222 (DTIC)](https://apps.dtic.mil/sti/tr/pdf/ADA414211.pdf) | [NASA drive-train summary](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19840022225.pdf) | [NASA eVTOL motor designs AIAA 2021-3279](https://arc.aiaa.org/doi/10.2514/6.2021-3279) | [NASA magnetic gearing](https://ntrs.nasa.gov/api/citations/20180004692/downloads/20180004692.pdf) | [Joby direct drive (IEEE Spectrum)](https://spectrum.ieee.org/joby-air-taxi-2676635230) | [Beta motor](https://beta.team/motor) | [29.1337 (Cornell LII)](https://www.law.cornell.edu/cfr/text/14/29.1337) | [EASA RMT.0725](https://easa.europa.eu/en/document-library/terms-of-reference-and-group-compositions/tor-rmt0725) | [CompositesWorld transmission mass](https://www.compositesworld.com/articles/new-aerocomposites-niche-helicopter-transmission-gears)


<!-- ==================== FILE: evidence/13_end_winding_research.md ==================== -->

# 13. End-Winding Loss, Cooling Burden and Axial Overhead: Evidence Base

**Purpose.** The proposal currently claims, without citation, that end-windings contribute 20-40% of winding resistance, extend axial length without producing torque, and are the least coolable part of the stator, and that terminating hairpin conductors at per-slot IC modules eliminates them structurally. This file assembles what the literature actually supports, flags what it does not, and supplies ready-to-use fragments. Research date: 1 August 2026. Proxy blocked full-text fetches; all claims are cross-checked across independent search results and marked NOT VERIFIED where full-text confirmation was not possible.

---

## 1. End-winding share of winding resistance and copper

**What is uncontested in the literature.** The end-winding (end-turn, overhang) region carries the full phase current through copper that links no useful flux: it adds DC resistance, copper mass, leakage inductance, axial length and cost while producing no torque. Patent and design literature states this plainly: the end-turn region "contributes to electrical losses, weight, cost, and volume but not to torque" (Ford Global Technologies patent family, e.g. US 11,228,216 and US 12,348,099).

**Published quantitative anchors.**

- **Geometric scaling law (textbook level).** Per coil, the in-slot length is twice the stack length L, while the end-turn length scales with coil span, i.e. with pole pitch tau_p = pi*D/(2p) for full-pitch distributed windings, multiplied by an empirical factor of roughly 1.2-1.8 to account for the three-dimensional overhang path. A design formula appearing in the induction-machine design literature gives one end-portion length as LE ≈ 0.8 * (pi*D/p) * (pi/2), and the total resistance as the sum of a stack-length term and an end-winding term 0.4*pi^2*D/p (design-textbook material, e.g. Pyrhonen, Jokinen and Hrabovcova, *Design of Rotating Electrical Machines*, Wiley; exact formula constants NOT VERIFIED against the book). The consequence is exact and citable in principle: the end-winding fraction of DC resistance rises directly with the ratio of pole pitch to stack length, so short axial (pancake) machines and low pole counts have the highest end-winding fractions.

- **Upper bound, industrial sources.** Multiple granted US patents on traction stators (Ford family, above) state that in short-stack machines, where radius greatly exceeds axial length, end-turns "can reach 50% of the total copper content". A Bosch-family stator patent (US 7,132,775) specifies a designed in-slot to total copper mass ratio of 0.43-0.55, i.e. an end-winding copper share of 45-57% for that machine class. These are industrial design documents, not peer-reviewed values, and should be cited as such or paraphrased.

- **Worked distributed-winding example.** For a 4-pole distributed winding with stack length equal to bore diameter (a common traction proportion), the scaling law above yields an end-winding share of total conductor length of roughly 30-45%; for an 8-pole machine of the same proportions roughly 15-25%. This is arithmetic from the geometric formula, not a published measurement, and should be presented in the proposal as an estimate to be quantified in WP1.

- **Concentrated windings.** Tooth-wound (fractional-slot concentrated) windings shorten the end-turn to roughly a tooth pitch, which is why El-Refaie's canonical review lists "short end turns" among the primary FSCW advantages (El-Refaie, IEEE Trans. Ind. Electron., 2010, ref R3 below). Published FSCW machines therefore sit at the low end, with end-winding copper fractions typically well below 20% (specific percentage NOT VERIFIED; the qualitative ranking distributed > hairpin distributed > FSCW is well supported).

- **Hairpin windings.** Hairpin (rectangular bar) windings shorten and regularise the overhang relative to random-wound stators but do not remove it: the crown and weld ends remain, and the welded end adds twist length. The Nottingham VPPC 2023 comparison (ref R5) found the hairpin stator 6.7% shorter in stack length and 8.3% smaller in outer diameter than the equivalent random-wound design at identical torque-speed rating. Berardi et al. (ref R6) attribute the hairpin efficiency gain mainly to reduced DC copper loss from higher slot fill, partially offset by higher AC loss.

**Verdict on the 20-40% figure.** Supportable as a stated range for the end-winding share of total winding copper length and DC resistance in conventional distributed and hairpin radial-flux machines of typical traction proportions, with two caveats. First, no single peer-reviewed source was found that states "20-40%" as a universal figure; the range is an honest synthesis of the geometric scaling law, industrial design documents (up to 50-57% for short stacks) and FSCW values below it. Second, the range is aspect-ratio and pole-count dependent: long two-pole machines fall below 20%, pancake machines exceed 40%. Recommended handling: keep 20-40% but anchor it as "typically 20-40% for machines of traction proportions, rising towards half the copper in short axial machines", cite the scaling argument plus refs R5/R6, and make its per-design quantification an explicit WP1/WP4 deliverable rather than an assumed input.

---

## 2. End-winding thermal problem

The claim that the end-winding is the winding hot-spot and the hardest region to cool is strongly supported and easily citable.

- **Hot-spot identification.** Madonna et al. (ref R2) open from the premise that end-windings are commonly identified as the machine hot-spot and that predicting and lowering end-winding temperature is a central task of machine thermal management; their solution is direct cooling applied to the end-windings specifically. Lumped-parameter thermal modelling literature (Mellor et al. 1991 TEFC model; Boglietti, Cavagnino and Staton 2005, ref R4) consistently treats the end-winding node as both the critical temperature and the hardest parameter to determine, because the end-winding sits outside the lamination stack: in-slot copper conducts heat radially through slot liner into iron and then to the cooling jacket, whereas end-winding copper hangs in the end-cap air space with only convection to enclosed air and a long conduction path back through the slot. Boglietti, Cavagnino and Staton (2005) show that even measuring the end-winding convection coefficient is problematic because the true wetted surface far exceeds the envelope area.

- **The mitigation literature as evidence of severity.** The size of the mitigation literature is itself the strongest evidence that the field recognises the problem:
  - *Potting and encapsulation.* High-conductivity potting of end-windings is a standard measure; a review of machine thermal management technologies (ref R7) reports a 100 kW PM machine where potting reduced end-winding temperature by 7 K, and Nottingham work on traction motor potting (Madonna et al., "Thermal and manufacturing aspects of traction motors potting", conference paper, details NOT VERIFIED) treats end-winding encapsulation as a manufacturing discipline in its own right. An extended end-winding cooling insert raised permissible continuous current density from 19.0 to 26.5 A/mm2 in one published study (reported in ref R2 context; original source NOT VERIFIED).
  - *Oil spray and jet cooling.* A dedicated experimental literature exists on spraying oil directly onto end-windings of EV machines: Wang et al. (ref R1) demonstrate large winding temperature reductions with end-winding oil spray; earlier Nottingham work demonstrated oil spray cooling on hairpin windings (Liang et al., IEEE Trans. Ind. Appl. / Ind. Electron., article 8848870, exact venue NOT VERIFIED); recent modelling reports around 25% hot-spot temperature reduction from oil spray on a specific application (MDPI Machines 2026, 14(1), 119). That the industry accepts the cost, sealing and drag penalties of flooding the end space with dielectric oil purely to reach the end-windings is direct evidence that this is the least coolable copper in the machine.
  - *End-region air management.* The convective end-region literature (Vukotic et al., ref R8; Micallef et al. and successors) exists precisely because end-winding convection is the dominant and least predictable heat path.

- **For the proposal.** The architecture's claim is well framed: removing the overhang does not merely delete a resistance, it deletes the copper that today forces spray cooling and potting, and leaves the winding terminations at the end-face where coolant access is easiest.

---

## 3. Axial length overhead

- End-windings extend the machine axially beyond the active stack at both ends. In traction machines the two overhangs together are commonly of the same order as a substantial fraction of the stack itself (tens of millimetres per end on stacks of 80-150 mm); precise published overhang-to-stack ratios are design specific and no universal figure should be quoted (specific per-machine teardown figures, e.g. ORNL teardown reports, NOT VERIFIED here).
- Hairpin versus stranded: the Nottingham VPPC 2023 study (ref R5) gives a concrete, citable pair of numbers: 6.7% shorter stack and 8.3% smaller outer diameter for the hairpin design at equal rating, driven by slot fill and a more compact, regular overhang. Industry development of X-pin and W-pin variants exists specifically to cut end-winding height further, confirming that overhang axial length is a live power-density constraint even within hairpin technology.
- The proposal's structural claim is stronger than any of these: termination of each hairpin at a per-slot IC module removes the crown and weld overhangs entirely, so the axial overhead reduces to the module and busbar thickness. No published machine does this; that is the point, and the comparison baseline (hairpin overhang height) should be measured and reported in WP4.

---

## 4. Fractional-slot concentrated windings: the field's existing partial answer

The machines community already has a partial answer to the end-winding problem: fractional-slot concentrated windings, which wind each coil around a single tooth and thereby cut the end-turn to roughly a tooth pitch. El-Refaie's review (ref R3) lists short end turns, high slot fill (especially with segmented stators), high power density and fault tolerance among FSCW advantages. The cost is well documented: the FSCW magnetomotive force is rich in sub- and higher-order space harmonics that do not rotate synchronously with the rotor, producing eddy-current losses in magnets and rotor iron, localised saturation, torque ripple, and noise and vibration; an extensive mitigation literature (multi-layer windings, stator shifting, harmonic-cancelling slot-pole combinations such as 24-slot/14-pole variants) exists to suppress these harmonics, at the price of complexity and partial loss of the end-turn advantage. The proposal should acknowledge FSCW as the existing structural response to end-winding overhead and position the per-slot architecture as removing the overhang without accepting the FSCW harmonic penalty, since the slot-level drive retains (indeed extends) control over the MMF spectrum.

---

## 5. Verified reference candidates

- **R1.** X. Wang, B. Li, K. Huang, Y. Yan, I. Stone, S. Worrall, "Experimental investigation on end winding thermal management with oil spray in electric vehicles", *Case Studies in Thermal Engineering*, vol. 35, 102082, 2022. DOI: 10.1016/j.csite.2022.102082. (Verified: venue, volume, article number, DOI.) Use for: oil spray on end-windings as recognised mitigation; end-winding as hot-spot premise.
- **R2.** V. Madonna, A. Walker, P. Giangrande, G. Serra, C. Gerada, M. Galea, "Improved thermal management and analysis for stator end-windings of electrical machines", *IEEE Transactions on Industrial Electronics*, vol. 66, no. 7, pp. 5057-5069, 2019. DOI: 10.1109/TIE.2018.2868288. (Verified: authors, venue, volume, issue, pages, DOI.) Use for: end-winding identified as machine hot-spot; direct end-winding cooling.
- **R3.** A. M. El-Refaie, "Fractional-slot concentrated-windings synchronous permanent magnet machines: opportunities and challenges", *IEEE Transactions on Industrial Electronics*, vol. 57, no. 1, pp. 107-121, 2010. DOI: 10.1109/TIE.2009.2030211 (volume/pages verified; DOI from standard records, NOT independently VERIFIED). Use for: FSCW short end turns and the FSCW trade-off paragraph.
- **R4.** A. Boglietti, A. Cavagnino, D. Staton, "Solving the more difficult aspects of electric motor thermal analysis in small and medium size industrial induction motors", *IEEE Transactions on Energy Conversion*, vol. 20, no. 3, 2005 (pages c. 620-628 and DOI NOT VERIFIED). Use for: end-winding convection as the hardest thermal parameter; end-winding outside the stack conduction path.
- **R5.** "Design of hairpin winding and random winding stators for high speed heavy-duty traction motor", *IEEE Vehicle Power and Propulsion Conference (VPPC)*, Milan, 2023, IEEE Xplore article 10403273 (University of Nottingham; author list NOT VERIFIED). Use for: hairpin vs random-wound axial length (6.7% shorter stack, 8.3% smaller OD at equal rating).
- **R6.** G. Berardi, S. Nategh, N. Bianchi, Y. Thioliere, "A comparison between random and hairpin winding in e-mobility applications", *IECON 2020, 46th Annual Conference of the IEEE Industrial Electronics Society*, Singapore, 2020, IEEE Xplore article 9255269 (DOI NOT VERIFIED). Use for: hairpin DC/AC copper loss trade-off.
- **R7.** "Advances in thermal management technologies of electrical machines", *Energies*, vol. 15, no. 9, 3249, 2022. DOI: 10.3390/en15093249 (verified DOI; author list NOT VERIFIED). Use for: potting/encapsulation of end-windings, 7 K end-winding reduction example, survey of cooling methods.
- **R8.** M. Vukotic et al., "Thermal effects in the end-winding region of electrical machines", *Energies*, vol. 16, no. 2, 930, 2023. DOI: 10.3390/en16020930 (verified venue, volume, article, DOI; author spelling NOT fully VERIFIED). Use for: end-region convection as the dominant, poorly predictable heat path.
- Industrial corroboration (cite sparingly or paraphrase, not peer reviewed): Ford Global Technologies patents US 11,228,216 / US 12,348,099 ("end-turns can reach 50% of the total copper content" in short-stack machines); Bosch-family patent US 7,132,775 (in-slot to total copper mass ratio 0.43-0.55).

---

## 6. PROPOSAL USE MAP

**Vision, "The unseen line", fourth constraint (end-windings).** Supported as written by R2/R4 (hot-spot, outside the stack) and by the geometric argument. Ready fragment:

> Fourth, end-windings: at both ends of the stator, copper leaves the slots to close the circuit, producing no torque yet carrying the full current. This overhang commonly holds 20 to 40 per cent of the winding copper in machines of traction proportions, approaching half in short axial machines, and it sits outside the lamination stack, where the conduction path to the coolant is poorest. It is the recognised hot-spot of the machine; an entire mitigation literature of end-winding potting and direct oil spray exists to manage it.

**"The cascade", end-winding-elimination claim.** Keep the 20-40% figure, but recast it as a copper and resistance share with its dependence stated, and keep the elimination claim structural. Ready fragment:

> Because every hairpin terminates at the module on the end-face, no conductor runs outside the active magnetic length. The end-winding overhang, typically 20 to 40 per cent of the winding copper and resistance in conventional machines of these proportions, is removed structurally rather than shortened, and with it the hottest, least coolable region of the stator. The terminations that remain sit exposed at the end-face, precisely where coolant access is easiest. Axial length shortens by the overhang height at both ends.

Flag for the drafter: do not write "winding resistance drops by 20-40%" as a measured fact anywhere a reviewer could read it as a literature value; write it as the structural upper bound to be quantified (see WP1/WP4 fragment). The literature supports the copper-share range; the exact resistance saving for the demonstrator geometry is a WP1 calculation.

**Approach, WP1 (design and modelling).** Add an explicit task: compute end-winding copper mass, DC and AC resistance share for the demonstrator geometry and a matched conventional hairpin baseline, as a function of pole count and stack aspect ratio. Ready fragment:

> WP1 quantifies the end-winding claim for the chosen geometry: copper mass, resistance and loss share of the overhang in a matched conventional hairpin baseline, computed across pole count and aspect ratio, establishing the machine-specific figure that the demonstrator must recover.

**Approach, WP4 (demonstrator).** Ready fragment:

> WP4 measures the recovered margin directly: phase resistance, axial length and end-region temperature of the per-slot demonstrator against the WP1 baseline, closing the loop on the end-winding elimination claim with measured rather than asserted percentages.

**FSCW acknowledgement (Vision or Approach, one paragraph).** Ready fragment:

> The field's existing answer to end-winding overhead is the fractional-slot concentrated winding, which shortens end-turns to a tooth pitch but pays for it in magnetomotive force space harmonics, magnet eddy-current loss, torque ripple and acoustic noise, and in a mitigation literature of its own. The architecture proposed here removes the overhang without that penalty: the winding remains free to realise a clean MMF spectrum because the harmonic content is set by per-slot electronic synthesis, not by coil geometry.

---

*Word count: c. 2,100. Sources consulted via web search 2026-08-01; page fetches blocked by proxy, so all "verified" markers refer to cross-checked search-result metadata, not full-text reads.*


<!-- ==================== FILE: evidence/14_per_slot_prior_art_research.md ==================== -->

# Evidence file 14 — Closest prior art to per-slot machine drives: ISCAD, smart stator tooth, and modular per-coil converter concepts

*Purpose: the Novelty section currently claims "no prior work has achieved per-slot bilateral IC drive in a rotating machine". Expert reviewers in electrical machines will know the stator-cage and per-coil converter literature. This file captures that literature accurately, states fairly what it achieved, and builds the airtight differentiation the Novelty passage and the Approach's "Building on previous work" section must carry. Sources were cross-checked across multiple independent web results; page fetches were blocked by the proxy, so every bibliographic detail not confirmed by at least two independent results carries a NOT VERIFIED marker.*

---

## 1. ISCAD — the Intelligent Stator Cage Drive (Dajaku, Gerling et al., Universitaet der Bundeswehr Muenchen / FEAAM, commercialised by Volabo GmbH, now Molabo GmbH)

**The concept.** ISCAD replaces the wound stator entirely: each stator slot carries a single solid aluminium bar rather than a multi-turn coil. All bars are short-circuited together at one axial end of the machine by a ring (exactly as in a rotor squirrel cage), and each bar is fed individually at the other axial end by a dedicated low-voltage half-bridge leg connected to a common 48 V DC bus. The machine is thus an N-phase induction machine (with a conventional squirrel-cage rotor) in which N equals the slot count, and the inverter is an N-leg low-voltage multiphase converter.

**Demonstrated hardware and headline numbers, as reported:**
- The canonical design is a **60-slot, 60-phase induction machine** with one aluminium bar per slot and one half-bridge per bar, on a **48 V** DC bus (below the 60 V DC extra-low-voltage safety limit), with design powers of **up to 240 kW** claimed feasible at that voltage.
- The half-bridge design paper (ICEMS 2016) describes a **60-phase inverter for up to 240 kW below 60 V**, one dedicated half-bridge per phase including driver circuitry, using paralleled low-voltage silicon MOSFETs. At 240 kW and 48 V the aggregate DC-side current is of the order of **5 kA**, i.e. per-bar currents in the hundreds of amperes range [NOT VERIFIED: exact per-bar RMS current figures; the kA-scale aggregate is arithmetic from the published power and voltage].
- The vehicle demonstration ("Vehicle Integration of ISCAD — 110 kW, 48 V Traction Drive") converted a Geely Emgrand EV to a third-generation **110 kW ISCAD prototype**, with reported power electronics of **42 half-bridge modules** based on low-voltage MOSFETs, phase taps connected directly to the aluminium bars. (Bar count differs between generations; the 60-bar figure is the design-study canon, 42 the reported vehicle build. Cite whichever paper is used, not a blended number.)
- Volabo/Molabo also demonstrated a **50 kW, 48 V marine drive** marketed with a "virtual gearbox" (electronic pole changing).

**Claimed benefits, which the proposal must concede accurately:**
1. **Extra-low-voltage safety**: the entire drive system sits below the 60 V DC touch-safe limit, removing HV safety measures, HV cabling and HV qualification (automotive context).
2. **High slot fill**: a solid bar fills the slot far better than a wound coil (reported fill factors around 90 percent versus roughly 45 percent for wound stators [NOT VERIFIED: exact figures, widely repeated in trade coverage]), plus rare-earth-free induction operation.
3. **Electronic pole changing**: because every bar current is independently controlled, the pole-pair number becomes a control variable; ISCAD publications explicitly claim arbitrary pole counts, soft cross-fading between pole numbers, and operation as "the first electrical gearbox". **This directly overlaps the proposal's variable-pole claim and must be cited, not omitted.**
4. **Fault tolerance / graceful degradation**: loss of one bar or half-bridge removes 1/N of the excitation, and the multiphase redundancy is claimed for functional safety (dedicated EVS28 control-strategies paper).
5. High-quality MMF from 60 independently fed bars (harmonic content controllable per slot).

**Limitations, as evidenced in the literature itself:**
- **The low voltage is supplied, not derived.** ISCAD requires the whole vehicle system, battery and DC distribution, to be 48 V. Nothing in ISCAD converts a high-voltage bus into safe winding sections; the safe voltage exists because the source is safe. The cost is kiloampere system currents, massive busbars, many paralleled MOSFETs per leg, and conduction-loss and cable-mass penalties that ISCAD's own half-bridge paper is devoted to managing.
- **Unilateral, short-circuited topology.** Bars are driven at one end only; the far end is a common short-circuit ring. There is no bilateral drive, no open-end winding section, and only half a degree of freedom per slot compared with an open-end section driven at both ends.
- **Discrete external power electronics.** The half-bridges are PCB modules with discrete MOSFETs and gate drivers at the machine end-face; there is no monolithic integration, and no IC technology is involved.
- **Hard-switched PWM**; no soft switching, no adiabatic operation, no magnetic voltage distribution; the "winding" (bars) plays no role in distributing the bus voltage.
- **Automotive 48 V motivation, not aerospace insulation physics.** The safety argument is electric shock below 60 V DC; partial discharge, altitude, Paschen behaviour and insulation ageing do not appear as design drivers.

**Key ISCAD publications (reference candidates, section 5 for formatted list):** EVS28 2015 concept paper; SAE 2016 journal paper (DOI verified); ICEMS 2015 analytical machine calculation; ICEMS 2016 half-bridge design; the 110 kW vehicle-integration paper; the 2019 Springer e+i overview.

## 2. Smart stator tooth and integrated modular motor drives (per-tooth / per-coil converter granularity)

**Smart Stator Tooth (SST), Brockerhoff (Infineon), Burkhardt (Siemens), Egger (ZF), Rauh (Fraunhofer IISB), PCIM Europe 2015.** Each stator tooth coil of an EV machine carries its own power electronics and control module, combined into one physical "smart tooth" unit; claimed benefits are packaging, weight, interface reduction, availability and safety. Granularity: **one converter module per tooth coil**, i.e. genuinely coil-level. What remains lumped: each module is fed from, and switches, the **full traction DC link**; the modules are discrete-device PCB assemblies, unilaterally connected, hard-switched, and the winding plays no voltage-distribution role. Related German work by the same group includes a highly integrated nine-phase drivetrain with a "disc inverter" at the machine end-face (EDPC 2016) [NOT VERIFIED: exact venue/pages].

**Integrated Modular Motor Drive (IMMD), University of Wisconsin (Jahns group).** Brown and Jahns (IAS 2007) defined the IMMD building block: a **segmented stator pole piece with a concentrated coil, fitted with a dedicated single-phase converter unit and controller**. Later Wisconsin work (Wang, Li and Han, IEEE TIA 2015, DOI verified) realised IMMD modules with low-voltage GaN FETs and, critically, proposed **connecting the inverter modules in series across the DC link so that each module sees only a fraction of the bus voltage**, precisely to enable low-voltage GaN devices. This is the closest prior art to the proposal's claim that no section sees the full bus, and it must be differentiated with care rather than ignored: the Wisconsin series stack divides the bus **capacitively across converter modules external to the winding**, per pole not per slot, unilaterally, with discrete devices, conventional PWM, module-voltage balancing as an acknowledged control burden, and with low-voltage device enablement (not insulation physics, not PD, not altitude) as the motivation. A Wisconsin follow-on line produced fault-tolerant IMMD prototypes; METU (Ugur and Keysan) built a GaN-based IMMD demonstrator and published an inverter-topology comparison for IMMD applications [NOT VERIFIED: exact citations]. The canonical IMD/IMMD reviews are Abebe et al. (IET EPA 2016, already verified in the References file) and Jahns and Sarlioglu (IEEE Power Electronics Magazine 2020, already verified).

**Per-phase modular fault-tolerant machines (Newcastle, Mecrow/Jack/Atkinson).** The aerospace fault-tolerant lineage drives each phase of a modular machine from its own H-bridge with electrical, magnetic, thermal and physical isolation between phases (e.g. the four-phase fuel-pump drive, and six-phase dual three-phase eVTOL descendants, one of which the proposal already cites as [9]). Granularity: **per phase**, with each H-bridge at full bus voltage. This community is the likely reviewer pool; the differentiation must speak its language.

## 3. Other slot-level, coil-level and bilateral converter proposals

- **Open-end winding dual-inverter drives** (Stemmler and Guggenbach, EPE 1993, and a large literature since): both ends of each phase winding are fed by separate inverters. This is the prior art for the word "bilateral", and it is **per phase, both inverters on the full DC bus** (or two isolated buses), with the machine winding unchanged. A recent hybrid exists: "A GaN-Based Integrated Modular Motor Drive for Open-Winding Permanent Magnet Synchronous Motor Application" (IEEE Xplore document 8734587, circa 2019 [NOT VERIFIED: authors, venue]) combines IMMD modularity with open-winding feed, still per phase, still full-bus modules.
- **Cascaded H-bridge and battery-integrated modular drives (MMSPC, Goetz et al., Duke/KIT)**: battery submodules dynamically rewired in series/parallel feed the machine terminals; voltage is subdivided across submodules, but the converter remains terminal-connected and the machine winding is untouched.
- **Slot-level patent art**: US 11,177,761 "Fault tolerant modular motor drive system" describes stator slots each occupied by a conductor supplied from separate three-phase inverters [NOT VERIFIED: assignee and claim scope; patent, not peer-reviewed]. Demonstrates the concept space is patented territory at slot granularity, unilaterally, with external inverters.
- **Continuously-variable-pole (CVP) drives** (Illinois, Krein/Banerjee group; already cited as [11], [12]): shared-bus modulation on an 18-leg discrete inverter, full bus at every terminal, two excitable harmonic orders.
- Searches for "per-slot inverter", "coil-level converter", "distributed inverter stator" and "modular stator drive" returned no work combining slot granularity with bilateral feed, monolithic integration, or winding-mediated voltage distribution. Absence of evidence is not proof, but the claim survives a determined search.

## 4. The differentiation, stated airtight

The honest headline: **slot-level converter granularity is not new (ISCAD), coil-level converter modules are not new (SST, IMMD), sub-bus module voltages are not new (Wisconsin series-stacked IMMD, CHB/MMSPC), bilateral feed is not new (open-end winding drives), and electronic pole changing is not new (ISCAD, CVP).** What is new is the specific combination and, more importantly, the mechanism: the winding itself is the voltage-distribution network, and the drive is a monolithic IC pair at every slot. No prior system has any of the five properties below; the proposal has all five from one architectural decision.

| Property | ISCAD | SST | IMMD (incl. GaN series-stack) | Open-end dual inverter | CHB / MMSPC | CVP | **This proposal** |
|---|---|---|---|---|---|---|---|
| Drive granularity | per slot (bar) | per tooth coil | per pole coil | per phase | per phase | per phase leg | **per slot section** |
| Feed topology | unilateral, far end short-circuited | unilateral | unilateral | bilateral, per phase | unilateral | unilateral | **bilateral, open-end, per slot** |
| Voltage each winding section sees | 48 V, but supplied by a 48 V system | full traction bus | bus/N across modules (capacitive stack outside winding) | full bus at both ends | submodule steps, full stack at terminal | full bus | **20 to 50 V of a 270 V bus, distributed magnetically by the winding** |
| Where the safe voltage comes from | external ELV source (whole system 48 V, kA currents) | nowhere (full bus) | series-connected converter modules, balancing required | nowhere | battery/capacitor submodules | nowhere | **the winding itself; system stays at 270 V, no kA distribution** |
| Power electronics realisation | discrete MOSFET PCBs | discrete-device module | discrete GaN PCBs | two discrete inverters | discrete submodules | discrete 18-leg inverter | **monolithic IC pair per slot** |
| Switching regime | hard-switched PWM | hard-switched | hard-switched PWM | PWM | PWM | PWM | **adiabatic ZVS** |
| Driving physics / motivation | automotive shock safety below 60 V, cost, rare-earth-free | packaging, redundancy | integration density, LV GaN enablement | DC-bus utilisation, multilevel effects | battery integration, efficiency | gearbox elimination | **PD elimination by design at altitude (Paschen physics)** |
| Pole changing | yes, electronic ("virtual gearbox") | no | no | no | no | yes, two harmonic orders | yes, arbitrary harmonic composition |

**The four load-bearing distinctions, in argument form:**

1. **Deriving versus supplying the safe voltage.** ISCAD achieves a sub-60 V winding by making the entire system extra-low-voltage, and pays in kiloampere currents, busbar mass and paralleled-device count; this trade is tolerable in a car and prohibitive on a 270 V aerospace bus. The Wisconsin series-stacked IMMD derives sub-bus module voltages, but capacitively, in converter hardware outside the machine, with balancing as an added control problem. The proposal is the only architecture in which the **machine winding magnetically distributes the bus**, so the system retains 270 V distribution currents while no winding section, device or slot ever stands off more than 20 to 50 V. This is a different mechanism from both, not a better version of either.
2. **Bilateral open-end per-slot drive.** Open-end drives are bilateral at phase level and full bus voltage; ISCAD is unilateral at slot level with a common short-circuit ring. Combining slot granularity with bilateral open-end feed gives 2N controllable degrees of freedom and removes the common ring as a fault-propagation and circulating-current path. No published system occupies this cell of the design space.
3. **Monolithic integration.** Every prior modular concept, ISCAD included, is built from discrete-device converter modules. The proposal places the complete per-slot drive (power stage, gate drive, level shifting, isolation, control interface) on a monolithic IC pair, already silicon-proven at battery-cell scale in the group's own work [1, 2]. Nobody has put an IC-integrated converter inside a stator slot environment; that is precisely the unstudied coupled physics the Scientific Contribution claims.
4. **PD elimination as the driving physics, with adiabatic ZVS as the enabling regime.** No prior slot- or coil-level concept engages Paschen physics, altitude derating or insulation ageing; ISCAD's safety claim is shock protection, which is adjacent but distinct (and should be acknowledged as adjacent). Adiabatic ZVS appears nowhere in this literature.

**What must be conceded, plainly:** ISCAD demonstrated slot-level individually controlled excitation and electronic pole changing in running vehicle hardware at 110 kW. Any Novelty wording implying that slot-level drive per se, or software-defined pole count per se, is unprecedented would be destroyed by a reviewer who knows ISCAD. The claim that survives is the conjunction: bilateral open-end per-slot drive, magnetically distributed bus voltage, monolithic integration, PD-elimination physics and adiabatic ZVS.

## 5. Verified reference candidates

1. G. Dajaku, F. Bachheibl, A. Patzak, and D. Gerling, "Intelligent Stator Cage Winding for Automotive Traction Electric Machines," in *Proc. 28th Int. Electric Vehicle Symp. (EVS28)*, Goyang (Kintex), Korea, May 2015. No DOI (symposium proceedings). VERIFIED (title, authors, venue via Semantic Scholar and proceedings copies).
2. A. Patzak, F. Bachheibl, A. Baumgardt, G. Dajaku, et al., "ISCAD — Electric High Performance Drive for Individual Mobility at Extra-Low Voltages," *SAE Int. J. Alternative Powertrains*, vol. 5, no. 1, pp. 148–156, 2016. DOI: 10.4271/2016-01-1179. VERIFIED (DOI, pages, volume from SAE Mobilus).
3. D. Gerling, G. Dajaku, F. Bachheibl, and A. Patzak, "Analytical calculation of the novel Stator Cage Machine," in *Proc. 18th Int. Conf. Electrical Machines and Systems (ICEMS)*, 2015, pp. 1346–1352. [NOT VERIFIED: DOI; author order.]
4. "Design of high current low voltage half-bridges for multi-phase inverter application in the ISCAD drive," in *Proc. 19th Int. Conf. Electrical Machines and Systems (ICEMS)*, Chiba, Japan, 2016. IEEE Xplore document 7837173. [NOT VERIFIED: author list; ICEMS 2016 papers carry no Crossref DOI.]
5. A. Patzak et al., "Vehicle Integration of ISCAD — 110 kW, 48 V Traction Drive," conference paper, circa 2018, available via TUM mediaTUM repository. [NOT VERIFIED: venue (likely EVS or VDE), year, author list — verify before citing; source of the 42-half-bridge, Geely Emgrand figures.]
6. F. Bachheibl, A. Patzak, and D. Gerling (with I. Kolb et al.), "ISCAD — nachhaltige Traktionsantriebe hoher Leistung bei 48 V," *e+i Elektrotechnik und Informationstechnik*, vol. 136, 2019. DOI: 10.1007/s00502-019-0713-0. VERIFIED (DOI via SpringerLink). German-language overview; cite the SAE paper in preference.
7. A. Patzak, F. Bachheibl, and D. Gerling, "48-V Traction Drive — High Power at Safe System Voltages," *ATZelectronics worldwide*, 2016. DOI: 10.1007/s38314-016-0050-6. VERIFIED DOI. Trade-journal register; prefer items 2 and 4 for the proposal.
8. P. Brockerhoff, Y. Burkhardt, K. Egger, and H. Rauh, "Smart Stator Tooth Design with novel Control and Safety Functions in Electric Vehicle Drivetrains," in *Proc. PCIM Europe*, Nuremberg, Germany, 2015, pp. 1–8. IEEE Xplore document 7149032 (VDE proceedings, no DOI). VERIFIED (authors, affiliations, venue).
9. N. R. Brown, T. M. Jahns, and R. D. Lorenz, "Power Converter Design for an Integrated Modular Motor Drive," in *Conf. Rec. IEEE Industry Applications Society Annual Meeting*, New Orleans, LA, USA, 2007, pp. 1322–1328. IEEE Xplore document 4347954. [NOT VERIFIED: exact DOI string (reported as 10.1109/IAS.2007.205 vs 10.1109/07IAS.2007.205) and whether Lorenz is a co-author — confirm on IEEE Xplore.]
10. J. Wang, Y. Li, and Y. Han, "Integrated Modular Motor Drive Design With GaN Power FETs," *IEEE Trans. Ind. Appl.*, vol. 51, no. 4, 2015. DOI: 10.1109/TIA.2015.2413380. VERIFIED (DOI via IEEE Xplore; series-connected module claim confirmed in abstract). [NOT VERIFIED: page range.]
11. H. Stemmler and P. Guggenbach, "Configurations of high-power voltage source inverter drives," in *Proc. 5th European Conf. Power Electronics and Applications (EPE)*, Brighton, UK, 1993, pp. 7–14. VERIFIED existence; [NOT VERIFIED: page range.]
12. Already in the References file, verified there: Abebe et al., IET EPA 2016 (DOI 10.1049/iet-epa.2015.0506); Jahns and Sarlioglu, IEEE PEM 2020 (DOI 10.1109/MPEL.2020.3011275); Chaubal et al. ITEC 2024 [11]; Libbos et al. TPEL 2022 [12].

Minimum set to add to `drafts/06_References.md`: items 2 and 4 (ISCAD concept plus its half-bridge hardware reality), item 8 (SST), and items 9 or 10 (IMMD; item 10 preferred because the series-stack must be differentiated and it is DOI-verified). Four new entries, roughly 90 words, within the stated References headroom.

## 6. PROPOSAL USE MAP

**A. Vision, Novelty and Scientific Contribution (`drafts/02_Vision.md`, line 39).** The sentence "no prior work has achieved per-slot bilateral IC drive in a rotating machine" is literally defensible but rhetorically exposed: a reviewer who knows ISCAD will read "per-slot ... drive" before reaching "bilateral IC" and conclude the authors do not know the field. The settled text is flagged verbatim-protected; if the PI permits one surgical edit, replace the second and third sentences of the paragraph with:

> *Architecturally, no prior work combines slot-level drive granularity with bilateral open-end excitation, monolithic integration and magnetic distribution of the bus voltage. The intelligent stator cage drive demonstrated slot-level excitation and electronic pole changing at vehicle scale, but by supplying the whole system at 48 V, with one discrete half-bridge per bar, the far ends short-circuited, and kiloampere distribution currents [ISCAD refs]. Modular and multilevel drives, including series-stacked integrated modules that hold each converter below the bus voltage [IMMD ref], subdivide the DC link in converter hardware; none distributes voltage through the winding itself, and none engages the per-slot insulation constraint that caps machine power density.*

If the verbatim rule wins, the differentiation must instead be carried entirely by the Approach (item B) and the ISCAD citations added there, since the Novelty paragraph's existing "Modular and multilevel drives subdivide the DC link..." sentence is the natural anchor and reads as covering ISCAD only to a reader who already agrees.

**B. Approach, "Building on previous work" (`drafts/03_Approach.md`, final paragraph of the section, "Two external bodies of work require explicit differentiation").** Change "Two external bodies" to "Three external bodies" and append:

> *Third, converter granularity at slot and coil level has been reached before, and this proposal builds on that lineage rather than repeating it. The intelligent stator cage drive [ISCAD refs] feeds each of 60 solid stator bars from a dedicated 48 V half-bridge and has demonstrated electronic pole changing in a 110 kW vehicle prototype; the smart stator tooth [SST ref] and integrated modular motor drives [IMMD refs] attach a converter module to each tooth coil or stator pole, and series-stacked modules have been used to hold each module below the bus voltage. All of these retain discrete converter hardware outside the winding, a unilateral feed, and hard-switched operation, and all obtain their module voltage either from an externally supplied extra-low-voltage system, at the cost of kiloampere currents, or from capacitive subdivision of the DC link with its attendant balancing burden. None derives safe per-section voltages from a 270 V bus through the winding itself, none integrates the complete per-slot drive monolithically, and none addresses partial discharge at altitude. The proposed architecture does all three, and the electronic pole changing that ISCAD and the continuously-variable-pole work pioneered emerges here as a corollary rather than the objective.*

**C. Vision, The Research Opportunity (line 35).** The variable-pole sentence cites only CVP prior art ([14,15] old, [11,12] new). Add the ISCAD SAE citation to that bracket so the pole-changing overlap is acknowledged at first mention: "...without the discrete switching transients of conventional variable-pole drives [11,12, ISCAD ref]."

**D. References (`drafts/06_References.md`).** Insert the four new entries at the tail (after [21] or after the IMD-review entry recommended in Residual check 3); update Map A and Map B accordingly. Note Residual check 3's recommended Abebe et al. IMD review also serves as the umbrella citation for item B's opening.

**E. Register guardrails.** Never describe ISCAD as a failure or a dead end; it is running hardware from a respected group and reviewers may include its authors' collaborators. The correct posture: ISCAD proved slot-level excitation and electronic pole changing are real and valuable, which strengthens the case that the remaining step, taken here, is worth funding. Avoid "merely", "only managed", "fails to". Use "supplies rather than derives", "retains", "does not address", "pioneered".

*Word count: approximately 2,600 (body sections 1 to 6).*


<!-- ==================== FILE: evidence/15_multiphase_research.md ==================== -->

# 15 — Multiphase Machine Drives: Evidence Base

**Purpose.** The proposal (Vision draft `drafts/02_Vision_ArcRevision.md`, "Third, multiphase redundancy, stated honestly") acknowledges multiphase machines as the field's existing fault-tolerance answer and prices them: redundancy bought by duplicating inverter channels, gate drives, isolated supplies, sensing and protection; power density diluted; winding still at full bus voltage; pole count fixed. That passage currently rests on reasoning plus the group's own dual three-phase paper [9]/[Ref 12]. This file supplies the canonical literature. All items verified by cross-checked web search (2026-08-01) unless marked NOT VERIFIED; page fetches were proxy-blocked, so quotations are paraphrases keyed to abstracts and secondary confirmations, flagged where the PI should sight the PDF before quoting verbatim.

---

## 1. The canonical reviews

**R1. E. Levi, "Multiphase electric machines for variable-speed applications," IEEE Trans. Industrial Electronics, vol. 55, no. 5, pp. 1893–1909, May 2008. DOI: 10.1109/TIE.2008.918488.** The single most-cited survey of the field (several thousand citations). Confirmed against IEEE Xplore record 4454446, Scholars Portal and SCIRP reference listings.

**R2. E. Levi, R. Bojoi, F. Profumo, H. A. Toliyat and S. Williamson, "Multiphase induction motor drives – a technology status review," IET Electric Power Applications, vol. 1, no. 4, pp. 489–516, 2007. DOI: 10.1049/iet-epa:20060342.** The companion IET status review; open PDF hosted by the IET itself. Broader on converter topologies (including five-phase two-level and multilevel supply combinations) than R1.

**R3. E. Levi, "Advances in converter control and innovative exploitation of additional degrees of freedom for multiphase machines," IEEE Trans. Industrial Electronics, vol. 63, no. 1, pp. 433–448, Jan. 2016. DOI: 10.1109/TIE.2015.2434999.** The 2016 follow-up. Confirmed via LJMU research repository (eprint 2767) and IEEE listing. Part of a TIE special section whose guest editorial, **E. Levi, F. Barrero and M. J. Duran, "Multiphase machines and drives – revisited," IEEE Trans. Ind. Electron., vol. 63, no. 1, pp. 429–432, 2016, DOI: 10.1109/TIE.2015.2493510** (open PDF at LJMU eprint 2769), is a compact citable statement of state of the art circa 2016.

**R4. F. Barrero and M. J. Duran, "Recent advances in the design, modeling, and control of multiphase machines — Part I," IEEE TIE, vol. 63, no. 1, pp. 449–458, 2016, DOI: 10.1109/TIE.2015.2447733; M. J. Duran and F. Barrero, "— Part II," pp. 459–468, DOI: 10.1109/TIE.2015.2448211.** Part II contains the survey treatment of fault-tolerant (post-fault) control, which is the natural citation for "the softening" the proposal describes.

**Fault-tolerant machine line (Newcastle school):**

**R5. B. C. Mecrow, A. G. Jack, J. A. Haylock and J. Coles, "Fault-tolerant permanent magnet machine drives," IEE Proc. Electric Power Applications, vol. 143, no. 6, pp. 437–442, 1996. DOI: 10.1049/ip-epa:19960796.** The founding paper of the fault-tolerant PM machine line: fault tolerance via a modular drive in which each phase is electrically, magnetically, thermally and physically independent (wording from the IET Digital Library abstract). Follow-ons in the same journal: aerospace fuel-pump demonstrator (DOI: 10.1049/ip-epa:19982164) and sensorless operation (DOI: 10.1049/ip-epa:20030153). Note the honest-pricing angle: independence per phase is achieved precisely by giving every phase its own single-phase converter bridge, i.e. maximal channel duplication.

**R6. W. Cao, B. C. Mecrow, G. J. Atkinson, J. W. Bennett and D. J. Atkinson, "Overview of electric motor technologies used for more electric aircraft (MEA)," IEEE Trans. Ind. Electron., vol. 59, no. 9, pp. 3523–3531, 2012. DOI: 10.1109/TIE.2011.2165453.** The standard aerospace-facing survey of candidate machines and drive topologies for safety-critical use.

**R7. A. G. Yepes, O. Lopez, I. Gonzalez-Prieto, M. J. Duran and J. Doval-Gandoy, "A comprehensive survey on fault tolerance in multiphase AC drives, Part 1: general overview considering multiple fault types," Machines, vol. 10, no. 3, art. 208, 2022, DOI: 10.3390/machines10030208; and "Part 2: phase and switch open-circuit faults," art. 221, DOI: 10.3390/machines10030221.** The most recent dedicated fault-tolerance survey; open access (MDPI). Part 1's framing sentence (from the abstract): multiphase drives offer enhanced fault tolerance versus three-phase because phase redundancy lets them continue running with faults in certain phases.

---

## 2. What multiphase demonstrably buys

- **Continued rotating-field operation after an open phase, without extra hardware.** A three-phase star-connected machine with one phase open cannot sustain a controllable rotating MMF and must stop unless hardware is added (neutral connection to the DC-link midpoint, or a spare leg). Any machine with n ≥ 5 (or n = 4 with neutral) keeps a controllable field with one phase out. This is the core claim of R1/R4-Part II/R7 and is safe to state without qualification.
- **Reduced per-phase power.** Total power splits across n inverter legs, so each leg carries roughly 3/n of the three-phase per-leg current at the same voltage; this, not fault tolerance, was the original high-power motivation (ship propulsion). Standard statement in R1 and R2.
- **Torque-ripple and DC-link benefits.** Lowest torque-pulsation harmonic order rises with phase number; DC-link current harmonics and capacitor requirement fall. R1, R2; also A. Salem and M. Narimani, "A review on multiphase drives for automotive traction applications," IEEE Trans. Transportation Electrification, 2019 (see item 5), which additionally credits six-phase with reduced DC-bus capacitor sizing.

**Canonical post-fault derating numbers (one phase open, healthy-phase current kept at rated peak):**

- **Three-phase baseline:** no ride-through in the standard star-connected two-level drive; with one inverter switch failed open, a comparative study puts the three-phase machine at about 33% of average rated torque (pulsating, with hardware assistance) against **80% for a five-phase machine** (Energies, vol. 9, no. 5, art. 355, 2016, DOI: 10.3390/en9050355). Use as a secondary, not headline, number.
- **Five-phase, one open phase: roughly 70–71% of rated torque** while keeping the remaining four currents balanced at rated magnitude; a 2024 Scientific Reports comparative study gives 70.85% as the minimum-derating figure with stator-current balance (DOI: 10.1038/s41598-024-76257-5). Equivalently, holding rated torque requires about 1.4 per-unit current in the healthy phases, i.e. a thermal, not stability, limit. Cross-checked against fault-tolerant five-phase control papers (e.g. Guzman et al. line, R4-Part II references).
- **Asymmetrical six-phase (dual three-phase, 30 deg), one open phase:** H. S. Che, M. J. Duran, E. Levi, M. Jones, W.-P. Hew and N. A. Rahim, "Postfault operation of an asymmetrical six-phase induction machine with single and two isolated neutral points," IEEE Trans. Power Electronics, vol. 29, no. 10, pp. 5406–5416, Oct. 2014 (IEEE Xplore 6676799; DOI: 10.1109/TPEL.2013.2293195 — PI to sight-check DOI digits on the PDF). Key verified finding: the neutral arrangement changes what is recoverable; with a **single neutral** the machine can reach substantially higher post-fault torque than with **two isolated neutrals** (follow-on studies quote up to ~54% more torque for single-neutral than two-neutral operation, and maximum-torque-mode derating factors of order 65–70% of rated; secondary sources: Kamel et al., ResearchGate 341849516; AIP Conf. Proc. 2173, 020016, 2019, for the symmetrical six-phase analogue, 69.4% in maximum-torque mode). The systematic comparison across symmetrical/asymmetrical and neutral arrangements is **A. M. S. Munim, M. J. Duran, H. S. Che, M. Bermudez, I. Gonzalez-Prieto and N. A. Rahim, "A unified analysis of the fault tolerance capability in six-phase induction motor drives," IEEE TPEL, vol. 32, no. 10, pp. 7824–7836, 2017, DOI: 10.1109/TPEL.2016.2632118.** For the proposal, the safe citable sentence is: achievable post-fault torque depends on phase number AND neutral arrangement, with reported single-open-phase figures of roughly 70% (five-phase) and 65–70% (six-phase, favourable neutral arrangement) of rated torque at rated current. Exact per-mode table values: mark any specific decimal beyond the above NOT VERIFIED until the PI opens Che 2014 / Munim 2017.
- **Dual three-phase, module-level strategy:** disabling the faulted three-phase set leaves **50% torque by construction** (half the legs carry the load); this is the standard industrial fallback and the reason finer-grained post-fault current control (Che 2014) is studied at all. Nine-phase triple three-phase, losing one set: 2/3 by the same arithmetic; phase-level nine-phase ride-through is demonstrated in "Fault-tolerant operation of a nine-phase induction machine with open phases" (IEEE conf., Xplore 8101830, 2017).

---

## 3. What it demonstrably costs

- **Leg count and everything that scales with it.** An n-phase two-level VSI has n legs against 3: n half-bridges, n gate-drive channels with isolated supplies, n phase-current sensors, n sets of desat/overcurrent protection, and (for dual three-phase with independent neutrals) duplicated DC-link connections and contactors. This is arithmetic, not literature, and can be asserted directly. The reviews say it in words: R1 and R2 list, among the reasons multiphase remained a niche, the larger number of inverter legs, the more involved PWM and control, and the fact that off-the-shelf converters and controllers are three-phase (paraphrase; PI to lift the exact sentence from R1 Section I or R2 Section 8 before quoting). The 2016 editorial R3-editorial makes the same point about control complexity growing with the extra degrees of freedom.
- **Control and modelling complexity.** Extra orthogonal subspaces (x-y planes) must be actively controlled or they circulate loss-making currents; post-fault operation requires reconfigured current references and reduced modulation range (R4 Part II; R7 Part 2).
- **Mass/volume comparison of complete three-phase vs multiphase drive systems: NOT VERIFIED.** No published like-for-like mass or volume audit of a complete three-phase versus six/nine-phase drive (machine + converter + gate drives + sensing + protection) at equal power and equal fault specification was found in the searches. Nearest neighbours: S. Sirimanna et al., "Comparison of electrified aircraft propulsion drive systems with different electric motor topologies," J. Propulsion and Power, vol. 37, no. 5, pp. 733–747, 2021, DOI: 10.2514/1.B38195 (1.5 MW propulsor Pareto study including power electronics and fault-response equipment, but across machine types, not phase counts); and "System weight comparison of electric machine topologies for electric aircraft propulsion," IEEE conf. 2018, Xplore 8552785 (machines only). **What CAN be claimed from leg-count arithmetic:** silicon area and conduction loss to first order follow total VA and are roughly phase-count neutral, but gate drives, isolated supplies, sensors, protection channels, controller I/O and connectorisation scale linearly with n while the per-leg voltage rating is unchanged; and partial offsets exist (smaller DC-link capacitor, thinner cables: Salem & Narimani 2019). So the honest claim is "channel-count overhead grows linearly with phase number at unchanged voltage rating", not a specific kg or litre figure.

---

## 4. What it does not address (the proposal's two differentiators)

- **Per-winding voltage stress.** In an n-phase machine fed from a two-level VSI, every phase is switched between the same DC rails; increasing n divides the current, not the voltage. The reviews frame the per-phase power reduction explicitly as splitting power across more legs so lower-current devices can be used (R1, R2); when the literature wants lower voltage stress it reaches for a different lever entirely, the multilevel converter, and the multiphase reviews treat multiphase-plus-multilevel as a combination precisely because the phase count alone does nothing for voltage (R2's five-phase multilevel material; Salem & Narimani's multiphase traction inverter coverage; "Design considerations of multi-phase multilevel inverters for high-power density traction drives," IEEE conf. 2022, Xplore 9813937). No source found claims any per-winding voltage reduction from phase count. Safe to state: multiphase redundancy leaves the full bus voltage across each winding's insulation system.
- **Pole count.** A wound multiphase machine has its pole count fixed at design time exactly as a three-phase one does. The only literature exception is the dedicated **pole-phase modulation / electronic pole-changing** line, which uses a high phase count (typically nine) plus an independent-leg inverter to re-map the winding between, e.g., 4-pole/9-phase and 12-pole/3-phase operation: "Nine-phase induction machine with electric pole change for emerging heavy-duty and off-road micro/mild hybrid vehicle applications," IEEE conf. 2017, Xplore 8101711; "The limits of pole changing operation of a nine-phase induction motor," IEEE conf., Xplore 11061073; lineage back to pole-phase modulation modelling (ResearchGate 300412720). This is induction-machine work with its own penalties (magnetising current rises steeply with pole number) and is not a property of the mainstream multiphase PM fault-tolerance literature. So the proposal's claim stands with one clause: conventional multiphase machines leave the pole count fixed; the exception is a dedicated pole-phase-modulation research line, which the proposal can cite as proving the rule.

---

## 5. Verified reference candidates (for drafts/06_References.md)

1. **E. Levi, "Multiphase electric machines for variable-speed applications," IEEE Trans. Ind. Electron., vol. 55, no. 5, pp. 1893–1909, 2008. DOI: 10.1109/TIE.2008.918488.** (Canonical review; benefits and costs in one citation.)
2. **E. Levi, "Advances in converter control and innovative exploitation of additional degrees of freedom for multiphase machines," IEEE Trans. Ind. Electron., vol. 63, no. 1, pp. 433–448, 2016. DOI: 10.1109/TIE.2015.2434999.** (State of the art a decade on; pair with Barrero/Duran Parts I–II, DOIs 10.1109/TIE.2015.2447733 and 10.1109/TIE.2015.2448211, if two slots are available.)
3. **B. C. Mecrow, A. G. Jack, J. A. Haylock and J. Coles, "Fault-tolerant permanent magnet machine drives," IEE Proc. Electr. Power Appl., vol. 143, no. 6, pp. 437–442, 1996. DOI: 10.1049/ip-epa:19960796.** (Origin of per-phase-independence fault tolerance; makes the duplication cost visible.)
4. **H. S. Che, M. J. Duran, E. Levi, M. Jones, W.-P. Hew and N. A. Rahim, "Postfault operation of an asymmetrical six-phase induction machine with single and two isolated neutral points," IEEE Trans. Power Electron., vol. 29, no. 10, pp. 5406–5416, 2014.** (The derating-versus-neutral-arrangement evidence; PI to confirm DOI string from PDF.)
5. **A. G. Yepes, O. Lopez, I. Gonzalez-Prieto, M. J. Duran and J. Doval-Gandoy, "A comprehensive survey on fault tolerance in multiphase AC drives," Machines, vol. 10, no. 3, arts. 208 and 221, 2022. DOIs: 10.3390/machines10030208, 10.3390/machines10030221.** (Recent, open access, dedicated to exactly the fault-tolerance claim.)

Reserve: Cao et al. 2012 (DOI: 10.1109/TIE.2011.2165453) if an aerospace-survey anchor is wanted alongside the group's own eVTOL paper [9].

---

## 6. PROPOSAL USE MAP

| Proposal location | Fact from this file | Reference |
|---|---|---|
| Vision "Opening" (acknowledging multiphase progress) | Multiphase is a mature, reviewed field with demonstrated post-fault ride-through | R1 (Levi 2008), R3 (Levi 2016) |
| Vision "The unseen line", third constraint (multiphase priced honestly) | Leg-count overhead scales linearly at unchanged voltage rating; reviews themselves list converter and control overhead as the reason multiphase stayed niche | R1, R3-editorial, Yepes 2022 |
| "The cascade": fault tolerance without duplication | Derating comparison: five-phase ~70% after one open phase; six-phase 65–70% only with favourable neutral arrangement; dual three-phase fallback 50%; all bought with n gate-drive/sensing/protection channels | Che 2014, Munim 2017, Yepes 2022 |
| Differentiator 1 (voltage) | Phase count divides current, not voltage; winding insulation still sees full bus; literature adds multilevel converters when voltage is the problem | R1, R2, Salem & Narimani 2019 |
| Differentiator 2 (pole count) | Pole count fixed except the dedicated nine-phase pole-phase-modulation line (induction machines, own penalties) | Xplore 8101711, 11061073 |
| Reference list [9] context | Group's dual three-phase eVTOL paper sits inside the R5/R6 Newcastle-to-aerospace lineage | R5, R6 |

**Ready-to-use fragments (UK English, no em dashes):**

- "Multiphase machines are the field's established answer to the loss of a phase: a five-phase machine can sustain roughly 70 per cent of rated torque with one phase open, and a six-phase machine 65 to 70 per cent under a favourable neutral arrangement, against zero for a conventional three-phase drive [Levi 2008; Che et al. 2014]."
- "That capability is bought in hardware: every added phase brings its own inverter leg, gate drive, isolated supply, current sensor and protection channel, and the reviews themselves identify this converter and control overhead as the reason multiphase drives remained confined to niche applications [Levi 2008; Yepes et al. 2022]."
- "The added phases divide the current, not the voltage: each winding is still switched across the full DC bus, which is why the literature reaches for multilevel converters, a separate lever, whenever voltage stress is the binding constraint [Levi et al. 2007; Salem and Narimani 2019]."
- "Nor does the phase count free the pole count, which remains fixed at design time; the exception, electronic pole-phase modulation in nine-phase induction machines, proves the rule by requiring a dedicated winding, an independent-leg inverter and a steep magnetising-current penalty."
- "Where the dual three-phase practice falls back to the healthy winding set and accepts 50 per cent torque, finer-grained post-fault current control recovers more only by pushing the remaining phases towards their thermal limits [Che et al. 2014; Munim et al. 2017]."

**Caveats for the PI.** (1) Sight-check the Che 2014 DOI digits and lift exact derating table values before quoting decimals. (2) The 70.85% five-phase figure traces to a 2024 Scientific Reports study; for reviewer-proofing, prefer "roughly 70 per cent" anchored to Che/Munim-style analysis. (3) No published mass/volume audit of three-phase versus multiphase complete drives was found; keep the density-dilution claim as channel-count arithmetic, which no reviewer can dispute, rather than a sourced kg figure.


<!-- ==================== FILE: evidence/16_aero_environment_research.md ==================== -->

# 16. Aerospace electrical environment and certification context

Research digest supporting three proposal claims: (1) the 270 V DC demonstrator bus choice, (2) the certification framing around graceful degradation and fault tolerance, and (3) the per-motor power class attributed to advanced air mobility (AAM). All web sources cross-checked across at least two independent results; page fetches blocked by proxy, so standards text could not be read verbatim. Items requiring verbatim confirmation are flagged [PI TO CONFIRM].

---

## 1. The 270 V DC bus: why it is an aerospace-relevant choice

**MIL-STD-704F (US DoD, "Aircraft Electric Power Characteristics").** Revision F was issued in March 2004 and remains the current revision, with Change 1 dated 5 December 2016. The standard defines the electrical power interface between military aircraft and utilisation equipment (voltage, frequency, ripple, transients, abnormal and emergency conditions) and includes 270 V DC as a standardised nominal DC bus voltage alongside 28 V DC and 115 V AC. The companion handbook series MIL-HDBK-704-1 to -704-8 gives compliance test procedures; MIL-HDBK-704-7 specifically covers demonstration of utilisation-equipment compliance for 270 V DC power. [PI TO CONFIRM the exact clause numbering for 270 V DC steady-state limits, typically 250 to 280 V normal steady state, from the standard text.]

**Military platforms in service.** The F-35 Lightning II uses 270 V DC as its primary electrical power, generated by an engine-driven starter/generator, feeding high-power loads including the electro-hydrostatic actuators that replace centralised hydraulics; 28 V DC and 115 V AC are retained for avionics and legacy loads. The F-22 Raptor similarly uses 270 V DC distribution. Ground support infrastructure for the F-35 (depot and flight-line power carts) is specified at 270 V DC, which is independent commercial evidence that the bus standard is real and operational, not a paper figure.

**Civil more-electric aircraft.** The Boeing 787, the emblematic more-electric airliner, uses a hybrid voltage architecture of 235 V AC (variable frequency), 115 V AC, 28 V DC, +/-130 V DC and +/-270 V DC. Auto-transformer rectifier units (ATRUs) convert the 235 V AC generator output to +/-270 V DC, which drives the largest loads (cabin pressurisation compressor motors, environmental control) via motor drives. The +/-270 V DC bus is therefore 540 V pole-to-pole, but each rail is at 270 V to structure, which is the insulation-relevant quantity for partial discharge.

**Why 270 V is defensible for a demonstrator.** Three converging arguments, all sourced:
1. It is the standardised military DC bus (MIL-STD-704F) and the rail voltage of the flagship civil MEA platform (787 +/-270 V DC), so results transfer directly to both domains.
2. 270 V DC arises naturally from rectified 115/200 V AC three-phase power (approximately 1.35 x 200 V line-to-line), which is why the aerospace community converged on it; a demonstrator at this voltage inherits realistic converter topologies and insulation stress levels.
3. For eVTOL, announced battery bus voltages cluster in the 400 to 900 V class (e.g. Lilium selected an 800 to 900 V class distribution; automotive-derived 400 V packs elsewhere), so 270 V sits at the conservative end of the emerging AAM range while remaining the only DC bus level with a mature airworthiness standard behind it. [PI TO CONFIRM specific eVTOL bus voltages if cited; company figures are less stable than the standards.]

**Altitude and partial discharge relevance.** RTCA DO-160 (current revision G; revision H work has been ongoing at RTCA SC-135 [NOT VERIFIED whether H is published]) is the environmental qualification standard for airborne equipment. Section 4 (Temperature and Altitude) requires operation at chamber pressures corresponding to the equipment category's maximum operating altitude, with unpressurised categories tested to 21,300 m (70,000 ft) and decompression/overpressure cases. Reduced pressure lowers the Paschen-curve breakdown voltage of air gaps, so partial discharge inception voltages fall with altitude; a 270 V DC bus that is PD-benign at sea level may not be at altitude. This is the standards hook for any PD/insulation-integrity content in the proposal: DO-160 Section 4 defines the altitude environment the converter must survive, even though DO-160 itself does not prescribe PD test methods [accurate statement; PD-specific aerospace test guidance is emerging through IEC 60034-27 adjacent work and SAE committees, NOT VERIFIED for citation].

---

## 2. Certification and failure philosophy: what can honestly be claimed

**EASA SC-VTOL-01, "Special Condition for small-category VTOL aircraft", issued 2 July 2019** (with subsequent Means of Compliance issues: MOC SC-VTOL Issue 1 in 2020, Issue 2 published 12 May 2021, and further MOC batches thereafter). Applies to passenger-carrying VTOL aircraft up to 9 seats and 3,175 kg MTOW with distributed lift/thrust. It defines two certification categories:
- **Category Basic**: controlled emergency landing capability after failures (analogous to CS-23 forced-landing philosophy).
- **Category Enhanced**: required for commercial air transport of passengers over congested areas; the aircraft must be capable of **continued safe flight and landing (CSFL)** after failure, proceeding to the original destination or a suitable alternate vertiport.

Key requirement for our purposes: under VTOL.2510 (equipment, systems and installations) and the associated MOC, **no single failure, including of a lift/thrust unit, may prevent continued safe flight and landing** (Enhanced category), and catastrophic failure conditions must be shown to be extremely improbable, with the quantitative safety target for the most severe classifications set at the 10^-9 per flight hour level for Enhanced category commercial operations (10^-7 associated with lower-severity combinations) [PI TO CONFIRM the exact per-category probability allocations from SC-VTOL-01 and MOC VTOL.2510 before quoting numbers]. NASA and Vertical Flight Society analyses of SC-VTOL-01 single-failure criteria confirm this is read as a design driver for distributed propulsion redundancy.

**UK relevance.** The UK CAA has adopted SC-VTOL as the basis for eVTOL type certification in the UK and published its eVTOL Delivery Model (2025) targeting commercial operations by 2028, with Vertical Aerospace (Bristol) engaged in all CAA eVTOL working groups. The UK CAA also consulted on its own MOC to SC-VTOL. This lets the proposal cite a UK regulatory pathway, not only an EASA one.

**Propulsion-level special conditions.** EASA SC E-19 "Electric / Hybrid Propulsion System" (Issue 1, 7 April 2021) provides certification requirements for electric and hybrid propulsion systems (EHPS) for manned and unmanned aircraft, filling the gap left by CS-E, which predates electric propulsion. EASA SC E-18 covers electric propulsion units for CS-23 aeroplanes up to Level 1. The UK CAA has published its own Special Condition on Electric/Hybrid Propulsion Systems (Issue 01) mirroring SC E-19. SC E-19's development explicitly addresses failure-condition classification and hazard analysis for EHPS during normal and emergency operations.

**What can accurately be said about graceful degradation.** No standard mandates "gradual degradation" verbatim, and the proposal must not claim so. The accurate chain is:
1. SC-VTOL Category Enhanced requires continued safe flight and landing after lift/thrust unit failures; single failures must not be catastrophic (VTOL.2510, MOC fail-safe design concept).
2. Compliance therefore rewards architectures whose failure modes are **partial, bounded and predictable**: a propulsion drive that loses a fraction of capability in a known way is far easier to cover in the system safety assessment (failure-condition classification under SC E-19 / ARP4761-type analysis) than one whose single component failure removes the whole unit.
3. Hence a converter architecture with inherent post-fault operation (e.g. surviving device or submodule failure with graceful output derating) directly supports the CSFL demonstration and can reduce the redundancy that must be added around the drive.
This is a defensible engineering argument grounded in cited requirements, not an overclaim about standards text.

---

## 3. Per-motor power classes of announced eVTOL/AAM aircraft

Verified or best-available figures (peak values where stated; company figures are marketing-grade and should be cited with dates):

| Aircraft | Motors | Per-motor power | Basis |
|---|---|---|---|
| Joby S4 (USA) | 6 | ~236 kW peak | ~1,416 kW combined peak reported; widely repeated figure [company/press, NOT company-primary VERIFIED] |
| Archer Midnight (USA) | 12 | 120-125 kW peak | Archer motor unveil, Nov 2022 (AIN coverage): 120 kW, ~25 kg per motor |
| Lilium Jet (Germany; company insolvent 2024, figures still indicative) | 30 (later 36 in some configs) | ~100 kW | Denso/Honeywell e-motor: 100 kW output, <4 kg rotor+stator |
| Vertical Aerospace VX4 (UK) | 8 | ~175 kW average (1.4 MW peak total) | Vertical press material, 2024 prototype: 1.4 MW peak across 8 EPUs |
| Beta ALIA (USA) | 5 (4 lift + 1 pusher, VTOL variant) | ~100 kW class average (≈500 kW combined reported) | evtol.news / press [NOT VERIFIED per-motor split; H500A pusher motor rating unconfirmed] |
| Wisk Generation 6 (USA/Boeing) | 12 (6 tilting + 6 fixed lift) | not published; 120 kWh pack, 4-seat class implies tens-of-kW to ~100 kW per motor | Wisk press 2022 [per-motor NOT VERIFIED] |
| Volocopter VoloCity (Germany) | 18 | ~13-25 kW class | 18 rotors, small per-rotor power; one database cites 13 kW peak per motor [NOT VERIFIED against company data] |
| EHang EH216-S (China; type-certified CAAC 2023) | 16 | ~10 kW average | ~160 kW total propulsion reported across 16 rotors [secondary sources] |

**Honest assessment of the "5-50 kW per-motor class" claim.** It is **not supportable as a general description of passenger eVTOL**. The vectored-thrust passenger aircraft closest to service (Joby, Archer, Vertical, Lilium) sit at **100 to 240 kW per motor**. The 5-50 kW class is real but belongs to: multicopter wingless designs (EHang ~10 kW/rotor, Volocopter ~13-25 kW/rotor), cargo and logistics UAS, sub-scale demonstrators, and the individual lift units of highly distributed designs. A reviewer with aerospace background would catch the error immediately, particularly given the UK flagship (VX4) averages ~175 kW per propulsion unit.

**Recommended replacement wording** (see use map below): describe the sector as spanning "roughly 10 kW per rotor in multicopter and uncrewed designs to low hundreds of kW per propulsion unit in winged passenger eVTOLs", and position the 5-15 kW demonstrator as the scalable per-module/per-submodule building block and as directly representative of the uncrewed and distributed-lift end, rather than claiming the whole sector operates at 5-50 kW per motor.

---

## 4. Verified reference candidates

1. **MIL-STD-704F w/Change 1**, "Aircraft Electric Power Characteristics", US DoD, 12 March 2004; Change 1, 5 Dec 2016. VERIFIED (revision and 270 V DC content) via everyspec.com and IEEE-hosted copy. Cite as: MIL-STD-704F.
2. **MIL-HDBK-704-7**, test procedures for 270 V DC utilisation equipment compliance. VERIFIED existence.
3. **Boeing 787 electrical architecture** (+/-270 V DC via ATRU from 235 V AC): Boeing "787 No-Bleed Systems" AERO Magazine QTR_4.07 (Sinnett, M., "787 No-Bleed Systems: Saving Fuel and Enhancing Operational Efficiencies") is the canonical primary source [PI TO CONFIRM exact article]; corroborated by Boeing 787 systems presentations and multiple secondary sources. VERIFIED (voltages).
4. **EASA SC-VTOL-01**, "Special Condition for small-category VTOL aircraft", Issue 1, 2 July 2019. VERIFIED (designation, date, Basic/Enhanced categories, CSFL). Plus **MOC SC-VTOL Issue 2**, 12 May 2021, and **MOC VTOL.2510** fail-safe criteria. VERIFIED existence; clause text NOT read verbatim.
5. **EASA SC E-19**, "Electric / Hybrid Propulsion System", Issue 1, 7 April 2021. VERIFIED. **EASA SC E-18** (electric propulsion units for CS-23 up to Level 1). VERIFIED existence. **UK CAA Special Condition Electric/Hybrid Propulsion System Issue 01** (via CAA consultation). VERIFIED existence.
6. **RTCA DO-160G**, "Environmental Conditions and Test Procedures for Airborne Equipment", Section 4 (Temperature and Altitude; categories to 70,000 ft / 21,300 m). VERIFIED (section scope); PD-specific claims must be argued from physics, not from DO-160 text.
7. **UK CAA eVTOL Delivery Model** (published Sept 2025; commercial eVTOL operations targeted by 2028; SC-VTOL reaffirmed as certification basis). VERIFIED via CAA newsroom and multiple press reports.
8. **Aircraft per-motor figures**: Archer motor specification (120 kW, ~25 kg; AIN, 18 Nov 2022) VERIFIED-secondary. Lilium/Denso 100 kW motor (Electric Motor Engineering; Lilium technology blog) VERIFIED-secondary. Vertical VX4 1.4 MW peak / 8 EPUs (Vertical Aerospace press PDF, July 2024) VERIFIED-secondary. Joby ~1,416 kW / 6 motors: repeated secondary figure, NOT VERIFIED against a Joby primary document. EHang ~160 kW / 16 rotors: secondary databases, NOT VERIFIED primary. Volocopter and Wisk per-motor: NOT VERIFIED.
9. **F-35/F-22 270 V DC primary power**: Military & Aerospace Electronics reporting on 270 V DC ground-power procurement for F-35; ITW GSE / FCX 270 V DC GSE product lines. VERIFIED-secondary; adequate for a "fielded on F-22/F-35" statement.

---

## 5. PROPOSAL USE MAP

**(a) Approach WP4 and Vision "Crossing" (270 V justification).** Insert:
> "The demonstrator targets a 270 V DC bus, the nominal DC distribution voltage standardised for military aircraft in MIL-STD-704F and fielded as primary power on the F-35, and the rail-to-structure voltage of the Boeing 787's +/-270 V DC more-electric architecture. Results at 270 V therefore transfer directly to both the established military standard and the civil more-electric aircraft baseline, while sitting within the DC voltage range now emerging in advanced air mobility platforms."
[PI TO CONFIRM MIL-STD-704F clause reference for 270 V DC steady-state limits.]

**(b) "The cascade" fault-tolerance passage (certification framing).** Replace any "certification requires gradual degradation" phrasing with:
> "EASA's Special Condition SC-VTOL (2019), adopted by the UK CAA as the certification basis for eVTOL, requires in its Enhanced category that the aircraft remain capable of continued safe flight and landing after failures, including failure of a lift or thrust unit, and that no single failure be catastrophic. Compliance therefore favours propulsion electronics whose failure modes are partial, bounded and predictable: a converter that continues operating at reduced rating after an internal device failure directly supports the continued-safe-flight case, whereas an architecture that fails cleanly but completely forces that burden onto aircraft-level redundancy. EASA's SC E-19 (2021) extends this failure-condition-driven approach to the electric propulsion system itself."
[PI TO CONFIRM VTOL.2510 wording and SC E-19 clause numbers before verbatim quotation.]

**(c) "Timeliness" (corrected power-class wording).** Replace "scaling toward the 5-50 kW per-motor class" with:
> "Announced advanced air mobility aircraft span roughly 10 kW per rotor in multicopter and uncrewed designs (EHang EH216-S, Volocopter VoloCity) to low hundreds of kW per propulsion unit in winged passenger eVTOLs (Archer Midnight, 12 x 120 kW; Vertical Aerospace's Bristol-built VX4, 1.4 MW peak across eight units; Joby S4, six motors of roughly 236 kW). The 5-15 kW demonstrator is therefore representative of the uncrewed and distributed-lift end of this range and, as the per-module building block of a modular architecture, provides the scalable foundation for the higher per-unit powers of passenger platforms."

**(d) DO-160/altitude hook (if PD or insulation appears in WP text).**
> "Airborne equipment qualification under RTCA DO-160G Section 4 requires operation at reduced pressure corresponding to the equipment's altitude category; since partial discharge inception voltage falls with pressure, insulation margins demonstrated at sea level do not carry to altitude, and the 270 V DC bus must be evaluated under representative pressure."

**(e) UK relevance (Timeliness or National Importance).**
> "The UK CAA's eVTOL Delivery Model (2025) targets commercial eVTOL operations by 2028 with SC-VTOL as the certification basis, and the UK's flagship developer, Vertical Aerospace, is progressing the VX4 toward certification on that timeline."

---

### Source URLs (for the reference file)
- MIL-STD-704F: https://everyspec.com/MIL-STD/MIL-STD-0700-0799/MIL-STD-704F_1083/ ; https://www.ieee.li/pdf/standards-handbooks/MIL-STD-704F.pdf ; https://en.wikipedia.org/wiki/MIL-STD-704
- 787 electrical: http://787updates.newairplane.com/787-Electrical-Systems/787-electrical-system ; https://user.eng.umd.edu/~austin/ense622.d/lecture-resources/Boeing787-MoreElectricAircraft.pdf
- F-35 270 V DC: https://www.militaryaerospace.com/rf-analog/article/16716121/air-force-asks-industry-for-270-volt-dc-power-converters-for-use-in-f-35-depot-maintenance
- SC-VTOL-01: https://www.easa.europa.eu/sites/default/files/dfu/SC-VTOL-01.pdf ; https://www.easa.europa.eu/en/special-condition-vtol-aircraft-july-2019 ; MOC Issue 2: https://www.easa.europa.eu/sites/default/files/dfu/moc_sc_vtol_issue_2_12-may-2021_shaded_0.pdf ; NASA single-failure analysis: https://ntrs.nasa.gov/api/citations/20220005985/downloads/20220422a%20Propulsion_Committee-Single_Failures_06.pdf
- SC E-19: https://www.easa.europa.eu/sites/default/files/dfu/sc_e-19_issue_1_electric_hybrid_propulsion_system_-_2021-04-07.pdf ; SC E-18: https://www.easa.europa.eu/en/document-library/product-certification-consultations/electric-propulsion-units-cs-23-normal-utility ; UK CAA SC: https://consultations.caa.co.uk/airworthiness-policy-team/part-21-aircraft-airworthiness-special-conditions/user_uploads/08_uk-special-condition---electric-hybrid-propulsion-system---issue-01.pdf
- DO-160 Section 4: https://keystonecompliance.com/rtcado-160/temperature-altitude/
- UK CAA eVTOL Delivery Model: https://www.caa.co.uk/newsroom/news/new-safety-insights-to-guide-future-evtol-regulation-published/ ; https://www.aerospacetestinginternational.com/news/uk-caa-publishes-framework-for-evtol-operations-by-2028.html
- Aircraft figures: Archer https://backend.ainonline.com/news-article/2022-11-18/archer-details-motor-and-battery-design-midnight-evtol-air-taxi ; Lilium https://www.electricmotorengineering.com/evtol-electric-motors-for-the-lilium-jet/ ; Vertical https://vertical-aerospace.com/wp-content/uploads/2024/07/Vertical-Aerospace-Unveils-Advanced-VX4-Prototype.pdf ; Joby https://evtol.news/joby-aviation-s4-production-prototype ; EHang https://evtol.news/ehang-216/ ; Wisk https://wisk.aero/newsroom/generation6
