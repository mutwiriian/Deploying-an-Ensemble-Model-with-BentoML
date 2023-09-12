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
bentoml serve service:svc_array #:svc_json
```
Open your browser at the endpoint specified. Mine is at http://localhost/3000

Copy the contents of either `sample_array.txt` or `sample_json.txt` in the box obtained by clicking the button `Try it out`
For `svc_array` ensure the payload is within double square brackets.

# Contributing
You can make pull requests or open an issue for major changes.
