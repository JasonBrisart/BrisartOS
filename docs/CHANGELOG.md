## [0.4.3-alpha] - 2026-08-10

### Added
- Added permission-aware module API wrapper.
- Added runtime enforcement for module permissions.
- Added explicit `object_id` permission for modules that generate BrisartOS object identifiers.
- Added module permission display to module inspection output.

### Changed
- Modules now receive a permissioned API wrapper instead of the unrestricted core SystemAPI object.
- The Hello Lab module now declares its object identifier permission explicitly.

### Notes
- This update turns module metadata into an enforceable runtime contract.
- This keeps BrisartOS dependency-free and standard-library-only.
- This advances the module API and shell inspection roadmap.

## [0.4.2-alpha] - 2026-08-10

### Added
- Added a BrisartOS service registry for built-in operating environment services.
- Added runtime registration for archive, filesystem, settings, and update services.
- Added `services` shell command to list registered services and their current status.
- Added `service <name>` shell command to inspect an individual service.
- Added a dedicated `ServiceRecord` wrapper for service metadata and status reporting.

### Changed
- Runtime boot now initializes the service layer before module discovery.
- Shell help output now includes service inspection commands.

### Notes
- This update keeps BrisartOS dependency-free and standard-library-only.
- Existing service classes remain simple and unchanged.
- This update advances the short-term roadmap goal of wiring the service framework into the runtime.

## [0.4.1-alpha] - 2026-08-07

### Changed
- Centralized the BrisartOS version into a single source of truth (`brisartos/version.py`).
- `runtime.py` now imports NAME and VERSION from `version.py` instead of hardcoding.
- `build.py` boot banner now derives its version from `version.py`, fixing the stale `0.2.0-alpha` string (now `0.4.0-alpha`).

### Fixed
- Resolved version mismatch between the runtime (`0.4.0-alpha`) and the build boot banner (`0.2.0-alpha`).