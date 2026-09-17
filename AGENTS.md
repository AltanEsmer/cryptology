# Repository Guidelines

## Project Structure & Module Organization

This repository contains cryptology coursework, reusable Python algorithms, and worked mathematical exercises.

- `crypto_library/`: reusable implementations; `number_theory.py` contains Euclid’s GCD algorithm.
- `run_gcd.py`: command-line entry point using `argparse`.
- `tests/`: algorithm unit tests and subprocess-based CLI tests.
- `exercises/`: worked solutions, named `weekNN-solutions.md` or `exercise-N.N.md`.
- `docs/`: study plans and verification notes, such as `week01-plan.md`.

Keep algorithm logic in the library and argument parsing in the CLI. Local course PDFs are not required to run the project.

## Build, Test, and Development Commands

Use Python 3.9 or newer and run commands from the repository root. No installation, build step, or third-party dependencies are required.

```bash
python3 run_gcd.py 48 18                         # Prints 6
python3 run_gcd.py --help                        # Shows CLI usage
python3 -m unittest discover -s tests -v          # Runs all tests
python3 -m unittest discover -s tests -p 'test_number_theory.py' -v
```

The final command runs only algorithm tests.

## Coding Style & Naming Conventions

Follow the existing Python style: four-space indentation, `snake_case` functions and modules, `PascalCase` test classes, and uppercase constants. Use type annotations for public functions and concise docstrings describing their contract. Prefer the standard library and small, direct implementations. No formatter or linter is currently configured.

## Testing Guidelines

Use standard-library `unittest`, with files named `test_*.py` and methods named `test_*`. Cover ordinary inputs, zeros, negative values, and large integers where relevant. Compare mathematical results with a trusted oracle, such as `math.gcd`. CLI tests should check exit status and output. No numerical coverage threshold is configured; add regression coverage for changed behavior and run the full suite before handoff.

## Commit & Pull Request Guidelines

History uses scoped Conventional Commits, including `feat(number-theory):` and `docs(exercises):`. Use imperative messages and keep each commit focused on one behavior or documentation change. For behavior changes, expose the contract with tests before implementation.

PRs should explain the change and risk, link applicable issues or ADRs, and list verification commands and results. Include screenshots for relevant UI changes and identify any security, privacy, schema, or deployment impacts.

## Public Repository Scope

Do not commit textbooks, lecture PDFs, private notes, credentials, or local execution logs. Respect `.gitignore`. Cite exercise sources precisely and flag unverified edition or numbering assumptions.

## Local Course Resources

The source folder on this MacBook is `/Users/altanesmer/Desktop/SM1/CYR`. Consult it for course resources, lectures, and exercises.
