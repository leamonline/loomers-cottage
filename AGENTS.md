# Engineering rules
Home Assistant is the canonical controller; Apple Home remains a supported everyday interface. Prefer native/local integrations. No essential operation may depend on AI or a custom dashboard.
1. Read live configuration, actual entity IDs, dependencies and current hashes before proposing a change.
2. Record exact diff, impact, acceptance criteria, backup and rollback; obtain owner approval before persistent HA changes. Separate approval for security, access, EV actuation and safety-sensitive changes. Never autonomously unlock, expose services or disable protections.
3. Use synthetic fixtures in Lab; no actuator bindings until explicitly approved. Unknown, stale and unavailable are distinct; never infer secure from missing data.
4. Use small reviewable changes, test locally, verify on Apple devices and HA Green, read back changed objects, record results and stop on mismatch.
5. Keep native fallback and prior releases. Never delete existing entities or configuration without separate permission. Do not publish secrets or home identifiers.
6. Release gates: G0 recovery before live writes; F1/F2 foundation; P2.1 Lab only; C1 read mirror; C2 contextual/validated data; C3 allowlisted controls and overrides; E1 energy; H1 diagnostics; L1 advisory learning; R1 seven-day parallel trial and approval; L2 bounded adaptation separately approved.
