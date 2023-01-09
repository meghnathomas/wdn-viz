---
title: 'VisWaterNet: A Python package for visualization of water distribution networks'
tags:
  - Python
  - NetworkX
  - Water distribution
  - Visualization
authors:
  - name: Meghna Thomas
    corresponding: true 
    affiliation: 1
  - name: Tyler Trimble
    affiliation: 1
  - name: Lina Sela
    orcid: 0000-0002-5834-8451
    affiliation: 1
affiliations:
 - name: The University of Texas at Austin, USA
   index: 1
date: 09 January 2023
bibliography: paper.bib

---

# Summary

Water distribution systems (WDSs) are complex networks, and can contain different types and vast numbers of elements. These elements have both static characteristics, such as pipe diameter and nodal elevation, as well as time-varying states, such as pipe flow rate and nodal pressure. Researchers and engineers working with WDSs have the need to model, simulate, analyze, and visualize these systems. Several open-source tools, such as EPANET and the Python package WNTR, allow users to perform extended period simulations and analysis of water distribution system models under a range of different conditions. However, while these tools do provide basic visualization functionality, they are limited in their flexibility and capabilities. The visualization of data over network topology can lend spatial context and a better understanding of simulation results and network propeties.

# Statement of need

`Gala` is an Astropy-affiliated Python package for galactic dynamics. Python
enables wrapping low-level languages (e.g., C) for speed without losing
flexibility or ease-of-use in the user-interface. The API for `Gala` was
designed to provide a class-based and user-friendly interface to fast (C or
Cython-optimized) implementations of common operations such as gravitational
potential and force evaluation, orbit integration, dynamical transformations,
and chaos indicators for nonlinear dynamics. `Gala` also relies heavily on and
interfaces well with the implementations of physical units and astronomical
coordinate systems in the `Astropy` package [@astropy] (`astropy.units` and
`astropy.coordinates`).

`Gala` was designed to be used by both astronomical researchers and by
students in courses on gravitational dynamics or astronomy. It has already been
used in a number of scientific publications [@Pearson:2017] and has also been
used in graduate courses on Galactic dynamics to, e.g., provide interactive
visualizations of textbook material [@Binney:2008]. The combination of speed,
design, and support for Astropy functionality in `Gala` will enable exciting
scientific explorations of forthcoming data releases from the *Gaia* mission
[@gaia] by students and experts alike.

`VisWaterNet` is a Python package that enables visualization of WDSs. Existing open-source hydraulic simulation software allows users to plot the network layout as well as plot simulation results in a continuous manner, i.e., by varying element colors on a color bar. 

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

We would like to thank Gerardo Riano-Briceno, Erik Vosburgh, and Matthew Frankel for testing the package and providing valuable feedback.

# References
