import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

final = pd.DataFrame()
for j in range(1,80) :
    url = "https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page={}".format(j)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    webpage = requests.get(url,headers=headers).text

    soup = bs(webpage, 'lxml')

    Reviews = []
    Salaries = []
    Interviews = []
    Jobs = []
    Benifits = []
    Photos = []
    for j in soup.find_all('div', class_ ='companyCardWrapper__tertiaryInformation') :
        for t in j.find_all()[1] :
            try :
                Reviews.append(t.text)
            except :
                Reviews.append(np.nan)

        for t in j.find_all()[4] :
            try :
                Salaries.append(t.text)
            except :
                Salaries.append(np.nan) 

        for t in j.find_all()[7] :
            try :
                Interviews.append(t.text)
            except :
                Interviews.append(np.nan)

        for t in j.find_all()[10] :
            try :
                Jobs.append(t.text)
            except :
                Jobs.append(np.nan)

        for t in j.find_all()[13] :
            try :
                 Benifits.append(t.text)
            except :
                Benifits.append(np.nan)

        for t in j.find_all()[16] :
            try :
                Photos.append(t.text)
            except :
                Photos.append(np.nan)

    name = []
    for f in soup.find_all('h2', class_ ='companyCardWrapper__companyName') :
                try :
                     name.append(f.text.strip())
                except :
                    name.append(np.nan)

    rating = [] 
    for j in soup.find_all('span', class_ ='companyCardWrapper__companyRatingValue') :
                try :
                     rating.append(j.text.strip())
                except :
                    rating.append(np.nan)

    d = {'Company Name':name, 'Ratings':rating, 'Salaries':Salaries, 'Jobs':Jobs, 'Reviews':Reviews, 'Interviews':Interviews, 'Benifits':Benifits, 'Photos':Photos}
    df = pd.DataFrame(d)

    final = pd.concat([final,df],ignore_index=True)
final.to_csv('web_scraped_TopCompanies.csv')
print(final)