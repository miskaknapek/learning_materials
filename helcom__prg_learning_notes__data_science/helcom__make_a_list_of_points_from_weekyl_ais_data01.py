

"""
20160118
python script to make a list of points,
from helcom weekly data
"""


"""
general procedure

- import libraris
- read source file into pandas

- find the unique IMOs

- make an out_list.

- loop through unique IMOs

- for IMO:
	- find the points in the data related to into
	- append the list of points to the out_list

- presetn

"""


#### vars

out_list = []



###### code

import pandas as pd
import time 



## start the timer

start_time = time.time()


## open the file 

in_data = pd.read_csv("/Users/miska/Documents/open_something/helcom/_helcom_projects/helcom__SCOPE__ais_explorer/helcom_data/HELCOM_AIS_data__20150720/new_AIS_data_20150825/data_2014_scope_week_3_.csv")


# feedback 
in_data_len = len( in_data )
print "\n -- opened the input data - got "+str( in_data_len )+" num of rows ";



## find unique IMOs

unique_imos = in_data['imo'].unique();

print "\t ---- found "+str( len(unique_imos))+" num of unique imos"


## go through them and find the bit in the in data that have the imos

for curr_imo in unique_imos:
	temp_curr_imo_rows = in_data[ in_data[0:]['imo'] == curr_imo ]
	out_list.append( temp_curr_imo_rows )
	print "\t------- working on IMO "+str(curr_imo)+" (#"+str( len(out_list))+") - found "+str( len( temp_curr_imo_rows ))+" (/"+str( in_data_len)+")"


## finished? 

total_time_taken = ( time.time() - start_time ) 
print "\t ================ FINISHED - got a list of "+str( len( out_list ))+" different lines - and it took "+str( total_time_taken )+" seconds"