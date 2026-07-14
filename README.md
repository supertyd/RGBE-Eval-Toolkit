# FlexTrack-V2: Active Compensation for Missing Modalities in Multimodal Visual Tracking

This repository contains the LaTeX source code for the paper **"FlexTrack-V2: Active Compensation for Missing Modalities in Multimodal Visual Tracking"**.

## Abstract
Multimodal visual object tracking augments an RGB camera with auxiliary sensors (e.g., thermal, depth, or event) to maintain robustness in adverse conditions. However, real-world sensor rigs frequently suffer from de-synchronization or signal dropout, rendering the auxiliary modality intermittently missing. Conventional multimodal trackers degrade sharply under these conditions. In this paper, we propose FlexTrack-V2, a unified tracking framework that actively hallucinates missing information. We introduce the Bilateral Modality-specific feature Reconstruction (BMR) module, which couples with a Heterogeneous Mixture-of-Experts (HMoE) to actively synthesize missing features and dynamically allocate computation. We also propose Curriculum Missing Augmentation (CMA) with online self-distillation. Extensive experiments across nine benchmarks demonstrate that FlexTrack-V2 achieves parity with state-of-the-art models under complete modalities and yields substantial, consistent improvements under missing-modality regimes.

## Repository Structure
- `main.tex`: The main LaTeX file.
- `sections/`: Contains the individual sections (Abstract, Introduction, Related Work, Method, Experiments, Conclusion).
- `tables/`: Contains the LaTeX files for the experimental tables (main results, ablations).
- `figures/`: Contains the image assets.
- `main.bib`: Bibliography file containing references.

## Compilation
To compile the PDF, you can use `pdflatex`, `latexmk`, or simply upload this directory to an Overleaf project. 
For local compilation, ensure you have a standard TeX distribution (e.g., TeX Live, MacTeX) installed:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```
