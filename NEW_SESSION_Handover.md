# FRESH-SESSION HANDOVER — EPSRC PROPOSAL CAMPAIGN
## "Foundations of Monolithically Integrated Per-Slot Machine Drives for Reconfigurable Aerospace Propulsion"

*Paste this file as the opening message of a NEW session to take over the proposal campaign with zero context loss. Last updated: 1 August 2026.*

## 0. Which Claude surface to use — read this first

Only a **Claude Code session** (claude.ai/code, the CLI, or the desktop app) can commit and push to GitHub. A regular claude.ai chat page can at most READ repository files into project knowledge; it cannot write. Therefore:
- To continue with full GitHub capability: start a **Claude Code session** connected to the repository `me313b/proposal`, working branch `claude/epsrc-vision-approach-library-6qr50k`, and paste this document.
- A regular chat page is fine only for throwaway drafting riffs; anything worth keeping must be routed back into the repository via a Claude Code session or via Forge's Push.

## 1. The system (three surfaces, one source of truth)

- **GitHub repo `me313b/proposal`** (PRIVATE), branch `claude/epsrc-vision-approach-library-6qr50k` — CANONICAL for all proposal text. `main` holds only the PI's raw source uploads.
- **The Claude Code session** — sole writer of `drafts/`, `exports/`, `tools/`. Drafts, verifies against primary sources, exports, and serves the two Forge commands (§4).
- **Forge (EPSRC Workbench)** at `https://mb-vault.vercel.app/` — the PI's single-file web app for reading variants and making decisions; sole writer of `forge/` in the repo (`forge/DECISIONS.md` + `forge/state.json` via its Push). Forge is CANONICAL for decisions (chosen/rejected variants, directives); the repo is canonical for text.

## 2. Repository map

| Path | Content |
|---|---|
| `drafts/00_STATUS_and_Decisions.md` | START HERE: decision list, corrections applied from primary sources, consolidated [PI TO CONFIRM] checklist |
| `drafts/01…10_*.md` | All application sections, drafted with variants, four quality passes done (compliance-verify, revise, consistency, primary-source cross-check) |
| `drafts/gantt.html` | Print-verified one-page A4-landscape Gantt |
| `exports/FORGE_Import.md` | The draft package in Forge's exchange format (regenerate ONLY via `tools/make_forge_import.py`) |
| `exports/` (others) | Word package, Gantt PDF, integration brief, handover bundle |
| `tools/make_forge_import.py` | Deterministic Forge-export generator; run from repo root |
| `EPSRC_Master_Handover.md` | THE RULEBOOK: concept, S3 parameter table (all numbers must match it), S4 EPSRC format/voice rules, settled Vision text, evidence base, reference plan |
| `EPSRC_References_Handover.md`, `HANDOVER_2_…` | Source-by-source evidence notes |
| `EPSRC_Vision_Approach_Library.md` | Every superseded framing/variant (the menu) |
| PDFs, QFT.txt, docx | Primary sources: BTMLC paper (published: TPEL 41(8):12842-12854, Aug 2026), TCAS-I level-shifter paper, three doctoral theses, transfer viva, SkyDrive appendices |

## 3. Standing rules (digest — full versions in EPSRC_Master_Handover.md S3/S4)

UK English; Arial 11 destination; no em dashes in new Vision-arc text; no bullets in proposal prose; never "novel"/"innovative" standalone; never "this project will investigate"; problem before solution; acronyms expanded per section; every technical number from the S3 table exactly (270 V bus; 20–50 V per slot; ~200–300 V Paschen at quarter-atmosphere; 4–15×; 5–15 kW; 6,000–10,000 RPM; 18 slots; 6–9 sections; ~89% vs ~58%; 15.2 mm² BTMLC; >99% DCAT); unconfirmed facts flagged `[PI TO CONFIRM: …]`, never invented; anonymisation: the surnames Farhat, Tazehkand, Kolahian, Edwards, Grimm never appear in proposal text (use [Author]/"the group's work"); PI (Dr Mehdi Baghdadi) and Co-Is (Dr Pedram Asef, Dr Marilize Everts) appear normally. SkyDrive (100 kW, 18,000 RPM, partners ARC Aerosystems + iNetic, Eaton as non-funded Tier-1 adviser) is translation context ONLY, never the research target.

## 4. The Forge command contract (verbatim obligations)

- **"export to GitHub for Forge"** (aliases: "export for Forge", "push the drafts for Forge"): run `python3 tools/make_forge_import.py` from the repo root, commit `exports/FORGE_Import.md` with message `Drafts: regenerate Forge import (<n> blocks)`, push, confirm block count + short SHA. Without write access: paste the full file content into chat instead and say so.
- **"read Forge"** (alias: "apply Forge decisions"): read `forge/DECISIONS.md` (+ `forge/state.json` for detail); treat as authoritative for chosen/rejected variants, directives and tasks; apply directives to `drafts/`; honour chosen text as settled; never resurrect rejected variants; then run the export command; confirm with a one-line digest.
- Boundaries: session writes `drafts/`, `exports/`, `tools/` only; Forge writes `forge/` only.

## 5. State at handover

**Done:** all sections drafted with variants; primary-source verification complete (key corrections: partner is ARC Aerosystems not "ARC Additive"; BTMLC citation now final published form; TCAS-I 17×/22–66× figures are post-layout simulation, not silicon measurements; the thesis behind the BTMLC is dated Nov 2025 and lists motor/inductive-load testing verbatim as future work; no published "Edwards IMD review" exists — use Abebe et al. IET EPA 2016 / Lee et al. IEEE TTE 2018 / Jahns & Sarlioglu 2020 as candidates); Gantt print-verified; exports current; Forge import at 39 blocks (commit 985d38e).

**In flight at handover:** a full Vision revision on the Forge four-move arc (Opening: stand beside the expert / The unseen line / Crossing: the 50 V claim / The cascade and its price / Timeliness: ATI collision / National importance), written to EPSRC register WITHOUT metaphor conceits (the PI rejected "taxes/currencies" framing), with the gearbox stated clearly as a power-density/reliability challenge and multiphase machines acknowledged with their duplication cost. If `drafts/02_Vision_ArcRevision.md` exists in the repo, that revision landed (the generator auto-includes it); if not, it must be re-run.

**Waiting on the PI:** Vision opening choice (A/B/C/hybrid) — superseded by the arc revision if adopted; variant selections per section; WP skeleton sign-off; the `[PI TO CONFIRM]` checklist in `drafts/00_STATUS_and_Decisions.md` §5 (letters of support, FTEs, dynamometer envelope, missing DOIs, ATI/ADS editions).

## 6. Working mode the PI wants

Options over single guesses: for every section produce several EPSRC-style variants to choose from. Verification-heavy: never state a measured number without a source in the repo. Literature-grounded: reference gaps are resolved by finding and verifying real published sources (record findings in `drafts/06_References.md` with full bibliographic detail; keep `[PI TO CONFIRM]` until the PI signs off). Everything worth keeping lands in the repository as a commit.
