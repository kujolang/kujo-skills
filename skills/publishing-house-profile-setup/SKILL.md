---
name: publishing-house-profile-setup
description: "Use when onboarding or validating a portable Kujo Publishing House: House, Brand, and Audience profiles; owner and approval roles; mission, quality and risk posture; portfolio constraints; voice and terminology; audiences, channels, accessibility; destinations, adapter references, permission defaults, validity dates, or escalation contacts."
---

# Publishing House Profile Setup

Create portable profiles that inject organizational context without embedding credentials or owner-specific assumptions.

## Workflow

1. Read `../kujo-agents/publishing-house/00-publishing-house.md`, `00-quality-standard.md`, `00-shared-contracts.md`, and `00-permission-model.md`.
2. Create a House Profile with mission, principles, portfolio constraints, risk posture, default permission, owner/approval roles, destinations, escalation contacts, and review date.
3. Create a Brand Profile with position, audience promise, category frame, proof, voice principles, distinctive assets, terminology, prohibited shortcuts, examples, validity dates, and owner approval.
4. Create an Audience Profile with identity, context, needs, tensions, prior knowledge, desired movement, channels, accessibility needs, evidence sources, assumptions, and review date.
5. Reference adapter and credential environment-variable names; never store secret values. Record unavailable capabilities honestly.
6. Validate stable IDs, versions, dates, provenance, ownership, permission ceilings, and contradictions before a workflow consumes the profiles.

Profiles provide context and capability references. They do not grant ACT authority, human approval, rights, consent, or provider access. Preserve the distinction between owner-approved facts and agent inference.
