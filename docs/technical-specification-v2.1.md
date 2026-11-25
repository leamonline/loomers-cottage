# Loomer’s Cottage 2.0 · Consolidated technical specification v2.1

25 November 2026 · 66 owner-approved design decisions · P2.1 candidate prepared, not deployed.

This repository edition preserves the approved decisions and technical contracts. The private source holds instance bindings, exact live baselines, historical settings, and deployment manifests. Design approval does not authorize live changes. [Decision index](decisions.md) · [Release gates](roadmap.md).

## Part I · P2.1 decisions and precedence

# P2.1 decision register (33 additional approvals)
25 November 2026 · source: design interview in Loomer’s Cottage project. Original decisions retain identifiers O01–O33 (§1 of original specification). P01–P33 below are additive; later selections resolve conflicts as stated.

| ID | Approved choice | P2.1 implementation / later gate |
|---|---|---|
| P01 | D: Context-aware warnings | Distinguish unavailable, stale and confirmed; severity depends on source importance. |
| P02 | D: Context-aware expansion | Fixed order and widths, contextual detail in reserved areas; no reflow during interaction. |
| P03 | D: Adaptive hybrid accents | Stable category accents, text and icon warning overrides; natural environmental surfaces. |
| P04 | D: Detail panel with full view link | Modal focus return and internal destination navigation. |
| P05 | D: Intelligent architectural room cards | Six rooms, temperature and state-aware indicators; landing missing temperature explicit. |
| P06 | D: Adaptive atmosphere | CSS gradients by season, solar phase and weather; bounded transition; system reduced motion. |
| P07 | D: Contextually intelligent concierge | Deterministic prioritised facts and qualified inferences; expandable evidence. |
| P08 | D: Affected widgets + concise Right Now | Deduplicated priority list; affected widgets indicate state. |
| P09 | D: Predictive hybrid focus | Fixture context and deterministic rules now; approved learned preferences at L1/L2. |
| P10 | D: Intelligent defaults + granular control + pause | Local session preview controls; shared persistence deferred. Pause presentation only. |
| P11 | D: Shared preferences with device-specific overrides | Responsive profiles now; shared authenticated HA preference storage requires later gate. |
| P12 | D: Layered transparency | Short reason, source, age and rule evidence on demand. |
| P13 | D: Interaction lock | Freeze layout during dialog/focus interaction; no live updates in fixture-only Lab. |
| P14 | D: Context-aware escalation | Illustrate escalation policy only; notification delivery changes separately approved; never suppress safety. |
| P15 | A+B+C: Informative, advisory and predictive energy | No autonomous energy concierge; measured data, qualified advice, estimates only after C2 reconciliation. |
| P16 | D: Interactive learning | Evidence and review/correct/dismiss fixture; real approval/retention L1, bounded adaptation L2. |
| P17 | D: Privacy-first guest awareness | Manual/confirmed/inferred distinction; no individual guest profiling or security inference. |
| P18 | D: Context-aware override | Explain duration/extend/resume, preview only; C3 per-domain approval. |
| P19 | D: Self-monitoring home | Maintenance, history, diagnosis and approved repairs; no autonomous repairs. |
| P20 | D: Analytical workspace | Comparisons, graphs, qualified hypotheses; actual datasets C2/L1. |
| P21 | A: Consistent interface | Fixed category colours, order, shapes, navigation and interaction patterns; no arbitrary rearrangement. |
| P22 | C: Apple-inspired fluidity | Bounded eased/spring-like transition; reduced-motion always wins; real-client measurement. |
| P23 | D: Architectural hybrid | Translucent navigation and panels; softer natural-toned information widgets. |
| P24 | D: Refined hybrid typography | Georgia/system serif greeting, system sans labels, tabular numbers. No remote fonts. |
| P25 | D: Device-adaptive density | Compact <600, balanced 600–1023, rich ≥1024 CSS px; stable reading order. |
| P26 | B: Natural cottage | Limestone, sage, warm oak undertone; not a futuristic colour scheme. |
| P27 | A: Colour only | No photographic backgrounds, simulated grain or texture. |
| P28 | A: Limestone & sage | Light palette #F1EDE3 #D8D1C1 #A2B19A #63745D #343E34. |
| P29 | A: Midnight sage | Dark palette #182B24 #263C32 #3B5145 #A2B19A #E8EDE2. |
| P30 | D: State-aware icons | Fixed outline shapes, accented fill on activity; labels always present. |
| P31 | D: Intelligent lighting | Favourite scenes, brightness, recommendations; synthetic controls only until C1/C3. |
| P32 | D: Intelligent climate | Temperature, humidity, demand, predicted warm-up with evidence; commands C1/C3. |
| P33 | D: Context-aware security | Quiet summary, incomplete status explicit, cameras on request only after approval; sensitive actions separately gated. |

## Precedence and scope

P21 limits P02/P03/P06/P09 and refines O04/O25/O27/O28: maintain fixed visual anchors and category accent semantics, change only reserved detail content and background; do not reorder controls. P22 permits spatial transitions only for intentional navigation/panel opening, not unsolicited movement. P26–P29 refine O03/O06/O29: natural palette, no textures, translucent navigation rather than globally translucent widgets. P15 explicitly excludes autonomous energy management. P11 adds a later shared-preference storage contract; no browser-local storage is represented as synchronised. P14/P16–P20/P31–P33 are design requirements, not blanket approval to change automations or control devices. Original F1/F2 and C/L/R controls remain intact. The current roadmap and issue dependencies govern scheduling. P1 and P2 in the historical implementation table describe prototype stages. The P2.1 candidate is a fixture-only frontend demonstration, not the connected production release.


## Part II · Original architecture and decisions O01–O33

# Loomer’s Cottage 2.0 and Loomer’s Lab

Technical specification · 25 November 2026
**Authority** The approved design and later release gates apply to this repository edition. Deployment, device tests, installation and restore rehearsal require the gates below.

Cottage 2.0 is the stable household dashboard after acceptance. Loomer’s Lab is its permanent experimental counterpart. The stable dashboard and any approved Lab read mirror use the same Home Assistant data contracts. The fixture Lab runs offline. Apple Home stays available for everyday controls. The project starts by repairing existing references, then develops the adaptive dashboard in parallel. Home Assistant handles essential household functions independently of either dashboard or ChatGPT.

The standalone preview uses synthetic data. Connected telemetry, conditional dependencies and actuator capabilities require stage-specific verification.

## 1. Design decisions and acceptance

Original design interview decisions O01–O33. The source interview is held privately.

| ID | Approved decision | Implementation and acceptance |
|---:|---|---|
| O01 | Samsung bedroom TV wakes when Apple TV wakes | Verify direct power and observed HDMI-CEC privately. Disable the HA wake automation after gate F1 and retain its configuration for rollback. Verify cold and standby wake, sleep and backlight behavior. |
| O02 | Intelligent hybrid dashboard | Information takes precedence. Context reveals relevant controls within fixed routes and stable widget positions. |
| O03 | Apple-inspired clarity with futuristic intelligence | Rounded modules, system-style typography, restrained color and clear summaries. Detail includes useful trends and live indicators. |
| O04 | Adaptive information density | Routine conditions stay compact. Relevant events expand their own module or appear in Right Now. |
| O05 | Functional tabs and room pop-ups | Eleven destinations and six room details. Every room also has a stable deep link and Back destination. |
| O06 | Adaptive macOS 27 and iOS 27 inspired appearance | Layered translucent surfaces, restrained depth and automatic light/dark appearance. Opaque treatment supports reduced transparency or slower devices. |
| O07 | Factual summary with deeper intelligence on tap | Open history, explanations and supported recommendations from a reading. |
| O08 | Subtle affected-card alerts | Small icon with accessible severity text. Detail explains cause, age and action. Existing safety notifications remain independent. |
| O09 | Contextual room cards | Surface temperature where mapped. Add room-specific heating, humidity, lighting or fault indicators when relevant. |
| O10 | Contextual room shortcuts | Show an appropriate quick control only when relevant and supported. Room details retain the full approved controls. |
| O11 | Adaptive room detail with stable controls | Current conditions first. Device group order remains consistent. |
| O12 | Adaptive energy presentation | Consumption, cost, tariff or charging gets emphasis according to current context. All permanent metrics stay present. |
| O13 | Integrated Mokka management | Dedicated view includes vehicle state, charging, energy and costs, security and service information, with gated commands. |
| O14 | Explainable automations and overrides | Show source, observed reason, next scheduled action when known and an override only where supported. |
| O15 | Context-aware override duration | Expose expiry, Extend and Resume when supported. Durations respect each automation’s native boundaries. |
| O16 | Supervised household learning | Recommendations first. Later changes require per-policy approval and bounded adaptation. |
| O17 | Combined awareness | Combine schedule, daylight, environment, activity and approved preference. Indicate inference and confidence. |
| O18 | Hybrid guest awareness | Manual guest state, explicit confirmation and cautious inference. Label inferred presence and expose undo or expiry. |
| O19 | Context-aware security | Quiet summary, expansion on door/doorbell/unusual activity, camera only on request and explicit unknown states. |
| O20 | One dashboard with device-aware experiences | Same features and route contracts on iPhone, iPad and Mac, with layout and density tailored to each. |
| O21 | Analytical history | Graphs, comparisons, significant events, patterns and grounded suggestions where coverage supports them. |
| O22 | Adaptive performance | Keep Home light. Mount costly graphs, camera and richer effects on demand. Measure against §8. |
| O23 | Community plus bespoke components | Reuse installed components where useful. Build missing behavior as locally served, versioned components. Review each dependency at its gate. |
| O24 | Single-user personalization | One preferred dashboard layout and settings. Guest mode is household behavior. Existing HA authentication still applies. |
| O25 | Customizable permanent favorites | Save widget preferences for the owner. Restore the supplied defaults and give contextual content its own space. |
| O26 | Fourteen permanent categories | All fourteen are present on default Home, including explicit unavailable or pending labels. See §3. |
| O27 | Variable-size modular widgets | Group related readings and use compact, medium and wide slots. Maintain reading order and sensible keyboard focus. |
| O28 | In-place expansion plus Right Now | Expand the existing widget when it owns the data. Put other temporary content in Right Now, with no duplicate alert. |
| O29 | Environmental backgrounds | Local conditions, solar phase and season drive a restrained palette alongside automatic light/dark. |
| O30 | Eleven permanent destinations | Home, Climate, Energy, Mokka, Security, Entertainment, Routines, Learning & insights, Home Health, Settings, History & analytics. |
| O31 | Device-adaptive navigation | Floating iPhone dock with More, adaptive iPad sidebar and full Mac sidebar. Every route is addressable from each device. |
| O32 | Contextual greeting with concierge on tap | Brief factual summary at startup. On demand expand into source-linked explanations, forecasts and suggestions. |
| O33 | Parallel prototype, then a permanent Lab | Separate versioned builds on shared data, production cutover by approval, and permanent isolated experiments with a promotion process. |

## 2. Architecture and design system

- Create two new storage dashboards when approved. Prototype and eventual stable dashboard use `loomers-cottage-2` with title **Loomer’s Cottage 2.0**. Permanent experiment dashboard uses `loomers-lab` with title **Loomer’s Lab**. Both initially admin-only and hidden from the HA sidebar. Confirm route availability before creation. Keep the existing dashboard defaults until cutover. Admin-only limits dashboard access and is independent of entity-level authorization.
- Use native Sections, conditional cards, Tile and subviews for the functional baseline. Use the same view schema and allowlisted bindings across devices. Existing room routes provide a fallback while the new subviews are built. Dashboard configuration changes use HA’s supported dashboard editor or configuration API with fresh hashes.
- In Lab, prototype a locally served, versioned custom card for dashboard-scoped navigation, responsive widgets, drawer/dialog behavior and conditional imports. Use documented HA custom-card state and configuration interfaces. Where shell integration depends on undocumented HA internals, keep the dock/sidebar inside the dashboard’s own view and preserve native HA navigation as the fallback. Browser Mod is excluded from the initial dependency set. Bubble Card can be tested as a popup fallback, including close, browser Back and hash conflict behavior.
- Use HA Core and existing integrations as the canonical state and action owners. Presentation derives from state, with shared typed bindings for value, unit, timestamp, availability and provenance. Use explicit allowlists for UI actions. Lab defaults to synthetic fixtures and has no live actuator bindings. An optional live read mirror requires the same authenticated session and exposes only the approved display fields. Only approved production policies call existing device actions.
- Use the system font stack, 4/8/12/16/24/32 px spacing, 16–24 px corner radius, one background layer, a tint and a low-radius blur only where measured. Native baseline can use scoped opaque cards. Proposed grid breakpoints are under 600 CSS px, 600–1023 px and ≥1024 px. iPhone gets four primary items (Home, Climate, Energy, Mokka) plus More. iPad uses collapsible sidebar and Mac uses persistent sidebar. Keep safe-area inset, current page semantics, visible focus, 44 px minimum touch targets, keyboard Back/Escape, focus return and standard 4.5:1 text contrast.
- Background resolves automatic light/dark to a restrained palette by solar phase, coarse weather bucket and meteorological season. Update on source change or phase boundary. Use a static neutral fallback for missing inputs and respect reduced motion/transparency preferences. Color accents communicate status alongside text and icons.
- Proposed implementation artifacts are a versioned binding manifest, shared card source, stable/Lab dashboard definitions and a release manifest with resource checksums. Keep a native-only dashboard export for recovery. Resource registration is instance-wide, so preflight the effect on every existing dashboard and keep the first entry small. Never ship client code that embeds credentials or fetches public fonts, analytics or contextual assets at startup.

[Home Assistant dashboard views](https://www.home-assistant.io/dashboards/views/) · [Home Assistant custom card API](https://developers.home-assistant.io/docs/frontend/custom-ui/custom-card/)

## 3. Home and functional routes

### Permanent Home widgets

Each of these categories has a stable default place. Favorites may be selected subject to P21’s fixed visual anchors and stable category order. Below the favorites provide six room entry points and a Right Now region. In a narrow viewport preserve semantic order and allow scrolling.

| Widget | Permanent categories | Source and display contract |
|---|---|---|
| Weather and daylight | Weather, sunrise and sunset | Show condition and temperature in °C from the approved weather source. Show sunrise and sunset in local time and label tomorrow when applicable. Fetch forecast only on expansion. |
| Comfort | Indoor temperature, indoor humidity, heating status | At launch show labeled Living Room temperature and humidity using the room temperature source and the room humidity source. Expand to each measured room. The heating demand source indicates whole-home demand. Do not infer active heat from the `heat` mode. |
| Energy | Live electricity consumption, energy costs today, current energy tariff | The power source provides live power in W with meter scope recorded before calling it grid import. Current import tariff from the tariff source in GBP/kWh, displayed in p/kWh. Today’s cost shows “Awaiting data” initially and can offer last complete day with date and source. |
| Security | Home security | Use approved lock, contact and smoke sources. Show each lock/contact separately. Unknown required inputs yield “Status incomplete”. |
| Mokka | Battery and range | Show battery and range with source age. Expand for charging and controls. |
| Schedule | Upcoming routines | Use approved schedule, wake, pre-sleep, bedtime and active routine sources. Future entries must have a source and local timestamp. |
| Entertainment | Currently playing music | Use approved room playback sources. Show supported current playing metadata, or “Nothing playing” only when the relevant sources are healthy and idle/off. |
| Home Health | Household health | Show the verified health summary and explain its components. Detail separates backup age, Watchman candidates, battery, unavailable and intentionally excluded devices. |
| Occupancy | Household occupancy | Use approved person state, operational guest state, guest automation mode and applicable room occupancy sensors. Show home/away from the person source and guest mode separately. Presence detection is inferred unless explicitly confirmed. |

### Eleven permanent views

All paths are relative to the selected dashboard. Drill-down subviews link back to the parent. Write controls in this table are implementation proposals subject to stage and actuator approval.

| View / path | Content and behaviors |
|---|---|
| Home / `home` | Briefing, all favorites, room entry points and Right Now. Opening a widget provides details. Security actions and vehicle commands live in their own views. |
| Climate / `climate` | Four measured rooms with temperature, humidity, heating demand, schedule and mold/ventilation signals. Expose verified climate setpoint and named resume buttons after actuator sign-off. Use the displayed zone’s configured min/max/step. Show bathroom humidity history on demand. |
| Energy / `energy` | Live house and EV power, tariff now/next, known dispatch status, electricity/gas consumption and costs with source labels, standing charge separately, and plugs/charger breakdown. Link to the HA Energy dashboard for official stored setup. See §6. |
| Mokka / `mokka` | Car status, range, charging and costs, security, maintenance and battery health. Partition sources by Stellantis, Hypervolt and Octopus. Display location only on request. Gated remote commands require target confirmation, freshness checks and action acknowledgement. |
| Security / `security` | Locks, door contacts, occupancy signals, smoke, doorbell event and access to the camera on request. Existing emergency notifications run independently. A separate approval decides which manual lock operations enter the release. |
| Entertainment / `entertainment` | Room players, actual playback state and an approved speaker selection helper where supported. Distinguish playback targets by room and disable unsupported controls. |
| Routines / `routines` | Existing calendar planner, wake/preheat/bedtime signals, guest mode and circadian state. Show observed trigger, action result and known next scheduled time. Avoid exposing pulse helpers as durable toggles. |
| Learning & insights / `learning-insights` | Recommendation queue, evidence window, observations, confidence, dismiss/snooze/approve controls and experiment history. Stable starts in advisory mode. |
| Home Health / `home-health` | Confirmed faults and uncertain reports, backup inventory/status, integrations, batteries and updates with timestamp. Link to current Home Health while the new view is validated. Firmware/update actions stay in HA settings for first release. |
| Settings / `settings` | Owner favorites within fixed positions, display/theme preference and local support details. Stable/Lab link and release IDs. Use one owner preference store after cross-device verification. HA settings and security management stay on the native admin surface. |
| History & analytics / `history-analytics` | On-demand raw 24 h history and 7/30-day aggregated comparisons for supported inputs. Compare like periods, disclose gaps and units. Significant changes and automation traces are separate evidence streams. |

### Six room details

Proposed routes are `living-room`, `kitchen`, `bedroom`, `bathroom`, `landing`, `garden`. A popup uses the same room definition as its subview. Open the subview if the popup component fails. Group controls in this order where applicable: lighting/scenes, heating/ventilation, blinds, media, appliances. Proposed scope follows.

| Room | Proposed read context and gated controls |
|---|---|
| Living Room | Temperature, humidity, heating, lights, blinds and media |
| Kitchen | Temperature, humidity, heating, lights and appliance status |
| Bedroom | Temperature, humidity, heating, lights, blinds and TV |
| Bathroom | Temperature, humidity, heating, lights and extractor state |
| Landing | Motion, lighting and explicit unavailable temperature when unbound |
| Garden | Motion, lighting and clearly labelled outdoor forecast |

Resolve all room bindings from the approved private manifest. Preserve existing fallback navigation.

## 4. Context, automation explanations and learning

### Context contract

Normalize each input to value, source ID, source time, observed time, quality (confirmed, inferred, stale, unavailable or unknown) and unit. Freshness uses the integration’s expected update interval and a genuine data/report timestamp when exposed. Stable states can remain valid beyond their last change. For initial fixtures, use 5 min for actively reporting power, 30 min for room climate and 60 min for weather or vehicle telemetry, subject to source cadence calibration. Mark the last-known reading with its age. Hide action hooks whenever a safety prerequisite is stale or unknown.

Evaluate on changes to selected inputs and time boundaries, with a proposed 300 ms UI debounce for routine display changes. Precedence is safety/unknown security, current activity, scheduled transition, then passive context. Examples include doorbell or unusual activity expanding Security, high humidity expanding Comfort, EV power/dispatch expanding Energy or Mokka, and out-of-category activities in Right Now. Rank by severity and time, deduplicate by source/event identity, and expire transient items with their source condition. Keep favorites’ anchors and reading order fixed. The greeting uses local time and factual, source-linked conditions, with richer explanation generated on request from the same context. Any future external concierge requires separate data and access approval.

Use the verified guest mode helper and give manual selection precedence in the proposed display. Review any current automation that can set guest mode privately. Show “Guest mode on, source unconfirmed” unless attribution is recorded reliably. Inspection and testing of undo, quiet reset and cooldown are required before any refinement to existing guest logic. Guest status never changes lock or security policy.

### Existing automation ownership

Home Assistant owns TV wake, Thread device alerts, humidity extraction, heating schedules, lighting, charging, and access policies. Review trigger and action definitions, recent outcomes and consumer dependencies privately. Preserve independent safety rules. Capture source time, action or skip outcome and the next action only when calculable.

### Overrides and supervised adaptation

- Start with existing domain controls. Heating’s explicit Resume action targets only the corresponding verified Resume action. Only surface extension where the provider exposes expiry and its supported extension operation. Existing lighting uses a one-hour manual hold. Reuse its owning script or timer only after confirming per-room timer bindings and restart behavior. Show expiry only when measured. First release excludes override actions for ventilation safety, smoke, locks and EV dispatch.
- Later candidate overrides use a per-domain allowlist with native duration bounds, an absolute local display time derived from an unambiguous UTC deadline, one policy owner and explicit Extend/Resume actions. Manual restart or expiry reevaluates current conditions. Stale context, repeated taps, restart across expiry and simultaneous automation requests must leave policies in a consistent state. Stage C3 requires a reviewed object-level change and rollback.
- Learning v1 runs in Lab on local, bounded aggregates and produces proposals only. Start with one low-risk scenario, recurring edits to a lighting schedule, using same-context opportunities by weekday/time band. Proposed start criteria are ≥14 eligible observations over ≥21 days, ≥80% coverage and ≥70% agreement. Display sample size, period, coverage, exclusions, proposed change and the measured outcome. Guests, unavailable measurements and unusual one-offs are excluded by declared rules. No recommendation when evidence is insufficient. No identity inference or export of occupancy/vehicle history.
- Learning v2 requires per-routine approval with a signed-off adjustment bound. Proposed first policy is a lighting schedule offset of at most ±15 min, evaluated weekly, with a 7-day cooldown, explicit stop and rollback to previous schedule. Simulate DST transitions and manual holds. Security, smoke, heating protection and EV control stay outside automatic learning. Use Recorder/local facts first. No AppDaemon or other new runtime is needed for dashboard, context or the first offline learning experiment.

## 5. Live capability and dependency baseline

Keep health and registry exports, automation and trace inventories, live measurements, dashboard paths and fingerprints, local module inventory, and resource IDs in the owner’s private evidence. At each applicable gate re-read affected objects and dependencies, and verify against that evidence. Validate locally served dependency versions and native fallbacks before promotion.

## 6. Foundation changes and energy contract

### F1. Retired bedroom TV plug and TV wake

Review the owner-observed HDMI-CEC path. After exact diff and backup approval, disable the legacy wake automation while retaining its body, remove the retired outlet from both Thread alert branches, update affected dashboard controls and warning consumers, and remove only the obsolete device consumption preference. Preserve registry entries, historical statistics and genuine faults. Search remaining references against approved exceptions. Verify cold and standby wake, sleep, backlight and passive Thread behavior. Confirm exact targets and paths from the private manifest.

### F2. Other stale references and device warnings

Verify missing bindings, especially the door battery candidate, before any change. Preserve genuine unavailable device warnings and validate the Home Health producer before editing consumers. Bathroom ventilation, garden notifications and EV conflicts require separately reviewed fixes and retained safety behavior.

### C2 and E1. Energy and Mokka data model

Use native Energy statistics for historical values. Keep supplier electricity and gas consumption and costs separate from live sensor states. Identify whether charger readings describe house, grid or EV power, and prevent the charger from being counted twice. Track current and next tariff, dispatch windows, timestamp, units, provenance and stale/unavailable status. For a verified estimate, multiply metered interval consumption by the matched tax-inclusive tariff and display standing charges separately. Compare completed billed periods, allow for delayed intervals and DST, and label estimates and gaps. Vehicle location and commands require separate approval. Review target capabilities, freshness and acknowledgement beforehand.

## 7. Backups, staged delivery and release authority

### Recovery baseline

Backup receipts, fingerprints, location and identifiers belong in private recovery evidence. G0 requires verified encrypted off-host retrieval and isolated restoration.

- Before each approved state-changing batch capture the exact affected objects, current hashes, dependencies, versions and previous dashboard/default settings. Before F1, the first dependency/resource registration and cutover, take a new encrypted snapshot including database and the configuration/Apps required for recovery. Verify completed snapshot, included contents and matching off-host copy. Retain a protected pre-stage copy past the change window so normal automatic retention cannot remove the rollback point.
- Object rollback is the first response. Restore the prior dashboard JSON through the dashboard interface, automation body and enabled state through the config API, and Energy preference rows through the corresponding key after re-reading. Restore stable resource URL and dashboard references from the release manifest if a frontend regression affects users. Record and reconcile concurrent edits. Restore the broader archive only if object rollback cannot recover the required behavior, with explicit restore approval and downtime. Restore database only if required, considering history loss after the backup. After any restore, check logs, loaded integrations, automation states, dashboards, matter/Thread, Apple Home and backup state.
- Rehearse restore in an isolated HAOS instance with outbound integrations, notifications and radios isolated. Confirm access to the decrypted archive, dashboard paths, data history and recovery procedure. Retire rehearsal copies securely after acceptance. No restore, restart, backup creation or test device actuation was performed for this specification.

[Home Assistant backup procedures](https://www.home-assistant.io/common-tasks/general/#backups)

### Historical implementation tickets

Current dependencies and release gates are maintained in the [roadmap](roadmap.md) and issue backlog. The rows below retain the original deliverables and rollback intent.

| Gate / dependency | Exact proposed scope | Approval and exit evidence | Rollback |
|---|---|---|---|
| G0 · Source and recovery lock | Re-read the objects in §5–6, record the owner’s current dashboard defaults and verify pre-stage snapshot plus recovery kit. Build versioned, secret-free fixtures of affected display inputs and expected app actions. | Approve the specification and initial capture boundary before any HA write. Confirm authority for a pre-change backup before creating it. Require the archive/release point, fresh hashes and disposable test setup before applying configuration changes. A binding change or new live consumer requires revised scope. | Discard the draft export or fixture. Use the current dashboard as the access path. |
| F1 · G0 | Apply the TV wake disable, two Thread list edits, 17 card edits and one Energy consumption row removal from §6. | Approve the exact object diffs and wake test window. Verify existing dashboard hashes/diffs, unchanged backlight behavior, CEC wake/sleep and surviving Thread targets. | Restore three dashboard configs, Thread automation and exact Energy row from captured versions. Before re-enabling the old wake automation, confirm that its retained plug target can safely accept the original power command. Use the TV’s physical remote if the old path is unsafe or unavailable. |
| F2 · F1 | Triaging warnings and mapping replacement candidates. First proposed patch is the back-door battery binding where confirmed. Change the attention producer only after its exact source and consumers are inspected. | Present candidate-level diffs with source proof, owner acceptance of exclusions and read-back/render evidence. Device repair/unlink requires a distinct approval. | Restore the prior binding/template or ignore list, then recheck actual faults. |
| P1 · G0 and resolved F1 bindings | Create hidden admin-only `loomers-cottage-2`. Add eleven route entries and six subviews with native Sections/Tile baselines, approved widget defaults and safe read-only states. Stage Lab fixtures offline first. | Approve parallel dashboard creation. Confirm all navigation works, all 14 categories are reachable, and legacy default opens normally. | Revert or remove only the new prototype definition and use the current default. |
| P2 · P1 | Build versioned scoped Lab preview of responsive dock/sidebar, room popup, contextual widgets and backgrounds. Create hidden admin-only `loomers-lab` if approved and needed to test HA parity. Register at most one lightweight initial new local module after review. Reuse installed dependencies only for their chosen features. | Approve local bundled source and any global resource registration separately. Pass fallback, no unintended network/actions, cache invalidation, browser accessibility and no legacy regression. | Restore prior resource registry and dashboard build. Use native prototype or the legacy dashboard. |
| C1 · P1/P2 | Binding and action allowlist review, including existing individual room scenes/devices, player operations, weather, occupancy and owner preferences. Add contextual content in fixed positions, greeting and drill-downs. | Approve first read-only mirror for test and then individually approved low-risk actuator categories. Confirm Mokka, guests and security unknowns and camera on-demand behavior. Complete an actuator checklist before adding an action per entity. | Disable release flags or restore prototype. Existing integration and automation owners remain authoritative. |
| C2 · C1 | Add Energy/Mokka read-only presentation and Recorder detail, history coverage, and cost methodology from §6. Add calibrated estimate only after reconciliation. | Approve data/label contract. Separate gate for EV actuators, location and commands. Verify one ordinary day and one real Smart Charge session before same-day cost goes live. | Restore previous card/binding version. Retain current native Energy configuration except the F1 row. |
| C3 · C1 | Add trace-based explanations and eligible existing Resume/hold behavior. Add Extend only with verified owner integration semantics. | Approve exact target, scope and tests per domain. Require timer/expiry/boot review and mutual exclusion against existing rules. | Revert dashboard action or owning automation diff, clear newly created override state if used, and resume prior domain policy with owner oversight. |
| L1 · C1/C2 | Add read-only recommendation experiment with local statistics and evidence, then stable advisory view after successful trial. | Approve data scope, retention, sample criteria and specific recommendations independently. Demonstrate no action path from a recommendation alone. | Disable or remove the experiment route/policy and roll back its local artifacts. |
| R1 · F1, P2, C1, C2 and baseline C3/L1 | Freeze accepted release, repeat backups and verification, expose stable dashboard in sidebar, and designate it as owner default on approved profiles/devices. Keep legacy favorites and route bookmarks for recovery. Maintain permanent Lab for experiments. | Owner approves cutover and known residuals. Allow a seven-day parallel observation period with daily summary of regressions when measured. Keep security and optional EV controls behind their own gates. | Repoint defaults and sidebar to prior dashboard, then revert the relevant object or release module. |
| L2 · R1 and advisory evidence | Optional bounded adaptation trial for one approved low-risk lighting policy. | Separate approval per policy, limits and stop switch, verified 21-day evidence and simulation. Requires a named rollback state. | Stop adaptation, restore prior schedule and check manual control plus the recorded reason. |

When promoting Lab changes, record Core and resource versions, approved code/config diff, binding changes, fallback behavior and verification result. Stable loads only a tested release. Lab samples production data only with the approved read mirror and fails closed if the routing or action boundary cannot be guaranteed. Older dashboards may later be hidden or removed through an independently approved retirement change.

## 8. Test plan and performance budget

Measure the HA Green and Recorder baseline privately before testing release budgets.

### Proposed release budgets

| Measure | Provisional pass threshold and method |
|---|---|
| First useful Home | LAN cold p95 ≤2.5 s, warm p95 ≤1.2 s. Remote cold p95 ≤4 s on the same device with connection and conditions recorded. Start at navigation and stop when navigation plus weather, comfort, security and Energy values or valid fallback labels appear. |
| Interaction | Warm view transition p95 ≤500 ms. Room open, More and dismiss respond visibly ≤150 ms at p95. Test scroll, keyboard operation and quick successive route changes without stale content. |
| Initial payload | New Home’s view definition ≤35 KiB uncompressed, total new dashboard config ≤120 KiB, and ≤100 KiB compressed incremental startup resources compared with native baseline. Measure storage response separately from wire bytes and existing globally loaded modules. |
| Deferral | On clean Home startup, zero camera streams and zero history/statistics queries. Open exactly the requested detail and release streams/subscriptions on close. No whole-house sensor-list scan on every state change and no added upstream polling for live display. |
| Chart limits | Initial chart ≤4 series and ≤300 plotted points per series. Prefer aggregates and coalesce identical reads. 24 h raw views cap samples and disclose downsampling. Cancel or discard stale responses when range or route changes. |
| Green workload | Under a scripted 15 min two-client navigation workload, mean CPU ≤ baseline +5 percentage points, mean memory ≤ baseline +5 points and no sustained ≥75% memory for five consecutive minutes. Compare with a matched idle workload and investigate new Recorder growth over 72 hours before adding recorded data. |
| Stability | Four-hour open Home soak while inputs change. No growing requests/subscriptions, unbounded memory, console errors tied to release, lost focus, duplicate actions or continued camera traffic after close. |

Run 20 cold and 20 warm navigations per primary profile/surface and report sample count, p50/p95, config/resource versions and observed network. Primary profiles are real iPhone HA Companion, iPad Companion/Safari and Mac Safari. Use a desktop Chromium run for diagnostics. Test normal and reduced motion/transparency plus landscape and narrow widths. Keep the native fallback if a custom surface misses budget. Record any revised budget explicitly at P2 or R1.

### Release verification

| ID | Scenario and acceptance |
|---|---|
| V1 | Navigation and all 14 favorites across devices with keyboard and touch. Rotate and revisit, open a room from Home, close via Back/Escape and restore focus and scroll. Deep links load on refresh. Every missing measurement displays an explicit label. |
| V2 | Replay normal, bedtime, away, humidity, charging, doorbell, stale and unknown fixtures. Confirm context ordering, no favorite displacement, accurate guest/unknown language and no duplicate alerts. |
| V3 | Exercise known cold/warm TV wakes after F1 approval, Thread recovery in fixtures and passive live evidence, genuine health faults and legacy Energy charts. Search for retired plug references and match the approved exceptions in §6. |
| V4 | Apply approved low-risk actions one category at a time. Trace target, command count and acknowledgement. Test rejection, disconnected device and repeated taps. No actions to a missing/stale target. Security and vehicle only in their authorized test windows. |
| V5 | Test manual lighting hold and heating Resume, expiry/restart behavior in isolated fixtures, DST and simultaneous interactions. Confirm safety actions and existing Apple Home paths keep their owners. Explain using real traces, with missing evidence labeled. |
| V6 | Reconcile Energy datasets with different delay and units, partial coverage, current rate, ordinary charging, Smart Charge and DST. Verify the optional estimate only with evidence and the thresholds in §6. |
| V7 | On Home startup and normal room views, inspect network and runtime. Verify camera only on explicit request and stopped after exit. Verify native fallback on missing resource, loss of WAN and current entity unavailability. |
| V8 | Verify a Lab fixture emits no production action requests, the approved read mirror sends no writes, and only the promoted stable build can expose an approved action. Validate recommendation lifecycle and stop controls. |
| V9 | Restore object exports in rehearsal. Confirm one wider protected backup can be recovered on an isolated instance with the approved key. Check behavior and record results before R1. |
| V10 | Record performance runs and compare p95, App/host/Recorder metrics, console logs and request counts with native and existing dashboards. Recheck after Core or installed-resource updates before promotion. |

### Remaining evidence and release impact

| Open item | How it gets resolved |
|---|---|
| Real Apple-device behavior, current defaults and native fallback access | Read-only baseline and later P2/R1 client tests with the owner. No dashboard rendered or timed as part of this MCP audit. |
| Samsung wake without the legacy automation, real camera streaming, Apple Home exposure and commands | Owner-approved device tests. Review HomeKit bridge exposure only if an approved proposed change affects it. |
| Accurate same-day household cost, effective tariff, meter topology and historical dispatch coverage | Compare interval, meter and supplier evidence in C2. Charge and rate candidates stay clearly labeled when evidence is incomplete. |
| Home Health attention producer, Watchman false positives and remaining scanner items | Map each actionable candidate to current source and affected consumers during F2. |
| Per-client Browser Mod/Bubble behavior, custom navigation and cross-device preference persistence | P2 proof on real Apple devices and native fallback. No dependency purchase, install or upgrade assumed. |
| Landing temperature, dedicated garden temperature and complete room action allowlists | Bind confirmed sources only after registry/area review. Retain fallback labels from §3. |
| Recorder exact raw per-entity coverage, learning inputs and cost/vehicle history window | Probe bounded windows at C2/L1 and expose coverage to the user. Use the installed provided series and choose raw vs aggregate by verified support. |
| Off-device retrieval, recovery kit and decrypted test restore | G0 and V9. The protected archive, same-ID Mac copy and upload receipt are already observed. |

## Part III · P2.1 implementation and acceptance

The candidate is a fixture-only frontend. The standalone preview uses seven synthetic scenarios, nine grouped widgets, six room cards and eleven internal destinations. It has no live binding, device action, external asset or shared preference storage. The archive report records 120 Chromium assertions. The original harness and the additional browser regression suite both exercise the imported component.

### Deployment and object rollback

Deployment remains issue #6. Require G0, exact current config and resource hashes in a private manifest, an approved diff, and separate approval for a new global resource and Lab route. Use the supported Home Assistant configuration interface. Preserve existing dashboard defaults, resources and routes. Stop on drift, unexpected browser policy restrictions or a mismatched read-back. If needed, confirm whether a resource was registered before retrying. Verify the installed source, route and all legacy views before any promotion.

On failure, use the legacy route. After approval, re-read current state and remove only the reviewed additions with tested paths and optimistic locking. Search all references before removing the newly added resource and obtain separate deletion approval. Preserve legacy resources. An isolated restore rehearsal is part of G0. Any full restore requires separate authorization.

## Acceptance matrix
| Test | Criterion | State |
|---|---|---|
| T01 | Node syntax valid; 4 viewports × light/dark, 15 assertions each | Source report records 120/120 |
| T02 | 9 grouped widgets and 6 rooms; no page horizontal overflow | Source report records a pass in its local harness |
| T03 | Concurrent charging+humidity; unknown lock; stale vehicle age; smoke highest priority; uncertain occupancy | Source report records a fixture pass |
| T04 | Open detail, Escape, focus return; Settings reachable through mobile More or sidebar; environment off | Source report records a fixture pass |
| T05 | No external requests and no JS page errors in harness | Source report records a fixture pass. Live HA traffic pending |
| T06 | Every route accessible across iPhone/iPad/Mac, keyboard and touch, parent/back behavior, refresh of HA preview link; 44px targets | Pending real HA and complete route-by-route check |
| T07 | Inspect normal-motion transitions, OS light/dark, reduced transparency, contrast ≥4.5:1, screen reader, orientation, no dock overlap with HA chrome | Pending visual/accessibility measurement; local tests use reduced motion |
| T08 | Global pause freezes presentation but not warnings; no focus loss, no unexpected movement on live readings; real source ages | Partial fixture support, pending future live read mirror and interaction tests |
| T09 | Existing five dashboards and previous Lab unchanged; no duplicate module or console errors | Pending deployment regression |
| T10 | Original V1–V10 budgets, 20 cold/warm runs per primary device, 15-minute two-client load and 4h soak | Pending; no measured p95 or Green load claims |
| T11 | No camera/history requests on startup; no command path; actual HA network inspection | Source report records a static and fixture pass. Live HA traffic pending |
| T12 | Energy estimates, real learning/overrides, notifications, lighting/climate/security controls | Deferred to C1–C3/L1/L2, no device tests authorised |
| T13 | Rehearse rollback on copied config, verified off-site recovery and separate isolated restore | Pending |

The repository includes the archive’s original browser assertions and historical JSON results, plus a supplemental browser suite. Both load the component in memory. Tests establish DOM behavior only, not visual quality, performance, actual Apple hardware or service safety after future integration. Current CSS uses eased modal entry rather than a full native spring physics engine. Source age and readings are synthetic, not live. Global pause presently disables environmental changes and predictive summary, not all contextual highlights. Detail routes are intentionally minimal; no real brightness/temperature sliders, charts, camera playback, synced preferences or notification changes. Further code needed to meet those requirements. Category colour accents are fixed and warnings contain labels; full contrast testing remains open. Weather/solar gradients are simple fixture mapping, not production environmental resolution. No texture assets.
