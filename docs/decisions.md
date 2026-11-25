# Decision register

The [repository edition of the v2.1 specification](technical-specification-v2.1.md) records the approved choices and acceptance contracts. The release gates are defined in the [roadmap](roadmap.md) and issue dependencies. Design approval covers the product direction. Live changes require the engineering and recovery gates.

## Original decisions

| ID | Approved choice | Evidence or release gate |
|---|---|---|
| O01 | Samsung bedroom TV wakes when Apple TV wakes | F1 · Confirm HDMI-CEC wake and retire obsolete plug references. |
| O02 | Intelligent hybrid dashboard | P2.1 illustrates context in fixed slots. C1/C2 connect data and C3 gates controls. |
| O03 | Apple-inspired clarity with futuristic intelligence | P26–P29 refine the visual system. C2/E1 supply trends. |
| O04 | Adaptive information density | P02/P21 keep expansion within fixed slots. P25 sets breakpoints. |
| O05 | Functional tabs and room pop-ups | P2.1 shows dialogs and internal routes. C1 verifies stable deep links and native Back. |
| O06 | Adaptive macOS 27 and iOS 27 inspired appearance | P23 scopes translucent surfaces. Verify reduced transparency and fallback on Apple devices at #6. |
| O07 | Factual summary with deeper intelligence on tap | P2.1 shows synthetic briefing details. C2/E1 supply validated facts and history. |
| O08 | Subtle affected-card alerts | P2.1 shows affected cards and Right Now. P14 keeps safety escalation independent. |
| O09 | Contextual room cards | P2.1 shows six synthetic room cards. C1 validates real readings and unavailable states. |
| O10 | Contextual room shortcuts | C1 verifies capabilities. C3 gates the shortcuts and target allowlists. |
| O11 | Adaptive room detail with stable controls | P2.1 shows room context. P13/P21 stabilize interaction. C3 gates controls. |
| O12 | Adaptive energy presentation | P2.1 illustrates contextual emphasis. E1 validates tariff and cost sources. |
| O13 | Integrated Mokka management | P2.1 illustrates vehicle readings. C1/E1 verify data and separate approval governs EV commands. |
| O14 | Explainable automations and overrides | C2 adds factual explanations. C3 gates supported overrides. |
| O15 | Context-aware override duration | C3 verifies expiry, Extend, Resume and exclusions. |
| O16 | Supervised household learning | L1 is advisory. L2 requires separate approval and signed limits. |
| O17 | Combined awareness | P2.1 illustrates fixtures. C2 validates inputs. L1 governs learned preferences. |
| O18 | Hybrid guest awareness | P17 refines guest handling. C2 validates attribution and uncertainty. |
| O19 | Context-aware security | P2.1 shows incomplete status. P33 gates camera and sensitive operations separately. |
| O20 | One dashboard with device-aware experiences | P25 sets density. C1 and #6 verify device-specific layouts and route parity. |
| O21 | Analytical history | C2/E1/L1 provide bounded, validated datasets. |
| O22 | Adaptive performance | P2.1 has no startup network. #6 and R1 require measured device and Green budgets. |
| O23 | Community plus bespoke components | Review native and local dependencies at their gate. P2.1 is standalone. |
| O24 | Single-user personalization | Use authenticated owner preferences under C1. C2 governs guest context. |
| O25 | Customizable permanent favorites | P21 fixes layout anchors. C1 establishes supported preference storage and defaults. |
| O26 | Fourteen permanent categories | P2.1 groups fourteen categories in nine widgets. C1 validates connected data. |
| O27 | Variable-size modular widgets | P21 keeps widths and order stable. P25 sets device density. |
| O28 | In-place expansion plus Right Now | P08 adds deduplicated Right Now. P21 confines changes to reserved content. |
| O29 | Environmental backgrounds | P2.1 uses synthetic environmental gradients. P26–P29 govern surfaces. |
| O30 | Eleven permanent destinations | P2.1 has eleven internal destinations. C1 verifies stable HA routes. |
| O31 | Device-adaptive navigation | P2.1 shows mobile dock and sidebar. #6 verifies real touch, keyboard and overlap. |
| O32 | Contextual greeting with concierge on tap | P2.1 shows deterministic sample summaries. C2 verifies provenance and qualified inferences. |
| O33 | Parallel prototype, then a permanent Lab | G0 gates all live writes. #6 gates the Lab candidate. R1 gates promotion. |

## P2.1 decisions

| ID | Approved choice | Evidence or release gate |
|---|---|---|
| P01 | D: Context-aware warnings | Fixture warnings are exercised by Chromium. C1/C2 validate live quality. |
| P02 | D: Context-aware expansion | Fixed slot rules are binding. Real interaction and focus stability still need #6. |
| P03 | D: Adaptive hybrid accents | Fixture accents and warning text. Confirm contrast and perception at #6. |
| P04 | D: Detail panel with full view link | Fixture dialog and route links. Chromium covers Escape and focus return. |
| P05 | D: Intelligent architectural room cards | Fixture room cards and unavailable landing temperature. C1 supplies live bindings. |
| P06 | D: Adaptive atmosphere | Fixture environmental gradients. #6 measures transitions and user settings. |
| P07 | D: Contextually intelligent concierge | Fixture deterministic briefing. C2 verifies factual inputs and evidence. |
| P08 | D: Affected widgets + concise Right Now | Fixture Right Now and affected widgets. C2 verifies real event identity and ranking. |
| P09 | D: Predictive hybrid focus | Fixture rule-based focus. L1/L2 gate learning and adaptation. |
| P10 | D: Intelligent defaults + granular control + pause | Fixture session preferences partly demonstrate pause. C1 verifies preference lifecycle. |
| P11 | D: Shared preferences with device-specific overrides | Fixture responsive profiles. C1 gates shared authenticated storage and per-device overrides. |
| P12 | D: Layered transparency | Fixture explanations and synthetic ages. C2 verifies live source evidence. |
| P13 | D: Interaction lock | Fixture dialogs have no live updates. C1/C2 verify interaction lock on changing inputs. |
| P14 | D: Context-aware escalation | Fixture alert priorities. H1 validates escalation. Safety delivery remains independent. |
| P15 | A+B+C: Informative, advisory and predictive energy | E1 and C2 reconcile price, consumption, estimate uncertainty and advice. No autonomous energy actions. |
| P16 | D: Interactive learning | Fixture review/correct/dismiss. L1 gates actual scope, data and review. L2 gates adaptation. |
| P17 | D: Privacy-first guest awareness | Fixture uncertainty. C2 verifies manual and inferred states. No security action based on uncertainty. |
| P18 | D: Context-aware override | C3 verifies domain-specific approvals, safe exclusions and override lifecycle. |
| P19 | D: Self-monitoring home | H1 verifies diagnostics and deduplicated escalation. Repair requires approval. |
| P20 | D: Analytical workspace | C2/E1/L1 validate datasets and evidence. Fixture routes provide placeholders. |
| P21 | A: Consistent interface | Governs P02/P03/P06/P09 and O04/O25/O27/O28. Keep stable anchors and accent semantics. |
| P22 | C: Apple-inspired fluidity | Fixture CSS demonstrates eased transitions. #6 measures real motion and reduced motion. |
| P23 | D: Architectural hybrid | Refines O06. Verify natural surfaces and accessibility on Apple devices at #6. |
| P24 | D: Refined hybrid typography | Fixture uses system fonts and local styling. No remote font dependency. |
| P25 | D: Device-adaptive density | Fixture adaptive widths. #6 verifies real Apple devices and reading order. |
| P26 | B: Natural cottage | Refines O03/O29. Fixture uses natural cottage colours. |
| P27 | A: Colour only | Fixture uses gradients and colour without texture assets. |
| P28 | A: Limestone & sage | Approved light tokens in v2.1. Verify exact rendered tokens and contrast at #6. |
| P29 | A: Midnight sage | Approved dark tokens in v2.1. Verify exact rendered tokens and contrast at #6. |
| P30 | D: State-aware icons | Fixture labels and status accents. Full state-aware icon treatment needs review. |
| P31 | D: Intelligent lighting | C1 verifies scene and light reads. C3 gates brightness and actions. L1 governs advice. |
| P32 | D: Intelligent climate | C1 validates readings, C2 gates evidence-based predictions and C3 gates commands. |
| P33 | D: Context-aware security | Fixture shows incomplete status. C1 verifies reads and camera-on-demand only after approval. Security actions require their own approval. |
