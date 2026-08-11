## [0.4.5-alpha] - 2026-08-10

### Added
- Implemented real sandboxed file operations in FilesystemService
  (list_files, read_text, write_text, read_bytes, write_bytes,
  delete_file, exists, file_info), scoped per module under
  module_data/<module_name>/.
- Added path-containment enforcement in FilesystemService so no
  filename or path traversal attempt (e.g. "../../etc/evil.txt")
  can escape a module's own data directory.
- Wired ServiceRegistry to accept and inject module_data_root into
  FilesystemService at registration time.
- Wired BrisartRuntime to pass SystemAPI.module_data_root into
  ServiceRegistry, so SystemAPI and FilesystemService share one root.
- Updated the Hello Lab module to demonstrate the "service:filesystem"
  permission and ModuleAPI.get_service("filesystem") usage end-to-end.

### Changed
- FilesystemService version bumped from 0.1.0 to 0.2.0.
- Hello Lab module version bumped from 0.1.0 to 0.2.0.

### Notes
- This is the first built-in service with real (non-stub) behavior;
  Archive, Settings, and Update services remain stubs.
- This update completes the loop opened in 0.4.3-alpha (permission-aware
  ModuleAPI) and 0.4.4-alpha (ServiceRegistry wiring) by giving modules
  an actual, permission-gated service to call.
- Verified functionally: boot, service listing, module execution, file
  read/write through both module_data and the filesystem service,
  sandbox-escape rejection, and permission enforcement (PermissionError
  and ServiceUnavailableError) all tested and passing.

## [0.4.4-alpha] - 2026-08-10

### Added
- Added ServiceRegistry wiring through ModuleLoader into ModuleAPI.
- Added ModuleAPI.get_service(name), gated by "service:<name>" permission.
- Added ServiceRegistry.get_service_object() and has_service() accessors.
### Changed
- Modules can now request live service instances instead of only SystemAPI primitives.
### Notes
- Built-in services remain stubs; real service logic is the next step.

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