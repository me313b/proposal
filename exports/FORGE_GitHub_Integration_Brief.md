# REQUEST: CONNECT FORGE (EPSRC WORKBENCH) TO GITHUB
## Integration brief for the page building Forge — paste this whole document into that conversation

You are working on **Forge**, a single-file HTML app ("Forge · EPSRC Workbench") that manages an EPSRC proposal as sections → parts → variants, with state in `localStorage`, an import wizard (`parseStructuredMD`), and a compose-for-Claude feature. Your task: **add two-way GitHub synchronisation** so Forge pulls the latest proposal drafts from the repository and pushes its decisions and backups into it. Every fact you need is below; do not invent repository details.

---

## 1. The repository (the other half of the link)

- **Repo:** `me313b/proposal` — **PRIVATE** (this drives every design decision below)
- **Working branch:** `claude/epsrc-vision-approach-library-6qr50k` (do NOT default to `main`; `main` holds source uploads only)
- **Maintained by:** a Claude Code session that drafts and verifies the proposal content, keeps the repo canonical, and regenerates Forge's import file whenever drafts change.

**File inventory Forge cares about (all on the working branch):**

| Path | What it is | Forge's use |
|---|---|---|
| `exports/FORGE_Import.md` | The ENTIRE draft package pre-converted to Forge's own exchange format — 39 variant blocks (`## PART: Section :: Part` / `### VARIANT: CODE [status] (source)`), verified against Forge's `parseStructuredMD` logic | **The pull target.** Fetch this one file and feed it to the existing import pipeline |
| `drafts/00_STATUS_and_Decisions.md` … `drafts/10_Facilities.md` | The 11 canonical section drafts (markdown) | Optional per-file pull for reference viewing |
| `drafts/gantt.html` | One-page A4-landscape Gantt | Link out / open in new tab |
| `forge/` (does not exist yet) | **Forge's own directory — Forge is the sole writer** | The push target (see §4) |

**Variant status conventions in the import file:** settled Vision text = `[chosen]` with source `(handover)` (verbatim-locked — Forge must not present it for rewriting); drafted content = `[candidate]` `(claude)`; the partner-contributions skeleton = `[draft]`. `[PI TO CONFIRM: …]` flags inside any text must survive round-trips untouched.

## 2. Hosting — CONFIRMED DEPLOYMENT: `https://mb-vault.vercel.app/`

The user hosts Forge inside their Vercel app at **https://mb-vault.vercel.app/**. Consequences for your implementation:

- **GitHub API sync works from this origin.** `api.github.com` sends `Access-Control-Allow-Origin: *`, so browser `fetch` with the `Authorization` header succeeds from any HTTPS origin. No proxy or backend needed.
- **`localStorage` is scoped to `mb-vault.vercel.app`** — state persists per browser on that origin. If the vault app embeds Forge in an `<iframe>`, the iframe must NOT carry a `sandbox` attribute lacking `allow-same-origin allow-scripts`, or storage and fetch both break; serving Forge as a normal same-origin route/page is safest.
- **PRIVACY WARNING — public URL:** Vercel deployments are public by default; anyone with the URL can open this page. That is acceptable ONLY as long as the proposal text is NOT baked into the HTML. Keep the shipped file content-free (structure/seed only) and load all proposal content at runtime via the GitHub pull — then the unpublished proposal stays behind the user's token and browser. Never embed imported drafts, the user's GitHub token, or chosen text into the deployed HTML. If the user wants content served rather than pulled, the deployment needs access protection first.
- **If a copy is ever hosted as a claude.ai Artifact instead:** artifact CSP blocks ALL external requests (GitHub API and the current Google Fonts links included) — that copy is paste-import only. Inline the fonts or add a system-font fallback stack so the page degrades gracefully either way.

## 3. Authentication — the repo is private

Browser-side calls need a token. Instruct the user (show this in the UI, first-run):

1. GitHub → Settings → Developer settings → **Fine-grained personal access tokens** → Generate new token.
2. **Repository access: "Only select repositories" → `me313b/proposal` only.**
3. **Permissions: Contents → Read and write** (Read-only if the user wants pull-only). Nothing else.
4. Set an expiry (90 days is sensible); paste the token into Forge's Settings.

Storage and safety rules for your implementation:
- Keep the token in `localStorage` under Forge's existing state key or a sibling key; **never bake it into the HTML file** (the file gets shared/uploaded); show it masked; provide a "forget token" button.
- Warn in the UI: anyone with this token can read/write that one repo — treat it like a password.

## 4. The API calls (GitHub REST v3 — all CORS-enabled)

Common headers for every call:
```js
{ "Authorization": "Bearer " + token,
  "X-GitHub-Api-Version": "2022-11-28" }
```

**PULL — fetch the import file (raw):**
```js
const OWNER = "me313b", REPO = "proposal",
      BRANCH = "claude/epsrc-vision-approach-library-6qr50k";
const r = await fetch(
  `https://api.github.com/repos/${OWNER}/${REPO}/contents/exports/FORGE_Import.md?ref=${encodeURIComponent(BRANCH)}`,
  { headers: { ...common, Accept: "application/vnd.github.raw+json" } });
const markdown = await r.text();   // feed to parseStructuredMD → the existing import pipeline
```

**PUSH — write a file (create or update):**
```js
// 1) get current sha (404 → file doesn't exist yet, omit sha)
const meta = await fetch(
  `https://api.github.com/repos/${OWNER}/${REPO}/contents/${path}?ref=${encodeURIComponent(BRANCH)}`,
  { headers: { ...common, Accept: "application/vnd.github+json" } });
const sha = meta.ok ? (await meta.json()).sha : undefined;
// 2) PUT
await fetch(`https://api.github.com/repos/${OWNER}/${REPO}/contents/${path}`, {
  method: "PUT",
  headers: { ...common, Accept: "application/vnd.github+json" },
  body: JSON.stringify({
    message: commitMessage, branch: BRANCH, sha,             // sha only when updating
    content: btoa(unescape(encodeURIComponent(text)))        // UTF-8-safe base64
  })});
```

Notes: authenticated rate limit is 5,000 requests/hour (irrelevant at this usage); base64 the UTF-8 bytes exactly as above or em-dashes and ° signs will corrupt; a `409`/`422` on PUT means the sha went stale — re-GET and retry once.

## 5. The sync contract (what to pull, what to push — keeps two sources of truth sane)

**Design principle: GitHub `drafts/` is canonical for proposal TEXT; Forge is canonical for DECISIONS. Forge never writes into `drafts/`; the Claude Code session never writes into `forge/`.**

- **Pull** (button "Pull from GitHub", plus optional auto-pull on load when a token is present): fetch `exports/FORGE_Import.md` → run the import pipeline. Existing variants with identical `code` should be updated in place rather than duplicated (match on code; if local text differs from incoming and local status is beyond `draft`, keep local and surface a conflict chip instead of overwriting).
- **Push** (button "Push to GitHub"), writing exactly two files:
  1. `forge/state.json` — the full serialized state (`S`), pretty-printed. This is the durable backup that fixes Forge's localStorage fragility.
  2. `forge/DECISIONS.md` — human-readable digest generated from state: per part → chosen variant code + word count, plus open directives, task list with done-flags, and any variant the user marked `rejected` with its code. This file is how the Claude Code session reads Forge's decisions and applies them to the canonical drafts.
- Commit messages: `Forge: push decisions and state backup (<n> chosen, <m> directives)` — no other convention needed.
- Show sync status in the top bar: last pulled / last pushed timestamps and the short commit SHA.

## 6. Other features worth adding while you are in there (requester's wishlist, in priority order)

1. **Markdown table rendering** in `mdBlocks` — the imported risk register, project-plan and citation-map content contains pipe tables which currently render as raw text. A minimal `| a | b |` → `<table>` pass is enough.
2. **Auto-backup nudge** — if state changed and no push/backup for >48 h, show a gentle chip. localStorage is one cache-clear away from data loss; this is the app's biggest real risk.
3. **Chosen-set export** — one button producing a clean markdown document of only the chosen variants in section order (this becomes the assembly draft the repo session turns into the submission PDF).
4. **Verbatim lock enforcement** — variants imported with source `(handover)` are settled text: hide the Edit button behind a confirm ("This text is verbatim-locked from the master handover — edit anyway?").
5. **Style-constraint audit** — Forge's stored constraints say "no em dashes, no bullet points in prose", but the current canonical drafts (and the verbatim-locked settled text) use both. Add a Settings toggle to relax those two rules, or the compose feature will instruct Claude to fight the handover style. Flag this to the user rather than silently choosing.
6. Optional: **ETag polling** (`If-None-Match` on the pull GET, hourly) to show a "new drafts available" chip without a manual pull.

## 7. Acceptance checks (run these before calling it done)

1. With a valid token: Pull → toast reports ~39 variants filed; Vision shows 3 opening candidates + 7 chosen settled parts; no duplicates on a second Pull.
2. Without a token: Pull button disabled with a tooltip pointing at Settings; paste-import still works.
3. Push → `forge/state.json` and `forge/DECISIONS.md` appear on branch `claude/epsrc-vision-approach-library-6qr50k` (verify on github.com); pushing again updates rather than errors (sha handling).
4. A `[PI TO CONFIRM: …]` flag survives pull → edit-nothing → push → re-pull byte-identical.
5. Kill the network: every sync action fails with a readable toast, and no state is lost.
6. Open the file from `file://` and confirm both Pull and Push work (CORS sanity).

---
*End of brief. The repo side of this contract is already live: `exports/FORGE_Import.md` exists and is regenerated on every drafting change, and the maintaining session will read `forge/DECISIONS.md` whenever it appears.*
