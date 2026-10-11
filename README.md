# OpenFOAM Benchmark Meshes

A collection of public OpenFOAM meshes prepared for solver benchmarking,
performance analysis, and reproducible testing.

The repository itself contains only metadata and documentation. The mesh
archives are distributed through GitHub Releases.

Current dataset release:

- `dataset-v2`

## Mesh dataset

| Mesh | Cells / Faces, M | Archive, MB | License |
|---|---:|---:|---|
| motorBike | 0.35 / 1.05 | 19.25 | GPL-3.0-or-later |
| AHBody | 2.85 / 8.59 | 111.53 | Pending confirmation |
| AHBody RN | 2.85 / 8.59 | 112.16 | Pending confirmation |
| ConicalDiffuser | 3.10 / 9.26 | 115.12 | CC BY-SA 4.0 |
| ConicalDiffuser RN | 3.10 / 9.26 | 117.50 | CC BY-SA 4.0 |
| Cavity3d | 8.00 / 23.88 | 250.99 | CC BY-SA 4.0 |
| Cavity3d RN | 8.00 / 23.88 | 258.06 | CC BY-SA 4.0 |
| MTBHPC | 8.61 / 25.95 | 465.92 | GPL-3.0-or-later |
| MTBHPC RN | 8.61 / 25.95 | 472.16 | GPL-3.0-or-later |
| WD_DamBreak | 9.38 / 27.98 | 330.31 | Redistribution permitted by author |
| WD_DamBreak RN | 9.38 / 27.98 | 336.87 | Redistribution permitted by author |

**Notes:**
- **RN** = renumbered mesh.
- **M** = million cells / internal faces.
- **MB** = decimal megabytes (10⁶ bytes).

Exact file sizes, SHA-256 checksums, and additional topology statistics are
recorded in `mesh_catalog.json`.

## Mesh ordering locality summary

The table summarizes adjacency locality in each mesh's original/natural cell
numbering, before IH1 permutation. `Mean Δ/N` and `P99 Δ/N` are the mean and
99th-percentile absolute index distance between adjacent cells, normalized by
the number of cells. `same64B/4KiB/2MiB` is the fraction of adjacent endpoint
pairs whose cell indices fall in the same index span corresponding to that
size (assuming 8-byte scalar values). These are index-based locality proxies,
not measured hardware cache-hit rates or a prediction of physical `psi`
locality after a permutation. Roughness uses the benchmark analysis definition.

| Mesh | Cells / Faces, M | Mean Δ/N | P99 Δ/N | Locality 64B / 4K / 2M, % | R |
|---|---:|---:|---:|---:|---:|
| motorBike | 0.35 / 1.05 | 0.08676 | 0.80476 | 21.8 / 53.2 / 92.3 | 0.3117 |
| AHBody | 2.85 / 8.59 | 0.03785 | 0.34483 | 21.2 / 62.7 / 79.5 | 0.1454 |
| AHBody RN | 2.85 / 8.59 | 0.00528 | 0.01602 | 26.1 / 53.0 / 94.8 | 0.0251 |
| ConicalDiffuser | 3.10 / 9.26 | 0.00235 | 0.07308 | 28.3 / 64.0 / 98.4 | 0.0139 |
| ConicalDiffuser RN | 3.10 / 9.26 | 0.00262 | 0.00256 | 0.0 / 0.2 / 97.4 | 0.0070 |
| Cavity3d | 8.00 / 23.88 | 0.00183 | 0.00286 | 29.2 / 53.8 / 97.2 | 0.0098 |
| Cavity3d RN | 8.00 / 23.88 | 0.00234 | 0.00233 | 0.0 / 0.1 / 94.8 | 0.0067 |
| MTBHPC | 8.61 / 25.95 | 0.04199 | 0.39640 | 21.1 / 49.5 / 65.6 | 0.1566 |
| MTBHPC RN | 8.61 / 25.95 | 0.00497 | 0.01407 | 20.9 / 40.2 / 85.3 | 0.0178 |
| WD_DamBreak | 9.38 / 27.98 | 0.00168 | 0.00363 | 29.2 / 51.7 / 95.8 | 0.0095 |
| WD_DamBreak RN | 9.38 / 27.98 | 0.00171 | 0.00214 | 0.0 / 0.1 / 94.3 | 0.0039 |

Renumbering generally reduces roughness and long index-distance tails, but
does not improve every locality proxy: for some renumbered meshes, same64B and
same4KiB fractions are much lower. The metrics should therefore be interpreted
together, not as a single locality score. Full methodology and per-ordering
results are maintained in the WavefrontGaussSeidel mesh-ordering analysis.

## Mesh provenance

### MTB_example

`MTB_example` is based on the standard OpenFOAM `motorBike` tutorial mesh.

Upstream:

- [OpenFOAM `motorBike` tutorial](https://develop.openfoam.com/Development/openfoam/-/tree/master/tutorials/incompressibleFluid/motorBike)

The archive contains the generated OpenFOAM `polyMesh` used by the benchmark.

No renumbered variant is currently included for this mesh because of its
relatively small size.

### MTBHPC_small

`MTBHPC_small` is based on the OpenFOAM HPC Motorbike benchmark, size S.

The HPC Motorbike benchmark was derived from the standard OpenFOAM `motorBike`
tutorial. Its background mesh is refined by a factor of three in each
direction while retaining the original `snappyHexMesh` setup. The size-S case
contains approximately 8.6 million cells, matching the mesh distributed here.

Upstream/reference:

- [OpenFOAM HPC Motorbike benchmark](https://develop.openfoam.com/committees/hpc/-/wikis/HPC-motorbike)

Published mesh size:

- 8,613,999 cells
- 25,952,973 internal faces

Two variants are provided:

- `MTBHPC_small.tgz` — original numbering
- `MTBHPC_small_renumbered.tgz` — OpenFOAM-renumbered version

### AHBody

`AHBody` is an Ahmed-body OpenFOAM mesh used as a medium-sized benchmark case.

Upstream source:

- [Ahmed Bluff Body CFD](https://github.com/nathanrooy/ahmed-bluff-body-cfd)

Published mesh size:

- 2,845,652 cells
- 8,592,613 internal faces

Two variants are provided:

- `AHBody_mesh.tgz` — original numbering
- `AHBody_mesh_renumbered.tgz` — OpenFOAM-renumbered version

### Cavity3d

Cavity3d is sourced from the exaFOAM benchmark collection, listed there as
“MB1 – Cavity 3D” (solver: `icoFoam`, incompressible laminar flow).

Source:

- [exaFOAM Benchmarks](https://exafoam.eu/benchmarks/)

Two mesh archives are included:

- `Cavity3d_mesh.tgz` — original numbering
- `Cavity3d_mesh_renumbered.tgz` — renumbered version

The source mesh is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

### ConicalDiffuser

ConicalDiffuser is sourced from the exaFOAM benchmark collection, which lists
ERCOFTAC conical-diffuser benchmarks.

Source:

- [exaFOAM Benchmarks](https://exafoam.eu/benchmarks/)

Two mesh archives are included:

- `ConicalDiffuser_mesh.tgz` — original numbering
- `ConicalDiffuser_mesh_renumbered.tgz` — renumbered version

The source mesh is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

### WD_DamBreak

`WD_DamBreak` is a large dam-break OpenFOAM mesh used as a benchmark case.

It is not the small standard OpenFOAM `damBreak` tutorial mesh. The mesh
distributed here contains more than 9 million cells and comes from the
public Wolf Dynamics validation case.

Upstream source:

- [Wolf Dynamics 3D dam-break case](https://www.wolfdynamics.com/validations/3d_db/case0.tar.gz)

Published mesh size:

- 9,376,387 cells
- 27,975,312 internal faces

Two variants are provided:

- `WD_DamBreak_mesh.tgz` — original numbering
- `WD_DamBreak_mesh_renumbered.tgz` — OpenFOAM-renumbered version

**Redistribution permission:** Granted by Joel Guerrero
(Wolf Dynamics) via email on 2026-10-11.

Permission covers the publication of both original and
renumbered polyMesh archives in this benchmark repository.

## Preparation

The benchmark archives contain OpenFOAM mesh data rather than complete
simulation cases.

Solver fields, time directories, logs, post-processing output, and other
case-specific data are not included unless required to represent the mesh.

The original mesh topology is preserved when creating the benchmark archives.

### Renumbered variants

Files with the `_renumbered` suffix were produced from the corresponding
original mesh using the standard OpenFOAM command:

    renumberMesh -overwrite

The intention is to provide both:

- the original mesh numbering;
- the numbering produced by the standard OpenFOAM `renumberMesh` procedure.

Renumbering changes cell and face ordering but does not change the mesh
topology.

For every original/renumbered pair currently cataloged, the following invariants
were verified to be identical:

- number of cells;
- number of internal faces;
- total number of faces;
- number of points.

No topology-count discrepancies were found.

## Metadata generation

Each archive was unpacked into a temporary directory and read using the
`PolyMeshReader` used by the benchmark infrastructure.

The catalog records:

- archive filename;
- variant;
- exact archive size;
- SHA-256 digest;
- number of cells;
- number of internal faces;
- total number of faces;
- number of points.

The archive contents were not modified while collecting metadata.

## Reproducibility

Published release assets should be treated as immutable benchmark inputs.

If the contents of a mesh archive change, a new dataset release should be
created rather than replacing an existing asset under the same release tag.

For example:

    dataset-v1
    dataset-v2

This allows benchmark results to refer to an exact dataset version together
with the SHA-256 digest of each mesh archive.

## Usage

Mesh archives are available from the GitHub Releases section of this
repository.

Projects using this dataset should cache downloaded archives locally and verify
their SHA-256 digests against `mesh_catalog.json`.

The `WavefrontGaussSeidel` / `SmootherTest` benchmark infrastructure uses
these meshes as external benchmark inputs and downloads them on demand.

## License

The mesh datasets are subject to their respective upstream licenses, as indicated in the mesh table above.

Original scripts, tools, metadata, and documentation created specifically for this repository are licensed under the [MIT License](LICENSE).

This license does not apply to third-party mesh datasets or other upstream materials.
