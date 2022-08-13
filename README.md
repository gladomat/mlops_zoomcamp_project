# MLOps Zoomcamp Project August 2022

## Introduction
In this project I will use the [Diamond Prices Dataset](https://www.kaggle.com/datasets/nancyalaswad90/diamonds-prices). This dataset contains prices and attributes for approximately 54,000 round-cut diamonds.
There are 53,940 diamonds in the dataset with 10 features (carat, cut, color, clarity, depth, table, price, x, y, and z). Most variables are numeric in nature, but the variables cut, color, and clarity are ordered factor variables.

## First Steps
I first created a jupyter notebook to explore the data and get a feel of what needs to be preprocessed. The notebook is called `diamond_regression_with_eda.ipynb`. You can read about the detailed analysis in that file. I will summarize the results here:

* no missing values or `NaN`s were found,
* both numerical and categorical values were present,
* most variables were correlated with the target `price`,
* those that showed no correlation were excluded: `depth`, `table`,
* the dimensions in x, y, and z direction were combined into a volume.

I included the following features into the model: `carat`, `cut`, `volume`, `color`, and `clarity` with the target as `price`.

Below is a pair plot of the numerical variables included in the model and the target.

![Pairplot of numerical variables](pairplot.png?raw=true)

## Preprocessing and Modelling scripts
I've created a preprocessing script in the `./preproc_modelling` directory. The preprocessing script is called `preprocess_data.py`. The training is run with the `model_training.py` script and experiment tracking is taken care of by MLFlow.

