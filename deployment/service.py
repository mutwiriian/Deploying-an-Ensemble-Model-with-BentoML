import json
import pandas as pd

from bentoml.io import NumpyNdarray, JSON #data exchange formats
import bentoml #deployment
from pydantic import BaseModel #for data vizualization

#get model from store and send to Runner
stacked_classifier_runner = bentoml.sklearn.get('stacked_classifier:latest').to_runner()

#create dict of names and types
with open('sample.txt','r') as f:
    col_fields = json.load(f)

fields = {col_name: float for col_name in col_fields.keys()}

#define a pydantic model from dict of names and types
class WorkerFeatures(BaseModel):
    __annotations__ = fields

# Use pydantic to validate json data
input_spec = JSON(pydantic_model= WorkerFeatures)

svc = bentoml.Service(
    name='stacked_classifier',
    runners= [stacked_classifier_runner]
)

# Put the model in a bentoml.Service object which we then turn to an API by decorating
# with @svc.array.api. This defines an endpoint which invokes the function classifier()
# whenever it receives requests while sending data to the endpoint as an array.
@svc.api(
        input= input_spec,
        output= NumpyNdarray(),
        route='/predict')
def classify(sample: WorkerFeatures):
    input_df = pd.DataFrame([sample.dict()])
    return stacked_classifier_runner.run(input_df)