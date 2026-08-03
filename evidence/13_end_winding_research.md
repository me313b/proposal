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
