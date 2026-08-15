# Origin Story

**Origin Story** is a repository-intelligence skill for understanding how creative software, agent systems, archives, and production pipelines actually work.

It turns unfamiliar code into a usable story:

- what the project is for
- how its parts work together
- what assumptions and boundaries shape it
- which ideas are worth adapting
- which risks, gaps, and technical debt must be addressed
- how the project can contribute to a larger proprietary system

## What it produces

Origin Story builds an evidence-backed repository dossier covering:

1. **Identity** — purpose, users, inputs, outputs, and declared architecture
2. **Structure** — entry points, modules, dependencies, assets, configuration, and runtime paths
3. **Behavior** — how data moves from request to artifact
4. **Creative grammar** — visual style, composition, dialogue, pacing, lore, progression, and genre conventions
5. **Operational reality** — setup, execution, delivery, persistence, and failure modes
6. **Security and reliability** — secrets, credentials, parsing, manifests, provenance, and reproducibility
7. **Comparative value** — strengths, weaknesses, reusable patterns, and architectural boundaries
8. **Synthesis** — a recommended design for the system being built

## Core workflow

```text
Archive or repository
        ↓
Inventory
        ↓
Read the declared intent
        ↓
Trace executable paths
        ↓
Inspect data, assets, and outputs
        ↓
Evaluate creative and engineering behavior
        ↓
Verify claims against evidence
        ↓
Write dossier and synthesis
```

The skill separates **observed facts**, **reasonable inferences**, and **recommendations** so that interpretation never gets mistaken for implementation evidence.

## Repository layout

- `SKILL.md` — operating instructions for the skill
- `agents/openai.yaml` — agent-facing metadata
- `references/review-lenses.md` — technical, creative, security, and systems lenses
- `references/dossier-template.md` — reusable investigation structure
- `references/agent-skills-integration.md` — integration with the AvatarArts agent-skills ecosystem
- `references/creative-comic-lenses.md` — comic, manga, graphic-novel, and story-flow analysis
- `references/agent-role-cards.md` — role boundaries for architecture, security, testing, orchestration, and creative review
- `references/verification-protocol.md` — evidence and completion checks
- `scripts/inventory_archive.py` — archive inventory helper

## Example use

For a ZIP archive:

```bash
python scripts/inventory_archive.py ./project.zip
```

Then investigate in this order:

1. inventory the archive or repository
2. read README files, manifests, configuration, and entry points
3. map the primary execution path
4. inspect schemas, prompts, assets, and generated outputs
5. compare documentation with implementation
6. record security, parsing, and reproducibility issues
7. produce a dossier
8. derive reusable patterns and avoid copying accidental design

## Creative systems focus

Origin Story is designed for repositories that sit between software and authored worlds, including:

- comic and manga generators
- visual novel and graphic-book pipelines
- lore and worldbuilding systems
- evidence-based progression mechanics
- prompt and asset compilers
- agent orchestration frameworks
- image, dialogue, colorization, and publishing tools
- proprietary creative automation systems

It treats story as a system of interacting structures: identity, motive, conflict, evidence, ritual, visual grammar, pacing, continuity, and transformation.

## Relationship to AvatarArts

Origin Story supports the AvatarArts investigation and synthesis workflow. It can help evaluate creator repositories as source material while keeping the final architecture proprietary and provider-neutral.

The goal is not to reproduce any one project. The goal is to understand origins, extract durable principles, and compile them into a coherent system such as the AvatarArts Forge.

## Companion resources

- [AvatarArts Comic Creator Matrix](https://github.com/AvaTar-ArTs/AvatarArts-Comic-Creator-Matrix)
- [AvatarArts agent-skills](https://github.com/AvaTar-ArTs/agent-skills)
- [Installed skill package](https://github.com/AvaTar-ArTs/origin-story)

## Status

Early-stage, actively evolving. Contributions should improve evidence quality, creative analysis, verification, and the clarity of the resulting dossiers.
