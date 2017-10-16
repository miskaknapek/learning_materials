def get_hist( df, bins=10 ):
	print( "got df of size", df.shape )

	min_ = df.min()
	max_ = df.max()

	range_ = max_-min_

	binsize = range_/bins

	#
	hist = []

	for i in range( bins ):
		bin_low = i*binsize+min_
		bin_high = bin_low+binsize
		num_of_items = df[ ( df > bin_low ) &  (df <= bin_high) ].shape[0] 
		hist.append( { 'bin_low':bin_low, 'bin_high':bin_high, "count": num_of_items })
		print("index : "+str(i)+" bin_low: "+str(bin_low)+" bin_high: "+str(bin_high)+" count : "+str(num_of_items) )



	# print( "min_ : "+str(min_)+", max_: "+str(max_)+" bin#: binsizee: " )
	## return { 'bins':bins, 'min_':min_, 'max_':max_, 'range':range, 'binsize':binsize }
	return { 'bins':bins, 'min_':min_, 'max_':max_, 'range':range, 'histogram_data' : hist }
