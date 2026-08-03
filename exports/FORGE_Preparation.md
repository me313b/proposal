# Forge preparation template

Generated 3 August 2026 by the drafting session. Note carried once for the whole file: the composed request was built from the pre-revision seed (50 V, 270 V, 18 slots, ATI anchor, GaN). Every block below is prepared against the current canon: bus up to 1 kV, 64 steps, sections near 16 V, 32 slots baseline with 36 as the WP1 trade, 100 kW at 14,000 RPM, 64 degrees of freedom, timeliness as a three-fold convergence, monolithic 130 nm BCD silicon. The request's claim of nothing drafted is also superseded: v1 variants exist for all 37 parts, with four Vision openings and two public summaries awaiting judgement. Calendar dates below are relative waves because the submission deadline is unconfirmed [PI TO CONFIRM: submission deadline].

## PREP: Summary :: Summary  [SUM-MAIN]

TAKEAWAY:
A mixed panel finishes one page knowing the whole argument: insulation cannot protect kilovolt-class machines at altitude, dividing the bus inside the winding removes the physics, the same decision yields pole-count freedom and three per cent fault steps, the price is a 64 degree of freedom coupled co-design, and the grant buys that methodology plus 100 kW evidence.

REQUIRED POINTS:
The partition between converter and machine as the common cause of four separate cost families.
Magnetic composition of a bus of up to 1 kV into 64 steps so no section exceeds about 16 V.
Partial discharge eliminated by architecture rather than insulation, with the 330 V floor named.
The cascade: software pole count, about 3 per cent capability loss per fault, end-winding removal.
The price stated plainly: 32 coupled sections, 64 degrees of freedom, no existing methodology.
What the grant buys: methodology, controllability theory, scaled IC via a costed fabrication run, 100 kW validation.

EVIDENCE:
Nothing is asserted bare: the 16 V figure is shown as 1000 over 64, the discharge claim rests on the named floor and cruise inception numbers, and the fault figure is shown as 31 of 32 to first order.

FACTS:
BUS_V, STEPS, SECT_V, SLOTS, DOF, DEMO_KW, DEMO_RPM, PD_FLOOR, TAPEOUT_GBP from the fact registry; discharge numbers trace to Lusuardi 2021 [5] and Meyer 2018 [6]; fault comparison to Levi [10], [11].

FIGURES:
None; the Summary carries no figures by design.

OBJECTIVES:
All of O1 to O5 in one compressed pass.

WORK PACKAGES:
Names none individually; implies all four.

SOURCES:
exports/FORGE_Import.md variant SUM-MAIN-v1; the chosen public summary sets the register; evidence dossier index for every number.

OPEN QUESTIONS:
Intended use of this part versus the 550-word public summary is still flagged; align after the SUM-PUB judgement.

INSTRUCTIONS:
Technical-lay hybrid register, denser than SUM-PUB; fact tokens permitted here; four-move order preserved; no em dashes; acronyms expanded at first use; end on what funding buys, not on importance claims.

OWNER:
Drafting session, PI sign-off.

DUE:
Wave 1, with the public summary judgement.

## PREP: Summary :: Public summary (550 words)  [SUM-PUB]

TAKEAWAY:
A lay reader understands why electric flight is limited by sparks inside motors at altitude, how putting the electronics inside the winding removes that physics entirely, and why safety, reliability and simplicity then arrive together rather than being traded.

REQUIRED POINTS:
The two-object arrangement of today's drives and its invisible costs.
Thin air at cruise letting tiny discharges erode insulation that passed every ground test.
Sixteen volts per copper section from a thousand-volt supply, divided along the machine itself.
No section can spark at any altitude; safety by architecture, not thicker insulation.
The gearbox leaves; a fault costs about three per cent, not a third.
Thirty-two interacting sections as the honest research challenge; open publication; Eaton and Airbus support.

EVIDENCE:
Plain-language causation shown step by step; no number appears without its everyday meaning attached; the 100-kilowatt demonstrator anchored to the air-taxi motor class the reader may have seen.

FACTS:
Same registry numbers as SUM-MAIN but spelled in words; JOBS_UK for the closing national point.

FIGURES:
Not applicable.

OBJECTIVES:
O1 to O5 implicitly; none named.

WORK PACKAGES:
None named; three-year build-and-test arc described in plain terms.

SOURCES:
Variants SUM-PUB-v1 (problem-led) and SUM-PUB-v2 (assumption-removal-led), both filed as candidates.

OPEN QUESTIONS:
Which of v1 and v2 stands, or whether a merged third is wanted; this judgement sets the register SUM-MAIN then matches.

INSTRUCTIONS:
Fully literal by design: no fact tokens, no equations, no acronyms unexpanded, no citation keys; UK English lay register; the section names Eaton and Airbus but no other organisations; never oversell, the final sentence claims foundations, not aircraft.

OWNER:
Drafting session, PI judgement between variants.

DUE:
Wave 1, first judgement of the proposal.

## PREP: Vision :: Opening: stand beside the expert  [VIS-OPEN]

TAKEAWAY:
Within one paragraph the expert reader recognises their own field's constraints and meets the claim that all four share one removable cause; they feel recognised, not lectured, and they want the derivation that follows.

REQUIRED POINTS:
Mechanism and number in the first sentences, context and policy nowhere near the opening.
The partition named as the invisible assumption: converter makes voltages, winding makes torque, insulation rated for the full bus stands between.
Bus voltages climbing toward the kilovolt class carrying every partition cost with them.
The closing move: one IC pair at every slot and the converter as a separate object ceases to exist.

EVIDENCE:
The opening asserts only what the LINE and CROSS parts will derive; its own burden is recognition, so every named cost must be one the reader already owns.

FACTS:
WIND_C, DIE_MM2, NODE, BUS_V, SECT_V, JUNC_C, PDIV_CRUISE, PD_FLOOR, ALT_KPA, SLOTS appear across the four filed variants; all from the registry.

FIGURES:
None; the opening is prose only.

OBJECTIVES:
Frames the ground for all objectives; commits to none.

WORK PACKAGES:
Not applicable.

SOURCES:
Variants VIS-OPEN-v1 (partition-first), v2 (impact triad), v3 (historical audit), v4 (forced move from the Paschen floor); strategy return for the judgement framing.

OPEN QUESTIONS:
Which of the four strategies leads; the PI's A2 answer asked for a first line that is technically magnetic with impact woven early, which v2 and v4 serve most directly.

INSTRUCTIONS:
Hold one register once chosen; no metaphor conceits; the words novel and innovative never appear; this programme will establish, never this project will investigate; tokens as filed.

OWNER:
PI judgement; drafting session executes the choice.

DUE:
Wave 1; every other Vision part inherits this register.

## PREP: Vision :: The unseen line  [VIS-LINE]

TAKEAWAY:
The reader accepts that the converter-machine boundary is a design variable rather than a fixed interface, because four constraint families they treat as separate are shown to be one assumption's consequences.

REQUIRED POINTS:
Insulation and partial discharge: 40 to 60 per cent conductor fill in kilovolt form-wound machines; inception roughly halving to 350 to 500 V peak near 20 kPa; the 330 V floor no pressure can lower.
Wide-bandgap edges sharpening turn-to-turn stress.
The gearbox: pole count frozen in the winding, CS-29 loss-of-lubrication and chip detection, the Super Puma record, half to one per cent per mesh, the sector's direct-drive migration with Archer's geared Midnight as the honest counterexample.
Fault fragility and the multiphase price: five-phase about 70 per cent, dual three-phase about 50 per cent, bought with duplicated channels at bus voltage.
End-windings as least productive, least coolable copper with aspect-ratio-dependent share.

EVIDENCE:
Every family carries its citation; the multiphase concession is quantified from the Levi canon, not caricatured; the accident record is cited to the investigation reports, never dramatised.

FACTS:
PD_FLOOR, PDIV_CRUISE, ALT_KPA from the registry; fill figures from Hemmati [9]; inception from [5], [6]; stress from Madonna [7]; end-windings from Madonna [8]; multiphase from [10], [11]; gearbox from [29], [30], [31], [22].

FIGURES:
None mandatory; if space allows, a single small inception-versus-pressure sketch is the only candidate.

OBJECTIVES:
Motivates O1 and O4.

WORK PACKAGES:
Seeds the problems WP1 to WP4 answer; describes none.

SOURCES:
Variant VIS-LINE-v1; dossier sections on PD, gearbox and multiphase; prior-art file 14 for boundaries.

OPEN QUESTIONS:
Whether the Archer counterexample stays in the final cut; it costs a clause and buys credibility.

INSTRUCTIONS:
Derive rather than list: the four families must read as consequences of the one assumption, so each paragraph ends by handing its cost back to the partition; no bullets; citations inline by canonical number.

OWNER:
Drafting session.

DUE:
Wave 1, immediately after the opening register is fixed.

## PREP: Vision :: Crossing the line: the 50 V claim  [VIS-CROSS]

TAKEAWAY:
The reader watches the claim being derived rather than asserted: up to 1 kV composed magnetically along the open-end winding as 64 steps, 32 per end-face, so no insulation boundary ever sees more than about 16 V, a factor of twenty below the physical floor while a conventional kilovolt machine sits above cruise inception.

REQUIRED POINTS:
The bus is never delivered to the winding; it is composed by the winding.
The arithmetic shown: 1000 over 64 gives 15.6, written approximately 16 V.
Margin in both directions: twenty times below the 330 V floor; conventional 1 kV two to three times above cruise inception.
The autotransformer lineage above 99 per cent as the efficiency answer.
The dual identity: the IC is excitation source and switching element; the conductor is torque medium and distribution network.
The enabling die exists: 15.2 mm2 in 130 nm BCD, floating-domain gate control in the same process.

EVIDENCE:
The composition principle is evidenced from the group's own converters, including the eight-tap 400 V composition at 98.8 per cent and the closed-loop 400 V machine drive; the derivation must be checkable line by line.

FACTS:
BUS_V, STEPS, STEPS_SIDE, SECT_V, PD_FLOOR, PDIV_CRUISE, DIE_MM2, NODE from the registry; [1], [2], [3], [4] for the lineage; [5], [6] for inception.

FIGURES:
Figure V1, the part's one mandatory figure: open-end winding with bilateral per-slot IC pairs and the 64-step composition ladder, per-section voltage labelled near 16 V.

OBJECTIVES:
States the claim O1, O2 and O4 exist to prove.

WORK PACKAGES:
Previews WP1 and WP2 without naming tasks.

SOURCES:
Variant VIS-CROSS-v1; Kolahian thesis digest in the dossier; fact registry.

OPEN QUESTIONS:
The per-section envelope flag stays open, whether sections span one or two steps; the part rename to the 16 V claim is pending in the workbench and the header stays byte-identical until then.

INSTRUCTIONS:
Derivation register throughout; the flag [PI TO CONFIRM: per-section envelope of 15 to 16 V derived from 1 kV across 64 steps] is reproduced byte for byte wherever the envelope is stated; never call the predecessor IC adiabatic, the adiabatic claim belongs to the converter lineage.

OWNER:
Drafting session; PI closes the envelope flag.

DUE:
Wave 1.

## PREP: Vision :: The cascade and its price  [VIS-CASC]

TAKEAWAY:
The benefits are believed because they are derived from one decision rather than promised, and the section's credibility peaks where it pays: 32 coupled actuators on one core, a 64 degree of freedom co-design with no existing methodology, and that methodology, not the machine, named as the contribution.

REQUIRED POINTS:
Discharge eliminated because the voltage never arrives at any boundary.
Pole count as software: harmonic synthesis to 16 pole pairs, retuned per operating point, gearbox and its regime leave the drivetrain, terminal-level prior work generalised to full spatial resolution.
Fault tolerance without duplication: about 3 per cent per section to first order, the partial bounded predictable behaviour the vertical-lift condition rewards, against the multiphase price already conceded.
End-windings terminate at end-face modules where cooling is best.
The price in full: coupling, the three open questions named as research, and the crown jewel framed as the co-design discovery.

EVIDENCE:
The 3 per cent figure is shown as 31 of 32 ampere-conductors; the certification fit quotes the condition's requirement, not marketing language; the price paragraph names what could fail.

FACTS:
SLOTS, DOF, WIND_C, JUNC_C from the registry; [20], [21], [13] for pole-changing lineage; [23] for the condition; [10], [11] for comparison; [8] for end-windings.

FIGURES:
None; the derivation carries it.

OBJECTIVES:
Sets up O3, O4, O5 and the methodology deliverable of O1.

WORK PACKAGES:
Previews WP3's centrality and WP4's role as evidence.

SOURCES:
Variant VIS-CASC-v1; strategy return line for this part.

OPEN QUESTIONS:
None beyond the standing envelope flag inherited from CROSS.

INSTRUCTIONS:
The phrase partial, bounded and predictable is the certification vocabulary; gradual degradation never appears; the sentence naming the framework, not the demonstrator, as the contribution is load-bearing and survives every edit.

OWNER:
Drafting session.

DUE:
Wave 1.

## PREP: Vision :: Novelty and scientific contribution  [VIS-NOV]

TAKEAWAY:
The reviewer who knows the stator-cage and modular-drive literature finds it cited openly and fairly, and therefore believes the claim that survives: the conjunction has never existed, and the contribution is the co-design and controllability theory of magnetically coupled per-slot actuation.

REQUIRED POINTS:
ISCAD conceded: per-slot granularity and electronic pole changing at a supplied 48 V, paying in kiloampere system currents.
Wisconsin GaN stack conceded: sub-bus module voltages, capacitively, outside the winding, per pole, unilateral, hard-switched.
Open-end bilateral feed and terminal-level pole changing conceded.
The conjunction claimed: bilateral per-slot drive, magnetic derivation of about 16 V sections from a bus of up to 1 kV inside the winding, monolithic integration, discharge elimination at altitude by design, adiabatic soft switching.
Contribution named: the 64 degree of freedom co-design and controllability theory.

EVIDENCE:
Property-by-property differentiation available from the prior-art table; every concession carries its citation so no reviewer can add one the text hid.

FACTS:
BUS_V, SECT_V, DOF from the registry; [13], [14], [12], [20], [21] as the neighbouring art.

FIGURES:
Table V1 if space permits: the differentiation table condensed from evidence file 14; otherwise the prose carries all eight properties.

OBJECTIVES:
Defines what O1 and O3 must deliver to make the claim true.

WORK PACKAGES:
Not applicable.

SOURCES:
Variant VIS-NOV-v1; 14_per_slot_prior_art_research.md including its verified reference block.

OPEN QUESTIONS:
Whether Table V1 fits the four-page budget or stays a drafting aid.

INSTRUCTIONS:
Concede before claiming, every time; GaN appears only as the Wisconsin work's technology, never as this programme's; the conjunction sentence lists all five properties in one breath by design.

OWNER:
Drafting session.

DUE:
Wave 1.

## PREP: Vision :: Timeliness: the ATI collision  [VIS-TIME]

TAKEAWAY:
The reader accepts that this is the year: the enabling silicon completed and published in the current cycle, a certification framework that rewards exactly this failure behaviour, and a policy and electrical environment moving toward kilovolt-class distribution; and they notice no roadmap number they could not check.

REQUIRED POINTS:
Silicon complete: the per-slot die published, floating-domain control in press, the doctoral lineage naming motor loads at scale as the explicit next step, and this programme as that step.
SC-VTOL-01 requiring continued safe flight after lift or thrust unit failure, fitting a drive that loses 3 per cent per fault.
The environment: 270 V DC standardised and flying, distribution rising toward the kilovolt class this architecture tames.
Foundational work must start now for UK capability to meet the convergence rather than follow it.

EVIDENCE:
Each line of the convergence carries a checkable anchor: publication records for the silicon, the special condition by name and issue, the military standard for the flying baseline.

FACTS:
[1], [2], [3] for the silicon; [23] SC-VTOL-01 Issue 1, 2 July 2019; [28] MIL-STD-704F; no ATI figures anywhere, dropped as unverifiable per the PI's B6 answer.

FIGURES:
None.

OBJECTIVES:
Justifies the timing of the whole programme; serves no single objective.

WORK PACKAGES:
Not applicable.

SOURCES:
Variant VIS-TIME-v1; dossier verification notes on the dropped trajectories.

OPEN QUESTIONS:
The part rename from the ATI collision is pending in the workbench; the header stays byte-identical until the PI renames it.

INSTRUCTIONS:
No ATI power-density trajectory may appear in any form; the three-fold convergence is stated in plain register with no clock imagery per the A4 answer; platform bus-voltage examples beyond the verified anchors are not invented.

OWNER:
Drafting session.

DUE:
Wave 1.

## PREP: Vision :: National importance  [VIS-NATL]

TAKEAWAY:
Importance reads as capability rather than boosterism: named policy, two market figures each scoped to what it measures, a workforce number with a current source, and a training claim tied to the exact cross-disciplinary capability the programme creates.

REQUIRED POINTS:
Jet Zero named as the policy commitment.
PwC: up to 2.1 billion pounds annual UK socioeconomic benefit by 2040, advanced air mobility scope.
DfT Future of Flight: 45 billion pounds to the UK economy by 2030, whole drone and electric aviation scope, stated as such.
About 104,000 people employed in UK aerospace, ADS 2024.
UK strengths concentrated: power IC design, machines research, certification expertise; researcher training including the flagged co-funded studentship.

EVIDENCE:
The two market figures are never added or conflated; their differing scopes are stated in the text itself.

FACTS:
JOBS_UK from the registry; [24] Jet Zero; [26] PwC July 2023; [25] DfT March 2024; [27] ADS 2024.

FIGURES:
None.

OBJECTIVES:
Serves the case for funding; maps to no technical objective.

WORK PACKAGES:
Not applicable.

SOURCES:
Variant VIS-NATL-v1; dossier market-figure verification notes.

OPEN QUESTIONS:
The studentship agreement flag stays open and is reproduced byte for byte where the student is mentioned.

INSTRUCTIONS:
Both figures, carefully scoped, per the PI's B2 answer; the stale 111,000 jobs figure never returns; no supply-chain claims beyond what the partners evidence.

OWNER:
Drafting session.

DUE:
Wave 1.

## PREP: Vision :: Scope and funding rationale  [VIS-SCOPE]

TAKEAWAY:
The boundary of the ask is legible: a TRL 1 to 3 programme delivering methodology, controllability theory, scaled silicon and 100 kW evidence; industry supports but cannot fund foundations; adjacent programmes are environment, not commitment; and the demonstrator scale is a deliberate choice at the passenger-class per-motor point.

REQUIRED POINTS:
TRL 1 to 3 stated; deliverables enumerated.
Why EPSRC and not industry: pre-competitive, platform-agnostic, publishable, un-appropriable.
Adjacent, separately funded industrial programmes cited as translation environment with the separateness caveat.
The demonstrator is 32 slots at 100 kW and 14,000 RPM; every 18-slot and 5 to 15 kW framing is superseded and must not resurface.
What is deliberately out: platform integration, certification testing, productisation.

EVIDENCE:
The pre-competitive argument is argued, not asserted: the methodology redefines a boundary between two industries' products, which is why no single company can own it.

FACTS:
SLOTS, DEMO_KW, DEMO_RPM, BUS_V from the registry.

FIGURES:
None.

OBJECTIVES:
Frames all five as the content of the ask.

WORK PACKAGES:
Not applicable.

SOURCES:
Variant VIS-SCOPE-v1; PI answer block C6 and B1 as the parameter authority.

OPEN QUESTIONS:
None; scope is settled.

INSTRUCTIONS:
The separateness caveat accompanies every adjacent-programme mention without exception; the out-of-scope list is stated once, plainly, and never apologised for.

OWNER:
Drafting session.

DUE:
Wave 1, closing the Vision pass.

## PREP: Approach :: Hypotheses and objectives  [APP-HYPO]

TAKEAWAY:
The programme is falsifiable on its face: four hypotheses each of which could fail informatively, five research questions with the coupling question folded into RQ4, and five objectives that map one to one onto work packages with no orphan on either side.

REQUIRED POINTS:
H1 composition: a winding can divide a bus of up to 1 kV into 64 steps below about 16 V while producing torque.
H2 switching: adiabatic soft switching survives an inductive back-EMF source.
H3 control: the 64 degree of freedom coupled system is controllable at full slot count, or the limiting conditions can be stated and proven.
H4 thermal: monolithic ICs operate inside a 120 to 150 degrees Celsius winding within a junction class of 150 to 175 degrees Celsius.
RQ1 to RQ5 as filed, RQ4 expanded per the A3 answer.
O1 methodology and winding, O2 scaled IC via costed fabrication, O3 control framework with proofs, O4 100 kW discharge-free demonstration, O5 pole reconfiguration and ride-through above 95 per cent.

EVIDENCE:
Each hypothesis names its falsifier and the work package that would observe it; the objective-to-WP map is stated in the text, not implied.

FACTS:
BUS_V, STEPS, SECT_V, DOF, WIND_C, JUNC_C, DEMO_KW, DEMO_RPM, RIDE_PCT from the registry.

FIGURES:
Table A1 optional: one compact hypothesis, research question, objective, work package map if the six-page budget allows.

OBJECTIVES:
Defines O1 to O5.

WORK PACKAGES:
Maps all four; O1 to WP1, O2 to WP2, O3 to WP3, O4 and O5 to WP4 with WP3.

SOURCES:
Variant APP-HYPO-v1; strategy return; PI answer A3.

OPEN QUESTIONS:
Whether an overall drive efficiency target is stated; none is committed anywhere yet and inventing one is prohibited.

INSTRUCTIONS:
Falsifiable phrasing throughout: each hypothesis is written so a negative result is a defined, publishable outcome; the H3 negative branch is explicitly framed as success.

OWNER:
Drafting session.

DUE:
Wave 2, first block of the Approach pass.

## PREP: Approach :: WP1 (scope to confirm)  [APP-WP1]

TAKEAWAY:
WP1's scope is confirmed, not pending: the reconfigurable per-slot machine under Dr Asef, delivering the electromagnetic foundation, the slot-count decision, the dual-function winding, and the coupon discharge evidence the demonstrator depends on.

REQUIRED POINTS:
T1.1 topology: rotor without a committed pole count, cage against synchronous reluctance, and the 32 versus 36 slot trade made explicit.
T1.2 the winding as dual-function object: bilateral end-face access, section currents from the shared model, composition embedded in the turns.
T1.3 coupons and full stator, discharge campaign at 20 kPa.
T1.4 integration support and the electromagnetic layer of the delivered methodology.
Deliverables D1.1 to D1.4 with months 6, 12, 15, 20.

EVIDENCE:
The slot-count decision is evidenced as a trade study output at D1.1, not a preference; coupon discharge data at altitude-representative pressure is the part's hard evidence.

FACTS:
SLOTS, ALT_KPA, DEMO_KW from the registry; the 36-slot option's consequences (72 steps, about 13.9 V) noted from the facts sheet legend.

FIGURES:
None; the winding figure lives in VIS-CROSS and the module figure in WP2.

OBJECTIVES:
O1 primarily; feeds O4.

WORK PACKAGES:
Describes WP1; supplies WP2 with current targets and WP4 with the stator.

SOURCES:
Variant APP-WP1-v1; PI answer B1 including choose a proper slot; facts sheet cascade note.

OPEN QUESTIONS:
Baseline slot count flag and per-section current envelope flag both live here and are reproduced byte for byte.

INSTRUCTIONS:
The part header keeps its registry name including scope to confirm; the text states plainly that scope is now confirmed so no reviewer reads doubt into a stale label.

OWNER:
Dr Asef with the drafting session.

DUE:
Wave 2.

## PREP: Approach :: WP2: circuit in winding  [APP-WP2]

TAKEAWAY:
The programme's first centre of gravity: the published 2 A monolithic die scales to the per-slot module through a costed fabrication run, is packaged into the end-face, and is characterised across the winding's thermal environment, with a predecessor-silicon fallback held ready.

REQUIRED POINTS:
T2.1 module specification from the shared model: paralleled output stages and dies, floating-domain gate control carried over, the adiabatic regime unified with the integration platform for the first time.
T2.2 design freeze and multi-project-wafer submission at month 12, 50,000 pounds project-funded with Eaton's conditional 50,000 pound match.
T2.3 silicon characterisation across 120 to 150 degrees Celsius against RQ2 and RQ5; end-face packaging with WP4.
T2.4 the 64 qualified modules, with the hybrid fallback stack per risk R2.
Deliverables D2.1 to D2.4 with months 9, 12, 20, 24.

EVIDENCE:
The inheritance split shown, never blurred: the hard-switched integration precedent and the adiabatic converter lineage are distinct citations unified here; the current-scaling approach is a specified design output, not a hope.

FACTS:
DIE_MM2, NODE, TAPEOUT_GBP, MODULES, WIND_C, JUNC_C from the registry; [1] for the die, [2] for the platform, [3], [4] for the adiabatic lineage.

FIGURES:
Figure A1: per-slot module block diagram from predecessor die to scaled module, showing paralleled stages and the floating domains.

OBJECTIVES:
O2 primarily; enables O4.

WORK PACKAGES:
Describes WP2; depends on WP1 current targets; supplies WP4.

SOURCES:
Variant APP-WP2-v1; PI answer C4; dossier rule that the BTMLC is never called adiabatic.

OPEN QUESTIONS:
Form of the Eaton contribution, cash or in-kind, flagged byte for byte; per-section current envelope inherited from WP1.

INSTRUCTIONS:
Monolithic 130 nm BCD throughout; GaN never appears as this programme's technology; the fabrication run is presented as scope expansion matched by industry, not as a dependency.

OWNER:
PI with the drafting session.

DUE:
Wave 2.

## PREP: Approach :: WP3: coupled control  [APP-WP3]

TAKEAWAY:
The second centre of gravity pays the cascade's price in full: controllability of 32 coupled sections at full slot count or a proven fundamental limit, 64-channel loss-minimising allocation, measured post-fault re-optimisation speed, and hardware validation that starts on the existing 400 V bench a year before the demonstrator exists.

REQUIRED POINTS:
T3.1 analytical layer: controllability and observability under coupling, limit conditions, formal allocation statements across the pole programme.
T3.2 early hardware on the group's 400 V rotating bench from month 6: coupled-control primitives, soft switching against a rotating back-EMF, estimator designs.
T3.3 the full stack: real-time 64-channel allocation, pole-transition trajectories, re-optimisation speed as a measured output.
T3.4 demonstrator campaigns with WP4 including ride-through above 95 per cent with one section removed.
Deliverables D3.1 to D3.4 with months 12, 18, 24, 33.

EVIDENCE:
A controllability result exists at month 12 either way: theorem or limit; the bench work evidences observer and estimator designs on rotating hardware before scale-up.

FACTS:
SLOTS, DOF, RIDE_PCT from the registry; [3] for the bench.

FIGURES:
None mandatory; a small control-hierarchy sketch only if the six-page budget allows after Figures V1, A1, A2.

OBJECTIVES:
O3 primarily; delivers O5 with WP4.

WORK PACKAGES:
Describes WP3; depends on WP1 model structure; feeds WP4.

SOURCES:
Variant APP-WP3-v1; PI answer A3 folding coupling into RQ4.

OPEN QUESTIONS:
None beyond the standing envelope flags.

INSTRUCTIONS:
The proven-limit branch is written as a publishable success in the text itself; observer and estimator vocabulary appears since reviewers from control will look for it.

OWNER:
PI with the drafting session.

DUE:
Wave 2.

## PREP: Approach :: WP4 (scope to confirm)  [APP-WP4]

TAKEAWAY:
WP4's scope is confirmed: validation at 100 kW, 14,000 RPM and up to 1 kV under Dr Everts, framed throughout as the evidence layer that validates the framework and is deliberately not the contribution.

REQUIRED POINTS:
T4.1 integration and thermal design for ICs cohabiting the winding, RQ5's direct object.
T4.2 commissioning on the dynamometer at rated speed and voltage, about 68 newton metres.
T4.3 the validation matrix: full-bus composition near 16 V per section, efficiency mapping, pole change under load, single-section ride-through, discharge surveillance at altitude-representative pressure.
T4.4 measurement-informed methodology release and dataset.
Deliverables D4.1 to D4.4 with months 24, 28, 34, 36; WP4 runs months 18 to 36.

EVIDENCE:
Every hypothesis meets a measurement here; the matrix is enumerated so a reviewer can check falsifiability item by item.

FACTS:
DEMO_KW, DEMO_RPM, DEMO_NM, BUS_V, SECT_V, ALT_KPA, RIDE_PCT from the registry.

FIGURES:
Figure A2: demonstrator and test-cell schematic, machine on dynamometer with supply, instrumentation and reduced-pressure discharge surveillance indicated.

OBJECTIVES:
O4 and O5.

WORK PACKAGES:
Describes WP4; depends on WP1 stator, WP2 modules, WP3 stack.

SOURCES:
Variant APP-WP4-v1; PI answer C6.

OPEN QUESTIONS:
Dynamometer and high-voltage supply ratings, and reduced-pressure capability for the assembled machine, both flagged byte for byte; these gate risk R5.

INSTRUCTIONS:
The registry header keeps scope to confirm; the text confirms it; the sentence that WP4 validates and is not the contribution appears per the C2 answer.

OWNER:
Dr Everts with the drafting session.

DUE:
Wave 2.

## PREP: Approach :: Risk register and mitigation  [APP-RISK]

TAKEAWAY:
The register names the risks that could actually kill the programme and mitigations that visibly cost something: schedule held for silicon, a fallback stack built and maintained, derated campaigns accepted, and a control-limit outcome converted into a result.

REQUIRED POINTS:
R1 silicon current-scaling shortfall: staged parallelism fixed at D2.1, bounded derated fallback.
R2 fabrication slip: month 12 submission against a month 18 need, predecessor-silicon hybrid stack held ready.
R3 controllability limit: hierarchical reduced-DOF control, the limit itself publishable.
R4 thermal exceedance: segmented duty, enhanced end-face cooling, packaging qualification including mechanical robustness at 14,000 RPM.
R5 facility shortfall at 100 kW, 1 kV and reduced pressure: month 3 confirmation, procured access costed if needed.
R6 the 1 kV safety case from month 12.
R7 conditional partner contribution: the project-held 50,000 pounds funds a viable run alone.

EVIDENCE:
Each mitigation names its artefact and month; comfortable risks are absent by design.

FACTS:
TAPEOUT_GBP, DEMO_KW, DEMO_RPM, BUS_V from the registry; likelihood and impact ratings as filed.

FIGURES:
Table A2 if the format permits a compact register table; otherwise labelled prose entries as filed.

OBJECTIVES:
Protects O2, O3, O4 explicitly.

WORK PACKAGES:
Cuts across all four; R2 protects the WP2 to WP4 dependency.

SOURCES:
Variant APP-RISK-v1; PI answer C8 omitting a dedicated vibration row, honoured with mechanical robustness inside R4.

OPEN QUESTIONS:
Facility ratings flag gates R5's likelihood.

INSTRUCTIONS:
No mitigation may be free; each names time, money or scope it consumes; the C8 decision is respected, no standalone vibration row returns.

OWNER:
Drafting session, PI sign-off on ratings.

DUE:
Wave 2.

## PREP: Approach :: APL facilities and equipment  [APP-APL]

TAKEAWAY:
APL is evidenced as capable of this specific build and campaign: the converter benches and 400 V rotating rig already running, the IC design route already used to published silicon, and the two named confirmations still open are stated as such rather than papered over.

REQUIRED POINTS:
Existing: binary-tree converter benches, the 400 V back-to-back rotating rig, IC design infrastructure with the established multi-project-wafer route, machine prototyping, calorimetric and thermal-imaging instrumentation.
Required and flagged: dynamometer and supply at 100 kW, 14,000 RPM, up to 1 kV; reduced-pressure discharge testing for coupons and the assembled machine.
The escape path: any gap moves to Resources as procured access.

EVIDENCE:
Capability is shown through what has already been produced on these facilities, the published die and the closed-loop machine drive, not through inventory listing.

FACTS:
DEMO_KW, DEMO_RPM, BUS_V, ALT_KPA from the registry; [1], [3] as facility-proven outputs.

FIGURES:
None.

OBJECTIVES:
Underwrites O4.

WORK PACKAGES:
Serves WP4 chiefly; WP1 coupon testing and WP2 characterisation named.

SOURCES:
Variant APP-APL-v1; the facility-ratings flag text.

OPEN QUESTIONS:
The facility-ratings flag, byte for byte; resolving it is the single highest-priority PI action in the Approach.

INSTRUCTIONS:
The dyno and test cell are described in campaign terms, what they must do, not brochure terms; honesty about the two confirmations is the credibility move.

OWNER:
PI to confirm ratings; drafting session writes.

DUE:
Wave 2; the flag itself as early as possible.

## PREP: Approach :: Gantt, milestones and deliverables  [APP-GANTT]

TAKEAWAY:
Six milestones, each falsifiable, each gating named deliverables, with the single dependency visible: silicon at month 18 releases WP4, and the fallback branch is drawn, not implied.

REQUIRED POINTS:
MS1 month 6 envelope frozen: topology, slot count, section currents.
MS2 month 12 design freeze and fabrication submission, D1.2, D2.2, D3.1.
MS3 month 18 silicon received, reduced-scale validation done, WP4 released.
MS4 month 24 integrated demonstrator, 64 modules, control stack.
MS5 month 28 commissioning at rated speed and voltage.
MS6 month 36 full matrix, campaigns, methodology release.
The one-page landscape Gantt typeset from this schedule with the R2 fallback as a dashed branch.

EVIDENCE:
Each milestone is written as a testable state of the world, not an activity; deliverable identifiers appear beside their milestones.

FACTS:
MODULES, DEMO_KW from the registry; the month plan as filed under the C1 delegation.

FIGURES:
The Gantt page itself, produced at assembly from this part's schedule; a milestone table inside the part if space allows.

OBJECTIVES:
Time-binds O1 to O5.

WORK PACKAGES:
All four; the WP2 to WP4 dependency is the drawn critical path.

SOURCES:
Variant APP-GANTT-v1; PI answer C1, review yourself and advise, discharged by this schedule.

OPEN QUESTIONS:
None internal; the deadline flag governs absolute dates only outside the 36-month frame.

INSTRUCTIONS:
Falsifiable milestone language throughout; no milestone reads as continue working; the fallback branch appears in the figure, which is unusual and deliberate.

OWNER:
Drafting session.

DUE:
Wave 2; figure produced in Wave 4.

## PREP: Approach :: Management and partnership  [APP-MGMT]

TAKEAWAY:
Governance is light and legible: the PI directs, monthly work-package reviews run against the shared co-design model, milestone gates decide continuation, and both industrial partners meet the programme quarterly under secured letters.

REQUIRED POINTS:
Decision rights: PI directs, leads WP2 and WP3 at 12.5 per cent; Dr Asef WP1 and Dr Everts WP4 at 7.5 per cent each.
Two PDRAs and the flagged co-funded student with Eaton industrial support.
Cadence: monthly all-hands against the shared model, milestone gates, quarterly partner reviews.
Data management to UCL policy with releases at D3.4 and D4.4.

EVIDENCE:
The shared model as the management instrument is the substantive claim: reviews are against a living artefact, not minutes.

FACTS:
PI_FTE, COI_FTE from the registry.

FIGURES:
None.

OBJECTIVES:
Delivery assurance for all.

WORK PACKAGES:
All four.

SOURCES:
Variant APP-MGMT-v1; PI answers C3, C5, C7.

OPEN QUESTIONS:
Named partner contacts flagged; studentship agreement flagged; both byte for byte.

INSTRUCTIONS:
No advisory-board invention; governance described is governance that will exist; partner engagement wording stays consistent with PRT-LTRS.

OWNER:
Drafting session.

DUE:
Wave 2.

## PREP: Approach :: Research design and methodology  [APP-RDM]

TAKEAWAY:
The methodology is co-design under coupling in three strands: a unified state-space that keeps inter-slot coupling, two benches with the existing 400 V rig de-risking the demonstrator a year early, and a measurement loop that makes the delivered methodology measurement-informed rather than idealised.

REQUIRED POINTS:
Modelling strand: sections as simultaneous electromagnetic, converter, thermal and control objects; model order itself a research output.
Hardware strand: the 400 V rotating bench from month 6, then the 32-slot 100 kW demonstrator.
Measurement strand: coupon discharge at about 20 kPa, calorimetric and electrical efficiency, thermal imaging, fault injection, all fed back to the models.
The shared model as the mechanism forcing genuine co-design over sequential hand-off.

EVIDENCE:
Each hypothesis is matched to its measurement in this part so the reviewer sees the test plan behind H1 to H4 before reading the WPs.

FACTS:
SLOTS, DEMO_KW, ALT_KPA from the registry; [3] for the bench lineage.

FIGURES:
None mandatory; the shared-model data-flow can be a small inset in Figure A1 if space allows.

OBJECTIVES:
Methodology backbone of O1; test plan for O4, O5.

WORK PACKAGES:
Defines how all four interlock.

SOURCES:
Variant APP-RDM-v1.

OPEN QUESTIONS:
None.

INSTRUCTIONS:
The phrase measurement-informed is the part's signature and appears exactly once; the bench-first sequencing is stated as deliberate de-risking, tying to APP-WPSTR.

OWNER:
Drafting session.

DUE:
Wave 2.

## PREP: Approach :: Work package structure and parallelism  [APP-WPSTR]

TAKEAWAY:
The structure is visible at a glance: three work packages live in month 1, one genuine dependency at month 18 protected by a built fallback, centres of gravity named as WP2 and WP3, and WP4 framed as validation of the framework rather than the contribution.

REQUIRED POINTS:
WP1 and WP2 parallel from month 1, exchanging constraints through the shared model from month 3.
WP3 analytical from month 1, on hardware from month 6.
WP4 dependent from month 18 only.
Centres of gravity stated plainly per the C2 answer; no work package waits for its first year.
The critical path is silicon into demonstrator, and only that.

EVIDENCE:
The parallelism claim is checkable against the Gantt part month by month.

FACTS:
Not applicable beyond the schedule already stated.

FIGURES:
None; the Gantt carries the picture.

OBJECTIVES:
Schedule logic for all.

WORK PACKAGES:
All four and their dependency structure.

SOURCES:
Variant APP-WPSTR-v1; PI answer C2, adopt.

OPEN QUESTIONS:
None.

INSTRUCTIONS:
The sentence naming WP4 as not the contribution appears here and in WP4; identical framing, different sentences.

OWNER:
Drafting session.

DUE:
Wave 2.

## PREP: Approach :: Building on previous work  [APP-PREV]

TAKEAWAY:
The reviewer sees exactly what is de-risked and what genuinely remains open: published monolithic integration at 2 A, a characterised floating-domain platform, an adiabatic lineage above 99 per cent with a 400 V machine already driven closed-loop, and open questions that are precisely RQ1 to RQ5, no more and no less.

REQUIRED POINTS:
The published die: 15.2 mm2, 130 nm BCD, 2 A and about 26 V, DC to 5 kHz, measured 50 to 66 degrees Celsius loaded, modelled 1.522 W at 2 A and 10 kHz; hard-switched, integration precedent only.
The level-shifter platform with measured nanosecond figures and simulation results stated as simulation.
The adiabatic lineage: DCAT above 99 per cent; the thesis eight-tap 400 V composition at 98.8 per cent; the closed-loop 4 kW-rated 400 V induction machine drive.
The thesis future-work statement naming motor loads at scale, and the volume argument for integration.
Integrated motor drives shorten the partition; this programme dissolves it.

EVIDENCE:
Every number carries its measurement condition; simulation and measurement are never blended; the packaging-versus-architecture distinction closes the part.

FACTS:
DIE_MM2, NODE from the registry; [1], [2], [3], [4] as the lineage; [15], [16], [17] as the IMD state of the art.

FIGURES:
None.

OBJECTIVES:
Grounds O1 to O3 as feasible.

WORK PACKAGES:
Evidences WP2 and WP3 starting points.

SOURCES:
Variant APP-PREV-v1; dossier digests for the BTMLC, TCAS-I and Kolahian records.

OPEN QUESTIONS:
Whether the BTMLC thesis is quoted directly, which would add reference 32 per the REF-MAP rule.

INSTRUCTIONS:
Anonymisation holds: group authors appear as the group's work in body text, real names only in the reference list; the hard-switched versus adiabatic inheritance split is never blurred.

OWNER:
Drafting session.

DUE:
Wave 2.

## PREP: Approach :: Maximising translation of outputs  [APP-TRANS]

TAKEAWAY:
Translation has three concrete routes: open publication behind a dual-use screen, certification-facing evidence addressed to the vertical-lift condition, and partner channels into industrial practice, with the adjacent higher-readiness environment cited as destination and never as commitment.

REQUIRED POINTS:
Publication of methodology, controllability results and datasets, screened as described under Ethics.
Certification route: the failure-behaviour evidence speaks to SC-VTOL-01.
Partner routes: Eaton advisory on certification and industrialisation; flagged standards roles.
The separateness caveat on the adjacent programme, verbatim discipline.
IP through UCL's standard channels, flagged.

EVIDENCE:
Each route names who receives what artefact; supply-chain language is limited to what the partners evidence.

FACTS:
[23] for the condition; partner facts per PRT-LTRS.

FIGURES:
None.

OBJECTIVES:
Carries O1's methodology and O4's evidence outward.

WORK PACKAGES:
Consumes D3.4 and D4.4.

SOURCES:
Variant APP-TRANS-v1.

OPEN QUESTIONS:
Eaton standards-committee roles and IP arrangements, both flagged byte for byte.

INSTRUCTIONS:
Exploitation vocabulary stays modest at TRL 1 to 3; no licensing revenue projections; the caveat sentence is non-negotiable.

OWNER:
Drafting session.

DUE:
Wave 2, closing the Approach pass.

## PREP: Applicant and Team Capability :: PI track record  [CAP-PI]

TAKEAWAY:
The PI is read as capable of delivering this specific programme because its enabling lineage already happened under his direction: the published per-slot die, the floating-domain platform, the adiabatic converter family through to a closed-loop 400 V machine drive, and prior EPSRC doctoral investment carried forward rather than left on the bench.

REQUIRED POINTS:
The completed silicon and converter lineage as directed research, not a publication list.
EPSRC studentship EP/T517793/1 named as prior investment, per the B10 answer.
Supervision through to the doctoral works underpinning the platform.
Industrial engagement including the Eaton relationship, framed as relationship, never commitment.

EVIDENCE:
Capability is evidenced by delivered artefacts with dates and venues; the reference list carries the real names while body text stays anonymised.

FACTS:
DIE_MM2, NODE from the registry; [1], [2], [3], [4]; grant number EP/T517793/1.

FIGURES:
Not applicable.

OBJECTIVES:
Credibility for O1 to O3.

WORK PACKAGES:
WP2 and WP3 leadership.

SOURCES:
Variant CAP-PI-v1; dossier publication digests.

OPEN QUESTIONS:
Additional PI track-record items, grants held and leadership roles remain flagged; roughly this block's share of the 500-word Capability headroom waits on them.

INSTRUCTIONS:
Delivery framing throughout: verbs of building and directing, not of publishing; nothing invented to fill the flagged space.

OWNER:
PI supplies items; drafting session weaves.

DUE:
Wave 3; the PI's evidence is the pacing item.

## PREP: Applicant and Team Capability :: Co I: electrical machines  [CAP-ASEF]

TAKEAWAY:
Dr Asef covers the precise gap WP1 opens: machine design and optimisation for a winding that must be actuator, distribution network and thermal object at once, with the slot and rotor trades as his first-year deliverables.

REQUIRED POINTS:
The gap named: winding geometry for bilateral access, slot-count and rotor trades, the electromagnetic layer of the shared model.
Why the project needs it: no drive-side expertise substitutes for machine electromagnetics at this coupling depth.
Co-supervision of the flagged doctoral student across WP1 and WP3.

EVIDENCE:
Two or three named outputs or grants once supplied; until then the structural claim stands and the flag holds the space.

FACTS:
Not applicable beyond WP1's parameters already prepared.

FIGURES:
Not applicable.

OBJECTIVES:
O1.

WORK PACKAGES:
WP1 lead.

SOURCES:
Variant CAP-ASEF-v1.

OPEN QUESTIONS:
The named-outputs flag for Dr Asef, byte for byte; any hairpin, variable-pole or aerospace-machine work is the highest-value evidence.

INSTRUCTIONS:
Gap-first structure: the project's need defines the paragraph, the person answers it.

OWNER:
PI supplies evidence; drafting session writes.

DUE:
Wave 3.

## PREP: Applicant and Team Capability :: Co I: thermal management  [CAP-EVERT]

TAKEAWAY:
Dr Everts covers the gap RQ5 opens and WP4 must close: integrated circuits cohabiting a winding at 120 to 150 degrees Celsius within a junction class of 150 to 175 degrees Celsius, end-face packaging and cooling, and the thermal layer of the model through the 100 kW campaigns.

REQUIRED POINTS:
The gap named: coupled thermal behaviour, packaging, validation-scale thermal management.
Why the project needs it: H4 fails or passes in this discipline.
WP4 leadership and the WP2 thermal strand.

EVIDENCE:
Named outputs or grants once supplied; the flag holds the space.

FACTS:
WIND_C, JUNC_C, DEMO_KW from the registry.

FIGURES:
Not applicable.

OBJECTIVES:
O4; underwrites H4.

WORK PACKAGES:
WP4 lead; WP2 thermal strand.

SOURCES:
Variant CAP-EVERT-v1.

OPEN QUESTIONS:
The named-outputs flag for Dr Everts, byte for byte; electronics-cooling or two-phase work is the highest-value evidence.

INSTRUCTIONS:
Gap-first structure as for CAP-ASEF; no invented specialisms.

OWNER:
PI supplies evidence; drafting session writes.

DUE:
Wave 3.

## PREP: Applicant and Team Capability :: Team fit and industrial partnership  [CAP-FIT]

TAKEAWAY:
The team is the co-design problem made flesh, one named owner per research question working against one shared model from month 1, and the partnership is scaled to TRL 1 to 3: conditional co-investment in the silicon, certification advisory, airframer review, both letters secured.

REQUIRED POINTS:
Three disciplines the partition kept apart, now one structure.
Every research question has a named owner.
Eaton: conditional 50,000 pounds, certification and industrialisation advisory, studentship support.
Airbus: requirements and operating-environment review.
Letters secured; the adjacent programme cited as relationship with the separateness caveat.

EVIDENCE:
Fit shown through the RQ-to-owner map, not adjectives; partner value shown through the specific contributions PRT-LTRS tables.

FACTS:
TAPEOUT_GBP from the registry; letters-secured status per C7a and C7b.

FIGURES:
Not applicable.

OBJECTIVES:
Delivery credibility across all five.

WORK PACKAGES:
All four.

SOURCES:
Variant CAP-FIT-v1; PI answers C7a, C7b.

OPEN QUESTIONS:
Contribution form and named contacts, flagged byte for byte.

INSTRUCTIONS:
The whole-more-than-parts claim is demonstrated by the map and never stated as a slogan.

OWNER:
Drafting session.

DUE:
Wave 3.

## PREP: Applicant and Team Capability :: Full R4RI section draft  [CAP-R4RI]

TAKEAWAY:
The assembled section reads as one team told across the four UKRI headings, verified group lineage carrying the ideas module, development and community modules honest about what is evidenced versus flagged, and roughly 500 words of headroom explicitly reserved for the personal items still owed.

REQUIRED POINTS:
The four module headings in UKRI's order, exact strings verified against the live Funding Service form at assembly.
Team-woven per the D1 answer: individuals appear where the evidence sits.
Ideas module: the silicon and converter lineage plus EP/T517793/1.
Development, community and users modules with flags where personal evidence is owed.
The headroom sentence and word count stated.

EVIDENCE:
Everything in the ideas module is publication-anchored; nothing in the other modules is asserted beyond what the PI has supplied.

FACTS:
As CAP-PI; word budget 1,500 with about 520 currently drafted.

FIGURES:
Not applicable.

OBJECTIVES:
Not applicable.

WORK PACKAGES:
Not applicable.

SOURCES:
Variant CAP-R4RI-v1; the four person-based CAP variants as raw material.

OPEN QUESTIONS:
Heading-string verification; all personal-evidence flags; destinations, joint activity, community service and outreach flags, each byte for byte.

INSTRUCTIONS:
Modules are mandatory structure; within them, prose only, no bullets; the person-based variants feed this part and must never contradict it.

OWNER:
PI evidence; drafting session assembles.

DUE:
Wave 3; final assembly Wave 4.

## PREP: Resources and Cost Justification :: Staff resources  [RES-STAFF]

TAKEAWAY:
Staffing maps to effort where the contribution is created: PI at 12.5 per cent on the two centres of gravity, Co-Is at 7.5 per cent each on their work packages, one full-time PDRA per centre of gravity, and a co-funded student flagged pending the Eaton-supported agreement.

REQUIRED POINTS:
PI 12.5 per cent, 36 months, WP2 and WP3.
Dr Asef and Dr Everts, 7.5 per cent each, 36 months.
PDRA-A machines and power integration, 36 months; PDRA-B control, 33 months from month 4; both flagged as the drafting proposal under C1.
Co-funded student in collaboration with Eaton as industrial support, flagged.
Hours-per-week equivalents stated alongside FTE where the form requires.

EVIDENCE:
Each post is justified by the deliverables it carries, named by identifier.

FACTS:
PI_FTE, COI_FTE from the registry; PDRA plan flag; studentship flag.

FIGURES:
The staff table once figures land, produced at assembly.

OBJECTIVES:
Resourcing for O1 to O5.

WORK PACKAGES:
All four, mapped per post.

SOURCES:
Variants RES-STAFF-v1 and RES-FULL-v1; PI answers C3, C5.

OPEN QUESTIONS:
PDRA plan and studentship flags, byte for byte; hours-per-week conversion convention to confirm with UCL Research Services.

INSTRUCTIONS:
No post exists without named deliverables; UCL Research Services owns the EC activities section and is not duplicated here.

OWNER:
PI figures; drafting session writes.

DUE:
Wave 3.

## PREP: Resources and Cost Justification :: Equipment and consumables  [RES-EQUIP]

TAKEAWAY:
Every item ties to a work-package activity: the 50,000 pound fabrication run realising O2 with Eaton's conditional match recorded under partners, demonstrator materials awaiting an estimate, laboratory operations including the 1 kV safety provisions, and nothing re-purchased that the existing base covers.

REQUIRED POINTS:
Multi-project-wafer run, 50,000 pounds project-funded, T2.2.
Eaton's conditional 50,000 pounds under partner contributions, expanding scope not enabling it.
Demonstrator materials: stator, rotor, 64 modules, packaging, instrumentation, flagged estimate.
Operations: dynamometer and reduced-pressure campaigns, 1 kV safety, consumables, flagged figures, procured facility access if the APL confirmation finds a gap.
Travel and dissemination, flagged figures.

EVIDENCE:
The no-duplication claim is evidenced by naming what is deliberately absent: benches, tooling, the early rig.

FACTS:
TAPEOUT_GBP, MODULES, BUS_V from the registry; all other figures flagged.

FIGURES:
Cost table at assembly once figures land.

OBJECTIVES:
O2 and O4 chiefly.

WORK PACKAGES:
WP2 and WP4 dominate; WP1 coupon costs included.

SOURCES:
Variants RES-EQUIP-v1, RES-FULL-v1; PI answer C4.

OPEN QUESTIONS:
Demonstrator materials estimate, operations figures, travel figures, contribution form, all byte for byte.

INSTRUCTIONS:
Not a shopping list: each item's sentence names its work package and deliverable or it does not appear.

OWNER:
PI figures; drafting session writes.

DUE:
Wave 3.

## PREP: Resources and Cost Justification :: Justification narrative  [RES-JUST]

TAKEAWAY:
Value for money is argued structurally: every cost maps to a deliverable, the fabrication run is matched by industry, and the absence of infrastructure purchases is itself the argument that the request funds only what the existing base cannot supply.

REQUIRED POINTS:
Cost-to-deliverable mapping stated as a rule and then honoured item by item.
The run as O2's physical realisation, industry-matched.
The deliberate absences named.

EVIDENCE:
The narrative cites the same identifiers as STAFF and EQUIP; no number appears here that is not there.

FACTS:
As RES-EQUIP; nothing new introduced.

FIGURES:
Not applicable.

OBJECTIVES:
All, through the mapping rule.

WORK PACKAGES:
All.

SOURCES:
Variant RES-JUST-v1.

OPEN QUESTIONS:
Inherits every RES flag; adds none.

INSTRUCTIONS:
Never restate costs with different numbers; divergence between RES parts is the failure mode this part exists to prevent.

OWNER:
Drafting session.

DUE:
Wave 3.

## PREP: Resources and Cost Justification :: Full section draft  [RES-FULL]

TAKEAWAY:
The assembled section within 1,000 words, mirroring STAFF, EQUIP and JUST without divergence, with word count stated and flags intact until the PI's figures land.

REQUIRED POINTS:
Staff, equipment and fabrication, operations, travel, justification of scale, in that order.
Every flag from the three source parts reproduced byte for byte.
Word count stated at the end.

EVIDENCE:
Assembly fidelity: a reviewer comparing this to the source parts finds no contradiction.

FACTS:
Union of the section's registry facts; no new numbers.

FIGURES:
The section's tables at assembly.

OBJECTIVES:
As the section.

WORK PACKAGES:
All.

SOURCES:
Variant RES-FULL-v1 as the current assembled state.

OPEN QUESTIONS:
The flagged figures gate completion to the 1,000-word limit.

INSTRUCTIONS:
This part is derivative by design; it changes only when its sources change.

OWNER:
Drafting session.

DUE:
Wave 3 close, refreshed Wave 4.

## PREP: Ethics and RRI :: Ethics and RRI statement  [ETH-RRI]

TAKEAWAY:
Proportionate but serious: no human, animal or personal-data issues, and instead a genuinely engaged dual-use position with a working screen, environmental responsibility designed into the machine choice and the laboratory practice, and research integrity that pre-commits to publishing negative branches.

REQUIRED POINTS:
AREA framework as structure.
Dual use engaged, not denied: civil purpose, defence adjacency admitted, pre-publication export-control screen through UCL governance, methodology published at design-science level.
Partners engaged in screening, flagged arrangements.
Environment: enabling technology for Jet Zero; rare-earth-free rotor option held open; demonstrator and silicon designed for reuse; energy recovery on the back-to-back configuration.
Integrity: preregistered measurement protocols, open datasets at final milestones, the RQ4 negative branch as publishable success.
Development and EDI: cross-disciplinary training, UCL recruitment practice.

EVIDENCE:
The screen is described as a process with a trigger and an owner, not a value statement.

FACTS:
DEMO_KW for the campaigns; [24] for the policy anchor.

FIGURES:
Not applicable.

OBJECTIVES:
Governs the release of O1's and O4's outputs.

WORK PACKAGES:
Cross-cutting.

SOURCES:
Variant ETH-RRI-v1 at full dual-use weight per the D4 answer.

OPEN QUESTIONS:
Partner-specific review arrangements, flagged byte for byte; about 130 words of headroom to the 500 held for them.

INSTRUCTIONS:
Full weight per D4 but within 500 words; no boilerplate sentence survives that could appear in any other proposal unchanged.

OWNER:
Drafting session, PI sign-off.

DUE:
Wave 3.

## PREP: Facilities :: Facilities statement  [FAC-FACS]

TAKEAWAY:
Two sentences establishing that no EPSRC national facility is required and that the build and test happen on UCL Advanced Propulsion Laboratory infrastructure and standard commercial services, with brevity read as confidence because the substance lives under Approach and Resources.

REQUIRED POINTS:
No EPSRC national facility required.
UCL APL and standard commercial fabrication carry all experimental work, cross-referenced to Approach and Resources.

EVIDENCE:
Not applicable; the cross-references are the evidence.

FACTS:
Not applicable.

FIGURES:
Not applicable.

OBJECTIVES:
Not applicable.

WORK PACKAGES:
Not applicable.

SOURCES:
Variant FAC-FACS-v1, 26 words as filed.

OPEN QUESTIONS:
Whether the funder's form imposes a minimum content beyond the statement; check at assembly.

INSTRUCTIONS:
Resist expansion; the deliberate brevity is the strategy and the APL specifics stay in APP-APL.

OWNER:
Drafting session.

DUE:
Wave 3, trivially.

## PREP: Project Partners :: Partner contributions and letters  [PRT-LTRS]

TAKEAWAY:
Both partnerships are specific, valued and matched to secured letters: Eaton's conditional 50,000 pounds toward the fabrication run plus certification and industrialisation advisory and studentship support, Airbus's airframer review of requirements and operating environment, all advisory and evidential in character as a TRL 1 to 3 programme warrants.

REQUIRED POINTS:
Eaton: letter secured; conditional 50,000 pounds, form flagged; advisory role drawing on the adjacent-programme description with the separateness caveat; studentship support, flagged.
Airbus: letter secured; requirements and environment review; quarterly participation; specifics from the letter, flagged.
The template table completed from the letters at assembly: name, contribution type, value, period.
IP obligations rest with the applicant team, terms flagged.

EVIDENCE:
Every contribution in the table traces to a sentence in a letter; nothing appears that the letters do not support.

FACTS:
TAPEOUT_GBP; letters-secured status per C7a, C7b; contacts to follow per C7c.

FIGURES:
The mandated partner template table.

OBJECTIVES:
Underwrites O2's matched funding and the translation route.

WORK PACKAGES:
WP2 co-investment; programme-level review.

SOURCES:
Variant PRT-LTRS-v1; the letters themselves once transcribed.

OPEN QUESTIONS:
Named contacts, contribution form and categorisation, Airbus specifics, IP terms, each flagged byte for byte.

INSTRUCTIONS:
The separateness caveat verbatim wherever the adjacent programme appears; valuations only from the letters, never estimated by the drafting session.

OWNER:
PI transcribes letters; drafting session completes the table.

DUE:
Wave 3; table finalised Wave 4.

## PREP: References :: Reference list  [REF-LIST]

TAKEAWAY:
The list is reconciled with every inline key in the delivered set, DOIs appear only where verified, real author names live here while body text stays anonymised, and every entry still awaiting an exact string says so rather than approximating.

REQUIRED POINTS:
Canonical 31-entry list in the meaning-keyed order.
Verified DOIs as filed; no DOI ever asserted that cannot be checked.
Flagged carry-overs from the old References file: entries 1, 4, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19, 20, 21.
TCAS-I final metadata and the AIBN report number flagged.
Group-author entries with real names per the dossier convention.

EVIDENCE:
Reconciliation is demonstrable: a script pass confirms every inline [n] in the assembled text resolves to an entry and no entry is uncited.

FACTS:
The list itself as filed in REF-LIST-v1.

FIGURES:
Not applicable.

OBJECTIVES:
Not applicable.

WORK PACKAGES:
Not applicable.

SOURCES:
Variant REF-LIST-v1; drafts/06_References.md for carry-over strings; dossier verification notes.

OPEN QUESTIONS:
All carry-over flags; whether the BTMLC thesis enters as 32 per the map rule.

INSTRUCTIONS:
No hyperlinks; within the 1,000-word budget; the anonymisation boundary is the list edge and is never crossed inward.

OWNER:
PI supplies carry-over strings; drafting session reconciles.

DUE:
Wave 4, at assembly with the citation audit.

## PREP: References :: Citation renumbering map  [REF-MAP]

TAKEAWAY:
The meaning-to-number map is the single authority for citation identity: older drafts renumber by matching meaning and never by matching old numbers, and the map decides membership questions such as the thesis entry before they can corrupt the list.

REQUIRED POINTS:
The full key-to-number map as filed, BTMLC-IC equals 1 through AIBN-LN-OJF equals 31.
The renumbering rule stated as a rule.
The conditional entry 32 for the BTMLC thesis, only if a direct quotation survives assembly.

EVIDENCE:
The map's authority is demonstrated by using it: any legacy text merged into Forge is renumbered against it and the diff is checkable.

FACTS:
The map as filed in REF-MAP-v1.

FIGURES:
Not applicable.

OBJECTIVES:
Not applicable.

WORK PACKAGES:
Not applicable.

SOURCES:
Variant REF-MAP-v1.

OPEN QUESTIONS:
The entry-32 decision, flagged.

INSTRUCTIONS:
The map is metadata, not proposal prose; it is stripped at assembly and its rule survives in the drafting workflow.

OWNER:
Drafting session.

DUE:
Wave 4, with the reference reconciliation.
