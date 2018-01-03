# { quickstart : python plotting : matplotlib and seabron }
##### ( started : 20171015 )
---------------------------------------


# one 

## two

### three

#### four

##### five

###### six 


## matplot lib
-------------------------------

##### example datasets

    # something something… 



## seaborn lib
-------------------------------

#### loading 
------------
    <lorem ipsum placeholder>



#### basic line plot
------------
    plt.plot( range(10 )); plt.show();
    #numpy edition : 
    plt.plot( np.arange(10) ); plt.show();

#### plot multiple (4) lines
    df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
                      columns=['A', 'B', 'C', 'D'],
                      index=np.arange(0, 100, 10))
    df.plot()



#### bar plots
------------
titanic example - column order indicates demensions in plot

    # Load data
    titanic = sns.load_dataset("titanic")

    # Set up a factorplot - with bar charts as a variety
    # - note that the order of the data columns sets the dimensions
    # of the plot. i.e. bar groups are of "class", 
    #               "survived" is the height, 
    #               "sex" the subdimension
    g = sns.factorplot("class", "survived", "sex", data=titanic, kind="bar", palette="muted", legend=False)
                       
    # Show plot
    plt.show()


*another* way of doing barplots, apparently… 
    
    sns.countplot(x="HELCOM_Detail_ShipType", data=data )



#### scatter plot
------------
    # generate 100 x/y coordinates randomly
    plt.scatter( np.random.rand(100), np.random.rand(100) )
    plt.show()

with the pokemon data - including some analysis

    sns.lmplot(x='Attack', y='Defense', data=data )
    plt.show()

more with the same data - now with colour coding but without regression line

    # Scatterplot arguments
    sns.lmplot(x='Attack', y='Defense', data=df,
               fit_reg=False, # No regression line
               hue='Stage')   # Color by evolution stage



#### boxplot
------------
still with the Pokemon data

    sns.boxplot(data = data )
    plt.show()



#### swarmplot 
( vertical bar distribution plot but with dots - excess dots are distributed horisontally )
------------

    sns.swarmplot(x="Type 1", y="Attach", data=data2, palette=plkmn_type_colors)



#### heatmap
---------

( do this first, if you want to do correlations : 

    # get correlations data 
    corr = dataFrame.cor() 

    # plot heatmap
    sns.heatmap( corr )
    plt.show()



### distribution plotting ( aga histograms )
---------

##### distributions of Attack in Pokemon 

    sns.distplot( data2.Attack ) 
    plt.show()

#### using orginary histograph function
*note:* returns histogram data as variable return data!

    plt.hist( x="Attack", data=data2)
    plt.show()

### distribution plot : *scatterplot + histogram*

    sns.jointplot(x='Attack', y='Defense', data=df)



##### saving to disk
------------
    plt.savefig('figpath.svg')

    plt.savefig('figpath.png', dpi=400, bbox_inches='tight')

    from io import BytesIO buffer = BytesIO() plt.savefig(buffer) plot_data = buffer.getvalue()



#### change visual paramaters
------------------------
change *page size*

    plt.rcParams["figure.figsize"] = [9,9]


change *line width line width* ( notice the last parameter ) 

    sns.boxplot(data = data, linewidth=0.25 )


*reference* for the *line 2d class*
https://matplotlib.org/users/pyplot_tutorial.html
possibly related : contour class properties
https://matplotlib.org/api/contour_api.html

*matplotlib: pyplot : lots of appearance api info*
https://matplotlib.org/users/pyplot_tutorial.html




#### resources : 
-------------


#### python plotting gallery 
https://python-graph-gallery.com/


##### Python Seaborn Tutorials for Beginners ( datacamp )
https://www.datacamp.com/community/tutorials/seaborn-python-tutorial

##### The Ultimate … Searborn Tutorial… 
https://elitedatascience.com/python-seaborn-tutorial



#### plot configurations

##### genreal guide to changing output from Seaborn 
https://seaborn.pydata.org/tutorial/aesthetics.html

##### changing output size 
https://stackoverflow.com/questions/31594549/how-do-i-change-the-figure-size-for-a-seaborn-plot

##### chnging font size on output
    sns.set( font_scale=0.5 )
also: 

    sns.set_context("paper", rc={"font.size":8,"axes.titlesize":8,"axes.labelsize":5})









