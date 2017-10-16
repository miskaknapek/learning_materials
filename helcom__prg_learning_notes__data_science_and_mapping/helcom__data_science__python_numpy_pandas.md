#{ helcom : prg notes : data science session } 
####( started : 20150721 )
————————————


###To learn:
————————
- 30 mins each: 
- Python for data analysis bits 

- Python:
	- numpy
	- sci py
	- pandas
- Databases
	- PostGRES - postGIS
	- rethinkDB
	- couchDB
- Server processing
	- Apache Spark




————————————————————————

## Numpy
———————


### read csv 
( from http://stackoverflow.com/questions/25614749/

    how-to-import-csv-file-as-numpy-array-in-python )

#### one way:
    csv = np.genfromtxt ('file.csv', delimiter=",")

#### another way
second, third = loadtxt('data.csv', delimiter=',', usecols=(1,2), unpack=True, dtype=int)

### also some experiments in using the csv kit, together with numpy, to load csv files faster
( http://stackoverflow.com/posts/28554340/revisions )

( from Rickard )
    import csv
    import numpy as np
    with open(dest_file,'r') as dest_f:
        data_iter = csv.reader(dest_f, 
                               delimiter = delimiter, 
                               quotechar = '"')
        data = [data for data in data_iter]
    data_array = np.asarray(data, dtype = <whatever options>)  


    numpy.array << for converting standard python arrays, lists, typles, etc… into a numpy friendly format.

    numpy.asarray << another way of incorporating input into an ndarray

    arange << range

###### dtypes… suggests what kind of data type is in the array, etg. 
    one = numpy.array( [1,2,3], dtype=numpy.float64 )
    one.dtype >> dtype(“float64”)
    # retype
    one.astype( numpy.float32 )

##### for strings … which can be converted to floats
    one = numpy.array( [ “1.24”, “-9.6”, “42” ], dtype=numpy.string_ )

### you can do arthumetic operations on the arrays- eg. one-one, one * 2, one * two, etc… 

#### copying
    two = one[0].copy()

####slicing
- regular python slicing -> one[5:8]
- fill the whole array with the same value:

    one = numpy.arange( 10 )
    one[:] = 64 >>> array([64, 64, 64, 64, 64, 64, 64, 64, 64, 64])

####advanced slicing
    one = numpy.array( [ [ 1, 2, 3], [4, 5, 6], [7, 8, 9] ] )
    one[:,0:1]
    Out[16]: 
    array([[1],
           [4],
           [7]])
    #  [ a:b, c:d ]
    # a+b refer to the first dimension
    # c+d refer to the second dimension
    # and if there was another dimension, it would be defined by characters in the e+f positions… 

#### boolean indexing
#### you can do true/false comparison! 
    eg. with names
    names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
    In [46]: names == "Bob"
    Out[46]: array([ True, False, False,  True, False, False, False], dtype=bool)
    # the evaluated array can be passed as an index to another array
    In [84]: data = np.random.randn(7, 4)
    In [86]: data Out[86]: array([[-0.048 , 0.5433, -0.2349, 1.2792],
    [-0.268 , 0.5465, 0.0939, -2.0445], [-0.047 , -2.026 , 0.7719, 0.3103], [ 2.1452, 0.8799, -0.0523, 0.0672], [-1.0023, -0.1698, 1.1503, 1.7289],

    In [47]: data = np.random.randn(7, 4)
    In [48]: data[ names == "Bob" ]
    Out[48]: 
    array([[-0.48848304, -1.21884081,  0.89777396, -0.19064664],
           [-0.87763245, -0.02754977, -1.53655161, -0.24805539]])
    # IE: the matching values in the [ names == “Bob” ] array act as an index to the data array
    ## One can also make data masks using comparisons… 
    In [50]: mask = (names == "Bob") | (names == "Will")
    In [51]: mask
    Out[51]: array([ True, False,  True,  True,  True, False, False], dtype=bool)
    In [52]: data[ mask ]
    Out[52]: 
    array([[-0.48848304, -1.21884081,  0.89777396, -0.19064664],
           [ 1.41573894, -0.62078495, -1.70736132,  0.01976631],
           [-0.87763245, -0.02754977, -1.53655161, -0.24805539],
           [-0.62873389, -0.39659624,  0.10583516,  1.11040612]])
    ## data masks and if statements can be used to set values… eg.
    In [53]: data[ data < 0 ] = 0
    In [54]: data
    Out[54]: 
    array([[ 0.        ,  0.        ,  0.89777396,  0.        ],
           [ 0.        ,  1.52788136,  0.        ,  0.23923008],
           [ 1.41573894,  0.        ,  0.        ,  0.01976631],
           [ 0.        ,  0.        ,  0.        ,  0.        ],
           [ 0.        ,  0.        ,  0.10583516,  1.11040612],
           [ 0.54265984,  2.09874934,  0.00389728,  0.12745381],
           [ 1.75777929,  0.        ,  0.73935569,  0.        ]])

    # the data masks can also be used for setting arrays in a different way… 
    In [55]: data[names != "Joe"] = 7
    In [56]: data
    Out[56]: 
    array([[  7.00000000e+00,   7.00000000e+00,   7.00000000e+00,
              7.00000000e+00],
           [  0.00000000e+00,   1.52788136e+00,   0.00000000e+00,
              2.39230084e-01],
           [  7.00000000e+00,   7.00000000e+00,   7.00000000e+00,
              7.00000000e+00],
           [  7.00000000e+00,   7.00000000e+00,   7.00000000e+00,
              7.00000000e+00],
           [  7.00000000e+00,   7.00000000e+00,   7.00000000e+00,
              7.00000000e+00],
           [  5.42659842e-01,   2.09874934e+00,   3.89727932e-03,
              1.27453808e-01],
           [  1.75777929e+00,   0.00000000e+00,   7.39355691e-01,
              0.00000000e+00]])
    ## you can append a list of rows/bits of other arrays, to include
    In [59]: data = numpy.empty( (8,4) )
    In [60]: for i in xrange( 8 ):
       ....:     data[i] = i
    In [61]: data
    Out[61]: 
    array([[ 0.,  0.,  0.,  0.],
           [ 1.,  1.,  1.,  1.],
           [ 2.,  2.,  2.,  2.],
           [ 3.,  3.,  3.,  3.],
           [ 4.,  4.,  4.,  4.],
           [ 5.,  5.,  5.,  5.],
           [ 6.,  6.,  6.,  6.],
           [ 7.,  7.,  7.,  7.]])

    In [62]: data[ [7,6,5] ]
    Out[62]: 
    array([[ 7.,  7.,  7.,  7.],
           [ 6.,  6.,  6.,  6.],
           [ 5.,  5.,  5.,  5.]])
    # this also works with negative indicies, to select things from the end
    In [63]: data[ [-1,-2,-3] ]
    Out[63]: 
    array([[ 7.,  7.,  7.,  7.],
           [ 6.,  6.,  6.,  6.],
           [ 5.,  5.,  5.,  5.]])


#### Reshaping
    arr.T  # << reshaping


### Universal functions : fast element-wise array functions
### - they perform element wise operations on data in ndarrays
### eg.
    arr = numpy.arange( 10 );
    numpy.sqrt( arr )
    numpy.exp(arr)
    # generate arrays of random values
    x = numpy.random.rand( 8 )
    y = numpy.random.rand( 8 )
    numpy.maximum( x, y) # get/find the max values of the two arrays, in a single array
    # various ufuncts
    - sign << suggest whether the value is negative ( -1 ), zero ( 0 ), or positive ( 1 )
    - logical_not
    - add
    - subtract
    - multiply
    - divide, floor_divide
    - maximum & fmax ( the latter ignores NaN )
    - minimum & fmin ( the latter ignores NaN )
    - copysign
    - greater, greater_than, less, less_equal, equal, not_equal
    - logical_and, logical_or, logical_xor
    + the usual suspects - 




————————————————————————

## Pandas
———————

“””
Built on top of numpy.
“””

#### resources >>> at the bottom 
------------


#### overview a dataframe
dataframe.describe()


#### quick intro to Pandas datatypes
http://blog.mathandpencil.com/introduction-to-pandas-data-structures/
#### Safari Books online : Python Data Science Handbook ( which you also have a pdf )
https://www.safaribooksonline.com/library/view/python-data-science/9781491912126/ch04.html



### Pandas - load data! 

#### basically 

df = pd.read_csv("/Users/miska/Documents/creative/backup_of_works/helcom_work/shipping_lists/data/compiled_shipping_list__via_python_01.csv", sep=";" )


### Pandas - data structures - Series and DataFrame

#### Series
A one-dimensional array-like object, and an associated array of labels, called its Index.
obj = Series([4,7,-5,3])

#### Index 
#### index for the array series data. The default is the [ 0 -> N-1 ] one of arrays.
    obj.index
    Out[7]: Int64Index([0, 1, 2, 3], dtype='int64')
    # a named index can also be accomplished
    obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
    In [12]: obj2['a']
    Out[12]: -5
    In [13]: obj2.index
    Out[13]: Index([u'd', u'b', u'a', u'c'], dtype='object')
    # produce a list of indicies
    In [14]: obj2[['a', 'c', 'd']]
    Out[14]: 
    a   -5
    c    3
    d    4
    dtype: int64

#### numpy operations, such as filtering with a boolean array, scalar multiplicatin, or applying math operations withh preserve the index link, eg…
    In [15]: obj2[ obj2 > 0 ]
    Out[15]: 
    d    4
    b    7
    c    3
    dtype: int64

#### you can make a Series object, with an Index, 
#### using Pandas
    In [18]: one['one']
    Out[18]: 1

    In [19]: obj3 = Series( one )

    In [20]: obj3['one']
    Out[20]: 1

    In [21]: obj3
    Out[21]: 
    one      1
    three    3
    two      2
    dtype: int64

#### isnull can be used to identify missing data
    In [37]: pd.isnull(obj4)
    Out[37]: 
    California    True
    Ohio          True
    Oregon        True
    Texas         True
    dtype: bool

#### importantly, Series automatically realigns differently indexed data.

#### the object and the index may have names (!)
    In [38]: obj4.name = 'population'
    In [39]: obj4.index.name = 'state'


### Data Frames
 tabular, spreadsheet like data structure, containing an ordered collection of columns
 each of which can be of a different value type!
 the data frame has both a row and a column index 
 can be thought of as a dict of Series 
 unlike other data frame operations in other languages, eg. R’s data.frame 
 operations in DataFrame are treated roughly symmetrically. 
 under the hood the data is stored as one or more two-dimensional blocks,
 rather than as a list, dict or other collection of one-dimensional arrays.


#### constructing DataFrames
 usually a Data Frame is constructed of similarly length’ed 
 arrays, dict-styled…a bit like javascript arrays…
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002], 'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    frame = DataFrame(data)
    In [37]: frame Out[37]:
    pop state year
    	.	0  1.5 Ohio 2000 
    	.	1  1.7 Ohio 2001 
    	.	2  3.6 Ohio 2002 
    	.	3  2.4 Nevada 2001 
    	.	4  2.9 Nevada 2002 

####You can also specify a listing of the data frame in a different order:
    In [38]: DataFrame(data, columns=['year', 'state', 'pop']) Out[38]:
    year state pop 0 
    2000 Ohio 1.5 1 
    2001 Ohio 1.7 2 
    2002 Ohio 3.6 3 
    2001 Nevada 2.4 4 
    2002 Nevada 2.9
    # the above can also be used to specify a different array order…
    frame2.year
    frame2[ ‘state’ ] 

#### data can be indexed by both the column name
#### as well as the various row values, eg

    In [58]: frame2.year[0]
    Out[58]: 2000

    In [59]: frame2.year.three
    Out[59]: 2002

    In [60]: frame2.year['three']
    Out[60]: 2002

#### setting all values
    In [45]: frame2['debt'] = 16.5
    In [46]: frame2
    Out[46]: year
    one 2000 two 2001 three 2002 four 2001 five 2002
    state pop debt Ohio 1.5 16.5 Ohio 1.7 16.5 Ohio 3.6 16.5
    Nevada 2.4 16.5 Nevada 2.9 16.5

    In [72]: frame2['debt'] = numpy.arange(5)
    In [73]: frame2
    Out[73]: 
           year   state  pop  debt
    one    2000    Ohio  1.5     0
    two    2001    Ohio  1.7     1
    three  2002    Ohio  3.6     2
    four   2001  Nevada  2.4     3
    five   2002  Nevada  2.9     4

#### assigning a column name that doesn’t exist creates it

    In [75]: frame2['eastern'] = frame2.state == 'Ohio'

    In [76]: frame2
    Out[76]: 
           year   state  pop  debt eastern
    one    2000    Ohio  1.5     0    True
    two    2001    Ohio  1.7     1    True
    three  2002    Ohio  3.6     2    True
    four   2001  Nevada  2.4     3   False
    five   2002  Nevada  2.9     4   False

#### and one can remove a column rather easily

##### show columns!
    In [116]: data.columns
    Out[116]: 
    Index([u'timestamp_pretty', u'mmsi', u'imo', u'shipType', u'lat', u'long',
           u'month', u'week'],
          dtype='object')

##### get whole lines
    data.values
    #etc
    data.values[0]


#### viewing data : head/tails
    > df.head()
    > df.tail()

#### display the index
    > df.index

#### display the columns
    > df.columns
#### change the columns name
    > df.columns = list(‘ABCD’)
    > df.columns = [ “A”, “B”, “C”, “D” ]

#### describe - get summary statistics
    > df.describe()

#### transpose
    > df.T

#### SORTING

##### by axis
    > df.sort_index( axis=1, ascending=False )

##### one can only do data[ 0 ] / data[ N ] … if there is no labelled index



### indexing and slicing 

#### accessing arrays by row num = 
    > df.loc[ 0 ]

#### and labels… 
    > df.loc[ 0:10, [‘one’, ‘two’] ]
    # all rows, but with only some columns
    > df.loc[:, [‘one’, ‘three’ ]

#### fast access to a scalar
    > df.iat[1,1]

#### get a column by its label name
    > df[‘A’]

#### by a date range 
    > df[‘20130102’ : ‘20130104’ ]

#### indata
    In [147]: data
    Out[147]: 
              one  two  three  four
    Ohio        0    1      2     3
    Colorado    4    5      6     7
    Utah        8    9     10    11
    New York   12   13     14    15

#### sort the columns by their names
    > df.sort_index( axis=1, ascending=False )

#### sort by a particular column:
    df.sort( columns=‘B’ )

#### filtering
    In [143]: data[ data['one']> 2 ]
    Out[143]: 
              one  two  three  four
    Colorado    4    5      6     7
    Utah        8    9     10    11
    New York   12   13     14    15

#### a different way
    In [148]: data > 2
    Out[148]: 
                one    two  three  four
    Ohio      False  False  False  True
    Colorado   True   True   True  True
    Utah       True   True   True  True
    New York   True   True   True  True

#### filtering
    In [156]: data < 5
    Out[156]: 
                one    two  three   four
    Ohio       True   True   True   True
    Colorado   True  False  False  False
    Utah      False  False  False  False
    New York  False  False  False  False

#### filtering && assigning 
    In [157]: data[ data < 5 ] = 0

    In [158]: data
    Out[158]: 
              one  two  three  four
    Ohio        0    0      0     0
    Colorado    0    5      6     7
    Utah        8    9     10    11
    New York   12   13     14    15



##### logical operations in pandas 
    data[ (data['lat']>58) & (data['lat']<59 ) ].shape




### DATE+TIME operations
##

#### Create a Dates range ( using np.date_range() )
    > dates = pd.date_range('20130101', periods=6)
    > dates
    > DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
                   '2013-01-05', '2013-01-06'],
                  dtype='datetime64[ns]', freq='D', tz=None)

#### Create a dataframe with the dates above as an index, with some random data
#### and with some column indicies ( “ABCD”)
    > df = pd.DataFrame( np.random.randn(6,4), index=dates, columns=list('ABCD'))
    > df
    >                    A         B         C         D
    2013-01-01 -1.897977 -0.231252 -0.675079  0.974813
    2013-01-02  0.175409 -0.882461 -0.006945  0.487286
    2013-01-03 -0.881586  1.343007 -0.082846  1.004065
    2013-01-04 -0.840608 -0.275904 -1.676580 -1.263626
    2013-01-05  0.842908 -0.885889  0.661107 -0.608904
    2013-01-06  1.221979  1.101137 -0.637204 -0.595021


#### combine data frames, as a sort of dictionary
    > one = pd.Series( np.arange(10), index=['a','b','c','d','e','f','g','h','i','j'] )
    > two = pd.Series( np.arange(10,20), index=one.index )
    > three = pd.DataFrame( { ‘one’ : one, ‘two’ : two } )

#### delete column
    > del df[‘one’]
    > pop df[‘one’]


#### basic indexing + selection rules
    Operation
    Syntax
    Result
    Select column
    df[col]
    Series
    Select row by label
    df.loc[label]
    Series
    Select row by integer location
    df.iloc[loc]
    Series
    Slice rows
    df[5:10]
    DataFrame
    Select rows by boolean vector
    df[bool_vec]
    DataFrame



------------ 

### various pandas resources 

------------

##### quick intros & tutorials 
———————————

Pydata : 10 minutes to Pandas
https://pandas.pydata.org/pandas-docs/stable/10min.html

———————————

#### Connecting Pandas with SQL
http://pandas.pydata.org/pandas-docs/stable/io.html#io-sql


———————————

#### Relational databases ( sql )

———————————

#### Pandas <-> SQL
http://pandas.pydata.org/pandas-docs/stable/io.html#io-sql

####Load data into a post-gre 
#### resources:
http://www.kevfoo.com/2012/01/Importing-CSV-to-PostGIS/
http://gis.stackexchange.com/questions/82782/import-large-csv-file-into-postgis
#### postgresql sql intro
http://www.postgresql.org/docs/9.4/interactive/tutorial-join.html


#### Intersection tips from Jan
##### using Gdal
https://pcjericks.github.io/py-gdalogr-cookbook/geometry.html
##### using PostGIS
http://gis.stackexchange.com/questions/66253/how-to-find-the-intersection-point-of-polygon-geometry-and-multilinestring-geome


#### plotting 
———————————

##### Pandas & histograpm plotting

###### basic histogram plotting 
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.hist.html
( this also works : 

    df2['Net_tonnage'].hist(bins=100)
)

###### plotting ghistorgrams and grouping … 
https://stackoverflow.com/questions/19584029/plotting-histograms-from-grouped-data-in-a-pandas-dataframe



#### python debugging 
———————————

##### on using ipython and others for debugging 
https://stackoverflow.com/questions/16867347/step-by-step-debugging-with-ipython

##### ipython debugging info 
https://ipython.org/ipython-doc/rel-0.10.2/html/api/generated/IPython.Debugger.html

##### notes on different python debugggers 
https://stackoverflow.com/questions/893162/whats-a-good-ide-for-python-on-mac-os-x

