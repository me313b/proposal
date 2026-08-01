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

Policy alignment claimed: UK Aerospace Growth Partnership "Net Zero Aviation by 2050" ambition; Jet Zero and Destination Net Zero strategies; emerging CAA and EASA certification frameworks for electric propulsion.

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

Multi-phase HV motor at **1 kV and 18,000 rpm**; modular multilevel inverter (partial-discharge mitigation, EMI reduction, fault reconfiguration); integrated battery/hydrogen-fuel-cell balancing converter; advanced thermal management; fully integrated motor–inverter–energy-management package designed for joint certification; modular 100 kW unit scalable "toward megawatt class".

### 1.5 Revenue model

- **SkyDrive IM** (integrated motor drive): unit price ~**£35k**; demand projected at **200 units by 2031**, **>1,000 units by 2035**; also licensable at component level.
- **SkyDrive HPro** (hybrid propulsion with battery/fuel-cell balancing): unit price ~**£80k**.
- **SkyDrive Services**: recurring revenue at ~**20% of total product revenue**.
- ARC forecasts aircraft deliveries from year three post-development, scaling to **~50 aircraft per annum by year five**, each embedding a SkyDrive package.
- By **2040**: export revenues **>£200 million per year**, **>70% international**, **>500 direct high-skill UK jobs**.
- Manufacturing base: **iNetic's AS9100-certified facilities**; Eaton's industrialisation and global market access experience.

---

## 2. Q9 — Innovation Content

Q9 is a technology-by-technology table (challenge / SoA / innovation beyond SoA); all streams **TRL 3 → 6** except AI control (TRL 4 → 6).

1. **Ultra power-dense electric motor.** SoA benchmarks cited: Siemens ~5 kW/kg @ 11 krpm; Honeywell ~8 kW/kg @ 19 krpm; NASA prototypes ~10–13 kW/kg @ 20 krpm; EMRAX axial-flux ~10 kW/kg. Claim: **~13 kW/kg at 100 kW, 1 kV, 18,000 rpm, 95–98% efficiency**; additive-manufactured housings (+30% thermal conductivity, −25% temperature); hollow conductors at **25 A/mm²** with direct liquid cooling; spray cooling; amorphous laminations (−30% losses); carbon-fibre rotor sleeves (**>3 GPa**); **~24% higher density**, up to **47 kg system mass saving**, **10–15% more range**.
2. **Reliability/redundancy through multiphase design.** Six-phase and dual three-phase machines with integrated multilevel fault-tolerant inverters; torque ripple −50–80%; common-mode voltage −40–60%; operational life +>30%; continued operation under partial winding/phase loss. KPI: "100% improvement in fault tolerance vs SoA".
3. **Altitude-resilient multilevel drive for partial-discharge (PD) mitigation.** SoA limited to <800 V with thick insulation and bulky filters. Claim: stepped waveforms reduce dv/dt ~50%, suppress overshoot >90%; insulation life extended **2–3×**; reliable **1 kV operation at altitude**.
4. **Power-on-Chip converter with integrated cooling.** SoA (Evolito, Helix UK cited): SiC modules, cold plates, ~50–100 W/cm². Claim: WBG switches, drivers and passives on hybrid substrates; additive-manufactured microchannels achieving **>1,000 W/cm²**; 2× power density; hardware weight −50–75%; component count −up to 50%.
5. **Streamlined propulsion integration.** Motor, inverter and cooling in a single modular housing; cabling mass −20–40%; propulsion mass −≥10%; validated on ARC's jump take-off (**eJTO**) platform.
6. **AI-powered fault-tolerant control and validation.** FPGA-based closed-loop control with AI-driven digital twins for fault prediction/reconfiguration; validation on the ARC eJTO platform (altitude, pressure, dynamic load replication).

**KPI list (Q9 §9.2):** ≥10% propulsion mass reduction; **13 kW/kg motor** power density; 100% fault-tolerance improvement; 50–70% EMI reduction; ≥25% lower temperature; up to 50% power-electronics compactness gain; **16 kW/kg integrated system** power density; TRL 3→6 validation with digital twin; +10–15% range/payload.

**Baseline spec (Q9 §9.3):** continuous **100 kW**, **1 kV**, **18,000 rpm**, multilevel inverter, embedded cooling; requirements derived from ARC's **"LINX P3"** platform (note: Q7 and Q12 use **Linx P9** — an internal naming inconsistency in the SkyDrive documents; do not propagate either designation into EPSRC text without checking). Partner-led sections: iNetic on the multiphase machine (Vacoflux SiCo laminations, Metglas amorphous laminations, T1000G carbon-fibre sleeves, hollow conductors, spray cooling, planetary gearbox); UCL on power electronics (control-integrated chip sequencing cascaded H-bridge cells — stepped low-dv/dt synthesis instead of high-voltage PWM — plus microchannel-cooled substrates with dielectric coolant); ARC on eJTO testing (fault injection, thermal, EMI, digital-twin correlation, TRL 4→6).

**Note:** Q9's 13/16 kW/kg claims sit differently from Q12's stated targets (system >1.5 kW/kg, active-material >15 kW/kg) — quote whichever document is being referenced, never blend them.

---

## 3. Q12 — Technical Approach

### 3.1 Concept and specifications

Integrated **100 kW-class** HV propulsion subsystem: **six-phase motor at 1 kV and 18,000 rpm**, fault-tolerant **multilevel inverter**, **high-speed step-down gearbox**, integrated control and thermal management, co-designed as a single jointly certifiable subsystem. Energy storage is explicitly **out of scope (bought in)**. Targets: continuous high power; **system power density >1.5 kW/kg** for the integrated motor + inverter (**active-material >15 kW/kg**); **efficiency >97%**; defined fault tolerance; compliance-aligned validation evidence. TRL 3 → 6 via laboratory validation, HIL, environmental stress testing and integrated operation on ARC's **flight-representative Pegasus platform**, progressing to the **nine-seat Linx P9**; MW-class scaling identified (insulation coordination, multi-module thermal balancing, parallel-inverter control).

### 3.2 Partner roles — exact wording

- Consortium sentence: "**iNetic leads motor design, gearbox integration and aerospace-grade manufacturing; UCL contributes multilevel power electronics, control architecture and electro-thermal modelling; ARC provides system integration and flight-representative validation; and Eaton participates as a non-funded Tier-1 adviser on certification, industrialisation readiness and system safety.**"
- Eaton, on the WP diagram: "**Eaton advising across all of them**" (i.e. across WP0–WP4).
- iNetic dynamometer — the only explicit mention is the build-stream photograph caption: "**(left) iNetic six-phase motor and dynamometer rig; (centre) UCL multilevel power-electronics drive; (right) ARC flight-representative platform. Placeholders to be replaced with consortium images.**" (Q9 §9.6 additionally refers to "subsystem verification on dynamometers"; Q13 risk T1 refers to tuning models "with dyno telemetry after each build".)
- **UCL APL facilities: not mentioned anywhere in Q12** (nor in the other appendices as extracted). Any EPSRC statement about UCL's Advanced Propulsion Lab must be evidenced from elsewhere, not from SkyDrive documents.

### 3.3 Work-package structure

- **WP0 Project Management (iNetic)** — iNetic PM, Principal Investigator holds technical leadership; **xRL and PROLaunch** life-cycle tools; weekly/monthly/quarterly reviews; quarterly reports to the monitoring officer.
- **WP1 Six-Phase Motor Engineering (iNetic)** — WP1.1 electromagnetic/mechanical multi-physics optimisation at 18,000 rpm; WP1.2 advanced integrated cooling; WP1.3 high-speed step-down gearbox; WP1.4 hardware integration and bench test. Deliverable: manufactured and validated motor + cooling + gearbox assembly; defines the torque–speed envelope and motor interface for WP2/WP3.
- **WP2 Fault-Tolerant Power-Electronics Drive (UCL)** — WP2.1 topology definition (candidates include **neutral-point-clamped and flying-capacitor** arrangements for >1 kV, reduced dv/dt and common-mode stress) and six-phase modulation/digital control with balanced power sharing under single-phase or device-failure scenarios; WP2.2 electro-thermal design and cooling; WP2.3 hardware build and readiness verification (electrical, thermal, EMI). Deliverable: fully fabricated, readiness-verified drive unit.
- **WP3 System Integration and Experimental Validation (ARC Aerosystems)** — integrates motor-gearbox and drive; validates under aerospace-representative duty cycles: fault injection (graceful degradation under phase/device loss), thermal endurance, altitude-representative cycles, EMI characterisation; produces the TRL6 airworthiness-aligned evidence package.
- **WP4 Exploitation and Dissemination (iNetic)** — industrialisation/feasibility assessment, exploitation strategy, IP-protection framework, publications, industry engagement.

### 3.4 Timeline and milestones

**36 months**; motor and power electronics in parallel for two years; integration from mid-point; exploitation in the final year; **TRL6 by ~2029**. Milestones: **M1** requirements/baselines frozen (M6); **M2** detailed designs verified by analysis, TRL 4–5 (M12); **M3** hardware manufactured and bench-tested (M20); **M4** subsystem assembled (M30); **M5** validated on the SkyDrive platform, TRL6 (M36).

**Internal cross-reference note:** Q12's own preamble points to "Risks appendix (Q14)" and "Innovation appendix (Q13)", whereas the actual files are Q13 (risks) and Q9 (innovation) — evidence of drafting drift between versions; cite files by filename, not by internal cross-reference.

---

## 4. Q13 — Risk Register

**Format:** Risk = Likelihood (1–5) × Impact (1–5); bands **1–8 Low, 9–15 Medium, 16–25 High**; each risk scored **pre- and post-control** with cause, impact, mitigation and WP/owner. Categories: Technical T1–T33, Commercial C34–C40, Managerial M41–M50, Environmental E51–E53, Social S54–S55. Scores shown pre → post (L×I=S).

| ID | Risk (abridged) | Pre | Post | Mitigation (abridged) | Owner/WP |
|---|---|---|---|---|---|
| T1 | Model uncertainty (EM/thermal/PD) for 1 kV, 18,000 RPM multiphase motor, reduced pressure + spray cooling | 3×4=12 | 2×3=6 | Correlate FEM vs Epstein/BH and reduced-pressure PD coupons; tune with dyno telemetry; ±5% torque / ±5 °C gate criteria | WP1&2, iNetic/UCL |
| T2 | Incomplete system requirements (duty cycle, DC-link, EMI/EMC, cooling, interfaces) | 3×3=9 | 1×3=3 | Freeze SRS/ICD via OEM/regulator workshops; CCB change control | WP1, iNetic |
| T3 | Multilevel inverter cannot demonstrate fault-ride-through/redundancy at 1 kV with SiC | 4×4=16 | 2×3=6 | Two topologies to PDR; HIL fault-injection down-select; per-leg isolation; limp-home mode | WP1, iNetic |
| T4 | AM spray-cooling channels / hollow conductors fail yield/accuracy | 4×4=16 | 2×2=4 | DFAM trials, CT-scanned coupons; brazed-insert fallback if yield <90% | WP1, iNetic |
| T5 | Delays on Vacoflux laminations, carbon sleeves, HV insulation | 3×4=12 | 2×3=6 | Long-lead POs at PDR; dual-source; safety stock | WP1, iNetic |
| T6 | Component delay due to licence requirements | 4×5=20 | 3×4=12 | Order via licence-holding supplier; documentation provided | WP2, iNetic |
| T7 | Aerospace-grade SiC/GaN allocation limits | 2×3=6 | 1×2=2 | Pin-compatible second sources; derating; post-PDR buys | WP2, iNetic |
| T8 | Supplier/logistics slips stall assembly | 3×4=12 | 2×2=4 | Early orders; weekly expediting; pre-qualified alternates | WP3, iNetic/UCL |
| T9 | Weight/efficiency underperform benchmarks and business case | 3×3=9 | 2×2=4 | Re-optimise with dyno data/BoM; gearbox/cooling as levers | WP1&2, iNetic/UCL |
| T10 | Incorrect/unclear drawings | 4×4=16 | 2×3=6 | Clarification with stakeholders | WP1&2, iNetic/UCL |
| T11 | Component delivery delays (lead times underestimated) | 4×5=20 | 2×3=6 | Early ordering; dual-source | WP2, iNetic |
| T12 | Out-of-spec components / quality issues | 4×4=16 | 2×3=6 | Incoming QC; supplier QA agreement | WP3, iNetic |
| T13 | Performance/economics not commercially competitive | 2×3=6 | 2×2=4 | Re-optimise topology; define further optimisation work | WP1, iNetic |
| T14 | SkyDrive/test facilities damaged in testing | 1×4=4 | 1×2=2 | Instrumentation and protection; destructive tests last | WP3, iNetic/ARC |
| T15 | Rotor hoop-stress failure at 18,000 rpm (rotor burst) | 3×5=15 | 2×3=6 | FEA (stress/modal/fatigue); retaining sleeves; staged spin tests | WP3, iNetic |
| T16 | Coil-winding errors | 3×4=12 | 2×2=4 | Checked coil calculator; winding plan; validated temperature rating | WP3, iNetic |
| T17 | Component overheating (poor thermal design) | 3×4=12 | 2×2=4 | Thermal simulation; derating; certified materials | WP1, UCL |
| T18 | Incomplete/non-intuitive assembly SOPs | 3×3=9 | 1×2=2 | Visual SOPs; supervised pilot build with hold points | WP3, iNetic |
| T19 | Motor/powertrain fails final testing (design flaw) | 3×4=12 | 2×3=6 | Simulation; DVP; sub-assembly testing | WP3, iNetic |
| T20 | Test rig not ready | 2×4=8 | 2×2=4 | Parallel planning; early rig preparation | WP3, iNetic/ARC |
| T21 | Inadequate tooling (no early jig plan) | 2×4=8 | 1×2=2 | Fixture planning in early design | WP1, iNetic/UCL |
| T22 | Inadequate convective heat transfer (microchannel/oil spray) under dynamic loading | 2×4=8 | 1×3=4 | CFD; HIL bench test; redundant cooling path (hollow windings) | WP2, UCL |
| T23 | Thermal management under real operating conditions | 3×4=12 | 2×3=6 | Flight-like simulation/test; liquid cooling if needed | All, iNetic/UCL |
| T24 | Power density vs reliability trade-off | 4×4=16 | 2×3=6 | Conservative margins; accelerated life test; FMEA | WP1&3, iNetic |
| T25 | NVH from EM forces/assembly | 3×3=9 | 2×2=4 | FEA; NVH testing; precision balancing | WP1, iNetic |
| T26 | Precision manufacturing tolerances not consistently achievable | 4×4=16 | 2×3=6 | Supplier selection; CMM validation; pilot production | WP3, iNetic |
| T27 | Control tuning / software certification delays (DO-178C) | 3×5=15 | 2×3=6 | Experienced control partners; modular software architecture | WP3, iNetic |
| T28 | Inadequate testing environment (altitude/vibration/cooling not replicated) | 3×4=12 | 2×2=4 | HIL setups; vibration tables; altitude chambers | WP4*, iNetic |
| T29 | Battery/power-source compatibility mismatch | 3×4=12 | 2×2=4 | Early power requirements; involve battery partners | WP1, iNetic |
| T30 | Integration mismatches (mechanical/software interfaces) | 4×5=20 | 3×4=12 | WP1 interface definition with ARC; staged test plan | WP3, iNetic |
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
| E51 | Rare-earth magnet supply and sustainability (NdFeB, e.g. N48UH) | 4×5=20 | 3×3=9 | ISO 14001 suppliers; recycled magnets; disclosure | (no owner listed) |
| E52 | Energy savings not achieved | 3×3=9 | 2×2=4 | Energy monitoring; AI tweaks | WP3 |
| E53 | Scrap rate exceeds target | 2×4=8 | 1×3=3 | Lean kitting; error-proofing | WP3 |
| S54 | Skills gap in digital manufacturing | 2×3=6 | 1×2=2 | STEM workshops | WP3, iNetic |
| S55 | H&S incident during assembly | 2×5=10 | 1×2=2 | Document/version control (as written) | WP3, iNetic |

\*T28/T31/T32 cite "WP4/Testing" although Q12 defines WP4 as exploitation — another internal inconsistency between the register and the final WP structure. **These risks inform the EPSRC risk table's thinking (e.g. PD at altitude, rotor burst, SiC supply, interface freeze) but are not to be copied into it** — the EPSRC risks must be research risks owned by the EPSRC team.

---

## 5. "good photos for Question 10.docx"

Despite the filename, this is a full **Q10/benefits appendix draft** (internally numbered §7.1–7.6) containing **six embedded PNG images** (`word/media/image1.png`–`image6.png`) and these table/figure captions:

- **Table 1.** "Benefits at a glance, with the source of each in this appendix" (aircraft-level 30–80 vs 150–200 gCO₂/pax-km; >400,000 tCO₂/yr abated by 2040, ~900 t per 100 kW unit; ~1,220 UK jobs and £268m revenue by 2040, £37m reinvested; sovereign capability at TRL6 by ~2029).
- **Figure 1.** "Line of sight from validated component performance, through the efficiency and mass levers, to aircraft-level and fleet benefit."
- **Figure 2.** "Aircraft CO₂ intensity, electric and hybrid versus conventional, across the classes SkyDrive's propulsion addresses."
- **Figure 3.** "Post-project industrialisation and certification investment, 2029 to 2032 (£37m total), by category and year."
- **Figure 4.** "Projected UK employment and revenue growth to 2040, consistent with the bid's established figures."
- **Figure 5.** "SkyDrive commercialisation roadmap, from TRL6 validation on the Pegasus platform to higher-power derivatives."

Notable body figures (SkyDrive's claims): ~£1.9m programme over three years; ~£0.42m industrial match; ATI contribution ~£1.50m; £37m industrialisation 2029–2032; direct employment ~450 by 2040 (iNetic ~280, ARC ~150, UCL ~20), **ONS multiplier 1.72** → ~1,220 total; revenue ~£130m by 2036, ~£268m by 2040 (~£200m/yr export); "every £1 of aerospace R&D leverages ~£14" (attributed to ATI); three patent families; **five PhD completions and UCL-led publications**; Eaton in **SAE AE-7/AE-10** standards work; noise −10–15 dB; ATI 2026 strategy alignment (double UK share by 2035; propulsion >US$17bn/yr by 2050; >65,000 deliveries to 2050, ~70% single-aisle).

---

## 6. Proposal mapping — what the EPSRC proposal may draw from SkyDrive, and how

| EPSRC section | Permitted use of SkyDrive material | Mandatory caveats |
|---|---|---|
| **Capability / track record — industrial engagement** | Cite the SkyDrive programme (ATI project 10192096, iNetic + UCL + ARC) as evidence of an active industrial translation environment; cite iNetic's AS9100 facilities and dynamometer rig and ARC's flight-representative Pegasus environment as infrastructure the EPSRC outputs could later exploit. | Context and translation pathway only; state that SkyDrive is separately funded with independent objectives. Do **not** claim UCL APL facilities from these documents — no SkyDrive appendix mentions them. |
| **Partner contributions — Eaton evidence** | Quote Eaton's role verbatim: "non-funded Tier-1 adviser on certification, industrialisation readiness and system safety", advising across all WPs; plus Q7's "actively supporting system architecture, certification strategy, and industrialisation planning" and SAE AE-7/AE-10 involvement (Q10 doc). | Eaton's commitment is to *SkyDrive*; an EPSRC letter of support must be obtained separately. Never imply Eaton funding — the documents state it is non-funded. |
| **Impact narrative — context** | Sector framing (decarbonisation drivers, Jet Zero/AGP alignment, 1 kV class, power-density trajectory, staged certification pathway) may set the scene. Every figure (435M passengers; 38,000 aircraft/£4.65tn; £35bn; 120,000 jobs; 3,000 companies; ATI £1.37bn/£20bn; 1.5→3.5 kW/kg) is **[PI TO CONFIRM]** — another programme's claims, mostly uncited, with the ATI power-density provenance uncertain. | Attribute explicitly ("figures stated in the ATI-funded SkyDrive documentation") or substitute independently cited sources (ADS, ATI publications, DfT Jet Zero). Never present SkyDrive's revenue/jobs forecasts as EPSRC impact claims. |
| **Research vision / objectives** | May state that findings could transfer to programmes "such as" a 100 kW, 1 kV, 18,000 rpm class integrated drive — an *application class*, not a deliverable. | SkyDrive specs must never appear as EPSRC objectives, KPIs or milestones. The internal inconsistencies (13 vs 16 vs >15 kW/kg; LINX P3 vs Linx P9; Q13/Q14 cross-references) are further reason not to import numbers. |
| **Risk management** | The Q13 register informs which risk *themes* are real in this domain (PD at altitude, rotor containment at 18 krpm, SiC/GaN supply, model-correlation criteria, interface freeze) and evidences L×I pre/post-control practice. | EPSRC risks must be written afresh; no SkyDrive rows, scores or owners copied. |

**Blanket rule:** every SkyDrive-derived number in EPSRC text carries attribution to SkyDrive and a **[PI TO CONFIRM]** flag until verified or substituted with an independent source.
