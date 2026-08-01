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

**2.3.3 Integration Configurations (pp. 8–9).** The IMD taxonomy. Figure 2.1 (from [8]) gives the four canonical configurations: **(a) radial housing-mounted, (b) radial stator-mounted, (c) axial housing-mounted, (d) axial stator-mounted (endplate)**. Selection logic: radial mounting suits high-speed machines, axial suits high-torque (stack-length/stator-diameter ratio, per [8]); stator-mounted variants are "purer" integration (compact, interconnects fully eradicated) but complicate cooling; housing-mounted variants use the housing as a thermal barrier and ease cooling at the cost of volume. Figure 2.2 adds real examples: **(a) single-location radial mounting by Danfoss [38]** (VLT DriveMotor FCM 300), **(b) distributed-electronics radial by H3X [39]**, **(c) endplate integration from [14]**, **(d) the tilt-rotor motor system of the Archer Midnight eVTOL [43]**. Aerospace-specific argument: single-location radial's non-axisymmetric geometry increases parasitic drag and interferes with tilt mechanisms, so **distributed radial or endplate mounting is preferred for aerospace**; endplate integration needs a co-designed endplate and restricts end-winding ventilation but does not grow the diameter.

**2.3.4 Integrated Modular Motor Drives (pp. 10–11).** IMMD defined: basic module = stator pole-piece with concentrated coil and dedicated power converter; modules held by a bearing housing, capped by a redesigned endplate — **Brown, Jahns & Lorenz, IEEE IAS Annual Meeting 2007 [12]**. The modules are termed **'Smart Stator Teeth' (SST)** in **Brockerhoff et al., IEEE EDPC 2014 [13]**, each SST connected to a central control unit, forming a multiphase machine with integrated electronics. Benefits: phase-number flexibility, redundancy, fault management, scalability. Both [12] and [13] flag **DC bus capacitor size as the critical issue**: electrolytic capacitors are thermally excluded, and film capacitors that fit cannot handle two-level-inverter DC-link ripple current.

**2.3.5 Wide Bandgap Devices (p. 11).** (Section heading misprinted "Wind Bandgap Devices".) **SiC and GaN devices: practical temperature limit ~600 °C vs 225 °C for Si**; SiC has higher thermal conductivity and suits >1000 V; choice is application-dependent — all cited to **[10] Abebe et al., IET Electric Power Applications 2016**.

**2.3.6 Existing IMD Implementations (pp. 11–13).** Worked examples: **[14]** Wheeler et al. (EPE 2005) — fully integrated 30 kW matrix-converter drive, endplate-mounted, finned endplate + shaft fan; **[15]** Hilpert et al. (EDPC 2014) — endplate integration with liquid cooling, 'inverter building blocks' (IBB) each driving one half-bridge, on direct-cooled aluminium baseplates; **[16]** Chen et al. (IEEE TTE) — radial integration, WBG current-source inverter replacing DC-link capacitors with inductors, shared water jacket in a hexagonal stator housing; **[17]/[18]** Wang et al. (IEEE JESTPE 2025) and Swanke et al. (IEMDC 2021) — the aerospace flagship: a **2 kV, 1 MW, 20,000 rpm IMMD** with a 200 kW risk-retirement build, radial submodules of paired SiC H-bridges, 9 cold plates for 18 power modules, flooded slots, plus explicit PD countermeasures (extra insulation at PD-prone areas, rounded edges, optimised gaps). Summary judgement (p. 13): aerospace IMD literature remains thin; thermal management is inseparable from the integration strategy; no consensus inverter topology; WBG generally adopted; high power needs liquid + air cooling.

### 2.4 Electric Machine Considerations (pp. 13–15)

Machine-topology comparison from **[19] El Hajji et al., *Aerospace* 2024 (1 MW S-PMSM case study)**: PMSM best overall (power/torque density, efficiency, power quality); WFSM/IM magnet-free but lossier; HTSM cryogenics too complex; SRM robust but lower efficiency, larger, higher torque ripple. **Slot/pole vs speed weight trade-off, also from [19]:** for a **12/10** slot/pole combination, weight falls substantially up to **10,000 rpm** then plateaus; **24/20** keeps improving to **15,000 rpm**; **36/30** only gains significantly up to **5,000 rpm**. Decision: PMSM, preliminary target speed **5,000–15,000 rpm**, exact value to follow slot-pole and power-electronics choices.

### 2.5 Advanced Inverter Topologies (pp. 15–18)

**2.5.1 Motivation for MLIs (pp. 15–16).** Second headline claim: "typically, about **40% of the volume of the motor drive constitutes of the capacitors**, rendering compact integrated drives above 7.5 kW unfeasible within the original motor envelope **[14]**" — i.e. the 40%-capacitor-volume figure is sourced to the **2005 Wheeler paper**, twenty years old; the 7.5 kW envelope statement here is also pinned to [14] (while §2.3.2 pinned a similar 7.5 kW threshold to the 2000 trade article [11]). Both the number's age and the double attribution should be noted. MLIs reduce DC-link capacitor needs and THD. **THD comparison from [20] (Paterakis, Marouchos & Darwish, UPEC 2017): a 13-level MLI measured 5.285% THD vs 73.98% for a 3-level PWM inverter.** Reduced dv/dt steps also shrink voltage spikes, cutting PD risk. Trade-offs: device count, control complexity, capacitor balancing.

**2.5.2 MLI Control and Topologies (pp. 16–18).** Survey keyed to **[21] Poorfakhraei, Narimani & Emadi, IEEE Open Journal of Power Electronics 2021**: NPC (compact, poor scalability, unequal switch loss), ANPC (equalised losses, more complex control), Flying Capacitor (cost-scalable but bulky, needs balancing and many sensors), NNPC (compromise, still capacitor-bound), CHB (modular, scalable, but needs isolated DC sources), MMC (reliable/modular/scalable but capacitor-heavy with pre-charge circuits), T-type (simple but high switch stress, unsuitable for high-voltage traction). Then the **generalised MLI [22] (Peng, IEEE Trans. Ind. Appl. 2001)** — self-balancing via redundant states, but very high component count. Pivot to the project's core idea: **[23] — the DCAT (DC-autotransformer)**: DC bus divided by a DCAT, multilevel waveform synthesised by a voltage tap selector; H-bridge modules paralleled with capacitors defining intermediate levels, magnetically coupled via a multi-winding transformer that forces balancing currents; fewer, smaller capacitors; drawbacks are the added voltage-splitting stage and the non-trivial multi-winding HF transformer. Finally, **open-end-winding machines [24]** avoid capacitor balancing, add redundancy, allow separate supplies per inverter and level scaling beyond a single inverter, at the price of control complexity.

### 2.6 IC Implementation (pp. 19–21)

Monolithic integration as a further miniaturisation route: **[25] Farhat & Baghdadi (IEEE Trans. Power Electronics, 2026, pp. 1–13)** — on-chip binary-tree multilevel converter in a **130 nm Bipolar-CMOS-DMOS** process, limited to **8 levels** by breakdown voltage, die on daughterboard with **33 µm Al bond wires**, prototype **3.530 mm × 4.297 mm**, reliable operation demonstrated only to **2 A**; **[26] Weiss et al. (IEEE CSICS 2015)** — monolithic single-phase diode-clamped converter in AlGaN/GaN-on-Si, chip **2 × 3 mm²**, current max **5 A**; **[27] Li et al. (IEEE EDL 2017)** — 200 V p-GaN HEMTs on GaN-on-SOI, cited for fabrication/substrate-coupling issues. Scaling routes: higher-voltage processes, wider devices, or series/parallel stacking of chips at board level [25]. **Defects observed here:** the figure on p. 20 is numbered **"Figure 2.12"**, duplicating the DCAT figure number on p. 19; its caption attributes the binary-tree topology and chip to **[27]** and chip layout (c) to **[28]**, while the body text attributes them to [25]/[27] and [26] respectively — and [28] is actually the RS wire datasheet. The [25]/[27] and [26]/[28] cross-references are internally inconsistent.

### 2.7 Summary and Identified Research Gaps (p. 21)

Integration reduces parasitics → PD mitigation + power density; eVTOL trends constrain design; DEP emphasises scalability; radial vs endplate mounting each with tailored cooling; IMMDs add phase redundancy; MLIs cut voltage steps; open-ended-winding dual inverters enable level scaling under space constraints; monolithic integration aids feasibility.

### 3.1 Battery-to-IMD Connection study (pp. 22–25)

Original (unpublished) analysis. Motivation: capacitor sizing is driven by voltage ripple / 'neutral point drift' (demonstrated in PSIM, Figure 3.1: binary inverter with ideal 100 V sources vs four 1 mF capacitors on a 400 V bus). Three ripple-avoidance options (Figure 3.2): (a) direct multi-wire connection to intra-battery terminals, (b) 2 wires + DCAT voltage-splitting stage, (c) CHB with isolated sources — CHB rejected for its isolated-source requirement.

- **2-wire configuration (p. 23):** modelled on the **AS22759/34 aerospace wire** (RS datasheet [28]); gauge sweep with **J_max = 3 A/mm²** and ≤1% power loss; result for a **20 kW, 400 V** system: **one pair of AWG 8 wires**.
- **Binary configuration (p. 24):** N-level MLI fed by **(N+1) wires** (incl. ground); per-wire currents from an rms band-splitting algorithm (Figure 3.3 shows 4- and 8-level cases); gauges assigned per-wire to equalise total loss with the 2-wire case, then weight/area compared.
- **Table 3.1 (p. 24)**, as printed:

| Levels | Power loss (W/m) 2-wire | Binary | Weight (kg/m) 2-wire | Binary | Total area (mm²) 2-wire | Binary |
|---|---|---|---|---|---|---|
| 4 | 5.74 | 5.70 | 0.08 | 0.03 | 20.06 | 12.36 |
| 8 | 5.74 | 5.58 | 0.08 | 0.05 | 20.06 | 21.33 |
| 16 | 5.74 | 5.56 | 0.08 | 0.11 | 20.06 | 33.51 |
| 32 | 5.74 | 5.41 | 0.08 | 0.22 | 20.06 | 68.04 |

- **Conclusion (p. 25):** a 4-level system could justify multi-wire (lighter, smaller), but the advantage vanishes and reverses with level count; sweeps up to **500 kW** (Figure 3.4) show binary wiring grows in mass/area with levels at high power — **the binary battery-tap approach is not scalable**; the 2-wire + DCAT route is adopted.

### 3.2 DC-Autotransformer Based Voltage Division (pp. 25–44)

PSIM demonstration that adding the DCAT tightens capacitor voltage profiles and improves output quality (Figure 3.5, p. 25). Then design physics: magnetising inductance via core reluctance (pp. 26–27, Erickson & Maksimovic [29]); copper losses and the case for **copper foil windings** (skin/proximity/eddy suppression, thermal spreading, pp. 27–28); core losses, ferrite choice, **B_sat 0.25–0.5 T** for ferrites (p. 28); leakage inductance and **interleaving** (pp. 28–29, [30] Barrios et al.); parasitic inductance minimisation (p. 29); **adiabatic (soft) switching** via the LC tank of MOSFET parasitic capacitances and magnetising inductance (pp. 29–30, [31]).

**DCAT literature review (pp. 30–33):** **[31] Kolahian, Grimm, Bucknall & Baghdadi (TechRxiv preprint, 2025)** — 8 balanced 50 V levels from a 32-board PCB stack, central gate H-bridge distributing signals via internal gate magnetics; derivation of the energy-exchange interval **t_f** (all-switches-off resonant transfer between L_m^p and C_eq^p = C_ds·N_s·N_L) and the gate-circuit compensation interval **t_z** (t_f = t_f^g + t_z, clamping states holding V_TG at zero). **[32] Zhao et al. (IEEE TTE 2022)** — 100 kW matrix-core transformer for more-electric-aircraft distribution: multiple parallel cores, symmetric circular-friendly layout, good natural-convection heat paths.

**Proposed high-power DCAT (pp. 33–35):** hybrid of [31] and [32]: copper-foil windings coupled by ferrite cores each built from 4 custom-cut slabs in a circular array; PCB modules with H-bridges between adjacent cores; MCU generates 4 gate signals, per-PCB gate H-bridge + buffer, gate transformer distributes isolated gate drive. Parameter set defined in Table 3.2 (p. 35): N_L, N_c, N_s; power-core geometry a, b, H_core, W_core; gate core A_e^g, l_e^g, l_g, N_turns; timings t_f, t_z.

**Parameter calculation and algorithm (pp. 35–41):** closed-form chain from 50 A rating (20 kW / 400 V) with **J_max = 5 A/mm² in the foils**, foil-stack geometry → core reluctance → L_m^p → t_f → B_pk; gate side from EE-core datasheet values → L_m^g → t_z → gate-wire rms current and AWG fit within the core window. Python search algorithm (flowchart, Figure 3.17): H-bridges per module divisible by 4; a swept 10–20 mm; **b fixed at 20 mm** (largest Kemet FPL ferrite slab on the market [33]); N_s ∈ {1, 2}; l_g in 50 µm multiples; **TDK EE-core catalogue [34]**; **design constraints: t_f ≥ 500 ns** (so t_f > t_d incl. gate-driver delays), **B_sat = 0.35 T** with 5% loss allowance, t_z > 0, gate wires within rated current, and **outer diameter ≤ 300 mm** (limited by market-available copper sheet); any slack diameter is fed back into W_foil. (Defects: p. 40 cites "**[69]**" for the AWG matching table — the reference list stops at [44]; presumably [42] was meant. The Figure 3.18 caption draws the dotted limit at **D_o = 305 mm** while the text says 300 mm.)

**Chosen design (pp. 41–42):** N_L = 36 is the largest level count under the diameter limit; of the 36-level candidates the one with the smallest gate core is selected. **Table 3.3 (p. 42), as printed:** N_L 36; N_c 9; N_s 2; power ferrite core a = 10 mm, b = 20 mm, H_core = 14.7 mm, W_core = 46 mm; **gate core geometry E20/10/6**, l_g = "300 μs" (obvious unit misprint for µm), N_turns = 6; timings **t_f = 868 ns, t_z = 384 ns**. Stated magnetising inductances: **L_m^g = 453 µH, L_m^p = 25.2 µH**. PSIM confirms adiabatic switching (Figure 3.19).

**Practical design and the two IMD configurations (pp. 42–44):** KiCad PCB of a single module, replicated in a circular array to the full 36-level structure (Figures 3.20–3.21). Cooling options considered: water jackets, or a **customised annular oil bath** (more uniform cooling, closer PCB-foil connection, lower parasitics). Then the two proposed IMD architectures (Figure 3.22):

- **Configuration 1 — single DCAT, singly-excited winding:** one DCAT feeds an inverter stage in which **each inverter module supplies one slot of the machine**; balanced split levels delivered per-slot; level allocation flexible with phase count and slots-per-pole-per-phase (printed as "SPPR").
- **Configuration 2 — dual DCAT, open-ended winding:** DCAT duplicated on the opposite side of the machine, battery voltage halved to each end; **levels double from 36 to 72** because the winding potential is controlled from both ends; extra redundancy; challenges are the shaft passing through the DCAT structure and much more complex control. Feasibility to be judged after a single-DCAT prototype.

**Defect — figure-label swap:** the body text describes Figure 3.22**a** as the single-DCAT/per-slot configuration and 3.22**b** as the dual-DCAT open-ended-winding one, but the printed caption reads "(a) Open-Ended winding and dual-inverter setup (b) Singly excited winding with single inverter" — the (a)/(b) assignments in caption and text are swapped. Anyone reusing this figure internally must check against the text, not the caption.

### 4. Relevant Experimental Work (pp. 45–46)

**4.1 Current sensor:** shunt-based Ultrafast Current Shunt (UFCS) per **[35] Shillaber et al. (IEEE TPEL 2022)** — shunt array, RL low-pass, two amplifier stages; board assembled with an embedded half-bridge for insertion-inductance-free testing; **experiments not yet run**. **4.2 Double pulse test:** DPT circuit per **[36]** designed to **50 A / 400 V**; PCB assembled, external inductor, setup photographed.

### 5. Future Work (p. 47)

Plan to October 2028: May–Sept 2026 voltage splitter (analysis, PCB, custom ferrites, testing); Oct 2026–Sept 2027 3-phase multilevel inverter (design, control, prototype, system testing); Oct 2027–Mar 2028 monolithic integration **or** full IMD integration; Apr–Oct 2028 thesis. Notably candid admission: "**there is a lack of quantitative metrics to target**; this project focuses on the feasibility of system-level architectures".

### 6. References (pp. 48–50) — quality issues

44 entries, [1]–[44]. Systematic problems: **nearly all journal entries omit volume and issue numbers** (only [27] carries "vol. 38, no. 7"); several conference entries lack page ranges or locations. Specific defects, as printed:

- **[23] is malformed:** "F. Grimm, J. Wood and M. Baghdadi, 'A DC-Autotransformer based Multilevel Inverter for Automotive Applications,' pp. Grimm, Ferdinand; Wood, John; Baghdadi, Mehdi, 2020." — the author names are duplicated into the page field and **no venue is given**. Since [23] is the foundational DCAT citation, the correct bibliographic record must be established independently before the proposal cites it.
- **[16]** title contains "…Current-Source Inverter **or** EV Traction Applications" (for "for") and is dated **2026** despite the surrounding text treating it as established work — year needs verification.
- **[36]** title is truncated: "A tutorial on double pulse test of silicon and silicon" (presumably "…and silicon carbide devices").
- **[3]** (Statista) and [39] (bare H3X homepage) are weak grey-web citations; [2] carries a `utm_source=chatgpt.com` tracking parameter in its URL.
- Dangling in-text citation **[69]** on p. 40 with no corresponding entry.
- [31] is a **TechRxiv preprint** (not peer-reviewed as listed); [25] is listed with pp. 1–13, apparently early access.

## 3. Published sources it relies on (citable substitutes)

The proposal should cite these directly, never the transfer report. As printed in the report (details to be verified/completed before use, given the missing volume/issue data):

**Peer-reviewed journals / magazines**
- [7] Madonna, Giangrande, Zhao, Zhang, Gerada, Galea — "Electrical Machines for the More Electric Aircraft: Partial Discharges Investigation," IEEE Trans. Industry Applications, pp. 1389–1398, 2021. *(PD/PDIV at altitude.)*
- [8] Lee, Li, Han, Sarlioglu, Minav, Pietola — "A Review of Integrated Motor Drive and Wide-Bandgap Power Electronics for High-Performance Electro-Hydrostatic Actuators," IEEE Trans. Transportation Electrification, pp. 684–693, 2018. *(IMD taxonomy; 10–20% volume; 30–40% cost; EMC.)*
- [9] Jahns & Sarlioglu — "The Incredible Shrinking Motor Drive," IEEE Power Electronics Magazine, pp. 18–27, Sept 2020.
- [10] Abebe, Vakil, Lo Calzo, Cox, Lambert, Johnson, Gerada, Mecrow — "Integrated motor drives: state of the art and future trends," IET Electric Power Applications, pp. 757–771, 2016. *(IMD challenges; SiC/GaN 600 °C vs Si 225 °C.)*
- [16] Chen, Lee, Feng, Chen, Paddock, Jahns, Sarlioglu — "Power-Dense Integrated Motor Drive Using a WBG-Enabled Current-Source Inverter [f]or EV Traction Applications," IEEE Trans. Transportation Electrification, pp. 542–555, printed 2026 (verify).
- [17] Wang, Jahns, McCluskey, Kizito, Sarlioglu, et al. — "2-kV 1-MW 20 000-r/min Integrated Modular Motor Drive for Electrified Aircraft Propulsion," IEEE JESTPE, pp. 394–407, 2025.
- [19] El Hajji, Hemeida, Lehikoinen, Martin, Belahcen — "Optimal Design of High Specific Power Electric Machines for Fully Electric Regional Aircraft: A Case Study of 1MW S-PMSM," Aerospace, pp. 1–12, 2024. *(Machine comparison; slot/pole vs speed weight trade-off.)*
- [21] Poorfakhraei, Narimani, Emadi — "A Review of Multilevel Inverter Topologies in Electric Vehicles…," IEEE Open Journal of Power Electronics, pp. 155–170, 2021.
- [22] Peng — "A Generalized Multilevel Inverter Topology with Self Voltage Balancing," IEEE Trans. Industry Applications, pp. 611–618, 2001.
- [24] Aihsan, Idin, Alias, Sutikno — IJPEDS, pp. 1270–1279, 2023. *(Open-end winding.)*
- [25] Farhat & Baghdadi — "On-Chip Design and Implementation of a Battery-Cell-Level Binary-Tree Multilevel Converter," IEEE Trans. Power Electronics, pp. 1–13, 2026. *(Team's own published on-chip MLC work — copy in repo.)*
- [27] Li et al. — "200 V Enhancement-Mode p-GaN HEMTs Fabricated on 200 mm GaN-on-SOI…," IEEE Electron Device Letters, vol. 38, no. 7, pp. 918–921, 2017.
- [30] Barrios, Urtasun, Ursúa, Marroyo, Sanchis — "High-Frequency Power Transformers With Foil Windings…," IEEE Trans. Power Electronics, pp. 5712–5723, 2015.
- [32] Zhao, Wu, Dao, Lin, Du, Zhao, Zhu — "Design and Demonstration of a 100 kW High-Frequency Matrix Core Transformer for More Electric Aircraft Power Distribution," IEEE Trans. Transportation Electrification, pp. 4279–4290, 2022.
- [35] Shillaber, Jiang, Ran, Long — "Ultrafast Current Shunt (UFCS)…," IEEE Trans. Power Electronics, pp. 15493–15504, 2022.
- [41] Wang, Zhang, Zhang, Li — "Review of High-Power-Density and Fault-Tolerant Design of Propulsion Motors for Electric Aircraft," Energies, pp. 1–31, 2023.

**Conference papers**
- [6] Ugwueze, Statheros, Bromfield, Horri — "Trends in eVTOL Aircraft Development…," AIAA SciTech, 2023. *(120-concept survey.)*
- [12] Brown, Jahns, Lorenz — IEEE IAS Annual Meeting, pp. 1322–1328, 2007. *(IMMD.)*
- [13] Brockerhoff, Burkhardt, Egger, Rauh — IEEE EDPC, pp. 1–6, 2014. *(Smart Stator Teeth.)*
- [14] Wheeler, Clare, Apap, Empringham, Bradley, Pickering, Lampard — "A Fully Integrated 30kW Motor Drive Using Matrix Converter Technology," EPE 2005. *(40%-capacitor-volume and motor-envelope claims.)*
- [15] Hilpert, Brinkfeldt, Arenz — IEEE EDPC, pp. 1–8, 2014.
- [18] Swanke, Zeng, Bobba, Jahns, Sarlioglu — IEEE IEMDC, pp. 1–8, 2021.
- [20] Paterakis, Marouchos, Darwish — UPEC 2017. *(13-level vs 3-level THD.)*
- [26] Weiss et al. — IEEE CSICS, New Orleans, 2015.
- [36] Masoud, Issa, Yates — IEEE WEMDCD, 2023.
- [40] Tallerico, Chapman, Smith — AIAA AVIATION 2023 Forum, San Diego, 2023.

**Book:** [29] Erickson & Maksimovic, *Fundamentals of Power Electronics*, Springer Nature, Cham, 2020.

**Preprint (cite with care):** [31] Kolahian, Grimm, Bucknall, Baghdadi — "Multiport DC Solid State Transformer with Enhanced Power Efficiency: A Modular Architecture," TechRxiv, pp. 1–10, 2025.

**Needs bibliographic repair before any use:** [23] Grimm, Wood, Baghdadi — "A DC-Autotransformer based Multilevel Inverter for Automotive Applications," 2020 (venue missing in the report).

**Grey/web sources (use primaries instead where possible):** [1] UN net-zero page; [2] IEA Global EV Outlook 2023; [3] Statista aviation-emissions page; [4] ICCT Mukhopadhaya & Graver 2022 (this one is a solid report); [5] ARPA-E FOA (16 Dec 2019); [11] Bartos, Control Engineering, 2000; [28] RS AS22759/34 datasheet; [33] Kemet FPL ferrite tiles; [34] TDK EPCOS ferrite data book 2013; [37] Embry-Riddle textbook chapter; [38] Danfoss VLT DriveMotor FCM 300; [39] H3X website; [42] Meters UK AWG table; [43] Archer aircraft page; [44] Joby Aviation news.

## 4. Proposal mapping

**How it positions the "IMD shortens, per-slot dissolves" differentiation.** The report's taxonomy (pp. 8–9) establishes that conventional IMD practice — radial housing, radial stator, axial housing, axial endplate — *relocates and shortens* the inverter-to-machine path: the inverter remains a discrete block bolted onto or into the machine, and the literature's quantified benefits (10–20% volume, 30–40% cost via [8]) all flow from cable/housing elimination alone. The IMMD/SST thread ([12], [13], and the 1 MW aerospace build [17]/[18]) is the published stepping-stone towards *dissolution*: per-tooth converters, but still fed by a common DC link whose capacitors the same literature identifies as the binding constraint (~40% of drive volume per [14]; ripple-intolerant film capacitors per [12]/[13]). Edwards' Configuration 1 (p. 43) is exactly the differentiated position the proposal argues: a DCAT voltage-splitting stage supplying balanced levels so that **each inverter module drives one machine slot** with a multistep waveform, dissolving both the inverter *and* the DC-link capacitor problem into the machine periphery — with Configuration 2 (dual DCAT, open-ended winding, 36→72 levels) as the scaling escape hatch the gap analysis (p. 21) motivates. The report also supplies the negative result the proposal needs: the multi-wire battery-tap alternative is quantitatively non-scalable (Table 3.1, Figure 3.4), leaving 2-wire + DCAT as the defensible route.

**Claims that must NEVER be sourced to this report** (cite the primary instead, or drop):

1. 10–20% volume reduction and 30–40% installation/manufacturing cost reduction → cite [8] Lee et al. 2018 (and note it is itself a review).
2. "Boosts system efficiency by 30% or more" → **no adequate source exists in the report**; do not use at all unless an independent primary source is found.
3. DC-link capacitors ≈ 40% of drive volume; >7.5 kW unfeasible in the motor envelope → [14] Wheeler et al. 2005 — flag the 2005 vintage.
4. 7.5 kW thermal barrier for IMDs → [11] Bartos 2000, a trade article; avoid as an evidential claim.
5. ARPA-E 12 kW/kg and 93% cruise efficiency → [5] ARPA-E FOA 2019 (retrieve document directly).
6. Aviation CO₂e 882 Mt (2024) and doubling since 1990 → replace Statista [3] with a primary source; 49–88% CO₂e reduction and 3× cruise efficiency → [4] ICCT 2022.
7. eVTOL survey statistics (120 concepts; 57% powered-lift; 53% vectored thrust) → [6] Ugwueze et al. 2023.
8. THD 5.285% (13-level) vs 73.98% (3-level) → [20] Paterakis et al. 2017.
9. SiC/GaN 600 °C vs Si 225 °C limits → [10] Abebe et al. 2016.
10. Slot/pole weight-vs-speed plateaus (12/10 @ 10 krpm; 24/20 @ 15 krpm; 36/30 @ 5 krpm) → [19] El Hajji et al. 2024.
11. **Unpublished and uncitable anywhere:** the Table 3.1 wiring comparison and non-scalability conclusion; the DCAT design algorithm, constraints and Table 3.3 parameters (36 levels, 9 cores, E20/10/6, t_f = 868 ns, t_z = 384 ns, L_m^p = 25.2 µH, L_m^g = 453 µH, 300 mm limit); the two IMD configurations and the 36→72 level doubling; the annular-oil-bath cooling concept; the UFCS/DPT hardware status. These are Edwards' original unpublished results — the proposal may describe them as the team's preliminary work but must not reference this document, and must not present them as established findings.

**Internal-use cautions:** the (a)/(b) caption swap on Figure 3.22, the duplicated "Figure 2.12" numbering with crossed [25]/[27]/[26]/[28] attributions, the dangling [69] citation, the "300 μs" airgap unit misprint, the 300 vs 305 mm diameter inconsistency, and the malformed [23] all mean this draft must be treated as a working document: verify every figure and reference against the body text before reuse.
