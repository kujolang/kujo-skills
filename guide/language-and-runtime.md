# Language And Runtime Reference

## Sources

- `docs/LANGUAGE_SPEC.md`
- `README.md`
- `docs/VM_INTERPRETER_PARITY_MATRIX.md`
- `docs/VM_INTERPRETER_MIGRATION_PLAYBOOK.md`
- `examples/README_examples.md`
- `tests/vm_interpreter_parity_surfaces.rs`

## Baseline

Kujo source files use `.kujo`, UTF-8, and current syntax from `docs/LANGUAGE_SPEC.md`. CLI parse entrypoints reject source files larger than `1,048,576` bytes with parser diagnostics.

## Bindings

- `let name := value`: immutable binding; reassignment and in-place mutation through the binding are rejected.
- `mut name := value`: mutable binding; reassignment and in-place mutation are allowed.
- `const name := value`: constant binding; reassignment and in-place mutation are rejected.
- `name := value`: assignment form; updates existing mutable binding when present, otherwise creates a mutable binding in current scope.
- `=` also appears in legacy examples/tests, but new idiomatic code should follow the spec's binding forms unless preserving existing fixture style.

## Control Flow And Data

Supported surfaces include functions, async functions, conditionals, `while`, `loop`, `for ... in`, `match`, `try`/`except`, `throw`, arrays, dictionaries, structs, tests, spread literals, and imports.

Truthiness:

- Falsey: `false`, `null`, `0`, `0.0`, `""`, `[]`, `{}`.
- Truthy: everything else, including `"false"`.
- `&&` and `||` short-circuit and return booleans.

Runtime errors:

- Unknown identifiers: `Undefined variable: <name>`.
- Missing dictionary keys: runtime error; use `has_key`, `get`, `get_default`.
- Array/string out of bounds: `Index out of bounds: <index>`.
- Integer overflow, division by zero, and modulo by zero are runtime errors.

## Imports

Kujo supports:

```kujo
import math_helpers
from metrics import average, total
from src.util import value
from src.core.math import add
```

Module names must not contain traversal or absolute/drive-prefixed paths. Import cycles are rejected with deterministic diagnostics.

## Runtime Commands

- `kujo run <file>`: VM default.
- `kujo run --interpreter <file>`: explicit fallback/debug path.
- `kujo test --runtime dual`: VM-primary with bounded interpreter fallback for fixture compatibility.
- `kujo test --runtime vm`: strict VM-only validation.
- `kujo test-run <file>`: interpreter-hosted test declaration runner today.

Do not recommend interpreter mode for ordinary dotted/flat module imports.

