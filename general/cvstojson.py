import pandas as pd
import requests
import json
import jsonpath

data = pd.read_csv(r'C:\Users\saivi\pyWorkSpace\algorithms\general\Weather_Linear_Regression_Model.csv')  #read csv data
a = data.to_json (r'C:\Users\saivi\pyWorkSpace\algorithms\general\WeatherJson.json')
