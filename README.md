# BSC with Python

A collection of Python-based homework assignments focused on fundamental
concepts in **Statistics, Probability, Data Analysis, and
Visualization**.

This repository contains standalone scripts developed as part of
coursework exercises. Each file typically demonstrates a specific
statistical concept through simulation, computation, and graphical
visualization.

------------------------------------------------------------------------

## Project Overview

The repository includes multiple homework assignments covering topics
such as:

-   Data visualization (bar charts, pie charts, histograms)
-   Effect of outliers on statistical measures
-   Gaussian (Normal) distributions
-   Probability Density Functions (PDF)
-   Cumulative Distribution Functions (CDF)
-   Data normalization and scaling
-   Statistical testing and analysis

Each script is independent and can be executed individually.

------------------------------------------------------------------------

## Repository Structure

Example files included in the project:

    HW1-q1.py
    HW1-q2.py
    HW2.py
    HW3-ch4q*.py
    HW3-ch8q*.py
    HW4-ch9q*.py
    HW5-ch6-q*.py
    HW3-reports.pdf

Naming convention:

-   `HW` → Homework number\
-   `chX` → Chapter number\
-   `qY` → Question number

------------------------------------------------------------------------

## Requirements

-   Python 3.9+ (recommended)

Required libraries (depending on the script):

-   numpy
-   matplotlib
-   scipy
-   scikit-learn

------------------------------------------------------------------------

## Installation

It is recommended to use a virtual environment:

``` bash
python -m venv venv
```

Activate the environment:

**Linux / macOS**

``` bash
source venv/bin/activate
```

**Windows**

``` bash
venv\Scripts\activate
```

Install dependencies:

``` bash
pip install numpy matplotlib scipy scikit-learn
```

------------------------------------------------------------------------

## Running the Scripts

Each file can be executed independently:

``` bash
python HW2.py
python HW3-ch8q6.py
python HW5-ch6-q1.py
```

Most scripts generate visual outputs using `matplotlib`. Some scripts
also print numerical results in the terminal.

------------------------------------------------------------------------

## Reproducibility

Several scripts rely on random number generation. To ensure reproducible
results, you may add a random seed at the beginning of the script:

``` python
import numpy as np
np.random.seed(42)
```

------------------------------------------------------------------------


## Author
Mahan Baneshi
Developed as part of academic coursework in statistics and data analysis
using Python.
