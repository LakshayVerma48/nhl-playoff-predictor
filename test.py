import pandas as pd
import requests
import pandasql as pdsql

response = requests.get("https://statsapi.web.nhl.com/api/v1/teams")

print(response.status_code)