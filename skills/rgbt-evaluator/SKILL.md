---
name: rgbt-evaluator
description: Guide for evaluating multi-modal RGBT (RGB + Thermal) tracking results using the rgbt pip package (opacity-black/RGBT_toolkit). Use when testing, verifying, or computing SR (Success Rate/MSR) and PR (Precision/MPR) for RGBT datasets like RGBT234, GTOT, RGBT210, and LasHeR.
metadata:
  short-description: Run RGBT tracking evaluations
---

# RGBT Evaluator Skill

This skill provides procedures for evaluating RGBT (RGB + Thermal) Single Object Tracking (SOT) results using the `opacity-black/RGBT_toolkit` package.

## When to Use This Skill
- The user provides a tracking result folder for RGBT datasets.
- The user asks to compute PR (MPR) or SR (MSR) for datasets like RGBT234, LasHeR, GTOT, or RGBT210.
- The user wants to generate precision and success plots or radar charts for RGBT tracking.

## Core Evaluation Workflow

**1. Install the Toolkit**
If not already installed, install the toolkit via pip:
`pip install rgbt`

**2. Evaluate via Python Script**
Create a short Python script to run the evaluation dynamically. For example, to evaluate a tracker on RGBT234:

```python
from rgbt import RGBT234
from rgbt.utils import RGBT_start, RGBT_end
import os

# GTOT requires RGBT_start() and RGBT_end() due to metric compatibility. For other datasets it is safe to omit or keep.
RGBT_start()

# Initialize the dataset evaluator (e.g., RGBT234(), LasHeR(), GTOT(), RGBT210())
evaluator = RGBT234()

tracker_name = "MyTracker"
result_path = "/path/to/results/folder"  # Folder containing the sequence results (.txt)

# Register the tracker. 
# Note: Ensure bbox_type matches the format. Standard is "ltwh" [x, y, w, h]. 
evaluator(
    tracker_name=tracker_name, 
    result_path=result_path, 
    bbox_type="ltwh"
)

# Evaluate
pr_dict = evaluator.MPR()
sr_dict = evaluator.MSR()

print(f"MPR (Precision) for {tracker_name}: {pr_dict[tracker_name][0]:.4f}")
print(f"MSR (Success) for {tracker_name}: {sr_dict[tracker_name][0]:.4f}")

# Optional: Draw plots
evaluator.draw_plot(metric_fun=evaluator.MPR)
evaluator.draw_plot(metric_fun=evaluator.MSR)
evaluator.draw_attributeRadar(metric_fun=evaluator.MPR)

RGBT_end()
```

**3. Execute and Report**
Run the Python script you generated. Once the execution is complete, report the MPR (Precision) and MSR (Success Rate) to the user.

## Important Notes
- Always check the bounding box format. Standard output for trackers is usually `[x, y, w, h]`, which corresponds to `bbox_type="ltwh"`. If the tracker outputs 8 corner coordinates, use `bbox_type="corner"`.
- GTOT evaluation *requires* calling `RGBT_start()` before and `RGBT_end()` after the evaluation to handle historical compatibility differences.
