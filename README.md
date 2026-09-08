# Residual Verification Cards (RVC)

Public reproducibility artifact accompanying the manuscript:

**Residual Verification Cards: A Fail-Closed Audit Contract with Bounded Cross-Object Conformance Tests for Neural PDE Outputs**

## Purpose

Residual Verification Cards (RVC) provide an executable, machine-readable claim-admissibility contract for neural-PDE audit records. The artifact checks artifact identity, prediction dependency, numerical operator, evaluation support, comparison object, aggregation, provenance, and requested claim level before releasing a diagnostic.

This repository is a reproducibility and conformance artifact. It is not a solver, leaderboard, universal validation method, deployment certificate, or residual-to-solution guarantee.

## Residual181 verification status

- Baseline unit tests: **36/36 PASS**.
- Cross-object extension unit tests: **49/49 PASS**.
- Fresh H05-H10 external-source rejection challenge: **6/6 overall-state agreement** and **6/6 semantic-route completion**.
- Positive external controls: **PC01 and PC06** are claim-scoped admissions.

These results do **not** establish universal external validity, independent third-party validation, population sensitivity/specificity, exact checkpoint-training lineage for PC01/PC06, deployment readiness, certification, model superiority, or a residual-to-solution guarantee.

## Public code/configuration artifact

The complete author-created public code/configuration payload is stored under:

`archives/code_config/`

The authoritative reconstruction path is the fail-closed verifier:

```bash
python archives/code_config/reconstruct_verified.py
```

The script reconstructs:

`RVC_CODE_CONFIG_COMPLETE.zip`

and refuses to report PASS unless all of the following hold:

- Base64 decoding succeeds;
- SHA-256 equals `093ef05675fecd3a4e41e9dd3765aa3920d8cff834ff12179a1a58bb146a0a2c`;
- ZIP CRC validation succeeds; and
- the archive contains the expected **61 files**.

The repository history contains legacy segmented copies of parts 15, 17, and 18 that must **not** be used for manual concatenation. Their verified replacement text is stored under `archives/code_config/corrections/`, and `reconstruct_verified.py` selects those replacements explicitly. Parts 1–14, 16, and 19 are read from the original segmented files. This preserves repository history while making the current reconstruction procedure deterministic and fail-closed.

The reconstructed ZIP contains the baseline implementation and unit tests, cross-object extension implementation and tests, package-intake schema, public acquisition tooling, post-lock challenge tooling, positive-control execution code, environment specifications, RVC schemas/cards, and operator/reconstruction definitions.

Third-party datasets/checkpoints and third-party source snapshots are not redistributed through this public repository when upstream licensing/provenance should remain authoritative. The journal supplementary package contains claim-bounded provenance records and publication-safe source references.

## Licensing

Author-created source code is released under the BSD 3-Clause License. Author-created non-code scientific artifacts are released under CC BY 4.0. Third-party materials retain their upstream licenses and attribution requirements.

## Citation

Citation metadata are provided in `CITATION.cff`. For a journal resubmission requiring an immutable public reference, cite the exact Git commit URL supplied in the manuscript rather than an unfrozen branch URL.
