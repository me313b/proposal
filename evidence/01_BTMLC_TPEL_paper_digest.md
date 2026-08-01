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

## 6. Proposal mapping

### Work packages

- **WP1 (machine electromagnetics):** The paper's total silence on winding loads, back-EMF and mutual coupling (Section 5 above) is the evidence of need; its geometry data (15.2 mm² die, 3.530 mm × 4.297 mm, p. 12850) bound what a per-slot IC occupies within a slot; the 5–10 A practical-current guidance and parallel-IC scaling (p. 12849) set the per-slot current design space WP1's winding design must match.
- **WP2 (per-slot circuit):** Direct inheritance — topology laws (1)–(5), loss model (6)–(17), Zener-regulated cell-referenced gate supplies (p. 12848), single-dead-time differential MOLS scheme (pp. 12846–12847), 130-nm BCD 6-metal process with buried-N isolation (p. 12849). Calibration data: 0.472 Ω path resistance, 1.522 W model vs 1.88 W measured, metallisation ≈ channel resistance, 64–80 mm switch widths (pp. 12846, 12849). Known defects to fix: 50 ns commutation overshoot; 24 V-device penalty in the output stage.
- **WP3 (control):** Three-signal NLC control of eight levels (Table II, p. 12844); demonstrated arbitrary random tap sequencing under load (Fig. 12) and smooth variable-voltage variable-frequency response (Fig. 13, 100 Hz–5 kHz, 3.3–23.1 V) establish the actuator's controllability envelope; frequency law (4)/(5) fixes the per-level switching-rate constraints WP3's modulator must respect.
- **WP4 (demonstrator):** The complete test methodology (daughterboard/motherboard, card-edge interfacing, decoupling network, microcontroller drive, thermal imaging under Fig. 11(n) conditions, pp. 12849–12852) is the baseline the demonstrator extends from resistive to machine loads; the 52 W / 2 A / 26 V / DC–5 kHz measured envelope is the benchmark to surpass.

### Research questions

- **RQ1 (winding geometry):** Unaddressed by the paper — its die dimensions and standalone-drive framing (p. 12853) motivate the question; no winding data exist here.
- **RQ2 (ZVS under inductive source):** Open. Hard-switched resistive-load operation only; the finding that switching losses are already "negligible" versus conduction (p. 12846) reframes RQ2 towards commutation quality/dv/dt rather than pure loss recovery — an evidence-based sharpening.
- **RQ3 (transient voltage distribution):** Seeded by the 50 ns overshoot mechanism (asymmetric turn-on across Levels I–III, p. 12850) and the stacked-NDMOS shifter's equal-voltage-distribution design (pp. 12846–12847); dynamic distribution under inductive commutation remains fully open.
- **RQ4 (2N-DOF control):** Supported by the log2(n) control-signal compression (three signals, eight levels), the bidirectionality claim (p. 12842), and demonstrated arbitrary/random tap selection (Fig. 12); per-cell/per-slot degree-of-freedom exploitation (balancing, fault bypass) is explicitly future work (pp. 12852–12853).
- **RQ5 (thermal co-design):** Directly motivated by the measured 65 °C die / 26 °C PCB decoupling at only ~moderate loss (p. 12852) and the authors' own call for thermal pads/vias/heat-spreading — none implemented, none co-designed with a machine's thermal environment.
