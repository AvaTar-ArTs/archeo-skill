# Deep Dive: Visual Story-Writing

**Source:** [Masson, Zhao, and Chevalier — Visual Story-Writing: Writing by Manipulating Visual Representations of Stories](https://arxiv.org/html/2410.07486v2)  
**Venue:** UIST 2025  
**arXiv version:** 2410.07486v2, 2025-07-31  
**Relevance:** Direct design reference for Origin Story and the AvatarArts Forge authoring layer.

## Executive finding

The paper's central insight is that writers should be able to manipulate a story through representations that match the kind of reasoning they are doing.

A writer who wants to change a character's location should be able to move the character on a map. A writer who wants to reorder events should be able to move them on a timeline. A writer who wants to change a relationship should be able to edit a graph.

The text is then updated from the structured manipulation.

This is more important than a visual dashboard. It is a **bidirectional story compiler**:

```text
Narrative text
↔ structured story model
↔ visual representation
↔ direct manipulation
↔ revised narrative text
```

For AvatarArts, this suggests a core product principle:

> The creator should be able to edit the storyworld in the representation that best matches the intended change.

## 1. Problem the paper identifies

The paper observes that creative writers already maintain external maps, spreadsheets, timelines, character sheets, and diagrams because narrative text alone is a poor representation for some reasoning tasks.

The difficulty is not simply generating prose. It is maintaining relationships between:

- characters
- actions
- locations
- time
- narrative order
- point of view
- traits
- causal chains
- spatial coherence
- revisions and alternate possibilities

A textual instruction such as “move the cat from the barn to the lake” is ambiguous. It may require changing the location, updating connected actions, preserving the barn as a prior location, and deciding which event in the story is affected.

The paper therefore frames visual representations as both:

- review tools for understanding a story
- input tools for expressing precise editing intent

Source: [Introduction](https://arxiv.org/html/2410.07486v2).

## 2. The narratology model

The paper separates story structure into two related perspectives:

### Fabula

The underlying chronological story:

- actor
- location
- time
- event

### Syuzhet

The way the story is presented:

- character
- space
- temporality
- focalization

This distinction is useful for AvatarArts because it separates:

- what happened
- how it is revealed
- where it physically occurred
- how it is framed
- whose perspective controls the audience's knowledge

### AvatarArts extension

Origin Story should extend this model with additional first-class constructs:

| Paper construct | AvatarArts extension |
|---|---|
| Actor | Character, creature, artifact, force, institution, spirit |
| Character | Identity profile, psychology, voice, visual grammar |
| Location | Realm, place, scene environment, symbolic space |
| Space | Mood, atmosphere, mythology, spatial meaning |
| Time | Chronology, age, duration, historical era |
| Temporality | Flashback, foreshadowing, reveal order, montage |
| Event | Beat, action, conflict, ritual, transformation |
| Focalization | Viewpoint, narrator, witness, camera, reader knowledge |
| Trait | Motivation, fear, wound, desire, belief, contradiction |
| Relationship | Trust, debt, conflict, kinship, influence, possession |
| Theme | Motif, curse, symbol, philosophy, emotional signature |
| — | Evidence, canon status, progression state, provenance |

The paper itself notes that emotions and motivations are promising extensions beyond the basic model. This directly supports adding psychology, lore, evidence, and progression to the AvatarArts semantic core. citeturn10view3

## 3. Story constructs and operators

The paper defines four operators for composing story elements into visualizable constructs.

### Position

Places one element according to another.

Example:

```text
position(time, location)
→ map of movement through locations over time
```

AvatarArts applications:

- track a character through realms
- visualize ritual stages by location
- map where evidence was discovered
- inspect spatial continuity across panels
- show a curse spreading through a setting

### Associate

Adds and associates elements.

Example:

```text
associate(time, focalization)
→ timeline of events by point of view
```

AvatarArts applications:

- attach motifs to beats
- connect emotions to scenes
- associate evidence with transformations
- connect characters to rituals, artifacts, and factions
- show which lore is active in a scene

### Connect

Creates edges between elements according to another element.

Example:

```text
connect(characters, events)
→ character interaction graph
```

AvatarArts applications:

- relationship graph
- conflict graph
- influence and debt network
- canon dependency graph
- character-to-motif network
- evidence-to-claim graph

### Unfold

Duplicates and organizes elements according to another dimension.

Example:

```text
unfold(locations, characters)
→ locations visited by each character
```

AvatarArts applications:

- character arc across chapters
- motif recurrence across scenes
- costume evolution across progression states
- asset variants by publication format
- alternate timeline branches
- panel versions by style or provider

## 4. Prototype interaction model

The prototype contains three primary synchronized views.

### Entities and actions view

Characters and objects appear as nodes. Actions appear as directed edges.

The prototype supports:

- editing entity traits
- adding and removing entities
- adding and removing actions
- editing action labels
- filtering or navigating overlapping edges
- highlighting related text

The paper's trait editor uses intensity values from 1 to 10 for properties such as curiosity, adventurousness, and talkativeness.

### Locations and entities view

Locations appear as spatial nodes, with entities positioned within them.

The prototype supports:

- creating locations
- moving entities between locations
- updating the narrative after movement
- representing an entity in multiple locations when the story requires it

### Event timeline

Events are displayed in narrated order.

The prototype supports:

- selecting one or multiple events
- highlighting corresponding text
- filtering associated entities and locations
- reordering events
- applying subsequent edits to selected events only

This selection behavior is especially important. It prevents a global edit from accidentally changing every occurrence of a character or location.

### Bi-directional editor

The prototype combines:

- a text editor
- synchronized visualizations
- history tree
- refresh and rewrite controls
- hover-based highlighting between text and visual elements
- visual-to-text and text-to-visual updates
- track changes

## 5. Implementation method

The paper uses a staged extraction pipeline.

### Entity extraction

The system extracts:

- entity name
- emoji or visual marker
- up to three descriptive properties
- property intensity from 1 to 10

### Location extraction

The system extracts:

- main locations
- name
- visual marker

### Event extraction

The story is split into sentences. For each sentence, the system extracts:

- action name
- source entity
- target entity
- location
- source sentence

The event extractor receives prior text for context but is instructed to extract only actions occurring in the current sentence. Memories and earlier actions are excluded.

Only changed sentences are re-extracted to improve efficiency.

### Rewrite pipeline

When the user manipulates a visual representation:

1. the current structured state is read
2. the intended new state is calculated
3. a constrained rewrite instruction is generated
4. the story text is rewritten
5. the revised text is re-extracted
6. visual representations are regenerated
7. the history tree records the change

The paper's prototype used OpenAI GPT-4o for extraction and engineered prompts for edits. citeturn10view5

## 6. What the studies found

### Study 1: planning and review

The first study included 12 participants with varied writing experience. Participants reviewed short stories using either visualizations or text-only interfaces.

The visualizations helped participants:

- confirm intuitions
- analyze character interactions
- identify unnecessary locations
- reason about who could know what
- find gaps in event progression
- inspect alternative points of view
- feel more confident that they had not missed structural details

The paper reports that participants used the visual views as a form of reassurance and analysis, not merely decoration. citeturn10view1

### Study 2: editing and free-form writing

The second study included eight experienced creative writers. Participants performed:

- entity and action edits
- location movement
- new location creation
- event reordering
- free-form story exploration

The reported results indicate that the system was understandable and usable for structured edits, and it supported exploration. The prototype received an overall Creativity Support Index score of 71.50 in the reported study context. citeturn10view2

### Important user tension

The visual interface improved precision for structured changes but constrained free expression. Participants noted that connecting nodes and selecting fixed actions could feel limiting compared with writing an unconstrained sentence.

This yields a key design rule for AvatarArts:

> Use direct manipulation for precise structural intent; use language and freeform tools for ambiguity, tone, metaphor, and emergence.

The two modes should complement each other rather than compete.

## 7. Important limitations

### Explicit information only

The prototype mainly visualizes information explicitly present in the text. Participants observed that it did not adequately capture motivations and deeper implicit meaning.

This limitation is central to AvatarArts. A surface graph of entities and events is not enough for:

- hidden motives
- psychological wounds
- symbolic meaning
- ritual significance
- unreliable narration
- implied lore
- emotional transformation
- evidence strength
- canon confidence

### Small and exploratory studies

The studies were exploratory, with small participant groups recruited through social networks and mailing lists. The findings support the design direction but do not establish universal usability or production-scale effectiveness.

### Short stories

The prototype was tested on short stories rather than long-running graphic novels, serialized manga, or multi-season storyworlds.

Long-form systems introduce:

- versioned canon
- superseded facts
- recurring motifs
- character aging
- costume changes
- multiple timelines
- contradiction management
- publication-specific edits
- rights and provenance
- asset reuse

### LLM rewrite risk

The system depends on constrained language-model rewrites. Any rewrite may introduce:

- accidental canon changes
- tone drift
- altered causality
- missing details
- unsupported motivations
- continuity errors

AvatarArts needs a semantic diff and validation layer around every rewrite.

### Visual overload

As the number of characters, events, locations, and relationships increases, graphs can become unreadable. Origin Story should support:

- filters
- focus mode
- progressive disclosure
- chapter and scene scopes
- relationship type filters
- motif and evidence overlays
- density warnings
- alternate views

## 8. Translation into Origin Story

### Core principle

Origin Story should not treat visualizations as a reporting layer added after generation. They should be executable authoring surfaces over a canonical storyworld model.

### Suggested semantic layers

```text
Storyworld
├── Canon
├── Characters
│   ├── Identity
│   ├── Psychology
│   ├── Voice
│   ├── Visual grammar
│   └── Progression
├── Realms and locations
├── Timeline and alternate branches
├── Events and beats
├── Relationships and factions
├── Motifs and symbols
├── Lore and rituals
├── Evidence and claims
├── Assets and references
├── Visual grammar
├── Publication targets
└── Provenance and review history
```

### Recommended authoring surfaces

#### Canon graph

Visualize:

- facts
- rules
- exceptions
- sources
- confidence
- contradictions
- superseded versions

#### Character constellation

Visualize:

- relationships
- current goals
- fears and wounds
- debts and loyalties
- emotional state
- motif associations
- progression state
- visual identity changes

#### Realm map

Visualize:

- locations
- routes
- thresholds
- factions
- symbolic meanings
- scene occupancy
- evidence discovered
- spatial constraints

#### Timeline and reveal order

Separate:

- chronological event order
- publication order
- flashbacks
- foreshadowing
- audience knowledge
- unreliable or hidden information

#### Beat and panel board

Visualize:

- story beats
- page turns
- panel count
- shot size
- focalization
- dialogue load
- visual motifs
- emotional intensity
- continuity warnings

#### Asset constellation

Connect:

- prompt
- reference images
- character identity
- scene
- panel
- generated output
- revision
- provider
- publication

## 9. Proposed AvatarArts operators

The paper's four operators can become a larger creative grammar.

| Operator | Meaning | AvatarArts use |
|---|---|---|
| position | place in space | move character, artifact, evidence, or scene |
| associate | attach meaning or metadata | link motif, emotion, lore, or evidence |
| connect | create relationship | bind characters, events, factions, and causes |
| unfold | expand across a dimension | show arc, recurrence, variants, or timelines |
| transform | change state | evolve character, curse, realm, artifact, or motif |
| reveal | change audience knowledge | expose lore, evidence, identity, or betrayal |
| echo | repeat with variation | recur motif, image, phrase, ritual, or visual pattern |
| branch | create an alternate path | explore what-if versions without destroying canon |
| bind | enforce a constraint | keep costume, prop, geography, or rule consistent |
| compile | turn semantics into media instructions | generate panels, shots, prompts, layouts, or exports |

## 10. Proposed schema fragment

```json
{
  "storyworld_id": "sw_001",
  "revision_id": "rev_014",
  "entities": [
    {
      "id": "char_001",
      "kind": "character",
      "name": "The Seeker",
      "traits": {
        "curiosity": 8,
        "fear": 6,
        "defiance": 9
      },
      "motives": [
        {
          "id": "mot_001",
          "description": "Understand the origin of the curse",
          "strength": 0.91,
          "status": "active"
        }
      ],
      "visual_identity_ref": "identity_001"
    }
  ],
  "locations": [
    {
      "id": "loc_001",
      "name": "The Crimson Archive",
      "symbolic_tags": ["memory", "poison", "forbidden-knowledge"]
    }
  ],
  "events": [
    {
      "id": "evt_001",
      "chronological_index": 4,
      "publication_index": 1,
      "kind": "revelation",
      "actors": ["char_001"],
      "location": "loc_001",
      "evidence_refs": ["evidence_003"],
      "motif_refs": ["motif_crimson_thread"],
      "canon_status": "proposed"
    }
  ],
  "history": {
    "parent_revision": "rev_013",
    "operation": {
      "type": "reveal",
      "target": "evidence_003"
    }
  }
}
```

## 11. Quality gates derived from the paper

Every visual edit should be checked for:

### Structural consistency

- Did the entity still exist where the event requires it?
- Did the action retain valid source and target entities?
- Did reordering break causal assumptions?
- Did moving an entity alter unrelated scenes?

### Semantic consistency

- Did the character's motive change unintentionally?
- Did the edit alter canon?
- Did the visual edit create unsupported knowledge?
- Did the rewrite preserve focalization?

### Creative consistency

- Does the edit preserve tone?
- Does it support the intended emotional progression?
- Does it preserve motif and symbolic meaning?
- Does it fit the chosen genre and visual grammar?

### Production consistency

- Are affected panels identified?
- Are dependent assets marked stale?
- Are prompts regenerated only where needed?
- Is the asset manifest updated?
- Can the previous version be restored?

## 12. What Origin Story can improve

The paper provides the authoring interaction model. Origin Story can extend it with:

- evidence-backed extraction
- confidence and uncertainty
- canon status
- character psychology
- lore and ritual systems
- progression state
- visual identity references
- asset provenance
- provider-neutral generation
- publication targets
- security boundaries
- reproducible manifests
- cross-format compilation
- branch and revision management

The strongest proprietary contribution is the connection between **meaning and production**:

```text
change a character's motive
→ update affected beats
→ identify affected panels
→ regenerate only dependent prompts/assets
→ run continuity and visual checks
→ update publication outputs
```

## 13. Final assessment

This paper is not a comic generator and not a complete storyworld engine. Its contribution is more foundational:

> It demonstrates that narrative authoring improves when the interface exposes the underlying structures writers are already mentally managing.

For AvatarArts, the next step is to build the same principle at a deeper level:

- visual representations for canon
- direct manipulation for psychology and progression
- maps for realms and evidence
- timelines for chronology and reveal
- graphs for relationships and motifs
- boards for beats and panels
- asset graphs for production and provenance
- synchronized text, visual, and media outputs

Origin Story should therefore treat the paper as a foundational interaction and compiler reference—not as a product to copy.

## Sources

- [Paper HTML](https://arxiv.org/html/2410.07486v2)
- [Paper DOI](https://doi.org/10.1145/3746059.3747758)
- [AvatarArts agent-skills](https://github.com/AvaTar-ArTs/agent-skills)
- [AvatarArts Comic Creator Matrix](https://github.com/AvaTar-ArTs/AvatarArts-Comic-Creator-Matrix)
