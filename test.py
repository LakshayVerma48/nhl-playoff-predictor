import pandas as pd
import requests
import pandasql as pdsql
import matplotlib.pyplot as plt 


numTeams = 31
teamNameAndStart = {}
for i in range(1, numTeams):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/teams/" + str(i)).json()
    yearOfStart = response['teams'][0]['firstYearOfPlay']
    teamNameAndStart[response['teams'][0]['name']] = yearOfStart

print(teamNameAndStart)