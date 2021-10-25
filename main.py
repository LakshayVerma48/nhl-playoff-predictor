import pandas as pd
import requests
import pandasql as pdsql
import matplotlib.pyplot as plt
import json 

response = requests.get("https://statsapi.web.nhl.com/api/v1/teams").json()
teamDF = pd.DataFrame(response['teams'])
teamDF.to_csv('Output Files/test.csv')



#Accesing item in dictionary within a DF Column
#print(teamDF['venue'][0]['name'])

# for i in range(0, len(response['teams'])):
#     yearOfStart = response['teams'][i]['firstYearOfPlay']
#     teamNameAndStart[response['teams'][i]['name']] = int(yearOfStart)
