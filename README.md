# Introduction
After doing analysis in R for quiet some time, I decided to take on Python in order to enjoy the 
flexiibity and convenience of being a bilingual data scientist. Here I analyse the productivity of garment workers by some descriptive statistics and ultimately building
a machine learning model. This is a simplied project and is among my first Python projects. 

The aim was to practice data wrangling and visualiation skills and not building state-of-the-art model
as this comes higher computational costs

# Usage
To see the model in action run:

```bash
git clone https://github.com/mutwiriian/Garment-Workers-Productivity-Analysis-and-Ensemble-Model-building-Scikit-Learn.git
```

```bash
cd deployment
```
Activate environment from `poetry.lock` with

```bash
poetry lock
```
and activate the environment with
```bash
poetry shell
```
Install the packages packages by running

```bash
poetry install
```

Run the service with

```bash
bentoml serve service:svc_array #:svc_json
```
Open your browser at the endpoint specified. Mine is at http://localhost/3000

Copy the contents of either `sample_array.txt' or 'sample_json.txt' int the `Tryout` button.
For `svc_array` ensure the payload is within double square brackets.

To run the notebook, follow the installation steps above but while in the root directory

# Contributing
You can make pull requests or open an issue for major changes.
