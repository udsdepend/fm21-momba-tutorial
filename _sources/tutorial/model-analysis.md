# Model Analysis

After constructing and validating the model, we can now harvest the benefits of formal modeling by handing it over to an analysis tool.
Momba provides interfaces to state-of-the-art model analysis tools such as [Storm](https://www.stormchecker.org) and the [Modest Toolset](https://www.modestchecker.net/).
For this tutorial, we will be using the Modest Toolset, in particular, the probabilistic model checker `mcsta`.
Using `mcsta` you will be plotting the optimal winning probability as a function of the failure probability for different tracks such as in {numref}`analysis-results`.

```{figure} ./images/analysis-results.svg
---
name: analysis-results
align: center
---
Optimal winning probability as a function of the failure probability for different tracks.
```

First, we have to install [Matplotlib](https://matplotlib.org/), a plotting package for Python:
```
poetry add matplotlib
```

```{admonition} Exercise

The file `fmracer/analysis.py` provides a skeleton for the analysis tool which you have to complete by filling in the gaps.
Again, each gap comes with detailed instructions and hints what you need to do.
```

To run the analysis, the virtual environment needs to be active (see [](model-validation)).
Having activated the virtual environment, you start the analysis with:
```
fmracer analyze tracks/simple.txt tracks/large.txt
```
This will run the analysis using the tracks defined in `tracks/simple.txt` and `tracks/large.txt`.
The result of the analysis will be written to the file `results.pdf` in the current working directory.

The file `solutions/analysis.py` contains a possible solution.
