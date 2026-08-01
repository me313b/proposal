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

## A6. Proposal mapping

- **Building on previous work:** direct lineage evidence — this preprint is the thesis-derived record that the team's BTMLC IC (a) exists in silicon, (b) stacks at board level to ~50 V/6 A per string with 98.5% peak efficiency, and (c) is explicitly positioned for motor driving, charging and balancing. It bridges the earlier BTMLC IC paper [23] and level-shifter paper [24] to the proposal's per-slot converter concept; the eight-tap breakdown limit + stacking argument (p. 5) is precisely the scaling narrative the proposal extends.
- **References candidate:** cite as — Q. Farhat, "A Scalable Hybrid Multilevel Power Converter Using Low-Voltage On-Chip Power Modules," preprint (engrXiv), 9 March 2026, no DOI printed. Also harvest its refs [17] (Herzog/Kolar/Huber 2025) and [10] (tree-type ANPC) for the state-of-the-art section.

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

Evidences breadth of on-chip integration capability in the **same 130-nm BCD process family** as the BTMLC: a second fabricated, measured IC (3.4 mm² die, 5 V lateral LDMOS) implementing four stacked half-bridge submodules with fully integrated dead-time generation, multiple-output level shifting and gate driving, operating 1 kHz–5 MHz over 2.4–4.3 V cell voltages and delivering up to 2.5 A average balancing current in a dual-IC complementary configuration. Together with Part A it shows the group can integrate the complete battery-facing power-processing suite (conversion + balancing) on one process platform — supporting the proposal's "unified power processing" claim — and it reuses the identical level-shifter/dead-time IP ([31]/[32] = the same Authorea preprints cited in Part A), demonstrating a coherent, reusable circuit-IP lineage.

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

## B6. Proposal mapping

- **Building on previous work:** demonstrates the second pillar of the platform — cell-level balancing IC in the same 130-nm BCD family, sharing the level-shifter/dead-time IP with the BTMLC ([31]/[32]); supports the claim that the team can deliver the complete on-chip battery-interface function set (multilevel conversion, balancing, gate-driving in series-stacked domains) and that the modular/stackable design language generalises. The eight-to-ten-cell headroom and SOI upgrade path (p. 10) mirror Part A's scaling argument, giving a consistent platform narrative.
- **References candidate:** cite as — Q. Farhat, "On-Chip Scalable High-Speed Active Battery Balancers," preprint, 7 March 2026, no DOI printed (hosted preprint view captured as PDF). Table 3 (p. 32) is directly reusable as competitive-landscape evidence; refs [16] and [21] are candidate additions for the balancing state of the art.

---

## Cross-cutting notes for the lineage argument

1. Both preprints carry the identical printed statement that they derive from a chapter of the author's 2025 UCL PhD thesis, and both acknowledge the same EPSRC studentship **EP/T517793/1 (Project Reference 2600345)** — a direct, citable EPSRC lineage.
2. Both cite the same two companion Authorea preprints (BTMLC IC, Oct. 2025; multiple-output level shifters, Feb. 2026), establishing a four-output publication chain from one thesis on one process platform.
3. Neither document prints a DOI — cite by title/date/hosting, and check engrXiv for assigned DOIs before submission.
4. Machine-load applicability is asserted (motor driving, machine insulation stress, "compact motor drive systems" — Part A, pp. 2, 3, 25) but all delivered-power demonstrations are into resistive loads; the proposal should present inductive/machine loading as the next step the new work funds.
