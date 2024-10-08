# WCG24 Cross Sections
Authors: Philip L. R. Weigel, Janet M. Conrad, Alfonso Garcia-Soto

This is the repository for the cross section files from [arxiv:2408.05866](https://arxiv.org/abs/2408.05866). The columns of each `.table` file correspond to the columns of the tables in Appendix C.
* `CT18ANNLO` primary NNLO cross sections from the paper
* `CT18ANLO` NLO version of the calculations
* `EPPS21nlo_CT18Anlo_O16` NLO oxygen cross sections (sigma/A)
* `EPPS21nlo_CT18Anlo_Fe56` NLO iron cross sections (sigma/A)
* `EPPS21nlo_CT18Anlo_Pb208` NLO oxygen cross sections (sigma/A)
* `NNPDF40_nnlo_as_01180_mhou` NNLO cross sections using NNPDF4

There is also a `sigma_splines` subfolder that contains [photospline](https://github.com/icecube/photospline) spline tables of the cross sections and the PDF uncertainties:
* `sigma_[PDFSET]_[PROJECTILE]_[TARGET]_[FLAVOR].fits`: Cross section spline for a given projectile, target, and flavor (including total sum of flavors)
* `sigma_[PDFSET]_[PROJECTILE]_[TARGET]_[FLAVOR]_unc.fits`: corresponding fractional uncertainties from the PDFs
For the EPPS21 cross sections, the target `nuclear` means that the cross section is the sum of `Z` protons and `N` neutrons divided by `A`.

An example python script for reading the splines can be found in `examples/spline_example.py`. Be aware that the splines can have some numerical inaccuracies, especially near boundaries.

I plan to include spline tables (using photospline) of the single- and double-differential cross sections and the PDF uncertainties soon.

I will also be releasing NC (without CKMT-PCAC) and nutau cross sections compatible with these cross sections in the near future. Stay tuned!

If you have any questions or find any issues, please contact me (pweigel@mit.edu)!
