## [0.4.1-alpha] - 2026-08-07

### Changed
- Centralized the BrisartOS version into a single source of truth (`brisartos/version.py`).
- `runtime.py` now imports NAME and VERSION from `version.py` instead of hardcoding.
- `build.py` boot banner now derives its version from `version.py`, fixing the stale `0.2.0-alpha` string (now `0.4.0-alpha`).

### Fixed
- Resolved version mismatch between the runtime (`0.4.0-alpha`) and the build boot banner (`0.2.0-alpha`).