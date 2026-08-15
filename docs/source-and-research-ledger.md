# Source and Research Ledger

Date: 2026-08-15  
Project: Origin Story / AvatarArts Forge  
Purpose: Preserve the websites, repositories, papers, registries, products, discussions, and research ideas used during the creative-systems investigation.

## How to read this ledger

Each source is classified by role:

- Primary implementation: repository, paper, official documentation, or official product page
- Discovery index: topic page, registry, catalog, or search result used to find candidates
- Product evidence: official marketing or product documentation
- Community evidence: discussion, Reddit, forum, or user-generated material
- Secondary analysis: article, guide, comparison, or commentary

A source can be useful without being authoritative. Product pages reveal positioning and demand. Repositories reveal implementation. Papers reveal methods and study results. Community discussions reveal friction and unmet needs.

The ledger separates:

- observed source content
- interpretation
- adaptation opportunity
- caveat

## 1. First-party AvatarArts sources

### AvatarArts Comic Creator Matrix

URL: https://github.com/AvaTar-ArTs/AvatarArts-Comic-Creator-Matrix  
Type: First-party repository and synthesis archive

Contribution:

- repository investigations
- comparative capability analysis
- AvatarArts Forge architecture
- security and manifest remediation
- comic, manga, lore, psychology, provenance, and publishing research

Thought:

This is the comparative and architectural memory of the broader system. It should remain the place where external systems are evaluated against AvatarArts requirements.

### Origin Story

URL: https://github.com/AvaTar-ArTs/origin-story  
Type: First-party skill and research repository

Contribution:

- repository archaeology
- archive inventory
- agent and skill integration
- evidence, inference, recommendation separation
- expanded creator ecosystem research
- owned-system analysis

Thought:

Origin Story is the research, excavation, and synthesis layer. It should not become another generic generation tool.

### chozen-land

URL: https://github.com/AvaTar-ArTs/chozen-land  
Type: First-party narrative reality system

Important source files:

- https://github.com/AvaTar-ArTs/chozen-land/blob/main/docs/CHOZEN_CORE.md
- https://github.com/AvaTar-ArTs/chozen-land/blob/main/docs/CHOZEN_ONTOLOGY.md
- https://github.com/AvaTar-ArTs/chozen-land/blob/main/docs/CHOZEN_PHILOSOPHY.md
- https://github.com/AvaTar-ArTs/chozen-land/blob/main/docs/ARCHITECTURE.md
- https://github.com/AvaTar-ArTs/chozen-land/tree/main/engines
- https://github.com/AvaTar-ArTs/chozen-land/tree/main/schemas

Contribution:

- Context, Meaning, Canon, Graph, Narrative, Artifacts, Intelligence, Evolution
- Discovery, Universe, Character, Relationship, Lore, Scene, Story, and Cinematic engines
- typed scene DAG
- character goal/fear/wound/voice/visual signature
- lore categories
- scene contracts
- cross-format artifact philosophy

Thought:

Chozen-land is one of the strongest first-party ancestors of AvatarArts Forge. It supplies semantic reality modeling that external comic tools generally lack.

### choTaku

URL: https://github.com/AvaTar-ArTs/choTaku  
Type: First-party repository

Observed state at review:

- public repository
- main branch
- empty Git repository
- no readable README or source tree

Thought:

No architectural claims should be assigned yet. It remains a reserved namespace or future product surface until content is added.

### AvatarArts agent-skills

URL: https://github.com/AvaTar-ArTs/agent-skills  
Type: First-party agent and skill ecosystem

Contribution:

- using-superpowers
- verification-before-completion
- workspace-ecosystem-audit
- workflow-orchestrator
- capability-atlas
- system-architect
- security-engineer
- testing-specialist
- content-organizer
- feedback-synthesizer
- creative-ideation
- baoyu-comic
- structured-asset-pipeline
- frontend-design
- taste-skill

Thought:

The useful material is methodological: role separation, verification, orchestration, creative ideation, visual design, and asset handling. Origin Story adapts those methods instead of copying the entire ecosystem.

## 2. External GitHub repositories

### AI Comic Factory

URL: https://github.com/jbilcke-hf/ai-comic-factory  
Type: Primary implementation

Contribution:

- LLM-to-panel decomposition
- prompt-driven comic generation
- SDXL rendering adapter
- simple creator-facing workflow

Thought:

Useful historical baseline and adapter target. It does not provide the complete canon, identity, evidence, or provenance architecture AvatarArts needs.

### Make Comics

URL: https://github.com/nutlope/make-comics  
Type: Primary implementation

Contribution:

- story, character, and page generation
- previous-page reference for coherence
- uploaded character images for consistency

Thought:

Strong example of page-level continuity and reference-image anchoring. The main missing layer is durable semantic memory.

### Comic Studio AI

URL: https://github.com/RobinaMirbahar/Comic-Studio-Ai  
Type: Primary implementation

Contribution:

- multi-agent comic generation
- consistent characters
- speech bubbles
- multilingual support
- FastAPI and Cloud Run delivery

Thought:

Useful for role orchestration and delivery boundaries. Its public description does not establish a deep storyworld or provenance layer.

### inkstone

URL: https://github.com/phaethix/inkstone  
Type: Primary implementation discovered through GitHub topic pages

Contribution:

- local-first novel-to-comic direction
- pluggable providers
- open-source positioning
- character-consistency concerns

Thought:

One of the closest matches to a provider-neutral execution layer. AvatarArts can place semantic canon above it.

### AIComics

URL: https://github.com/chfr19820610-cell/AIComics  
Type: Primary implementation discovered through GitHub topic pages

Contribution:

- story to image generation
- voice
- video composition
- multi-platform publishing
- ComfyUI, SDXL, and Piper TTS

Thought:

Strong media-production breadth. It reinforces the need for manifests and semantic state so downstream media remains reproducible.

### World-Forge

URL: https://github.com/AndreiNicu/World-Forge  
Type: Primary implementation

Contribution:

- multi-agent worldbuilding
- character cards
- tiered lorebooks
- runtime-aware export
- audit reports
- structured drafting phases

Thought:

One of the closest external systems to the lore, evidence, and role-based worldbuilding direction. Its runtime target is roleplay packaging rather than a general visual artifact compiler.

### OpenMontage

URL: https://github.com/calesthio/OpenMontage  
Type: Primary implementation or project page

Contribution:

- agentic video production
- many pipelines and tools
- production knowledge and skill files
- multimodal execution

Thought:

Useful as a production operating-system reference. Breadth of media operations does not automatically imply storyworld semantics.

### AgenticPlanning

URL: https://github.com/agentralabs/agentic-planning  
Type: Primary implementation

Contribution:

- persistent intention graph
- goals
- decisions
- rejected alternatives
- commitments
- blockers
- progress

Thought:

Highly relevant to evidence, progression, branch history, and the preservation of roads not taken.

### CharaConsist

URL: https://github.com/Murray-Wang/CharaConsist  
Type: Primary research implementation

Contribution:

- training-free foreground character consistency
- optional background consistency
- FLUX-based generation research

Thought:

Useful visual adapter. It preserves appearance, not motive, psychology, canon, or transformation.

### StoryMaker

URL: https://github.com/RedAIGC/StoryMaker  
Type: Primary research implementation

Contribution:

- face, clothing, hairstyle, body, and multi-character consistency
- visual story sequence support

Thought:

Useful identity-preservation reference. Identity must be expanded beyond visual features in AvatarArts.

### StoryCraftr

URL: https://github.com/raestrada/storycraftr  
Type: Primary open-source writing tool

Contribution:

- story creation
- worldbuilding
- book outlines
- chapter generation
- CLI-oriented workflow

Thought:

Useful lightweight writing reference, but likely not a complete visual production or asset-intelligence system.

### Creative Writing Skills

URL: https://github.com/haowjy/creative-writing-skills  
Type: Primary skill repository

Contribution:

- specialized writing modes
- critique
- revision
- voice
- continuity
- serial fiction workflow

Thought:

Supports separating creative roles and modes rather than using one undifferentiated writing agent.

### Inworld comic generator

URL: https://github.com/inworld-ai/comic-generator-node  
Type: Primary implementation

Contribution:

- graph-based processing pipeline
- staged AI comic generation
- runtime-oriented orchestration

Thought:

Relevant to the idea that a comic generator should be a graph of stages rather than one prompt call.

### GitHub comic-generator topic

URL: https://github.com/topics/comic-generator  
Type: Discovery index

Contribution:

Surfaced projects involving:

- local-first novel-to-comic generation
- manga and animation
- motion comics
- character consistency
- ComfyUI
- AI short drama
- MCP comic services

Thought:

Useful for candidate discovery, not evidence of project quality. Topic pages mix serious implementations, experiments, and marketing-oriented repositories.

### GitHub visual-storytelling topic

URL: https://github.com/topics/visual-storytelling  
Type: Discovery index

Contribution:

Surfaced visual-storytelling pipelines and character-consistency projects.

Thought:

Useful taxonomy for finding systems adjacent to comic generation but not limited to comics.

### GitHub worldbuilding topic

URL: https://github.com/topics/worldbuilding  
Type: Discovery index

Contribution:

Surfaced World-Forge and other lore, roleplay, and narrative systems.

Thought:

Worldbuilding repositories are often more relevant to AvatarArts semantics than image-generation repositories.

### GitHub creative-writing-ai topic

URL: https://github.com/topics/creative-writing-ai  
Type: Discovery index

Contribution:

Surfaced World-Forge, Serendipity-Engine, and structured story-generation projects.

Thought:

Useful for narrative orchestration and serial continuity research, but repository descriptions should be validated against code.

## 3. Hugging Face and model sources

### AI Comic Factory Space

URL: https://huggingface.co/spaces/jbilcke-hf/ai-comic-factory  
Type: Official demo and deployment surface

Contribution:

- accessible prompt-to-comic workflow
- comic-style generation
- public Space deployment model

Thought:

Useful baseline for creator accessibility. A Space is not automatically a durable creative operating system.

### AI Comic Factory mirror

URL: https://huggingface.co/spaces/makem/ai-comic-factory  
Type: Community or mirrored demo

Contribution:

- another accessible story-to-comic surface

Thought:

Useful for comparing deployment variants and ecosystem reuse.

### AI Comic Factory consistency discussion

URL: https://huggingface.co/spaces/jbilcke-hf/ai-comic-factory/discussions/108  
Type: Community discussion with maintainer response

Contribution:

The discussion explains limitations of early panel generation:

- fresh image generation per panel
- limited prompt window
- style instructions consuming context
- lack of true persistent character and location memory

Thought:

This is valuable negative evidence. It shows why AvatarArts should not confuse prompt continuity with storyworld continuity.

### AnimateDiff documentation

URL: https://huggingface.co/docs/diffusers/api/pipelines/animatediff  
Type: Official technical documentation

Contribution:

- text-to-video pipeline concepts
- temporal consistency
- diffusion-based animation workflows

Thought:

Relevant as a media adapter, not as a semantic story engine.

### Qwen Image Bench

URL: https://huggingface.co/datasets/Qwen/Qwen-Image-Bench  
Type: Benchmark and dataset documentation

Contribution:

Evaluation dimensions for:

- comic creation
- storyboard creation
- shot size
- camera angle
- composition
- visual style
- alignment

Thought:

Useful foundation for turning subjective visual review into explicit quality gates.

### Hugging Face papers search

URL: https://huggingface.co/papers  
Type: Discovery index

Contribution:

Surfaced visual storytelling, animation, multimodal art, and consistency research.

Thought:

Useful for model and paper discovery, but each result needs primary-source verification.

## 4. Academic and research sources

### Visual Story-Writing

URL: https://arxiv.org/html/2410.07486v2  
DOI: https://doi.org/10.1145/3746059.3747758  
Type: Primary academic paper

Contribution:

- visual representations of story elements
- entity/action graph
- location/entity view
- event timeline
- direct manipulation
- bidirectional text and visual editing
- history tree
- structured extraction
- visual story-writing framework

Thought:

This is a foundational interaction reference for AvatarArts. It suggests that the author should edit the representation matching the intended reasoning task.

### Visual story consistency survey

URL: https://link.springer.com/article/10.1007/s10462-025-11482-6  
Type: Academic survey

Contribution:

Six consistency dimensions:

- time
- space
- character
- event and plot
- style
- theme and purpose

Thought:

Provides a strong evaluation model that AvatarArts can extend with psychology, lore, evidence, progression, visual grammar, provenance, and publication readiness.

### Visual Writing Prompts

URL: https://aclanthology.org/2023.tacl-1.33.pdf  
Type: Primary academic paper and dataset

Contribution:

- image-grounded story generation
- coherent visual sequences
- character-grounded narrative research

Thought:

Supports treating visual sequences as story evidence, not isolated images.

### Story generation from visual inputs

URL: https://www.mdpi.com/2078-2489/16/9/812  
Type: Secondary or survey-style academic source

Contribution:

- modular visual-story generation
- character interaction
- coherence
- author-goal considerations

Thought:

Useful for mapping research modules, but primary cited methods should be checked individually.

### Character-driven narrative engine

URL: https://dl.digra.org/index.php/dl/article/download/1078/1078/1075  
Type: Academic paper

Contribution:

- character-driven interactive storytelling methodology

Thought:

Relevant to character agency and authored narrative systems, especially when building progression and relationship engines.

### Agents' Room

Referenced from the Visual Story-Writing paper: arXiv:2410.02603  
Type: Academic research

Contribution:

- multi-step collaboration for narrative generation

Thought:

Relevant to specialized editorial agents and structured collaboration.

## 5. Agent registries and skill marketplaces

### skills.sh

URL: https://skills.sh/  
Type: Agent skill directory

Contribution:

- installable agent skills
- npx-based distribution
- compatibility across multiple agents
- searchable procedural knowledge
- leaderboard and topic discovery

Thought:

Skills are becoming a package ecosystem. Origin Story should document skill contracts and provenance, not only names.

### OpenClaw skills index

URL: https://github.com/VoltAgent/awesome-openclaw-skills  
Type: Aggregator and discovery index

Contribution:

- large categorized list of agent skills
- image/video generation
- research
- automation
- memory
- governance
- documents
- media

Thought:

Discovery-rich but noisy. Every candidate requires installation and source review before adoption.

### MCP Market

URL: https://mcpmarket.com/  
Type: MCP and skill marketplace

Contribution:

- creator-facing MCP discovery
- comic, writing, PDF, and production skills
- installation and feature descriptions

Thought:

Useful for finding packaged workflows, but marketplace descriptions can overstate maturity.

### AgentSkills.me

URL: https://agentskills.me/  
Type: Agent skill directory

Contribution:

- baoyu-comic listing
- skill descriptions
- downloadable or linked skill packaging

Thought:

Useful for discovering domain-specific creative skills and comparing packaging conventions.

### LobeHub skills

URL: https://lobehub.com/skills/openclaw-skills-comi-cog  
Type: Skill marketplace

Contribution:

- comi-cog listing
- sequential art positioning
- OpenClaw-compatible discovery

Thought:

Useful for marketplace comparison; inspect actual source and permissions before treating listings as implementation evidence.

### Clawbot

URL: https://clawbot.ai/skills/comi-cog.html  
Type: Product and skill listing

Contribution:

- comic generation skill positioning for OpenClaw

Thought:

Shows how a comic workflow is packaged as an agent capability rather than a standalone application.

## 6. Commercial creator platforms

### LlamaGen

URL: https://llamagen.ai/  
Type: Product site

Contribution:

- comic, manga, manhwa, webtoon, storyboard, audio, and video workflows
- character consistency positioning
- multi-format conversion

Thought:

Good evidence of market demand for a broad creator studio. Marketing claims require implementation or user-testing verification.

### LlamaGen Comic API

URL: https://llamagen.ai/comic-api  
Type: Product API page

Contribution:

- REST and MCP comic generation
- story briefs
- customer uploads
- character references
- structured comic pages

Thought:

Useful example of a media capability exposed as an agent service.

### Anifusion

URL: https://anifusion.ai/  
Type: Product site

Contribution:

- manga pages
- layouts
- speech bubbles
- character sheets
- editing
- video
- model training

Thought:

Shows demand for an integrated manga studio rather than isolated image generation.

### GenToon

URL: https://www.gentoon.ai/en  
Type: Product site

Contribution:

- webtoon and social comic creation
- four-panel and vertical-scroll formats
- speech bubbles
- character consistency

Thought:

Useful for social-native output targets and format presets.

### ComicsAI

URL: https://www.comicsai.org/en  
Type: Product site

Contribution:

- comic panels
- manga pages
- webtoon scenes
- recurring characters
- browser export
- multi-language positioning

Thought:

Useful product comparison target. Inspect ownership, persistence, and export semantics.

### ComicPad / TaleAtelier reference

URL: https://www.comicpad.app/consistent-character-ai  
Type: Product explanation and SEO content

Contribution:

- locked character references
- same identity across many panels
- distinction between reference locking, LoRA, and per-prompt references

Thought:

Useful explanation of the market's identity problem. It focuses on visual identity, not authored identity.

### Adobe Firefly comic generator

URL: https://www.adobe.com/products/firefly/features/ai-comic-generator.html  
Type: Official product page

Contribution:

- comic panels
- styles
- boards
- dialogue and captions
- page arrangement
- commercial-safety positioning

Thought:

Shows how an established creative platform incorporates comics into a larger design ecosystem.

### Canva AI comic generator

URL: https://www.canva.com/ai-comic-generator/  
Type: Official product page

Contribution:

- accessible comic creation
- layout and design integration
- broad creator audience

Thought:

Useful reference for reducing complexity without removing composition control.

### Campfire

URL: https://www.campfirewriting.com/worldbuilding-tools  
Type: Official product page

Contribution:

- modular worldbuilding
- characters
- plots
- maps
- species
- publishing

Thought:

Strong reference for organizing authored worlds; its connection to automated multimodal production is less central.

### Twine

URL: https://twinery.org/  
Type: Official open-source project site

Contribution:

- nonlinear stories
- variables
- conditional logic
- multimedia
- HTML publishing

Thought:

Useful reference for branching logic and author control. AvatarArts can adapt its semantics into typed scene DAGs and alternate canon branches.

### SceneCraft

URL: https://mcpservers.org/servers/scenecraft-ink  
Type: MCP server directory and product listing

Contribution:

- beat boards
- scene cards
- screenplay formatting
- creative co-pilot
- scene-to-comic workflow

Thought:

Useful bridge between screenplay structure and comic production; needs a deeper storyworld and provenance layer.

### Storyboard Comic Generator

URL: https://app.artificialstudio.ai/tools/storyboard-comic-generator  
Type: Product tool page

Contribution:

- story description to sequential panels
- layout automation
- single-page storyboard output

Thought:

Evidence of demand for fast story visualization. It appears optimized for prototypes and presentations, not long-form canon.

### Drawstory comparison

URL: https://www.drawstory.ai/blog/best-manga-storyboard-generators  
Type: Product comparison and marketing article

Contribution:

- story-first manga storyboard demand
- prompt-free workflow positioning
- character consistency comparison
- tools named include Drawstory, Higgsfield, LlamaGen, Midjourney, and DaVinci

Thought:

Useful market language and demand evidence. It is not neutral benchmarking.

### Storyboard That

URL: https://www.storyboardthat.com/articles/e/create-comics  
Type: Official educational product page

Contribution:

- drag-and-drop comics
- characters, scenes, dialogue bubbles
- education and comprehension use cases

Thought:

Shows the value of direct manipulation and accessible structured composition even without generative AI.

### Webtoon localization

URL: https://www.theverge.com/ai-artificial-intelligence/899108/webtoon-canvas-ai-translation-localization-yongsoo-kim  
Type: Secondary reporting on product development

Contribution:

- optional AI localization
- glossary-aware translation
- creator control
- human quality review
- analytics and distribution

Thought:

Shows that publishing, translation, and audience growth are part of the creator system—not downstream afterthoughts.

## 7. Secondary articles, guides, and community sources

### AI comic creation overview

URL: https://llamagen.ai/blogs/professional-comic-creation-with-ai-simplify-your-storytelling-without-drawing-skills-by-2026  
Type: Product-oriented article

Contribution:

- market framing
- professional comic workflow claims
- style and adaptation language

Thought:

Useful for demand vocabulary, weak as independent evidence.

### AI storyboard and comic guides

URL: https://www.jenova.ai/en/resources/ai-comic-storyboard-generator  
URL: https://www.jenova.ai/en/resources/ai-comic-page-generator  
Type: Product-oriented guides

Contribution:

- story-to-panel framing
- character consistency language
- adaptive panel layout positioning

Thought:

Useful for product taxonomy and UX expectations, not neutral architecture evidence.

### AI storytelling role-playing agent

URL: https://www.jenova.ai/en/resources/ai-storytelling-role-playing-agent  
Type: Product-oriented guide

Contribution:

- worldbuilding
- character arcs
- dialogue
- editorial feedback
- narrative structures

Thought:

Useful as a demand map for creative assistants.

### OpenClaw image-generation discussion

URL: https://www.reddit.com/r/clawdbot/comments/1rnhih1/i_built_an_ai_image_generation_skill_for_openclaw/  
Type: Community discussion

Contribution:

- prompt enhancement
- parallel image variants
- workflow orchestration
- local agent image generation

Thought:

Useful for discovering grassroots skill patterns. Community claims require source inspection.

### Stable Diffusion comic consistency discussion

URL: https://www.reddit.com/r/StableDiffusion/comments/1qys7ex/dev_help_building_an_opensource_comic_storyboarder/  
Type: Community discussion

Contribution:

- real user pain around character consistency
- previous-panel conditioning
- IP-Adapter and ControlNet questions
- consistency slider ideas

Thought:

Strong evidence of unmet creator demand and practical experimentation.

### Writing and worldbuilding tool discussions

URL: https://www.reddit.com/r/opensource/comments/1s7ok59/fleshnote_an_open_source_novel_writing_and/  
Type: Community discussion

Contribution:

- open-source worldbuilding app demand
- linked characters and plots
- visual organization requirements

Thought:

Useful evidence for combining writing and structured world models.

### Comic production software discussion

URL: https://blenderartists.org/t/is-there-an-industry-standard-software-for-creating-web-comics/1459657  
Type: Community discussion

Contribution:

- mature division between art, lettering, layout, and project management
- use of Illustrator, InDesign, Clip Studio, Krita, and spreadsheets

Thought:

Important reminder that established comic workflows are multi-tool pipelines. AvatarArts should preserve these boundaries rather than pretend generation replaces production.

### Comic publishing workflow discussion

URL: https://www.reddit.com/r/ComicBookCollabs/comments/1uqusd7/what_program_do_i_use_to_put_it_all_together/  
Type: Community discussion

Contribution:

- practical post-art production problem
- PDF, EPUB, layout, and handoff needs

Thought:

Supports the need for a publication and export layer.

## 8. Search concepts used

The investigation searched across these concept families:

- AI comic generator
- AI manga generator
- graphic novel generator
- webtoon generator
- manhwa generator
- storyboard generator
- story to panels
- visual storytelling
- visual story-writing
- narrative AI
- worldbuilding agents
- creative writing skills
- character consistency
- character reference
- storybook consistency
- comic layout
- speech bubbles
- lettering
- motion comic
- comic to video
- story to video
- image-to-video
- agent skills comic
- skills.sh comic
- OpenClaw comic skill
- MCP comic generator
- story graph
- narrative graph
- world graph
- story bible
- canon engine
- lore engine
- asset provenance
- creative workflow orchestration
- multi-agent storytelling
- storyworld compiler
- publishing localization

## 9. Evidence quality and research thoughts

### Highest-confidence sources

- academic papers and official HTML/PDF versions
- source repositories and implementation files
- official documentation
- official product API pages
- first-party AvatarArts repositories

### Medium-confidence sources

- official product marketing pages
- GitHub topic pages
- skills registries
- MCP directories
- model cards and Space pages

### Lower-confidence sources

- SEO comparison pages
- marketplace summaries
- Reddit discussions
- community tutorials
- unverified user claims
- product pages making performance claims without tests

### Repeated thought across the research

The market repeatedly promises:

- character consistency
- full comic creation
- story-to-panel conversion
- easy publishing
- multi-format output

But the systems often do not expose:

- canon state
- motivation state
- evidence
- progression
- semantic diffs
- asset dependency graphs
- provenance
- regeneration scope
- branch history
- rights metadata

That is the main opportunity for AvatarArts Forge.

## 10. Research conclusion

The sources collectively describe a fragmented ecosystem:

    Papers explain how stories can be represented.
    Worldbuilding tools organize realities.
    Comic tools render pages.
    Character systems preserve appearances.
    Agent skills package procedures.
    MCP services expose capabilities.
    Publishing platforms distribute outputs.

Origin Story should preserve the evidence and compare these systems. Chozen should model authored realities. AvatarArts Forge should compile them into multimodal artifacts while preserving meaning, canon, identity, progression, continuity, provenance, and creator control.
