# BrisartOS

**A pure-Python, dependency-free, fully custom operating system research project.**

BrisartOS is an experimental operating system research project focused on building a fully custom computing environment using Python as the primary development language.

The project emphasizes local-first operation, offline capability, auditability, modular architecture, long-term maintainability, and complete ownership of the software stack.

BrisartOS is not a Linux distribution, Windows derivative, macOS clone, desktop environment, or wrapper around an existing operating system.

The long-term goal is to develop a fully custom operating environment designed for research, preservation, archive management, identity infrastructure, air-gapped deployments, and long-term digital stewardship.

---

# Philosophy

BrisartOS follows several core principles:

- Pure Python development
- No external dependencies
- Local-first architecture
- Offline-first operation
- Air-gapped environment compatibility
- Long-term maintainability
- Source transparency
- Full stack ownership
- Modular design
- Future-oriented architecture

The project prioritizes understanding and control over complexity and abstraction.

---

# Current Status

**Version:** 0.4.0-alpha

BrisartOS currently includes:

- Boot image generation research
- Binary image tooling
- Experimental boot infrastructure
- Runtime architecture
- Modular shell environment
- Service framework
- System API framework
- Built-in application structure
- Pure-Python module loading
- 128-bit internal object identifiers
- Dependency-free development model

The project remains in an active research and experimentation stage.

---

# Architecture

BrisartOS is organized into multiple layers.

## Boot Layer

Responsible for:

- Boot image generation
- Image inspection
- Startup experimentation
- Bare-metal research

---

## Runtime Layer

Responsible for:

- Runtime initialization
- Module loading
- Internal coordination
- System API management

---

## Service Layer

Responsible for:

- Archive services
- Identity services
- Filesystem services
- Settings services
- Update services

Services provide stable interfaces for applications and modules without requiring modifications to operating system internals.

---

## Application Layer

Built-in BrisartOS applications live here.

Examples include:

- Browser
- Archive tools
- Settings tools
- Future research utilities

Applications are considered part of the operating environment itself.

---

## Module Layer

Modules allow laboratories, archivists, researchers, and users to extend BrisartOS without modifying the operating system core.

Example:

```text
modules/
└── hello_lab/
    └── module.py
```

Modules are pure Python and communicate through the BrisartOS system APIs.

---

# Object Model

BrisartOS uses 128-bit internal identifiers.

These identifiers can be used for:

- Archive records
- Research datasets
- Services
- Modules
- Identity records
- Long-term digital references

Example:

```text
2dff55f9dad6a6fa8c88a67f57db8ae8
```

This object model is intended to provide durable identifiers for future operating system and research platform development.

---

# Repository Structure

```text
BrisartOS/

README.md

build/

docs/
├── ARCHITECTURE.md
├── ROADMAP.md
├── DEPENDENCY_POLICY.md
└── SAFETY.md

modules/

brisartos/
├── apps/
├── boot/
├── runtime/
├── services/
├── shell/
├── build.py
├── emitter.py
├── labels.py
└── platform.py
```

---

# Development Principles

## Pure Python

BrisartOS is authored using Python.

Python is used for:

- Runtime development
- Module development
- Operating system tooling
- Binary image generation
- Services
- Applications

Python standard library components are preferred whenever practical.

---

## No Dependencies

BrisartOS follows a strict dependency-free policy.

The project should not require:

- Third-party Python packages
- External frameworks
- Cloud infrastructure
- Online services
- Package managers

The Python standard library is preferred whenever possible.

---

## Fully Custom

BrisartOS is intended to be custom-built rather than layered on top of existing software ecosystems.

The project favors understanding how systems work internally rather than relying on hidden abstractions.

---

# Intended Environments

BrisartOS is being researched for environments such as:

- Research laboratories
- Digital preservation projects
- Archive environments
- Offline workstations
- Air-gapped systems
- Identity infrastructure
- Long-term knowledge repositories
- Preservation-focused computing environments

---

# Roadmap

## Short-Term Goals

- Expand runtime functionality
- Expand service architecture
- Improve module APIs
- Improve shell capabilities
- Build archive service infrastructure
- Build identity service infrastructure

## Mid-Term Goals

- Runtime initialization research
- Filesystem experimentation
- Settings management
- Update infrastructure
- Research application framework
- Modular workflow development

## Long-Term Goals

- Hardware-installable operating system
- Research-focused runtime environment
- Preservation tooling integration
- Identity management integration
- Offline documentation infrastructure
- Archive management capabilities
- Air-gapped workstation profile
- Long-term software stewardship platform

---

# Experimental Notice

BrisartOS is an experimental research project.

Boot artifacts, runtimes, modules, services, applications, and operating system components should not be considered production-ready.

All development should be treated as research and experimentation.

---

# Vision

The long-term vision of BrisartOS is to create a fully custom, local-first, dependency-free operating environment designed for research, digital preservation, identity infrastructure, archive management, and long-term ownership of information.

BrisartOS aims to provide:

- A fully custom runtime environment
- Modular research tooling
- Offline-first operation
- Air-gapped deployment capability
- Long-term maintainability
- Full source transparency
- Complete control over the software stack

---

# BrisartOS

*Pure Python. No Dependencies. Fully Custom. Modular by Design.*