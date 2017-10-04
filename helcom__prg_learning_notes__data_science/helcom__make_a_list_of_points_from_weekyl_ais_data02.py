

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




###### prerequsites

import pandas as pd
import time 


def find_lines_length( in_url ):

	print ">>>> find_lines_length - starting work on url |"+in_url+"|"

	#### vars

	out_list = []


	## start the timer

	start_time = time.time()


	## open the file 

	in_data = pd.read_csv( in_url )


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


	### 
	return out_list




def create_length_list_from_lines_listing( list_of_lines_list ):

	print "\n\n >>>> create_length_list_from_lines_listing - got a inlines list of length "+str( len( list_of_lines_list ))+" - here we go :) "

	lines_len_list = []

	for item in list_of_lines_list:
		lines_len_list.append( len(item) )

	#sort
	lines_len_list.sort()

	print "--- finished! - got a a list of "+str( len( lines_len_list))+" items"
	return lines_len_list

