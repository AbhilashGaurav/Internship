
#Making all necessary imports for the code
from datetime import date
from jugaad_data.nse import bhavcopy_save
import pandas as pd
from jugaad_data.holidays import holidays
from random import randint
import time, os

# declaring the range of dates to get the bhav.csv files
# here the declared range will of 30 days 

date_range = pd.bdate_range(start='28/23/2022', end = '12/27/2022', freq='C')
                         
savepath = os.path.join('C:', os.sep,'Users','Acer','Desktop','internship','bhav_data_2022')
total_files=0                                                
# here start and end dates in "MM-DD-YYYY" format
# here holidays() function in (year,month) format
# and here freq = 'C' is for custom

list_date = [x.date() for x in date_range]

# In this we are getting all the latest as well as the declared dates bhav.csv files
for dates in list_date:
     try:
          bhavcopy_save(dates, savepath)
          total_files+=1
          print("Download successful ",total_files)
          time.sleep(randint(1,10)) #adding random delay of 1-4 seconds
     except Exception:
          print("Holiday on this day ",dates)
          pass

               