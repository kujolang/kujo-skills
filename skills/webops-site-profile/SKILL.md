---
name: webops-site-profile
description: "Use when configuring or validating a portable WebOps site profile, repository binding, integration references, permission default, or site identity."
---

# Webops Site Profile

## Purpose

Use this skill for configuring or validating a portable WebOps site profile, repository binding, integration references, permission default, or site identity. Its primary sources are WebOps profile schema and Agency Runner site profiles.

## Workflow

1. Resolve the profile and schema without following symlinks outside its root.
2. Validate site ID, HTTP(S) URL, optional repository, platform, capabilities, integrations, and default permission.
3. Reference credential environment variables; never embed values.
4. Emit a normalized profile or exact validation errors.

## Required Output

- validated profile.
- capability declarations.
- credential references.
- permission default.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

A site profile grants no capability or ACT authority by itself. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
