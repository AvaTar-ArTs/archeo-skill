# Owned Systems Research: choTaku and Chozen

**Date:** 2026-08-15  
**Scope:** First-party AvatarArts repositories supplied for comparison with Origin Story and AvatarArts Forge.

## Executive finding

These repositories are not merely additional examples in the research set.

- **choTaku** is currently an empty GitHub repository with no readable README or source tree. It should be treated as an uninitialized or reserved namespace until content is added.
- **chozen-land** contains a far more important architectural signal: a narrative reality system that models context, meaning, canon, graphs, narrative, artifacts, intelligence, and evolution before rendering outputs.

Chozen-land is therefore one of the closest first-party architectural ancestors of the proposed AvatarArts Forge.

Its core flow is:

```text
Context
→ Meaning
→ Canon
→ Graph
→ Narrative
→ Visual DNA
→ Storyboards
→ Prompt Systems
→ Batch Creation
→ Artifacts
→ Intelligence
→ Evolution
```

This complements Origin Story's repository-intelligence workflow:

```text
Observe
→ understand
→ compare
→ extract
→ verify
→ synthesize
```

Together they form a research-to-reality loop.

## 1. choTaku

Repository: [AvaTar-ArTs/choTaku](https://github.com/AvaTar-ArTs/choTaku)

### Observed state

At the time of review:

- repository is public
- default branch is `main`
- GitHub reports an empty Git repository
- no README is available
- no source tree is available
- no implementation behavior can be verified

### Interpretation boundary

No architectural or creative claims should be attributed to choTaku until files, commits, or documentation exist.

The name may eventually become useful as:

- a creator identity or otaku-oriented interface
- a character or brand layer
- a media catalog
- a companion authoring surface
- a consumer-facing experience over Chozen or AvatarArts Forge

For now, the correct action is to preserve the provenance boundary:

```text
Observed: empty repository
Inferred: possible reserved or future project
Not established: purpose, architecture, features, or relationship to Chozen
```

## 2. Chozen-land

Repository: [AvaTar-ArTs/chozen-land](https://github.com/AvaTar-ArTs/chozen-land)

README: [Chozen — Narrative Reality Engine](https://github.com/AvaTar-ArTs/chozen-land/blob/main/README.md)

The repository describes Chozen as a system for building worlds, forging stories, and creating realities. Its stated artifact flow is:

```text
Universe
→ Characters
→ Relationships
→ Lore
→ Scenes
→ Stories
→ Cinematics
→ Exports
```

Its deeper core documentation expands that into:

```text
Context
→ Meaning
→ Canon
→ Graph
→ Narrative
→ Visual DNA
→ Storyboards
→ Prompt Systems
→ Batch Creation
→ Artifacts
→ Intelligence
→ Evolution
```

### Core philosophy

Chozen-land defines several strong principles:

- **Reality first** — model realities before artifacts
- **Meaning before narrative** — stories emerge from meaning
- **Truth before generation** — canon constrains creation
- **Relationships before objects** — connections matter more than isolated assets
- **Artifacts are expressions** — comics, anime, videos, posters, lore, and worlds are manifestations of one reality
- **Evolution is continuous** — every project improves the operating system

These principles are highly aligned with the AvatarArts direction and should be treated as first-party design evidence.

## 3. Chozen ontology

Source: [CHOZEN_ONTOLOGY.md](https://github.com/AvaTar-ArTs/chozen-land/blob/main/docs/CHOZEN_ONTOLOGY.md)

### Context

Context defines why a reality exists:

- purpose
- audience
- intent
- transformation
- constraints

### Meaning

Meaning captures the ideas beneath the narrative:

- themes
- symbols
- motifs
- archetypes
- metaphors
- emotions

### Canon

Canon defines the immutable truths of a reality:

- truths
- rules
- timeline
- glossary
- continuity

### Graph

Graph is the connective tissue of the world.

Node types include:

- Character
- Location
- Theme
- Symbol
- Artifact
- Event
- Scene
- Story

Edge types include:

- loves
- fears
- contains
- causes
- appears_in
- symbolizes
- evolves_into

### Narrative

Narrative organizes paths through:

- universes
- characters
- relationships
- lore
- scenes
- stories
- story arcs

### Artifacts

Artifacts are output manifestations:

- comics
- manga
- anime
- videos
- posters
- lore entries
- books
- games

### Intelligence

Intelligence validates and interprets the system through:

- continuity engine
- lore auditor
- narrative intelligence
- graph validator
- symbolism mapper

### Evolution

Evolution tracks:

- capability gaps
- capability growth
- roadmaps
- ecosystem learning

## 4. Chozen architecture

Source: [ARCHITECTURE.md](https://github.com/AvaTar-ArTs/chozen-land/blob/main/docs/ARCHITECTURE.md)

```text
Input
 ↓
Discovery Engine
 ↓
Universe Forge
 ↓
Character Forge
 ↓
Relationship Graph
 ↓
Lore Engine
 ↓
Scene Graph
 ↓
Story Engine
 ↓
Cinematic Engine
 ↓
Exports
```

This is a meaningful separation of concerns:

| Stage | Responsibility | Output |
|---|---|---|
| Discovery Engine | Extract context and meaning from raw input | Context + Meaning |
| Universe Forge | Establish world rules and themes | Universe |
| Character Forge | Derive identity and conflict from world rules | Characters |
| Relationship Graph | Model tensions between characters | Relationships |
| Lore Engine | Explain rules and histories | Lore |
| Scene Graph | Build connected dramatic units | Scenes |
| Story Engine | Traverse scenes into a story | Story |
| Cinematic Engine | Break scenes into renderable shots | Shots |
| Exports | Materialize the reality in a target format | Artifacts |

## 5. Engine analysis

### Discovery Engine

Source: [engines/discovery-engine.md](https://github.com/AvaTar-ArTs/chozen-land/blob/main/engines/discovery-engine.md)

The Discovery Engine takes raw material such as:

- an idea
- a song
- a conversation
- existing inspiration
- an archive or creative document

It is instructed to read the full source before summarizing, separate signal from contamination, and identify the transformation the audience should undergo.

This is a direct bridge to Origin Story's repository archaeology method:

```text
raw material
→ preserve source
→ identify signal and noise
→ capture intent
→ model meaning
→ hand off structured context
```

### Universe Forge

Source: [engines/universe-forge.md](https://github.com/AvaTar-ArTs/chozen-land/blob/main/engines/universe-forge.md)

It takes Context and Meaning and produces a universe with:

- name
- themes
- history
- technology
- magic or governing law
- cultures
- locations

A particularly strong design rule is that the universe must contain an internal rule explaining why things happen. That rule supplies stakes for later characters and lore.

### Character Forge

Source: [engines/character-forge.md](https://github.com/AvaTar-ArTs/chozen-land/blob/main/engines/character-forge.md)

It produces:

- name
- archetype
- goal
- fear
- wound
- symbol
- voice
- visual signature

The engine explicitly derives character goals, fears, and wounds from the universe's central law rather than from generic archetypes.

This is a major distinction from shallow character generators:

```text
generic archetype
→ personality description
```

versus:

```text
world rule
→ specific possible loss
→ character fear
→ conflicting goal
→ relationship tension
→ scene pressure
```

The visual signature is required to be renderable, not merely atmospheric.

### Relationship Graph

Source: [engines/relationship-graph.md](https://github.com/AvaTar-ArTs/chozen-land/blob/main/engines/relationship-graph.md)

It models:

- character pair
- relationship type
- specific tension
- history
- status

The system correctly identifies tension as the load-bearing field. A label such as “rivalry” or “romance” is not enough; the relationship must specify the disagreement that makes it narratively active.

It also distinguishes:

- resolved
- ongoing
- load-bearing

This creates a foundation for progression, continuity, and scene generation.

### Lore Engine

Source: [engines/lore-engine.md](https://github.com/AvaTar-ArTs/chozen-land/blob/main/engines/lore-engine.md)

The Lore Engine connects universe rules, character history, and relationships.

It distinguishes:

- cosmological law
- myth
- ordinary history

That distinction is crucial because a cosmological law should be continuity-checked differently from an unreliable in-world myth.

### Scene Graph

Source: [engines/scene-graph.md](https://github.com/AvaTar-ArTs/chozen-land/blob/main/engines/scene-graph.md)

Scenes form a typed directed acyclic graph with edges such as:

- precedes
- causes
- branches_from
- mirrors
- resolves

This is one of the strongest design decisions in the repository. It avoids reducing stories to a single linear list while retaining enough edge semantics for traversal, branching, callbacks, and resolution.

### Scene Contract

Source: [docs/contracts/SCENE_CONTRACT.md](https://github.com/AvaTar-ArTs/chozen-land/blob/main/docs/contracts/SCENE_CONTRACT.md)

A scene takes:

- characters
- location
- conflict
- goal

It produces:

- scene
- emotional change
- continuity impact

It validates:

- canon compliance
- character consistency
- timeline consistency

This is a compact but valuable production contract. It connects narrative intent to reviewable consequences.

### Story Engine

Source: [engines/story-engine.md](https://github.com/AvaTar-ArTs/chozen-land/blob/main/engines/story-engine.md)

The Story Engine turns connected scenes into a story while preserving the scene graph as the underlying structure.

The ordered scene list is treated as a reading default rather than the only valid traversal. This permits branching narratives without losing a canonical presentation order.

The engine also supports honest maturity states such as:

- seed
- incomplete
- draft
- developed
- published

This matches the Origin Story principle of separating observed, proposed, generated, reviewed, approved, and published states.

### Cinematic Engine

Source: [engines/cinematic-engine.md](https://github.com/AvaTar-ArTs/chozen-land/blob/main/engines/cinematic-engine.md)

The Cinematic Engine turns scenes into concrete shots containing:

- shot ID
- scene ID
- type
- camera
- duration
- action
- dialogue

Its strongest boundary rule is that the cinematic stage should decompose narrative truth rather than invent new narrative content.

Once a shot exists, it can be exported to:

- comic panels
- video frames
- storyboards
- other render targets

without rewriting the story or lore layer.

## 6. Relation to Visual Story-Writing research

The [Visual Story-Writing paper](https://arxiv.org/html/2410.07486v2) proposes visual representations of entities, relationships, locations, and timelines as editable story interfaces.

Chozen-land already supplies the semantic structures that such an interface would need:

| Visual Story-Writing concept | Chozen-land equivalent |
|---|---|
| Entities | Characters, artifacts, locations, events |
| Entity relationships | Relationship Graph |
| Locations | Universe and Scene schemas |
| Event timeline | Scene Graph and Story Engine |
| Trait editing | Character Forge |
| Story rewriting | Engine contracts and downstream artifacts |
| History tree | Evolution and revision layer |
| Spatial editing | Universe, locations, and scene links |

Visual Story-Writing provides an interaction model. Chozen-land provides a richer authored-world ontology and production architecture.

Combined direction:

```text
Chozen ontology
+ Visual Story-Writing interaction model
+ Origin Story evidence and archaeology
+ AvatarArts production adapters
```

## 7. Relation to AvatarArts Forge

Chozen-land is closest to the **semantic reality layer** of AvatarArts Forge.

Origin Story contributes:

- research and repository archaeology
- source provenance
- comparison across external systems
- evidence/inference/recommendation separation
- capability-gap analysis
- agent and skill integration
- verification protocols

Chozen-land contributes:

- context and meaning
- canon
- world ontology
- relationship graphs
- lore
- scene DAGs
- story and cinematic boundaries
- artifact pluralism
- intelligence and evolution concepts

The combined architecture is:

```text
Origin Story
  ↓ understands systems and sources
Chozen semantic core
  ↓ models authored realities
AvatarArts compiler
  ↓ turns meaning into production instructions
Provider adapters
  ↓ generate media
Artifacts
  ↓ comics, manga, video, music, books, web, games
Intelligence
  ↓ validates continuity, provenance, and quality
Evolution
  ↓ records gaps and improves the system
```

## 8. First-party capability comparison

| Capability | choTaku | chozen-land | Origin Story | AvatarArts Forge |
|---|---:|---:|---:|---:|
| Repository implementation | Not yet present | Documentation and schemas present | Skill and research docs present | Planned/in development |
| Context discovery | Unknown | Discovery Engine | Archaeology workflow | Unified intake |
| Meaning modeling | Unknown | Explicit ontology | Extracted and compared | Canonical meaning layer |
| Canon | Unknown | Explicit | Evidence-aware evaluation | Versioned canon graph |
| Character psychology | Unknown | Goal/fear/wound/voice | Review lens | Full identity/progression model |
| Relationships | Unknown | Typed narrative tensions | Comparative analysis | Dynamic relationship graph |
| Lore | Unknown | Lore Engine | Lore audit lens | Canon/lore/evidence compiler |
| Scene structure | Unknown | Typed DAG | Story trace | Beat and scene compiler |
| Visual story editing | Unknown | Not implemented as a full UI | Paper adaptation | Graph/map/timeline authoring |
| Cinematic decomposition | Unknown | Cinematic Engine | Panel/shot review | Multi-format compiler |
| Artifacts | Unknown | Explicit plural outputs | Research target | Provider-neutral outputs |
| Provenance | Unknown | Conceptual | Explicit requirement | Manifest-first production |
| Intelligence | Unknown | Continuity/lore/graph concepts | Verification protocol | Executable quality system |
| Evolution | Unknown | Explicit concept | Capability-gap analysis | Continuous system learning |

## 9. Gaps that Chozen-land exposes

Chozen-land establishes an excellent conceptual architecture, but the next engineering layer should make the system executable and durable.

### Semantic schemas need stronger contracts

The current schemas are useful seeds. They should gain:

- IDs and references
- versioning
- lifecycle states
- confidence
- provenance
- source evidence
- validation rules
- timestamps
- dependency relationships

### Intelligence systems need implementations

The ontology names:

- continuity engine
- lore auditor
- narrative intelligence
- graph validator
- symbolism mapper

These should become executable validators with machine-readable reports.

### Export contracts need manifests

Every comic, manga, cinematic, audio, or web output should carry:

- source story and scene IDs
- semantic references
- prompt version
- provider/model
- parent assets
- render parameters
- review status
- output hash
- rights metadata

### Visual authoring needs a client

The Visual Story-Writing paper suggests the right interaction model:

- graph view
- map view
- timeline view
- synchronized text
- history tree
- direct manipulation

Chozen-land supplies the domain model these views can operate on.

### Branching and canon need explicit state

The scene DAG supports branches, but a production system also needs:

- canonical branch
- experimental branch
- rejected branch
- alternate canon
- superseded facts
- merge decisions

### Batch creation needs dependency awareness

If a character's visual identity changes, the system should identify which:

- scenes
- shots
- panels
- prompts
- assets
- publications

are affected and mark them for regeneration.

## 10. First-party design principles to preserve

These should be treated as core AvatarArts principles:

1. Context precedes generation.
2. Meaning precedes narrative.
3. Canon constrains rendering.
4. Relationships carry more narrative value than isolated objects.
5. World rules generate stakes.
6. Character goals and fears must be world-specific.
7. Lore should explain or dramatize rules and relationships.
8. Scenes should have explicit typed links.
9. Cinematic decomposition should not invent new narrative truth.
10. Artifacts are expressions of a deeper reality.
11. Incomplete work should be labeled honestly.
12. Every system should be able to evolve through capability-gap analysis.

## 11. Recommended integration

### Origin Story should ingest Chozen-land as first-party source material

Create a structured dossier linking:

- source path
- concept
- observed behavior or stated intent
- reusable pattern
- unresolved gap
- AvatarArts adaptation

### Chozen-land should become the semantic reference implementation

The next implementation target should be:

```text
Context + Meaning
→ Universe
→ Character
→ Relationship
→ Lore
→ Scene DAG
→ Story
→ Shot
→ Artifact Manifest
```

### AvatarArts Forge should add the missing production layer

Add:

- visual story authoring
- panel and page compilation
- provider adapters
- asset manifests
- continuity validators
- publication exporters
- rights and provenance
- review workflows
- creative memory and search

## 12. Final assessment

choTaku currently provides no implementation evidence and should remain unclassified.

chozen-land, however, is a substantial first-party conceptual foundation. It is not merely a worldbuilding repository. It already expresses the architecture of a **Creative Reality Operating System**:

```text
understand meaning
→ preserve truth
→ model relationships
→ generate narrative
→ render artifacts
→ inspect intelligence
→ evolve capability
```

This makes Chozen-land a central bridge between Steven's creative work and the external systems researched across GitHub, Hugging Face, and academic work.

## Sources

- [choTaku](https://github.com/AvaTar-ArTs/choTaku)
- [chozen-land](https://github.com/AvaTar-ArTs/chozen-land)
- [Chozen README](https://github.com/AvaTar-ArTs/chozen-land/blob/main/README.md)
- [Chozen ontology](https://github.com/AvaTar-ArTs/chozen-land/blob/main/docs/CHOZEN_ONTOLOGY.md)
- [Chozen core](https://github.com/AvaTar-ArTs/chozen-land/blob/main/docs/CHOZEN_CORE.md)
- [Chozen architecture](https://github.com/AvaTar-ArTs/chozen-land/blob/main/docs/ARCHITECTURE.md)
- [Visual Story-Writing](https://arxiv.org/html/2410.07486v2)
