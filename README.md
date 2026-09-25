# OpenFOAM Benchmark Meshes

A collection of public OpenFOAM meshes prepared for benchmarking, performance analysis, and reproducible testing.

Large mesh archives are distributed through GitHub Releases. The repository itself contains only documentation and metadata.

Current dataset release:

- `dataset-v1`

## Dataset

| Mesh | Variant | Cells | Internal faces | Archive size |
|---|---|---:|---:|---:|
| AHBody | original | 2,845,652 | 8,592,613 | 111,531,462 B |
| AHBody | renumbered | 2,845,652 | 8,592,613 | 112,158,065 B |
| MTBHPC_small | original | 8,613,999 | 25,952,973 | 465,922,322 B |
| MTBHPC_small | renumbered | 8,613,999 | 25,952,973 | 472,156,064 B |
| MTB_example | original | 352,253 | 1,053,964 | 19,252,028 B |
| WD_DamBreak | original | 9,376,387 | 27,975,312 | 330,305,556 B |
| WD_DamBreak | renumbered | 9,376,387 | 27,975,312 | 336,870,809 B |

Exact file sizes, SHA-256 digests, and additional topology statistics are recorded in `manifest.json`.

## Mesh provenance

### MTB_example

Based on the standard OpenFOAM `motorBike` tutorial mesh.

Source:
- OpenFOAM `motorBike` tutorial

Preparation:
- generated from the upstream tutorial case;
- only the mesh data required by the benchmark was retained;
- archived as `MTB_example_polyMesh.tgz`.

### MTBHPC_small

Based on the OpenFOAM HPC Motorbike benchmark, size S.

Source:
- OpenFOAM HPC Motorbike benchmark

Published mesh size:
- 8,613,999 cells
- 25,952,973 internal faces

Variants:
- `MTBHPC_small.tgz` — original numbering;
- `MTBHPC_small_renumbered.tgz` — mesh after OpenFOAM renumbering.

### AHBody

Ahmed-body OpenFOAM mesh used as a medium-sized benchmark workload.

Source:
- TODO: add exact upstream URL/project

Published mesh size:
- 2,845,652 cells
- 8,592,613 internal faces

Variants:
- `AHBody_mesh.tgz` — original numbering;
- `AHBody_mesh_renumbered.tgz` — mesh after OpenFOAM renumbering.

### WD_DamBreak

Large dam-break OpenFOAM mesh used as a benchmark workload.

Source:
- TODO: add exact upstream URL/project

Published mesh size:
- 9,376,387 cells
- 27,975,312 internal faces

Variants:
- `WD_DamBreak_mesh.tgz` — original numbering;
- `WD_DamBreak_mesh_renumbered.tgz` — mesh after OpenFOAM renumbering.

## Preparation

The archives contain OpenFOAM mesh data rather than complete simulation cases.

Solver fields, time directories, logs, post-processing output, and other case-specific data are not included unless required to represent the mesh.

### Renumbered variants

Files with the `_renumbered` suffix were produced from the corresponding original mesh using OpenFOAM mesh renumbering.

The goal is to provide both:

- the original/upstream numbering;
- the numbering produced by the standard OpenFOAM renumbering workflow.

Renumbering changes cell and face ordering but preserves mesh topology.

For every original/renumbered pair in `dataset-v1`, the following invariants were verified:

- cells;
- internal faces;
- total faces;
- points.

No topology-count discrepancies were found.

## Metadata generation

Each archive was unpacked into a temporary directory and read with the benchmark project's existing `PolyMeshReader`.

The recorded topology fields are:

- cells;
- internal faces;
- total faces;
- points.

Archive sizes were obtained from the local files and digests were computed with SHA-256.

No archive contents were modified while collecting metadata.

## Reproducibility

Published release assets should be treated as immutable benchmark inputs.

If the contents of a mesh archive change, publish a new dataset release rather than replacing an existing asset under the same release tag.

For example:

- `dataset-v1`
- `dataset-v2`

This allows benchmark results to refer to an exact dataset version together with the SHA-256 digest of each archive.

## Usage

Mesh archives are available from the GitHub Releases section of this repository.

Projects using this dataset should cache downloaded archives locally and verify their SHA-256 digests against the repository metadata.