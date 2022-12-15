# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 17:42:53 2022

@author: frenz
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 13:23:18 2022

@author: 97798
"""
import os
import glob
import datetime
import pandas as pd
file_df=pd.DataFrame(columns=['file','m_date','FY'])
#files=glob.iglob('D:/GSD/Gravity/Field/**', recursive=True)
files=glob.iglob('E:\\Datasection\\Drive_D/**', recursive=True)

file_list=pd.DataFrame(columns=['files','m_date','FY'])
for file in files:
    mtime=datetime.datetime.fromtimestamp(os.path.getmtime(file))
    #print (file+"     "+ str (mtime))
    file_list.append([file,mtime, 1],)
    row=[file,mtime,'1']
    file_df.loc[len(file_df)] = row
    
#fiscal years

fy1=['2068/69','2011-07-17', '2012-07-15']
fy2=['2069/70','2012-07-16', '2013-07-16']
fy3=['2070/71','2013-07-16', '2014-07-16']
fy4=['2071/72','2014-07-17', '2015-07-16']
fy5=['2072/73','2015-07-17', '2016-07-15']
fy6=['2073/74','2016-07-16', '2017-07-15']
fy7=['2074/75','2017-07-16', '2018-07-16']
fy8=['2075/76','2018-07-17', '2019-07-16']
fy9=['2076/77','2019-07-17', '2020-07-15'] 
fy10=['2077/78','2020-07-16', '2021-07-15']
fy11=['2078/79','2021-07-16', '2022-07-15']     
  


fys=pd.DataFrame([fy1,fy2,fy3,fy4,fy5,fy6,fy7,fy8,fy9,fy10,fy11],columns=['fy','st_date','end_date',])


fys['st_date']=pd.to_datetime(fys['st_date'])
fys['end_date']=pd.to_datetime(fys['end_date'])


for index, rows in fys.iterrows():
    for index1 , rows1 in file_df.iterrows():
        m_date=rows1[1]
    
        #print (type (pd.to_datetime(rows)))
        st_date=rows[1]
        end_date=rows[2]
        
        if st_date< m_date <end_date:
            print ('matched',st_date,m_date,end_date,rows[0])
            #replacing value with loc method
            file_df.loc[index1,'FY']=rows[0]
            #iloc can be used wo query only not replace values
            #file_df.iloc[index1][2]=rows[0]
        else:
            print ("")
            #file_df.iloc[index1]['FY']=None
            #print (rows1[0],m_date,st_date, end_date)
            
    

