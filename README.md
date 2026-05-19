# Linear Algebra in Python

Hands-on implementation of core linear algebra concepts using NumPy and Matplotlib, built as part of a structured mechatronics and robotics self-study roadmap.

Every concept is coded from scratch — no robotics libraries, no shortcuts. The goal is to understand the mathematics that powers robot kinematics, control systems, and state estimation before using any higher-level tools.

---

## Concepts Covered

| Script | Concept |
|---|---|
| `01_numpy_basics.py` | NumPy arrays, operations, linear algebra functions |
| `02_rotation_matrices.py` | 2D and 3D rotation matrices, orthogonality, composition |
| `03_homogeneous_transforms.py` | T = [R│t], transform chaining, inverse, 3D frame visualization |
| `04_linear_systems.py` | Solving Ax=b — circuit analysis and beam force balance |
| `05_eigenvalues.py` | Eigendecomposition, geometric visualization, stability check |
| `06_svd.py` | SVD decomposition and image compression |
| `07_fk_2link_arm.py` | Forward kinematics of a 2-link planar arm using transforms |

---

## Output Figures

### Rotation Matrix — 2D
Vector [3, 0] rotated 90° to [0, 3] using R2(θ).

![Rotation Matrix 2D](output%20figures/rotation%20matrix%20in%202d.png)

### Homogeneous Transformation — 3D Frame
World frame (origin) and transformed frame shown as RGB coordinate axes (Red=X, Green=Y, Blue=Z).

![Homogeneous Transformation](output%20figures/Homogenous%20Transformation.png)

### Eigenvectors vs Random Vectors
Blue: random vectors. Red: same vectors after multiplication by A. Green: eigenvectors. Purple: A applied to eigenvectors — same direction, only scaled.

![Eigenvalues](output%20figures/eigen%20vectors.png)

### SVD Image Compression
Original image reconstructed using top k singular values. k=5 is heavily degraded, k=150 is nearly identical to the original.

![SVD Compression](output%20figures/SVD.png)

### 2-Link Planar Arm — Stick Figure
Arm configuration for user-defined link lengths and joint angles.

![2-Link Arm](output%20figures/2-link%20planar%20arm.png)

### 2-Link Planar Arm — Workspace
All reachable end-effector positions swept over θ1 and θ2 ∈ [−180°, 180°]. Inner radius = |L1−L2|, outer radius = L1+L2.

![Workspace](output%20figures/2-link%20planar%20arm%20workspace.png)

---

## How to Run

**Install dependencies:**
```bash
pip install numpy matplotlib pillow
```

**Run any script:**
```bash
python 01_numpy_basics.py
python 02_rotation_matrices.py
python 03_homogeneous_transforms.py
python 04_linear_systems.py
python 05_eigenvalues.py
python 06_svd.py          # requires image.png in the same folder
python 07_fk_2link_arm.py
```

Scripts `02`, `03`, `04`, and `07` take interactive inputs (vector, angle, link lengths, etc.) from the terminal.

---

## What I Learned

- NumPy linalg: `inv`, `det`, `norm`, `solve`, `matrix_rank`, `eig`, `svd`
- Rotation matrices built from scratch for 2D and 3D, orthogonality verified
- Homogeneous transforms T = [R│t]: assembly, application, chaining, and efficient inversion using R.T
- Solving physical systems (KCL/KVL circuit, beam equilibrium) as Ax=b
- Eigenvalue decomposition: geometric meaning and connection to system stability
- SVD: matrix factorization A = UΣVᵀ and low-rank approximation for image compression
- Forward kinematics of a 2-link planar arm using only matrix multiplication — no robotics libraries
