# OpenFOAM Benchmark Meshes

A collection of public OpenFOAM meshes prepared for solver benchmarking,
performance analysis, and reproducible testing.

The repository itself contains only metadata and documentation. The mesh
archives are distributed through GitHub Releases.

Current dataset release:

- `dataset-v1`

## Mesh dataset

| Mesh | Variant | Cells | Internal faces | Archive size |
|---|---|---:|---:|---:|
| AHBody | original | 2,845,652 | 8,592,613 | 111,531,462 B |
| AHBody | renumbered | 2,845,652 | 8,592,613 | 112,158,065 B |
| MTBHPC_small | original | 8,613,999 | 25,952,973 | 465,922,322 B |
| MTBHPC_small | renumbered | 8,613,999 | 25,952,973 | 472,156,064 B |
| MTB_example | original | 352,253 | 1,053,964 | 19,252,028 B |
| WD_DamBreak | original | 9,376,387 | 27,975,312 | 330,305,556 B |
| WD_DamBreak | renumbered | 9,376,387 | 27,975,312 | 336,870,809 B |

Exact file sizes, SHA-256 checksums, and additional topology statistics are
recorded in `mesh_catalog.json`.

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

For every original/renumbered pair in `dataset-v1`, the following invariants
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