import requests
import sys
response = requests.get("https://api.rootnet.in/covid19-in/stats/latest").json()
# print(response)                                                         # This will print the entire JSON response
# print(response['data']['regional'])                                    # This will print the regional data
for i in response['data']['regional']:
    print("no of deaths in",i['loc'],"are :",i['deaths'])
print("\n\n")

loc = []
discharged = []
deaths = []
totalConfirmed = []
for i in response['data']['regional']:
    loc.append(i['loc'])
    discharged.append(i['discharged'])
    deaths.append(i['deaths'])
    totalConfirmed.append(i['totalConfirmed'])

import pandas as pd
d = {'Region':loc,'discharged':discharged,'death_count':deaths,'Confirmed_cases':totalConfirmed} 
df = pd.DataFrame(d)
print(df.sort_values('death_count',ascending=False))
df.to_csv('covid.csv')
sys.exit()
# if we take a site with large amount of data in multiple pages then we can use the below code to hit multiple times on url and create database each Time
final = pd.DataFrame()
for j in range(1,501) :             # for site containing 500 pages
    df0 = requests.get("https://api.rootnet.in/covid19-in/stats/latest?page="+str(j)).json()   #  (   or   )
    df0 = requests.get("https://api.rootnet.in/covid19-in/stats/latest?page={}".format(j)).json()
    # then put the above code for creating dataframe using pandas inside this loop which iterates for each page of the site 
    df = pd.DataFrame(df0)
    final = pd.concat([final,df],ignore_index=True)   # (  or  )
    final = final.append(df,ignore_index=True)