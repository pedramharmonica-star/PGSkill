# AGENTS.md: PayamGostar skills (PGSkill)

Instructions for coding agents and agent frameworks that read `AGENTS.md`, such as OpenAI Codex, Cursor, GitHub Copilot, Gemini CLI, Jules and Aider.

This repository holds **four Agent Skills** (open SKILL.md format). They form a chain, knowledge → rfp-matcher → proposal → contracts, and reference each other by relative path, so keep them side by side:

| Skill | Use when |
|---|---|
| `skills/payamgostar-knowledge/` | Any question about what PayamGostar CRM can or cannot do, where a menu or setting is, which module, edition or version provides a feature, technical or security specs, installation, integrations, or facts for proposals. |
| `skills/payamgostar-rfp-matcher/` | A customer RFP, RFI, tender or feature checklist must be matched row by row against PayamGostar capabilities. |
| `skills/payamgostar-proposal/` | A designed, customer-facing proposal or RFP response PDF (Persian, RTL, A4, PayamGostar brand) is needed. Needs Python, Playwright/Chromium and the brand assets in `assets/`. |
| `skills/payamgostar-contracts/` | A closed deal needs paperwork: pre-invoice, sales contract, installation/training/support contract, SLA annex or NDA. Fills the official .docx templates (`scripts/fill_contract.py`, needs lxml) without changing contract wording. |

## How to use
1. Read the relevant `SKILL.md` **completely** before answering. Its rules are mandatory: no fabrication, "not documented" is not the same as "not available", attach module/version/edition qualifiers, apply source priority, and keep internal notes confidential.
2. Search: `python3 skills/payamgostar-knowledge/scripts/find.py "<question>" --top 8` (add `--json` for structured output). It needs only the Python 3 standard library.
3. Open the cited file under `skills/payamgostar-knowledge/references/` and read the article before making a claim.
4. Answer in Persian unless the user asks otherwise.

If your tool supports skills natively, point it at `skills/`. Otherwise treat this file plus the SKILL.md files as instructions.

For chat products without file-system access (ChatGPT, Gemini, Copilot Studio …) use `portable/` (see `portable/README.md`).

## Adding sources
New raw files go into `incoming/`. `incoming/README.md` lists what is missing and where each file belongs after processing.

## Maintenance
- After editing anything in `skills/`, run `python3 tools/build_portable.py`.
- To refresh the official help center, run `python3 skills/payamgostar-knowledge/scripts/convert_kb.py <PayamGostarDocs clone> skills/payamgostar-knowledge/references/kb <commit>`.
- Do not commit credentials. The converter redacts password and username lines.
