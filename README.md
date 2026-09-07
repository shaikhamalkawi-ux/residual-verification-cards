# Residual Verification Cards (RVC)

Public reproducibility artifact accompanying the manuscript:

**Residual Verification Cards: A Fail-Closed Audit Contract with Bounded Cross-Object Conformance Tests for Neural PDE Outputs**

## Purpose

Residual Verification Cards (RVC) provide an executable, machine-readable claim-admissibility contract for neural-PDE audit records. The artifact checks artifact identity, prediction dependency, numerical operator, evaluation support, comparison object, aggregation, provenance, and requested claim level before releasing a diagnostic.

This repository is a reproducibility and conformance artifact. It is not a solver, leaderboard, universal validation method, deployment certificate, or residual-to-solution guarantee.

## Residual181 verification status

- Baseline unit tests: **36/36 PASS**.
- Cross-object extension unit tests: **49/49 PASS**.
- Fresh H05–H10 external-source rejection challenge: **6/6 overall-state agreement** and **6/6 semantic-route completion**.
- Positive external controls: **PC01 and PC06** are claim-scoped admissions.

These results do **not** establish universal external validity, independent third-party validation, population sensitivity/specificity, exact checkpoint-training lineage for PC01/PC06, deployment readiness, certification, model superiority, or a residual-to-solution guarantee.

## Repository map

- `baseline/` — baseline RVC implementation, schemas, finite conformance suites, calculations, tests, and verification records.
- `cross_object_extension/` — bounded cross-object and package-intake extension with tests and verification records.
- `external_challenge/` — public-facing post-lock H05–H10 challenge records and execution evidence.
- `positive_external_controls/` — bounded positive-control code/configuration/provenance records.
- `interoperability/` — public source ledger, acquisition tools, and interoperability metadata.
- `documentation/` — revised supplementary material and public documentation.
- `licenses/` — licenses for author-created code and non-code scientific artifacts.

Third-party datasets/checkpoints are not redistributed where public re-hosting is unnecessary or upstream licensing/provenance should remain authoritative. Included provenance records identify relevant external sources and hashes for reacquisition and verification.

## Verification

For security, execute bundled verification code only in a disposable, no-network container or virtual machine.

### Baseline

```bash
cd baseline
python 02_Code/verify_rvc_package.py --full
python 02_Code/run_unit_tests.py
```

### Cross-object extension

```bash
cd cross_object_extension
PYTHONDONTWRITEBYTECODE=1 python 02_Code/rvc_extension/verify_extension.py
python 02_Code/run_extension_tests.py
python 02_Code/rvc_extension/package_audit.py 06_Package_Intake/Example_PASS
```

## Licensing

Author-created source code is released under the BSD 3-Clause License. Author-created non-code scientific artifacts are released under CC BY 4.0. Third-party materials retain their upstream licenses and attribution requirements.

## Citation

Citation metadata are provided in `CITATION.cff`.
