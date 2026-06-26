# metapyp

`metapyp` is an open-source, general-purpose Python library designed for the rapid modeling, simulation, and control of complex **metapopulation networks**. 

By bridging the gap between aerospace guidance, navigation, and control (GNC) architectures and network theory, `metapyp` treats complex urban, ecological, and multi-agent systems as engineered machines. 
It decouples network topology from local dynamics, allowing users to plug in arbitrary governing differential equations and evaluate centralized or distributed control laws.

---

## Core Features

* **Flexible Graph Ingestion:** Generate idealized topologies (e.g., Watts-Strogatz Small-World) or stream real-world spatial infrastructure directly from OpenStreetMap (`osmnx`) and GraphML files.
* **Context-Agnostic Dynamics:** A plug-and-play physics engine that maps arbitrary, user-defined node attributes directly into fast NumPy state matrices.
* **GNC-Style Control Loop:** Built around a classic closed-loop feedback structure: Reference Signal -> Controller -> Plant -> Observer.
* **High Performance:** Core network coupling and transport calculations are vectorized using matrix-based graph Laplacian operations.

---

## Project Architecture

The library separates the simulation into modular components, mirroring a standard control system layout:

```text
metapyp/
├── .github/workflows/    # Continuous Integration (Automated testing via GitHub Actions)
├── metapyp/              # Core source package
│   ├── __init__.py
│   ├── generators.py     # Graph Factory (Procedural, files, OSM)
│   ├── dynamics.py       # Plant/Physics Engine & state compiler
│   ├── controllers.py    # Global and distributed control policies
│   └── models.py         # Plug-and-play equations (SIR, Diffusion, etc.)
└── tests/                # Unit test suite (via pytest)