# RGBE-Eval-Toolkit

This is a Python evaluation toolkit for the **VisEvent SOT Benchmark**, originally implemented in MATLAB.
It accurately reproduces the evaluation metrics (Success Rate / AUC and Precision) of the official VisEvent benchmark while offering a modern, easy-to-use Python interface.

## Features
- **100% Metric Alignment:** Provides mathematically identical metric calculations to the original MATLAB toolkit (OPE Precision and Success Rate).
- **Missing Modality Support:** Accurately handles missing modalities and absent frames, just like the original code.
- **Visual Reproduction:** Generates precision and success plots with the exact same color palettes, line styles, and formatting as the MATLAB scripts.
- **Auto-Detection:** Automatically detects tracking results based on directory names ending with `_tracking_result`.
- **Easy Installation:** Can be installed as a standard Python package with a global CLI entry point.

## Installation

Clone the repository and install it via `pip`:

```bash
git clone https://github.com/supertyd/RGBE-Eval-Toolkit.git
cd RGBE-Eval-Toolkit
pip install -e .
```

## Usage

After installation, the toolkit provides a command-line interface (CLI) named `visevent-eval`.

### Directory Structure Requirements
Prepare your evaluation data. By default, the script looks for folders in your current directory:
- `./tracking_results/`: Place your tracking outputs here. Each tracker should have its own folder named `[TrackerName]_tracking_result/`.
- `./annos/`: The VisEvent annotations directory (containing `gt_rect` and `absent` folders).

### Running Evaluation
You can run the evaluation using the CLI:

```bash
visevent-eval \
    --tracking_results ./tracking_results \
    --annos ./annos \
    --tmp_mat ./tmp_mat \
    --res_fig ./res_fig
```

If you leave out the arguments, it will automatically search for the default folder names in the current directory:
```bash
visevent-eval
```

## Outputs
- **Metrics (.npz files):** Saved in the `tmp_mat` directory for further analysis (replacing the old MATLAB `.mat` files).
- **Figures:** High-quality plotted `.png` curves saved in the `res_fig` directory, perfectly matching the original MATLAB chart styles.
