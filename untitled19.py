# -*- coding: utf-8 -*-
"""Untitled19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TWW27SyS3qdT-6KKGnV3ayRUZyrRyeAS
"""

try:
    from faker import Faker
except:
   !pip install faker 
   from faker import Faker
    
try:
    import psycopg2 
except:
    !pip install psycopg2-binary 
    import psycopg2
    
try:
    from sqlalchemy import create_engine
except:
    !pip install sqlalchemy
    from sqlalchemy import create_engine
    
    
try:
    import pandas as pd 
except:
    !pip install pandas
    import pandas as pd 
     
try:
    import matplotlib 
except:
    !pip install matplotlib
    import matplotlib

try:
    import sklearn 
except:
    !pip install sklearn
    import sklearn

import pandas as pd 
URL='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv'
UID_ISO_FIPS_LookUp_Table=pd.read_csv(URL)
UID_ISO_FIPS_LookUp_Table.head(10)

import pandas as pd 
Day='01-01-2021'
URL_Day=f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{Day}.csv'
DF_day=pd.read_csv(URL_Day)
DF_day.head(10)

# Get all daily data for India directly from github repo up to now
import pandas as pd 
Day='01-01-2021'
URL_Day=f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{Day}.csv'
DF_day=pd.read_csv(URL_Day)
DF_day['Day']=Day
cond=(DF_day.Country_Region=='United Kingdom')
Selec_columns=['Day','Country_Region', 'Last_Update',
       'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered', 'Active',
       'Combined_Key', 'Incident_Rate', 'Case_Fatality_Ratio']
DF_i=DF_day[cond][Selec_columns].reset_index(drop=True)
DF_i

List_of_days=[]
for year in range(2020,2022):
  for month in range(1,13):
    for day in range(1,32):
      month=int(month)
      if day <=9:
        day=f'0{day}'

      if month <= 9 :
        month=f'0{month}'
      List_of_days.append(f'{month}-{day}-{year}')

# Check this list 
List_of_days[0:10]

len(List_of_days)

Day='01-01-2021'

def Get_DF_i(Day):
    DF_i=None
    try: 
        URL_Day=f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{Day}.csv'
        DF_day=pd.read_csv(URL_Day)
        DF_day['Day']=Day
        cond=(DF_day.Country_Region=='United Kingdom')
        Selec_columns=['Day','Country_Region', 'Last_Update',
              'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered', 'Active',
              'Combined_Key', 'Incident_Rate', 'Case_Fatality_Ratio']
        DF_i=DF_day[cond][Selec_columns].reset_index(drop=True)
    except:
     #print(f'{Day} is not available!')
     pass
    return DF_i

print(Get_DF_i(Day))

Day='02-31-2021'

print(Get_DF_i(Day))

import time 

Start=time.time()
DF_all=[]
for Day in List_of_days:
    DF_all.append(Get_DF_i(Day))
End=time.time()
Time_in_sec=round((End-Start)/60,2)
print(f'It took {Time_in_sec} minutes to get all data')

# task1
DF_UK=pd.concat(DF_all).reset_index(drop=True)
# Create DateTime for Last_Update
DF_UK['Last_Updat']=pd.to_datetime(DF_UK.Last_Update, infer_datetime_format=True)  
DF_UK['Day']=pd.to_datetime(DF_UK.Day, infer_datetime_format=True)  

DF_UK['Case_Fatality_Ratio']=DF_UK['Case_Fatality_Ratio'].astype(float)

DF_UK.head(10)

DF_UK.info()

import matplotlib.pyplot as plt 
import matplotlib
font = {'weight' : 'bold',
        'size'   : 18}

matplotlib.rc('font', **font)

plt.figure(figsize=(12,8))
DF_UK_u=DF_UK.copy()
DF_UK_u.index=DF_UK_u.Day
DF_UK_u['Case_Fatality_Ratio'].plot()
plt.ylabel('Case Fatality Ratio')
plt.grid()

plt.figure(figsize=(12,8))
DF_UK_u=DF_UK.copy()
DF_UK_u.index=DF_UK_u.Day
DF_UK_u['Confirmed'].plot()
plt.ylabel('Confirmed')
plt.grid()

plt.figure(figsize=(12,8))
DF_UK_u=DF_UK.copy()
DF_UK_u.index=DF_UK_u.Day
DF_UK_u['Active'].plot()
plt.ylabel('Active')
plt.grid()

Selec_Columns=['Confirmed','Deaths', 'Recovered', 'Active', 'Incident_Rate','Case_Fatality_Ratio']
DF_UK_u_2=DF_UK_u[Selec_Columns]

DF_UK_u_2

from sklearn.preprocessing import MinMaxScaler

min_max_scaler = MinMaxScaler()


DF_UK_u_3 = pd.DataFrame(min_max_scaler.fit_transform(DF_UK_u_2[Selec_Columns]),columns=Selec_Columns)
DF_UK_u_3.index=DF_UK_u_2.index
DF_UK_u_3['Day']=DF_UK_u.Day
DF_UK_u_3.head(3)

DF_UK_u_3[Selec_Columns].plot(figsize=(20,10))
plt.savefig('uk_scoring_report.png')

DF_UK_u_3.to_csv('uk_scoring_report.csv')
#DF_India_u_2.to_csv('output/India_scoring_report_NotScaled.csv')