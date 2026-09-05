# Requirements and planning experts

Use only the section whose trigger the canonical router selected. Repository
and tool facts must be discovered before asking the user.

## Interview and idea refinement

Original skills: `interview-me`, `idea-refine`.

Use when a consequential requirement remains underspecified or an idea needs
option comparison. Ask one decision at a time only when materially different
tradeoffs require the owner. State a recommended option and its cost. For facts
available in code, configuration, documentation, tools, or current state, read
them instead of asking.

Move from divergent options to one bounded proposal. Record the outcome,
non-goals, acceptance evidence, risks, and unresolved owner decisions. Do not
continue implementation through consequential ambiguity, but do not turn
ordinary reversible choices into approval ceremony.

For uncertain product value, challenge the premise using the intended user,
observed demand or current workaround, and the smallest useful outcome. Compare
material alternatives against that evidence before adding scope. Use only the
questions the current uncertainty requires; a fixed interview, alternatives
count, or product-validation ceremony is not a gate for routine engineering.

## Specification

Original skill: `spec-driven-development`.

Specify observable behavior, actors, inputs/outputs, valid and invalid states,
error outcomes, authority, effects, compatibility, data/resource bounds,
migration, and evidence before committing to a design. Reference authoritative
project contracts rather than copying them. The specification is complete when
an implementer can distinguish success from failure without inventing product
rules.

A specification is not mandatory for a trivial localized change. It must not
become a second tracker or substitute for working software.

## Constraint definition

Original skill: `constraint-driven-development`.

Use when the project lacks an explicit quality or operational bar. Derive the
smallest enforceable constraints from product risk, repository conventions, and
existing executable gates. Place cheap deterministic checks early and expensive
or environment-bound checks at the latest safe boundary. Never invent a
threshold, tool, or mandatory file merely because the original provider uses
one.

Constraints cannot be silenced, weakened, or reclassified merely to obtain a
green result. A changed constraint follows handbook exception and change-control
rules.

## Task decomposition

Original skill: `planning-and-task-breakdown`.

Decompose into vertical, independently verifiable tasks with explicit outputs,
dependencies, owned files/interfaces, acceptance evidence, and stop conditions.
Keep one mutation owner for shared files. Parallelize only genuinely independent
work. The plan must name real paths and commands and contain no placeholders,
scaffolds-as-deliverables, or deferred current blockers.

## Incremental implementation boundary

The related `incremental-implementation` original belongs to the quality and
operations module. Plans should nevertheless produce the smallest safe usable
slice first, then separately ordered improvements. A task is complete only when
its behavior and evidence are complete, not when a layer or skeleton exists.
