# Resources and Cost Justification — Draft Variants
## EPSRC Standard Grant: "Foundations of Monolithically Integrated Per-Slot Machine Drives for Reconfigurable Aerospace Propulsion"

*Separately assessed section; limit 1,000 words. No costings are confirmed: every figure is flagged [PI TO CONFIRM: ...]. Two variants follow — A is narrative-led (prose by cost category); B is table-led (compact items table plus tight justification prose). Choose one.*

---

## VARIANT A — Narrative-led (prose by cost category)

### Directly incurred staff — [PI TO CONFIRM: total staff cost]

The programme's structure demands two Postdoctoral Research Associates (PDRAs), not one. Work Package 1 (WP1, machine electromagnetic design) and WP2 (per-slot circuit module architecture) must run in parallel from month 1, because the machine and the circuit constrain each other bidirectionally: the winding geometry sets the impedance, back electromotive force (back-EMF) and thermal environment each integrated circuit (IC) module must operate within, while the module's electrical and thermal limits set the winding's permissible current density and harmonic content. A single researcher would force these strands into sequence, which the Approach shows is scientifically invalid for a co-design problem of this kind. Two PDRAs with complementary disciplines are therefore the minimum staffing that delivers the methodology.

**PDRA1 (power electronics, [PI TO CONFIRM: 36 months], [PI TO CONFIRM: salary and grade])** carries WP2, WP3 and WP4. In WP2 they characterise the per-slot circuit module under inductive winding-source conditions, mapping the adiabatic zero-voltage-switching envelope (Research Question 2, RQ2) and the coupled module thermal behaviour (RQ5) on the discrete prototype boards. In WP3 they implement and test the 2N-degree-of-freedom control framework on the hardware-in-the-loop platform (RQ4), and in WP4 they lead electrical integration and fault-insertion testing. Circuit expertise is required continuously from month 1 to month 36; a shorter appointment would break the WP2-to-WP4 knowledge chain at exactly the integration point where it matters most.

**PDRA2 (electrical machines, [PI TO CONFIRM: 18 or 36 months], [PI TO CONFIRM: salary and grade])** carries WP1 and WP4. Under Co-I Asef they develop the extended winding-factor models, multi-harmonic finite-element analysis and the distributed-parameter transient voltage model (RQ1, RQ3), then transfer to WP4 for the demonstrator build, electromagnetic validation and end-winding-elimination quantification.

### Investigator time — [PI TO CONFIRM: cost]

The PI (Dr Baghdadi, [PI TO CONFIRM: full-time-equivalent (FTE) percentage]) leads WP2 and WP3, directs the co-design iteration between work packages, and owns overall delivery, partner liaison and risk management. Co-I Asef ([PI TO CONFIRM: FTE percentage]) leads WP1 machine electromagnetic design and supervises PDRA2. Co-I Everts ([PI TO CONFIRM: FTE percentage]) leads the thermal strand across WP2 and WP4, including the thermal network modelling and packaging specification that RQ5 requires. Each allocation maps to a named work-package leadership role; none is discretionary.

### Equipment and consumables — [PI TO CONFIRM: total]

The programme requests four project-specific items; none duplicates existing UCL Advanced Propulsion Laboratory (APL) capability.

**Prototype machine build ([PI TO CONFIRM: cost]).** The 18-slot open-end hairpin stator, with both conductor ends terminated at the stator end-face for bilateral per-slot access, is the physical object the entire programme validates. No commercial machine offers open-end per-slot access; it must be built to the WP1 geometry. Without it, RQ1 and RQ3 remain simulation-only and WP4 cannot exist.

**12–18 discrete functional-equivalent prototype boards ([PI TO CONFIRM: cost]).** These boards are the primary experimental vehicle for WP2 and WP4 — one bilateral pair per driven section, replicating the per-slot circuit architecture in discrete devices. They answer RQ2 and RQ5 and de-risk the programme entirely from IC fabrication. A monolithic IC tape-out is a stretch enhancement, not a costed dependency [PI TO CONFIRM: whether a multi-project-wafer run is costed].

**High-bandwidth differential voltage probes ([PI TO CONFIRM: number and cost]).** RQ3 asks whether the transient per-slot voltage ever approaches the ~200–300 V Paschen inception threshold during switching and field reconfiguration. Answering it requires floating differential measurement across individual winding sections during fast transients — a measurement APL's existing instrumentation cannot make [PI TO CONFIRM: existing scopes are single-ended, without floating differential capability].

**Thermal imaging instrumentation ([PI TO CONFIRM: cost]).** RQ5 requires spatial temperature maps of IC modules dissipating inside a 120–150 °C winding environment; the packaging specification depends on resolving gradients that point sensors cannot capture.

### Travel and subsistence — [PI TO CONFIRM: cost]

Travel funds dissemination at the leading international power-electronics and electrical-machines venues [PI TO CONFIRM: which venues], where the target academic beneficiaries are concentrated, and visits to project partners Eaton and Airbus [PI TO CONFIRM: letters of support] to align the Technology Readiness Level (TRL) 3 handover.

### Other directly incurred costs — [PI TO CONFIRM: cost]

This request covers open-access publication charges for programme outputs, and data storage and curation for the open experimental dataset that WP4 delivers to the community.

### Value for money

The architecture research runs on discrete prototype boards and on APL's existing dynamometer, oscilloscopes, electronic loads, hardware-in-the-loop platform and modelling tools — all provided at no cost to the grant. Grant funds therefore buy only what is project-specific and does not exist: the staff who do the science, the machine and boards that embody the architecture, and the two instruments that make the RQ3 and RQ5 measurements possible.

*[Word count: 804]*

---

## VARIANT B — Table-led (items table plus tight justification)

Every requested resource maps to a specific work package (WP), research question (RQ) and measurement. No confirmed costings exist at this stage; all figures are flagged for confirmation.

| Resource | Cost | WP / RQ | Why essential |
|---|---|---|---|
| Postdoctoral Research Associate 1 (PDRA1), power electronics, [PI TO CONFIRM: 36 months] | [PI TO CONFIRM] | WP2, WP3, WP4 / RQ2, RQ4, RQ5 | Circuit-module characterisation, control implementation, demonstrator electrical integration |
| PDRA2, electrical machines, [PI TO CONFIRM: 18 or 36 months] | [PI TO CONFIRM] | WP1, WP4 / RQ1, RQ3 | Winding models, multi-harmonic finite-element analysis, demonstrator build and validation |
| PI Dr Baghdadi, [PI TO CONFIRM: full-time-equivalent (FTE) %] | [PI TO CONFIRM] | WP2, WP3 lead; delivery | Co-design direction, partner liaison, risk ownership |
| Co-I Dr Asef, [PI TO CONFIRM: FTE %] | [PI TO CONFIRM] | WP1 lead | Machine electromagnetic design; PDRA2 supervision |
| Co-I Dr Everts, [PI TO CONFIRM: FTE %] | [PI TO CONFIRM] | WP2, WP4 thermal lead | Thermal network modelling; packaging specification (RQ5) |
| Prototype machine: 18-slot open-end hairpin stator | [PI TO CONFIRM] | WP1, WP4 / RQ1, RQ3 | No commercial machine offers open-end per-slot access; must be built to WP1 geometry |
| 12–18 discrete functional-equivalent prototype boards | [PI TO CONFIRM] | WP2, WP4 / RQ2, RQ5 | Primary experimental vehicle; one bilateral pair per driven section; de-risks from integrated-circuit (IC) fabrication |
| High-bandwidth differential voltage probes | [PI TO CONFIRM: number and cost] | WP1, WP4 / RQ3 | Floating differential measurement of transient per-slot voltage against the ~200–300 V Paschen threshold |
| Thermal imaging instrumentation | [PI TO CONFIRM] | WP2, WP4 / RQ5 | Spatial temperature mapping of IC modules inside the 120–150 °C winding environment |
| Travel and subsistence | [PI TO CONFIRM] | Dissemination; partners | Leading power-electronics and machines venues [PI TO CONFIRM: which venues]; Eaton and Airbus visits [PI TO CONFIRM: letters of support] |
| Open access; data storage and curation | [PI TO CONFIRM] | All WPs; WP4 dataset | Open-access charges; curation of the open experimental dataset |

**Staff.** Two Postdoctoral Research Associates (PDRAs) are the minimum staffing the methodology permits. Work Package 1 (machine) and WP2 (circuit) must run in parallel from month 1 because the two subsystems constrain each other bidirectionally — the winding sets the impedance, back electromotive force (back-EMF) and thermal environment of each integrated circuit (IC) module, while the module's limits set the winding's current density and harmonic content. One PDRA would force sequential working and invalidate the co-design methodology. PDRA1 runs [PI TO CONFIRM: 36 months] because circuit expertise must persist unbroken from WP2 characterisation through WP3 control to WP4 integration. Investigator allocations each map to a named work-package leadership role.

**Equipment.** All four items are project-specific and none duplicates existing UCL Advanced Propulsion Laboratory (APL) capability. The stator embodies the architecture under investigation. The discrete boards carry all WP2–WP4 research, making a monolithic IC tape-out a stretch enhancement rather than a costed dependency [PI TO CONFIRM: whether a multi-project-wafer run is costed]. The differential probes enable the one measurement on which the partial-discharge claim rests (Research Question 3, RQ3): whether transient per-slot voltage ever approaches the Paschen threshold. The thermal imaging enables the RQ5 gradient maps that point sensors cannot capture.

**Value for money.** APL's dynamometer, oscilloscopes, electronic loads, hardware-in-the-loop platform and modelling tools all come at no cost to the grant. Grant funds buy only what does not exist and cannot be borrowed: the researchers, the machine and boards that embody the architecture, and the two instruments that make the RQ3 and RQ5 measurements possible.

*[Word count: 564]*
