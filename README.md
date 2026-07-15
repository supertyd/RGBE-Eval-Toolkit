# RGBE-Eval-Toolkit

This is a Python evaluation toolkit originally designed for the **VisEvent SOT Benchmark** but has been extended to act as a **Universal Evaluation Toolkit** for RGB-E and other multi-modal tracking datasets like **CRSOT**, **COESOT**, and custom benchmarks.

It accurately reproduces the evaluation metrics (Success Rate / AUC and Precision) of the official benchmarks while offering a modern, easy-to-use Python interface.

## Features
- **Universal Evaluation (New!):** Fully supports other benchmarks like **CRSOT** and **COESOT** out-of-the-box by simply pointing to their annotations. It automatically scans custom dataset structures and plots using your provided dataset name.
- **Zero-Config VisEvent Evaluation:** Comes with **built-in annotations (Ground Truth)** for VisEvent. No need to download datasets or match paths—just provide your tracking results.
- **100% Metric Alignment:** Provides mathematically identical metric calculations to the original MATLAB toolkit (OPE Precision and Success Rate).
- **Missing Modality Support:** Accurately handles missing modalities and absent frames automatically (even if the dataset omits `absent` annotations).
- **Visual Reproduction:** Generates precision and success plots with the exact same color palettes, line styles, and formatting as the MATLAB scripts.
- **Auto-Detection:** Automatically detects tracking results based on directory names ending with `_tracking_result`.
- **Flexible Delimiters:** Automatically adapts to both comma-separated and space-separated bounding box annotations.
- **Easy Installation:** Can be installed as a standard Python package.

## Installation

Clone the repository and install it via `pip`:

```bash
git clone https://github.com/supertyd/RGBE-Eval-Toolkit.git
cd RGBE-Eval-Toolkit
pip install -e .
```

## Usage

### 1. Zero-Config VisEvent Evaluation
If you are evaluating VisEvent, the annotations are already securely bundled inside the package. Run the evaluation with a single command:

```bash
python -m visevent_eval.evaluator --tracking_results ./tracking_results
```

### 2. General Evaluation (e.g. CRSOT, COESOT)
If you are evaluating another dataset like **CRSOT** or **COESOT**, you can provide your own `--annos` path and a `--dataset_name`. The toolkit will automatically scan the annotations folder, figure out the sequence list, format the data, and adapt the plot titles.

```bash
python -m visevent_eval.evaluator \
    --tracking_results ./CRSOT_Evaluation/tracking_results \
    --annos ./CRSOT_Evaluation/annos \
    --dataset_name CRSOT \
    --tmp_mat ./tmp_mat \
    --res_fig ./res_fig
```

### 3. Adding Support for Custom Datasets
The toolkit is highly flexible and accepts almost any custom tracking dataset out of the box. As long as your folder structure follows any of these standard conventions, you just need to point `--annos` to the dataset directory:

**Supported Annotation Formats:**
1. **VisEvent Style:** `annos/gt_rect/[sequence_name].txt` and optionally `annos/absent/[sequence_name].txt`
2. **CRSOT/Flat Style:** `annos/[sequence_name].txt` and optionally `annos/absent/[sequence_name].txt`
3. **COESOT/Nested Style:** `annos/coesot_anno/[sequence_name]/groundtruth.txt` or `annos/[sequence_name]/groundtruth.txt`

Simply run it with `--dataset_name YOUR_DATASET_NAME` to get beautifully titled plots!

### Advanced Parameters Explained
- `--tracking_results`: Path to your tracking results folder. 
- `--annos`: (Optional) Path to custom annotations. If omitted, the **built-in VisEvent annotations** are used automatically.
- `--dataset_name`: (Optional) The title of the dataset to be rendered on the output plot charts. Defaults to "VisEvent Testing Set".
- `--tmp_mat`: Path to save intermediate cached `.npz` files.
- `--res_fig`: Path to save the final plotted `.png` curves.

## Outputs
- **Metrics (.npz files):** Saved in the `tmp_mat` directory for further analysis.
- **Figures:** High-quality plotted `.png` curves saved in the `res_fig` directory, perfectly matching the original MATLAB chart styles.

## 🤖 AI Agent / Codex Skills
This repository includes built-in AI skills designed for agentic coding assistants like **Codex**. These skills transform the evaluation process into a fully automated, conversational experience.

**Included Skills:**
- **`rgbe-evaluator`**: Auto-evaluates RGB-Event datasets (VisEvent, CRSOT, COESOT) using this toolkit.
- **`rgbt-evaluator`**: Auto-evaluates RGB-Thermal datasets (RGBT234, LasHeR, GTOT, RGBT210) using the [opacity-black/RGBT_toolkit](https://github.com/opacity-black/RGBT_toolkit).

**How to use:**
1. Install the skills from the `skills/` directory in your agent environment.
2. Simply ask your agent: *"Evaluate the tracking results in `./my_results` using the rgbt-evaluator skill."*
3. The agent will autonomously install the tools, run the correct scripts, draw radar/curve charts, and summarize the final PR (Precision Rate) and SR (Success Rate) metrics directly in the chat.

## Related Projects
- [opacity-black/RGBT_toolkit](https://github.com/opacity-black/RGBT_toolkit) - A comprehensive toolkit for RGBT (RGB + Thermal) tracking evaluation. Highly recommended if you are working with RGBT datasets!
