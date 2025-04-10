# Transforming Total Field Anomaly into Anomalous Magnetic Field: Using Dual-Layer Gradient-Boosted Equivalent Sources

by
[India Uppal](https://orcid.org/0000-0003-3531-2656),
[Leonardo Uieda](https://orcid.org/0000-0001-6123-9515),
[Vanderlei Coelho Oliveira Jr.](https://orcid.org/0000-0002-6338-4086),
[Richard Holme](https://orcid.org/0009-0002-2178-2083).

This repository contains the data and source code used to produce the results
presented in:

> Uppal, I., Uieda, L., Oliveira Jr., V. C., Holme, R. (2025). Transforming Total Field Anomaly into Anomalous Magnetic Field: Using Dual-Layer Gradient-Boosted Equivalent Sources. EarthArXiv. doi:[EARTHARXIV_DOI](https://doi.org/EARTHARXIV_DOI)

|  | Info |
|-:|:-----|
| Version of record | https://doi.org/JOURNAL_DOI |
| Open-access version on EarthArXiv | https://doi.org/EARTHARXIV_DOI |
| Archive of this repository | https://doi.org/10.5281/zenodo.15120458 |
| Reproducing our results | [`REPRODUCING.md`](REPRODUCING.md) |

## About

This is the first paper of India's PhD thesis. It was motivated by our desire to improve the currently available magnetic data products available for Antarctica. We realised that more sophisticated methods of interpolating and joining the the different survey data were needed and that equivalent sources was likely the way forward. These results serve as the basis for further exploration into the challenging Antarctic magnetic datasets.

## Abstract

Potential field data often require interpolation onto a regular grid at constant height before further analysis. A widely used approach for this is the equivalent sources technique, which has been adapted over time to improve its computational efficiency and accuracy of the predictions. However, many of these approaches still face challenges, including border effects in the predictions or reliance on a stabilising parameter. To address these limitations, we introduce the dual-layer gradient-boosted equivalent sources to: (1) use a dual-layer approach to improve the predictions of long-wavelength signals and reduce border effect; (2) use block-averaging and the gradient-boosted equivalent sources method to reduce the computational load; (3) apply Block K-Fold cross-validation to guide optimal parameter selection for the model. The proposed method was tested on both synthetic datasets and the ICEGRAV aeromagnetic dataset to evaluate the methods ability to interpolate and upward continue onto a regular grid at constant height as well as predict the amplitude of the anomalous field from total-field anomaly data. The dual-layer approach proved superior to the single-layer approach at predicting both short- and long-wavelength signals, particularly in the presence of truncated long-wavelength anomalies. The use of block-averaging and the gradient-boosting method make our dual-layer approach computationally light, being able to grid over 400,000 data points in under 2 minutes on a moderate workstation computer.

## License

All Python source code (including `.py` and `.ipynb` files) is made available
under the MIT license. You can freely use and modify the code, without
warranty, so long as you provide attribution to the authors. See
`LICENSE-MIT.txt` for the full license text.

The manuscript text (including all LaTeX files), figures, and data/models
produced as part of this research are available under the [Creative Commons
Attribution 4.0 License (CC-BY)][cc-by]. See `LICENSE-CC-BY.txt` for the full
license text.

[cc-by]: https://creativecommons.org/licenses/by/4.0/
