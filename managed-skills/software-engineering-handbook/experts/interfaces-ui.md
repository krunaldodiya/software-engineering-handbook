# Interface and UI experts

Use for the public API, module contract, or user-facing interface selected by
the canonical router.

## API and interface design

Define the contract before implementation:

- caller and owner;
- inputs, outputs, invariants, invalid states, and error semantics;
- authentication, authorization, validation, privacy, and rate/resource bounds;
- compatibility and version behavior;
- idempotency, ordering, concurrency, and partial-failure behavior where
  applicable; and
- migration, deprecation, observability, and acceptance evidence.

Use one versioned contract and one source of truth. Avoid speculative generic
interfaces, magic string resolution, or a second convention beside the existing
one. Validate untrusted input at the boundary and keep vendor/platform details
behind scoped adapters. A public contract change requires every caller,
document, test, and migration path in the authorized cutover.

## Frontend and interaction design

Start from the user's task and actual application surface. Reuse the established
design system, components, state ownership, and interaction patterns. Prefer
semantic HTML and native controls before JavaScript or dependencies. Preserve:

- keyboard operation and visible focus;
- labels, names, roles, states, and assistive-technology semantics;
- responsive behavior, readable contrast, zoom/reflow, and reduced motion;
- loading, empty, error, disabled, and partial-data states;
- deterministic state transitions and recoverable user actions; and
- privacy-safe analytics and network behavior.

Separate server, URL, shared application, and local view state deliberately.
Avoid duplicating derived state or adding a client store for one local flow.
Visual polish cannot hide missing behavior or inaccessible controls.

## Verification

API work needs executable consumer/contract checks for changed behavior and
failure semantics. UI work needs actual-browser or native-surface exercise,
accessibility-tree or equivalent semantic evidence, and visual confirmation at
relevant responsive states. A snapshot or build alone is not proof of
interaction behavior.
