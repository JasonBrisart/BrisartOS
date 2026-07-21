# BrisartOS

**A pure-Python, dependency-free, fully custom operating system research project.**

BrisartOS is an experimental hardware operating system being built from the ground up using Python as the primary development language.

The project focuses on local-first operation, auditability, long-term maintainability, offline capability, and complete control over the software stack.

BrisartOS is not a Linux distribution, Windows replacement, macOS clone, or wrapper around an existing operating system.

The goal is to create a fully custom operating system designed around research, preservation, identity management, offline operation, and long-term digital stewardship.

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

The project prioritizes understanding and control over complexity and abstraction.

---

# Current Status

**Version:** 0.2.0-alpha

BrisartOS currently contains:

- Python-generated boot images
- Custom binary image generation
- Dependency-free build process
- Image inspection tooling
- Experimental bare-metal boot infrastructure

The project remains in an early research stage.

---

# Project Goals

## Short Term

- Improve boot image generation
- Expand Python-based instruction emitters
- Create flexible binary layout tooling
- Improve image inspection and validation

## Mid Term

- Second-stage loader
- Runtime initialization
- Memory management experiments
- Shell research
- Local filesystem research

## Long Term

- Hardware-installable operating system
- Research-focused runtime environment
- Preservation tooling integration
- Identity management integration
- Offline documentation system
- Archive management capabilities
- Air-gapped research workstation profile

---

# Design Rules

## Pure Python

BrisartOS is intended to be authored using Python.

Python is used to generate the binary structures required for hardware startup and operating system functionality.

## No Dependencies

BrisartOS follows a strict dependency-free policy.

The project should not require:

- Third-party Python packages
- External frameworks
- Online services
- Package managers
- Cloud infrastructure

Python standard library modules are preferred whenever possible.

## Fully Custom

BrisartOS is intended to be custom-built rather than layered on top of existing operating systems.

The project prioritizes understanding how systems work internally rather than abstracting those details away.

---

# Example Build

```bash
python brisartos/build.py
```

Example output:

```text
===================================
 BrisartOS Build Complete
===================================
Output : build/brisartos_boot.img
Size   : 512 bytes
Message: BrisartOS 0.2.0-alpha
Signature: 55AA
```

---

# Repository Structure

```text
BrisartOS/

README.md
requirements.txt

brisartos/
├── build.py
├── emitter.py
├── labels.py
├── inspect_image.py

docs/
├── ARCHITECTURE.md
├── ROADMAP.md
├── DEPENDENCY_POLICY.md
└── SAFETY.md

build/
```

---

# Intended Environments

BrisartOS is being researched for environments such as:

- Research laboratories
- Digital preservation projects
- Archive environments
- Offline workstations
- Air-gapped systems
- Identity verification systems
- Long-term knowledge repositories

---

# Experimental Notice

BrisartOS is an experimental research project.

Generated boot images, runtimes, and operating system components should not be considered production-ready.

All development should be treated as research and experimentation.

---

# Vision

The long-term vision of BrisartOS is simple:

> Build a local-first, dependency-free, fully custom operating system designed for research environments, digital preservation, identity infrastructure, and long-term ownership of data.

---

**BrisartOS**

*Pure Python. No Dependencies. Fully Custom.*