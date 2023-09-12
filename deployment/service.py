import json
import numpy as np
import pandas as pd

from bentoml.io import NumpyNdarray, JSON #data exchange formats
from pydantic import BaseModel #for data vizualization
import bentoml #deployment

#get model from store and send to Runner
stacked_classifier_runner = bentoml.sklearn.get('stacked_classifier:latest').to_runner()

# Put the model in a bentoml.Service object which we then turn to an API by decorating
# with @svc.array.api. This defines an endpoint which invokes the function classifier()
# whenever it receives requests while sending data to the endpoint as an array.
svc_array = bentoml.Service(
    name = 'stacked_classifier_arr',
    runners= [stacked_classifier_runner]
)

@svc_array.api(input= NumpyNdarray(dtype= np.float32),
         output= NumpyNdarray(dtype= np.int64, shape= (-1,)))
def classifier(sample: np.array) -> np.array:
    '''Get prediction'''
    res = stacked_classifier_runner.predict.run(sample)
    return np.array(res)

with open('sample_dict.txt','r') as f:
    col_fields = json.load(f)

fields = {col_name: float for col_name in col_fields.keys()}

class WorkerFeatures(BaseModel):
    __annotations__ = fields

# Use pydantic to validate json data
input_spec = JSON(pydantic_model= WorkerFeatures)

svc_json = bentoml.Service(
    name='stacked_classifier_json',
    runners= [stacked_classifier_runner]
)

@svc_json.api(input= input_spec, output= NumpyNdarray())
def predict(sample: WorkerFeatures):
    input_df = pd.DataFrame([sample.dict()])
    return stacked_classifier_runner.run(input_df)