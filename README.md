# graph-control

`graph-control` is an open-source research initiative designed to extract unified abstraction patterns across complex network control problems by bridging aerospace guidance/navigation/control (GNC), urban systems, and network theory.

## Development Approach: Prototype-Driven Framework Design
Rather than designing abstract interfaces top-down, `graph-control` is built by implementing concrete simulation testbeds across distinct domain problems to identify shared math, state representation, and graph-coupling dynamics:

* **`prototypes/drone_swarm/`** *(Active)*: Multi-agent spatial coordination using double-integrator dynamics, regularized friction, and NetworkX geometric graph topologies.
* **`prototypes/epidemic_metapopulation/`** *(Planned)*: Spatial SIR/SEIR dynamics coupled via transport network matrices.
* **`prototypes/infrastructure_flow/`** *(Planned)*: Cascading capacity and failure propagation on Directed Acyclic Graphs (DAGs).

The core engine (`graph-control/`) is being implemented by extracting common state-space compilation, integration, and graph-coupling logic across these case studies.