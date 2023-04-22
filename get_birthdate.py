k=0
import pandas as pd
import numpy as np
for year in range(2006,2023):
	for m in [1,2,3,4,5,6,7,8,9,10,11,12]:
		if m<10:
			month = "0"+str(m)
		else:
			month = str(m)
		file_name ="/disk/homedirs/nber/sc4331/equifax_scratch/equifax/equifax_aws/"+str(year)
		file_name =file_name+month
		file_name=file_name+".csv.gz"
		cols=['CONSUMER_ID', 'ARCHIVE_DATE', 'CONSUMER_AGE_ARCHIVE']
		curr= pd.read_csv(file_name, usecols=cols)
		if k>0
			data=prev.merge(current,on=['CONSUMER_ID'], how ="inner")
			data==data.loc[data['CONSUMER_AGE_ARCHIVE_x']!=data['CONSUMER_AGE_ARCHIVE_y']]
			data["year"]=year
			data["month"]=m
			if (month ==2) & (year ==2006)
				data.to_csv(birthdays.csv,index=False,header=True,mode='w')
			else: 
				data.to_csv(birthdays.csv,index=False,header=False,mode='a')
		curr=prev
		k=k+1
