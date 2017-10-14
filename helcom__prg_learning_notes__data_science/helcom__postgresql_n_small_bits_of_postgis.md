# { learning : PostgreSQL and Postgis Notes ( with python )}
##### ( started : 20151227 )

-----------
## learning resources
------------------

##### postgis manual :
http://postgis.net/docs/

##### postgresql and postgis installation ( and few useful commands )
http://morphocode.com/how-to-install-postgis-on-mac-os-x/

##### general list of postgreSQL tutorials
https://wiki.postgresql.org/wiki/PostgreSQL_Tutorials

##### postgresql tutorial - tutorialspoint
http://www.tutorialspoint.com/postgresql/postgresql_and_or_clauses.htm

##### quick guide & list of commands - postgresql - tutorialspoint
http://www.tutorialspoint.com/postgresql/postgresql_quick_guide.htm

##### python psql interfacing library tutorial
https://wiki.postgresql.org/wiki/Psycopg2_Tutorial



##### postGIS overview - good with overivew and some comamnds, but depends on a bit of GUI thingies… 
http://workshops.boundlessgeo.com/postgis-intro/

##### GOOD, I suppose
##### postGIS tutorial - good for a lot of things - including postGIS specific thingies!
http://revenant.ca/www/postgis/workshop/

##### postGIS DEV MANUAL
http://postgis.net/docs/


##### loading a shape file into postgres
http://gis.stackexchange.com/questions/110854/importing-shp-to-postgresql



## postgresql
------------------------------

### ;;;;;; DON'T FORGET THE SEMI-COLON! at the end of each line ;;;;;;  ###


#### find the version 
    SELECT version;


#### get help
    \h


#### quit
    \q 

#### Create database
    CREATE DATABASE databasename;
( there are some options too, outlined on this page… http://www.tutorialspoint.com/postgresql/postgresql_create_database.htm )

#### Delete database
    DROP DATABASE datbasename;

#### connect to a database
\connect databsename

#### list all databases 
    > \l   OR   \list
##### list all databases and their sizes
    > \l+

##### lists all tables in the current database 
    \dt

##### show columns in the curren table
    \t

##### describe the table columns
    \t+

##### get column names from table 
    \d+ table_name;

#### comments, look like this : 
    -- comment text


### data types : 
    - varchar(80) << characters, up to 80 chars
    - int << int
    - real << single precision floating numbers
    - date << dates
    - smallint
    - double precision
    - char(n)
    - varchar(n),
    - time
    - timestamp
    - interval
    - point << for geographic references


#### CREATE TABLE 
    CREATE TABLE weather (
        city            varchar(80),
        temp_lo         int,           -- low temperature
        temp_hi         int,           -- high temperature
        prcp            real,          -- precipitation
        date            date
    );


#### CREATE TABLE - part 2 : 
    CREATE TABLE cities (
        name            varchar(80),
        location        point
    );

#### CREATE TABLE - part Helcom data:
    > CREATE TABLE week_41( 
    	timestamp_pretty varchar(40),
    	mmsi int,  
      imo int,
    	shipType varchar(20),
    	lat double precision,
    	long double precision,
    	month int,
      week int 
    );


#### CREATE A NEW TABLE BY C-O-P-Y-I-N-G from other table
    > CREATE TABLE ais_weeks_copy_test AS SELECT * FROM ais_weeks LIMIT 10;
    SELECT 10
    postgis_test=# select * from ais_weeks_copy_test ;
      timestamp_pretty   |   mmsi    |   imo   | shiptype  |    lat    |   long    | week | month 
    ---------------------+-----------+---------+-----------+-----------+-----------+------+-------
     01/01/2014 00:00:05 | 220234000 | 9130808 | TANKER    |  58.03327 | 18.254667 |    1 |     1
     01/01/2014 00:00:12 | 276297000 | 8711760 | TANKER    | 59.329166 | 24.046167 |    1 |     1
     01/01/2014 00:00:12 | 311996000 | 9316294 | CARGO     | 59.353794 | 24.043749 |    1 |     1
     01/01/2014 00:00:15 | 566904000 | 9635755 | TANKER    |  54.78683 |  12.76512 |    1 |     1
     01/01/2014 00:00:23 | 636015187 | 9482574 | TANKER    | 54.673595 | 14.172838 |    1 |     1
     01/01/2014 00:00:24 | 305694000 | 9454230 | CARGO     |  54.41631 |  10.21397 |    1 |     1
     01/01/2014 00:00:26 | 220609000 | 9327475 | TANKER    | 55.744335 |   12.6445 |    1 |     1
     01/01/2014 00:00:28 | 245689000 | 9266413 | TANKER    | 57.691326 | 11.871054 |    1 |     1
     01/01/2014 00:00:28 | 265698740 | 9616125 | PASSENGER | 55.865463 | 12.825347 |    1 |     1
     01/01/2014 00:00:29 | 636015187 | 9482574 | TANKER    | 54.673737 | 14.172098 |    1 |     1
    (10 rows)


#### CREATE DATA BY _COPY_ing from table data : 
> http://stackoverflow.com/questions/1745105/postgres-dump-of-only-parts-of-tables-for-a-dev-snapshot
> http://www.postgresql.org/docs/8.4/interactive/sql-copy.html





#### DELETE TABLE
------------------------------
    > DROP TABLE cities;



### INSERT VALUES
------------------------------

##### into the weather table
    > INSERT INTO weather VALUES ( 'San Francisco', 46, 50, 0.25, '1994-11-27');
##### and into the cities table
    > INSERT INTO cities VALUES ('San Francisco', '(-194.0, 53.0)');

##### alternative ways of adding the data more explicitly 
##### - maybe easier for keeping an overview of what goes where
##### 
    > INSERT INTO weather (city, temp_lo, temp_hi, prcp, date)
        VALUES ('San Francisco', 43, 57, 0.0, '1994-11-29');
##### also allowing for a different data order
    > INSERT INTO weather (date, city, temp_hi, temp_lo)
        VALUES ('1994-11-29', 'Hayward', 54, 37);


#### COPY values from a file
##### eg
    COPY weather FROM '/user/miska/psql/weather.txt';
##### or more realistically ( including a CSV & HEADER designation and )
    > COPY cities5 from '/Users/miska/Documents/prg2/web_coding/javascript/d3/d3_tests/testdata/cities.csv' delimiter ',' CSV HEADER;
##### and for the HELCOM DATA 
    > COPY week_41 from '/Users/miska/Documents/open_something/helcom/_helcom_projects/helcom__SCOPE__ais_explorer/helcom_data/HELCOM_AIS_data__20150720/new_AIS_data_20150825/data_2014_scope_week_41_.csv' DELIMITER ',' CSV HEADER;


#### COPY several lines of values at once
##### [[note]] the comma after every values line…
    > INSERT INTO weather (city, temp_lo, temp_hi, prcp, date)
        VALUES ('San Francisco', 43, 57, 0.0, '1994-11-29'),
        VALUES ('New York', 56, 89, 2.0, '1994-11-29'),
        VALUES ('Savannah', 12, 22, 3.0, '1994-11-29');


#### COPY 2 
##### make a new table BASED ON the results of a search
#####   ( and only make it the first 10 lines… )
    > SELECT * INTO new_table_ FROM existing_table LIMIT 10;

##### copy only one column ( geom ) into a new table
    > select geom into april2014shpfile_minimal from april2014shapefile;


#### INSERT data into table from another table ( or the same table? )

##### ( do note that the the specification of output/input col names works as with functions. the names are important, but not that they're the same colnames between the different tables. So you can choose to insert only particular values ( eg. point values ) into one table, from particular columns in a different table )
    > INSERT INTO table_name ( output_table_col_name_1, output_table_col_name2, output_table_col_name3 ) SELECT source_table_name, input_field_name1, inputfield_name2, inputfield_name3 ;



#### UPDATE :  Change rows of data 
------------------------------
##### eg. make a point of some existing table data
    > UPDATE ais_test3 SET point_data = GeomFromEWKT('SRID=3035;POINT(' || ais_test3.lat || ' ' || ais_test3.long || ')');
##### OR OR OR OR OR OR 
    > UPDATE ais_test3 SET point_data SST_SetSRID( ST_MakePoint( lat, long), 3035);

#### UPDATE - PART 2 : 

##### Change rows of data


#### ADD COLUMN 
#####   ( in this case a date column )
    > ALTER TABLE ais_weeks_test5_w_loc_col ADD COLUMN timestamp_postgresql timestamp ;


### CONVERT DATE into postgresql date format
#####   - from what's in a text string to a postgresql date

##### about postgresql dates 
http://www.techonthenet.com/postgresql/functions/to_timestamp.php
http://www.postgresql.org/docs/8.1/static/functions-formatting.html

##### single date 
    > SELECT to_timestamp( '02/01/2014 15:39:34', 'DD/MM/YYY HH24:MI:SS' );
          to_timestamp      
    ------------------------
     2014-01-02 15:39:34+02
    (1 row)
    ##### 
##### update dates in a table 
    > UPDATE ais_weeks_test5_w_loc_col SET timestamp_postgresql = to_timestamp( timestamp_pretty, 'DD/MM/YYY HH24:MI:SS' );



### QUERYING a table
------------------------------

##### get it all
    SELECT * from weather;
##### or specify what you want 
    SELECT city, temp_lo, temp_hi, prcp, date FROM weather;

##### you can also write expression in the query 
    SELECT city, (temp_hi+temp_lo)/2 AS temp_avg, date FROM weather;
##### AS is used to relabel the column… - it is otherwise optional ( but still nice )

##### more queries - AND as well as higher/lower
    SELECT * FROM weather WHERE city = 'San Francisco' AND prcp > 0.0;

##### more queries - sorting
    SELECT * FROM weather ORDER BY city, temp_lo;

##### find and remove duplicate rows
    SELECT DISTINCT city FROM weather; 

##### find distinct values
    > SELECT DISTINCT 
    >  column_1
    > FROM table_name


### Analyses
------------------------------

##### sum()
    > SELECT Sum(popn_total) AS population From nyc_census_blocks;
    ##### ( 'population' merely sets the column name )

     population 
    ------------
        8175032
    (1 row)

##### building on the above - FILTER RESULTS - find only people who live in The Bronx
    > postgis_test2=# SELECT Sum(popn_total) AS population FROM nyc_census_blocks WHERE boroname = 'The Bronx';
     population 
    ------------
        1385108
    (1 row)

##### and then do some MORE CALCULATIONS 
##### - find the percentage of white to black people per neighbourhood
    > SELECT boroname, 100*Sum( popn_white)/Sum(popn_total) as white_pct FROM nyc_census_blocks GROUP BY boroname;
       boroname    |    white_pct     
    ---------------+------------------
     Brooklyn      | 42.8011737932687
     Manhattan     | 57.4493039480463
     The Bronx     | 27.9037446899448
     Queens        |  39.722077394591
     Staten Island | 72.8942034860154
    (5 rows)



### JOINS
------------------------------

##### allows one to combine the results of several tables where there 
##### are common references
##### eg. here the common reference is the city name in both tables, referred to as city/name in the different tables
> SELECT * FROM weather, cities WHERE CITY = name;

     city      | temp_lo | temp_hi | prcp |    date    |     name      | location  
    ---------------+---------+---------+------+------------+---------------+-----------
     San Francisco |      46 |      50 | 0.25 | 1994-11-27 | San Francisco | (-194,53)
     San Francisco |      46 |      50 | 0.25 | 1994-11-27 | San Francisco | (-194,53)
     San Francisco |      46 |      50 | 0.75 | 1994-11-27 | San Francisco | (-194,53)

#### DO NOTE ABOUT THE ABOVE, that not all columns are listed, so this 
##### 		needs to be done explicitly : 

    > SELECT city, temp_lo, temp_hi, prcp, date, location FROM weather, cities WHERE city = name;

         city      | temp_lo | temp_hi | prcp |    date    | location  
    ---------------+---------+---------+------+------------+-----------
     San Francisco |      46 |      50 | 0.25 | 1994-11-27 | (-194,53)
     San Francisco |      46 |      50 | 0.25 | 1994-11-27 | (-194,53)
     San Francisco |      46 |      50 | 0.75 | 1994-11-27 | (-194,53)
    (3 rows)

#### the above query can also be written, with more explicit references to the various tables, like so:
    > SELECT weather.city, weather.temp_lo, weather.temp_hi,
       weather.prcp, weather.date, cities.location
    FROM weather, cities
    WHERE cities.name = weather.city;

          city      | temp_lo | temp_hi | prcp |    date    | location  
    ---------------+---------+---------+------+------------+-----------
     San Francisco |      46 |      50 | 0.25 | 1994-11-27 | (-194,53)
     San Francisco |      46 |      50 | 0.25 | 1994-11-27 | (-194,53)
     San Francisco |      46 |      50 | 0.75 | 1994-11-27 | (-194,53)
    (3 rows)



### AGGREGATE FUNCTIONS
------------------------------
#####   eg. functions that consider a whole bunch of data and return a result

##### eg. find the max temperature in temp_lo
    > SELECT max( temp_lo ) FROM weather;

     max 
    -----
      46
    (1 row)

##### - …and, in the above, if we explicitly wanted to name the cities… 
    > SELECT city FROM weather WHERE temp_lo = (SELECT max(temp_lo) FROM weather);

         city      
    ---------------
     San Francisco
     ( 1 row)


### GROUPING
------------------------------

##### BUT… if we wanted to know the city and temperature of the above,
##### based on each individual city… 
    > SELECT city, max(temp_lo) FROM weather GROUP BY city;

         city      | max 
    ---------------+-----
     Hayward       |  45
     San Francisco |  46
    (2 rows)


### FURTHER FILTERING 
------------------------------
#####   building on the above, using HAVING

    > SELECT city, max(temp_lo)
        FROM weather
        WHERE city LIKE 'S%'(1)
        GROUP BY city
        HAVING max(temp_lo) < 40;


### Operations on the results
------------------------------

##### eg. get the length of the names
    > SELECT char_length(name), name FROM nyc_neighborhoods;

##### AND the above, for only WHERE boroname = 'Brooklyn':
    > SELECT char_length(name), name FROM nyc_neighborhoods WHERE boroname = 'Brooklyn';

               name           | char_length 
    --------------------------+-------------
     Bensonhurst              |          11
     Bay Ridge                |           9
     Boerum Hill              |          11
     Cobble Hill              |          11
     Downtown                 |           8
     Sunset Park              |          11
     Borough Park             |          12
     East Brooklyn            |          13
     Flatbush                 |           8
     Park Slope               |          10
     Williamsburg             |          12
    etc… 

##### AND AND - you can also do arthimetic (and other) operations on the results
##### … eg. adding the length of the name with itself
    > SELECT char_length(name)+char_length(name), name FROM nyc_neighborhoods WHERE boroname = 'Brooklyn';



##### Finding the ships around Copenhagen
    > FROM week_41 WHERE lat > 55.6 AND lat < 55.9 AND long > 12.5 AND long < 12.58 ;


### UPDATE rows, wiht the UPDATE command
    > UPDATE weather SET temp_hi = temp_hi - 2, temp_lo = temp_lo - 2 WHERE date > '1994-11-28';

##### Documentation on updating large tables in postgresql
> http://blog.codacy.com/2015/05/14/how-to-update-large-tables-in-postgresql/#gs.LpuZKT0


### count the number of matches
------------------------------
    > SELECT count(*) FROM databaseName ; 
##### or
    postgis_test=# SELECT count(*) FROM week_41;
      count  
    ---------
     5497106
    (1 row)

##### also in practice… yste
    > SELECT count(*) FROM week_41 WHERE lat > 55.6 AND lat < 55.9 AND long > 12.5 AND long < 12.58 ;
     count 
    -------
     11441
    (1 row)




### FIND THE SIZE OF DATABASES
------------------------------

    > \l+


         Name     | Owner | Encoding |   Collate   |    Ctype    | Access privileges |  Size   | Tablespace |                Description                 
    --------------+-------+----------+-------------+-------------+-------------------+---------+------------+--------------------------------------------
     miska        | miska | UTF8     | en_US.UTF-8 | en_US.UTF-8 |                   | 11 MB   | pg_default | 
     postgis_test | miska | UTF8     | en_US.UTF-8 | en_US.UTF-8 |                   | 489 MB  | pg_default | 
     postgres     | miska | UTF8     | en_US.UTF-8 | en_US.UTF-8 |                   | 6620 kB | pg_default | default administrative connection database
     template0    | miska | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/miska         +| 6497 kB | pg_default | unmodifiable empty database
                  |       |          |             |             | miska=CTc/miska   |         |            | 
     template1    | miska | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/miska         +| 6505 kB | pg_default | default template for new databases
                  |       |          |             |             | miska=CTc/miska   |         |            | 


## Find the tables in the current database and their size
------------------------------

    > \d+
                                      List of relations
     Schema |             Name             |   Type   | Owner |    Size    | Description 
    --------+------------------------------+----------+-------+------------+-------------
     public | geography_columns            | view     | miska | 0 bytes    | 
     public | geometry_columns             | view     | miska | 0 bytes    | 
     public | nyc__subway_stations         | table    | miska | 120 kB     | 
     public | nyc__subway_stations_gid_seq | sequence | miska | 8192 bytes | 
     public | nyc_census_blocks            | table    | miska | 13 MB      | 
     public | nyc_census_blocks_gid_seq    | sequence | miska | 8192 bytes | 
     public | nyc_census_sociodata         | table    | miska | 264 kB     | 
     public | nyc_homicides                | table    | miska | 504 kB     | 
     public | nyc_homicides_gid_seq        | sequence | miska | 8192 bytes | 
     public | nyc_neighborhoods            | table    | miska | 200 kB     | 
     public | nyc_neighborhoods_gid_seq    | sequence | miska | 8192 bytes | 
     public | nyc_streets                  | table    | miska | 4208 kB    | 
     public | nyc_streets_gid_seq          | sequence | miska | 8192 bytes | 
     public | raster_columns               | view     | miska | 0 bytes    | 
     public | raster_overviews             | view     | miska | 0 bytes    | 
     public | spatial_ref_sys              | table    | miska | 3216 kB    | 
    (16 rows)





