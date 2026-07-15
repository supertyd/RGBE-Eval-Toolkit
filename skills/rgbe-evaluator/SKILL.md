---
name: rgbe-evaluator
description: Guide for running zero-config multi-modal visual tracking evaluations using RGBE-Eval-Toolkit. Use when testing, verifying, or computing SR/PR benchmarks on datasets like VisEvent, CRSOT, and COESOT for tracking results.
metadata:
  short-description: Run multi-modal tracking evaluations
---

# RGBE Evaluator Skill

This skill provides procedures for evaluating Single Object Tracking (SOT) results on multi-modal tracking datasets (like VisEvent, CRSOT, COESOT) using the `RGBE-Eval-Toolkit`.

## When to Use This Skill
- The user provides a tracking result folder (containing `.txt` result files for bounding boxes).
- The user asks to compute PR (Precision Rate) or SR/AUC (Success Rate / Area Under Curve) for datasets like VisEvent, CRSOT, or COESOT.
- The user wants to generate precision and success plots.

## Core Evaluation Workflow

**1. Locate or Prepare Tracking Results**
Ensure the tracking results are inside a folder ending with `_tracking_result` (e.g., `Ours_tracking_result/`) and placed within a parent directory (e.g., `tracking_results/`).

**2. Ensure the Toolkit is Installed**
If not already installed, install the toolkit via pip from the repository:
`pip install git+https://github.com/supertyd/RGBE-Eval-Toolkit.git`

**3. Execute Evaluation Command**
Run the evaluation depending on the dataset requested. 

*For VisEvent (Zero-config, annotations are built-in):*
```bash
python -m visevent_eval.evaluator \
    --tracking_results <path_to_tracking_results_parent_dir>
```

*For CRSOT / COESOT or Custom Datasets:*
Point to their respective annotation directories.
```bash
python -m visevent_eval.evaluator \
    --tracking_results <path_to_tracking_results_parent_dir> \
    --annos <path_to_custom_annos_dir> \
    --dataset_name "CRSOT"  # or "COESOT", etc.
```

**4. Retrieve and Report Results**
- The evaluation will output `.npz` files in `tmp_mat/` (or the folder specified by `--tmp_mat`).
- The evaluation will output `.png` charts in `res_fig/` (or the folder specified by `--res_fig`).
- To report exact numerical results, use a short python script to read `aveSuccessRatePlot...overlap_OPE.npz` (for AUC) and `aveSuccessRatePlot...error_OPE.npz` (for Precision at threshold index 20), calculate the mean, and print them.

## Important Notes
- The toolkit natively handles missing modalities and `absent.txt` files automatically.
- Precision is reported using the Location Error Threshold at 20 pixels (index 20).
- AUC is calculated by taking the mean over the overlap threshold array.
