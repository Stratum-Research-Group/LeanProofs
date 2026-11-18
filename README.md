# ETH Research & TensorSAT Engineering Framework

<p align="center">
  <img src="TensorSAT/assets/tensorsat_logo.png" alt="TensorSAT - Stratum Research Group" width="100%" />
</p>

This folder contains the complete audit, independent verification, and practical application engineering derived from Anthropic's research paper *"A $2^{o(n)}$ Time Algorithm for 3-SAT"* (October 26, 2026).

---

## Folder Contents & Structure

* **[`01-anthropic-eth-research-2026-11-17-6521692d.txt`](01-anthropic-eth-research-2026-11-17-6521692d.txt)**: Original executive research brief.
* **[`eth-review-report-2026-11-18.txt`](eth-review-report-2026-11-18.txt)**: Comprehensive formal verification and audit report covering Stages A through D (specification audit, contraction experiment, proof audit, and complete Lean 4 toolchain build).
* **[`verify_contraction_identity.py`](verify_contraction_identity.py)**: Standalone Python verification script validating 4,384 parameter configurations of the single-bit and multi-bit uncrossing identity ($X_1 = I_1 - s \otimes s$) against brute force.
* **[`formal-math-repo/`](formal-math-repo/)**: Full clone of the official `anthropics/formal-math` repository at commit `16a5ce41304fcdaea4e0be7c132e1c361dc26da5`.
  * Paper: `formal-math-repo/eth/paper.pdf`
  * Formal Claims: `formal-math-repo/eth/MainResults.lean`
  * Proof-to-Paper Mapping: `formal-math-repo/eth/proof/PaperIndex.lean`
* **[`TensorSAT/`](TensorSAT/)**: The practical software library and application suite putting the core mathematical breakthrough to work.

---

## Verification Summary (Lean 4 & Mathematics)

1. **Full Kernel Replay & Axiom Closure:**
   - Compiled all 9,768 jobs in the Lean 4 development using `leanprover/lean4:v4.33.1`.
   - Executed `lake env lean scripts/PrintAxioms.lean`, proving both `MainResults.ethIsFalse` and `MainResults.mainTheorem` rest strictly on Lean's 3 standard foundation axioms (`propext`, `Classical.choice`, `Quot.sound`) with no external hypotheses or custom axioms.
2. **Public Reproduction Report:**
   - Formal reproduction report submitted and tracked on GitHub: [anthropics/formal-math#50](https://github.com/anthropics/formal-math/issues/50).

---

## TensorSAT: Engineering the Breakthrough

To translate the planar tensor contraction and singlet uncrossing identity ($\text{SWAP} = I - 2 \cdot \text{singlet}$) into real-world software, **TensorSAT** provides:
- **`SingletAttention`**: A PyTorch sub-quadratic attention module scaling long context windows to 16,384+ tokens in 9 ms without GPU Out-of-Memory crashes.
- **`CNFFormula` Preprocessor**: Separates dense variable interaction cliques for GPU tensor contraction while delegating sparse logic to CDCL counters.
- **8 Architectural Blueprints**: Covering Quantum simulation, VLSI chip routing, Bayesian networks, exact #SAT counting, protein rotamer optimization, post-quantum cryptanalysis, warehouse robot pathfinding, and smart contract auditing.

See the dedicated documentation in **[`TensorSAT/README.md`](TensorSAT/README.md)**.
