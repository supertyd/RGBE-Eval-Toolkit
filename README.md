# RGBE-Eval-Toolkit

This is a Python evaluation toolkit for the **VisEvent SOT Benchmark**, originally implemented in MATLAB.
It accurately reproduces the evaluation metrics (Success Rate / AUC and Precision) of the official VisEvent benchmark while offering a modern, easy-to-use Python interface.

## Features
- **Zero-Config Evaluation:** Comes with **built-in annotations (Ground Truth)**. No need to download datasets or match paths—just provide your tracking results.
- **100% Metric Alignment:** Provides mathematically identical metric calculations to the original MATLAB toolkit (OPE Precision and Success Rate).
- **Missing Modality Support:** Accurately handles missing modalities and absent frames, just like the original code.
- **Visual Reproduction:** Generates precision and success plots with the exact same color palettes, line styles, and formatting as the MATLAB scripts.
- **Auto-Detection:** Automatically detects tracking results based on directory names ending with `_tracking_result`.
- **Easy Installation:** Can be installed as a standard Python package.

## Installation

Clone the repository and install it via `pip`:

```bash
git clone https://github.com/supertyd/RGBE-Eval-Toolkit.git
cd RGBE-Eval-Toolkit
pip install -e .
```

## Usage

You can use the evaluation script directly as a module or through the CLI if configured. The toolkit allows for a completely hassle-free evaluation process.

### Directory Structure Requirements
Prepare your tracking outputs. Your folder structure should look like this:
- `./tracking_results/`: Place your tracking outputs here. Each tracker should have its own folder.

### Running Evaluation
Run the evaluation with a single command:

```bash
python -m visevent_eval.evaluator --tracking_results ./tracking_results
```

That's it! You don't need to specify the `--annos` path because the VisEvent annotations are securely bundled inside the package.

### Advanced Parameters

```bash
python -m visevent_eval.evaluator \
    --tracking_results ./tracking_results \
    --annos ./custom_annos \
    --tmp_mat ./tmp_mat \
    --res_fig ./res_fig
```

- `--tracking_results`: Path to your tracking results folder. 
- `--annos`: (Optional) Path to custom annotations. If omitted, the **built-in VisEvent annotations** are used automatically.
- `--tmp_mat` (Temporary Matrix): Path to save intermediate cached data. The evaluation involves heavy computations for IoU and center errors. To save time on future runs (e.g., if you just want to re-draw the plot or print metrics again), the script caches the massive result matrices as `.npz` files in this folder.
- `--res_fig` (Result Figures): Path to save the final plotted curve images. The script will output high-resolution `.png` files of the Precision and Success Rate plots into this folder, perfectly formatted and ready to be pasted into your paper.

## Outputs
- **Metrics (.npz files):** Saved in the `tmp_mat` directory for further analysis.
- **Figures:** High-quality plotted `.png` curves saved in the `res_fig` directory, perfectly matching the original MATLAB chart styles.
