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
