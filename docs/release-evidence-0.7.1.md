# Skills 0.7.1 release evidence

The portable release-readiness and clean temporary-profile installation gates
passed on Node 26.12.1. These validate all 135 skills, routing fixtures, local
links, imported executable/assets integrity, and video compiler/motion contracts.
No live agent profile was modified.

## Workcell host blocker

The current release definition is `docs/workcell-release-gate.json`; the old
`docs/workcell-launch-gate.json` remains historical 0.1.0 evidence.

Command: `workcell run --file docs/workcell-release-gate.json --repo . --no-pull --summary`.
Run: `wc-953d8afb7fc44133b60bfcba17a72ebd`. The current rootful Docker host
does not report AppArmor, so Workcell refused execution before starting a
container. Cleanup completed. The documented Colima `kujo-workcell` socket is
not running. This is a blocker receipt, not successful container proof.

The closest passing proof is the complete portable gate and isolated temporary
profile installation above. After a policy-compatible Docker host is available,
rerun the command against the tagged source and verify its receipt with
`workcell verify --run .workcell/runs/<run-id> --json`. Do not disable AppArmor
or weaken the Workcell policy to produce a passing receipt.

The original receipt and test logs are retained outside Git in the release
operator's `final-ten-releases-20261022` report directory. This release preserves
the technical-preview scope and makes no new container-isolation claim.
