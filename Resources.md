web scraping companies site :
        https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav



covid related API :
        https://api.rootnet.in/covid19-in/stats/latest



JSON viewer :
      https://jsonviewer.stack.hu/

helps to concisely view the contents of the site and make good descision in respect to what rows and columns we will add in our dataframe and how to extract correctly.



API to PANDAS dataframe extraction :
      https://www.youtube.com/watch?v=HOSGP23DAHI&list=PLKnIA16_RmvZAqJzKstVHywcRNMn6pcGD&index=7



Basic outline for API to dataframe :
import requests
import pandas as pd
api_url = 'https://api.example.com/data'
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    
else:
    print(f"Failed to retrieve data: {response.status_code}")
