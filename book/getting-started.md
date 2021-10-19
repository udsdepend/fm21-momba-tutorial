---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Getting Started

```{code-cell} ipython3
from momba import model

ctx = model.Context(model.ModelType.MDP)

print(ctx)
```