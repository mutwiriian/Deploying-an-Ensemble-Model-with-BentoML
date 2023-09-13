# Introduction
Here I deploy the trained model as a microservice which users and other programs can interact with.

There are many methods of deploying machine learning as have been discussed 
[here](https://towardsdatascience.com/various-types-of-deployment-in-machine-learning-b503017e6bae#:~:text=The%20batch%20inference%20is%20a,as%20generating%20reports%20or%20predictions.). I am starting out with RESTful APIs as they have an easier learning curve. I have worked with [FastAPI](https://github.com/mutwiriian?tab=repositories). It is awesome! But sooner one will realize that ML models need to have low-latency in production settings where we expect high traffic. A specialized tool, BentoML, is built exactly for that. The bentoml API provides a `runner` object that optimizes inference by enabling concurrent runs, dynamically alocating resources and independent scaling.

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
bentoml serve service:svc
```
Open your browser at the endpoint specified. Mine is at http://localhost/3000

Copy the contents of `sample.txt` in the box obtained by clicking the button `Try it out`

# Creating the Bento object
A `Bento` is a collection of the artifacts that are required to successfully run the model
This is created by running

```bash
bentoml build
```
This file is the standard format for uniform distribution in BentoML

# Docker
To run the model in its own environment, I use Docker. Bentoml generates a Docker image when we run
```bash
bentoml containerize stacked_classifier:latest
```
We can then run the image by
```bash
docker run --rm -p 3000:3000 stacked_classifier:kt3lcfcsakylpmo6
```
Navigate to `http://localhost:3000` where you can interact with the deployed model.

# Contributing
You can make pull requests or open an issue for major changes.
