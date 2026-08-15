---
name: repository-archaeology
description: Reverse-engineer creative software repositories, archives, and agent-skill systems to explain their purpose, execution, reusable patterns, failures, and proprietary design opportunities. Use when comparing projects, auditing uploaded code, studying GitHub repositories, or converting several experiments into one coherent system.
---

# Repository Archaeology

Use this skill when the user wants to understand what a collection of repositories or archives was made for, how the pieces work, what they actually do versus claim to do, and how to synthesize a new proprietary architecture.

## Operating principles

- Read before redesigning. Do not infer purpose from filenames alone.
- Separate stated intent, observed behavior, and proposed improvement.
- Treat authored projects and external references with the same analytical rigor.
- Preserve provenance: repository, branch, path, commit, archive, source, and generated output.
- Never expose, copy, or relocate secrets. Replace code-level secret exposure with runtime configuration.
- Do not confuse an agent role, a skill instruction set, a library, and an MCP service.
- Prefer semantic contracts and provider-neutral interfaces over one vendor's implementation.

## Workflow

### 1. Establish scope

Record every input: repository URL and branch, uploaded archive path, requested outcome, available tools, and whether the task is analysis-only or includes changes. Identify the authoritative branch before reading files.

### 2. Inventory the artifact

List the archive or repository tree. Locate README files, design documents, package manifests, environment templates, entry points, source directories, tests, examples, assets, generated outputs, and deployment configuration. Do not begin with random deep files.

### 3. Read in layers

Read in this order:

1. README and project metadata for stated intent.
2. Dependency and deployment files for runtime reality.
3. Entry points and routes for execution flow.
4. Core transformation modules for data movement.
5. UI, exporters, and storage for user-facing behavior.
6. Tests, examples, screenshots, and outputs for evidence.

For each file, record: inputs, outputs, side effects, external services, state changes, failure behavior, and unresolved assumptions.

### 4. Trace the pipeline

Map the actual flow as:

`intent -> input model -> parsing -> orchestration -> provider call -> transformation -> storage -> export -> review`

When the project is creative, also map:

`brief -> world/canon -> character identity -> beat -> panel/shot -> prompt -> asset -> composition -> publication`

Mark every boundary where structure is lost, such as free text becoming regex output, images losing prompt metadata, or UI state becoming a PDF with no semantic manifest.

### 5. Apply review lenses

Select only relevant available GitHub agent-skills or local skills. Use them as explicit lenses:

- repository/software archaeology: intent versus implementation
- security: secrets, trust boundaries, unsafe defaults
- creative systems: visual grammar, typography, layout, narrative rhythm
- frontend design: hierarchy, distinctiveness, motion, density, responsive behavior
- agent architecture: roles, handoffs, tool contracts, state, validation
- testing: executable claims, fixtures, regression coverage, reproducibility
- publishing: provenance, licensing, packaging, deployment readiness

If a named skill is unavailable, use the lens as a documented fallback; never claim it was invoked.

### 6. Produce a per-project dossier

For each project, document:

- purpose and audience
- actual entry point and execution path
- input/output contracts
- core modules and dependencies
- state and storage model
- creative decisions automated versus manual
- strengths
- limitations and technical debt
- security and provenance findings
- reusable patterns
- patterns to reject

Use source paths and links when available. Distinguish verified facts from inference.

### 7. Compare without flattening

Build a matrix across narrative, visual generation, composition, UI, storage, finishing, delivery, continuity, provenance, security, and testability. Do not call one project the universal foundation unless its boundaries actually cover the requested system.

### 8. Synthesize the proprietary system

Derive a provider-neutral semantic core. Define canonical objects such as Storyworld, Character, Realm, Motif, Beat, Panel, Asset, Publication, and Review. Define states such as proposed, observed, canon, generated, needs_revision, approved, published, and superseded.

Adapters may wrap LLMs, image providers, PDF libraries, Canvas, Firebase, colorizers, super-resolution models, or video services. The proprietary value should remain in canon, identity, psychology, progression, visual grammar, evidence, continuity, provenance, and publication logic.

### 9. Validate the synthesis

Check that the proposed system:

- can reproduce an output from its manifest
- can identify why an output was generated
- can show uncertainty and failed assets
- can preserve character and motif continuity
- can target comic, manga, webtoon, graphic novel, and motion formats
- can replace providers without changing storyworld data
- can run without secrets in source or browser bundles

## Output format

Return, as appropriate:

1. scope and evidence boundary
2. per-project dossiers
3. execution-flow diagrams or tables
4. comparative capability matrix
5. security and provenance findings
6. reusable versus rejected patterns
7. proprietary architecture
8. schemas, adapter boundaries, and roadmap
9. confidence and unresolved questions

Do not create an auxiliary README or generic summary when the user requested the skill itself. Keep detailed domain references in the bundled references directory and deterministic helpers in scripts.

## Bundled references

- Read `references/review-lenses.md` when selecting agent or skill lenses.
- Read `references/dossier-template.md` when producing repeatable repository reports.
- Use `scripts/inventory_archive.py` for deterministic archive inventory before interpretation.
- Read `references/agent-skills-integration.md` to choose process, engineering, organization, and creative lenses from the source agent-skills repository.
- Read `references/agent-role-cards.md` when orchestrating multiple analytical roles.
- Read `references/creative-comic-lenses.md` for comic, manga, webtoon, visual, and taste-aware review.
- Read `references/verification-protocol.md` before reporting completion or confidence.

