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
