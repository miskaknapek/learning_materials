#{ learning : Postgis (and postgreSql) Notes ( with python )}
####( started : 20151227 )

-----------
### learning resources
------------------

#### recommended postGIS tutorial ( by the postGIS site )
http://workshops.boundlessgeo.com/postgis-intro/

#### planet GIS - community
http://gis.stackexchange.com/questions/tagged/postgis



## theoretical bits 
-----------

####  ? What is a spatial database?
- Spatial databases allow one to store and manipulate spatial objects 
as one would any other data in databases.
- Multi-dimensional spatial indexign is used for efficent processing of spatial operations.
- Spatial functions exist to process spatial properties and relationships easily


#### History
…in the beginning, there was GIS.
Early gis stored data in proprietary ways.
Later gis stored data in relational database.s
And later still, where we are now, people developed database features specifically for spatial needs.


#### Spatial data types
- everything is treated as geometry - though geometry is organised in hierarchical ways:

	- Spatial reference system
        - Geometry
        	- Point
        	- Curve
        		- Line string
        	- Surface
        		- polygon
        	- Geometry collection
        		- Multi-Surface
        			- MultiPolygon
        		- Multi-Curve
        			- Multi line string
        		- Multi-Point


#### Spatial indicies and bounding boxes
- General relational databases have various 'access methods' - aka indicies - 
to allow quick access to data. 
Indexing for standard data types ( numbers, strings, dates ) is usually done with B-tree indexes.
A b-tree partitions the data using the natural sort order to put the data into a hierarchical tree.
The natural sort order of numbers, strings, and dates are simple to determine - each values
is higher or lower than the other. 
HOWEVER, relations of spatial data is more complex - it can overlap, be contained in one another, 
and be arrayed in two (or more ) dimensional space. The standard ways of indexing features of 
'regular' relational databases, isn't entirely useful for spatial databases.

#### Spatial databases have other indexing methods,
eg. a BOUNDING BOX. 
Different spatial databases have different spatial indexes, most common is the R-tree ( used in postGIS )

#### Spatial databases have special functions for dealing with geo-data.
These typically call into the following categories:
- Conversaion : functions that convert between geometries and external data formats.
- Management : functions that manage information about spatial tables and postGIS administration.
- Retrieval : retrieve poertries and measurement of geometry.
- Comparison : functions that compare two geometries with respect to their spatial relation.
- GEeneration : functions that generate new gemoetries from others.

#### … soooo… what is postGIS?
- postGIS are a bunch of extensions, turning the relational database postgreSQL into a spatial database,
adding the possibility to use spatial types, indicies and functions. 
Thanks to building on top of postgreSQL, postGIS 'inherits' various other standard database features.

#### …why postgresSQL?
- it was built to be open, extendable, and to run new features in at run time.

-----
## practical bits
-------------------



#### setting up a postgis database
#####			… in postgresql

###### create the database
    CREATE DATABASE postgis_test2;

###### add postgis extension
#
###### step 1
    CREATE EXTENSION postgis;
###### step 2 : confirm that it exists by running a postgis function
    SELECT postgis_full_version();




------------
## coding 
-----------------------------------------------------


### Creating a spatial table! 
 Creating a table with spatial data is done in two stages:
  - Create a normal non-spatial table.
      For example: CREATE TABLE ROADS_GEOM ( ID int4, NAME varchar(25) )
  - Add a spatial column, eg… ( when using the same schema as an existing table )
    > SELECT AddGeometryColumn( 'roads_geom', 'geom', 423, 'LINESTRING', 2);
    > SELECT AddGeometryColumn( 'ais_test3', 'point_data', 3035, 'POINT', 2);



#### enter some geo data
    > INSERT INTO geometries VALUES                                                                                                              ('Point', 'POINT(0 0)'),
    ('Linestring', 'LINESTRING(0 0, 1 1, 2 1, 2 2)'),
    ('Polygon', 'POLYGON((0 0, 1 0, 1 1, 0 1, 0 0))'),
    ('PolygonWithHole', 'POLYGON((0 0, 10 0, 10 10, 0 10, 0 0),(1 1, 1 2, 2 2, 2 1, 1 1))'),
    ('Collection', 'GEOMETRYCOLLECTION(POINT(2 0),POLYGON((0 0, 1 0, 1 1, 0 1, 0 0)))');

    INSERT 0 5

#### select a postGIS FUNCTION
    > postgis_test2=# SELECT name, ST_AsText(geom) from geometries;
          name       |                           
          st_astext  |                         
    -----------------+---------------------------------------------------------
     Point           | POINT(0 0)
     Linestring      | LINESTRING(0 0,1 1,2 1,2 2)
     Polygon         | POLYGON((0 0,1 0,1 1,0 1,0 0))
     PolygonWithHole | POLYGON((0 0,10 0,10 10,0 10,0 0),(1 1,1 2,2 2,2 1,1 1))
     Collection      | GEOMETRYCOLLECTION(POINT(2 0),POLYGON((0 0,1 0,1 1,0 1,0 0)))
    (5 rows)



#### Find information about geometry tables 
    > SELECT name, ST_GeometryType(geom), ST_NDims(geom), ST_SRID(geom) FROM geometries;

          name       |    st_geometrytype    | st_ndims | st_srid 
    -----------------+-----------------------+----------+---------
     Point           | ST_Point              |        2 |       0
     Linestring      | ST_LineString         |        2 |       0
     Polygon         | ST_Polygon            |        2 |       0
     PolygonWithHole | ST_Polygon            |        2 |       0
     Collection      | ST_GeometryCollection |        2 |       0



### CREATE
-----------
#### ADD / UPDATE POINT based on existing columns
####  - i.e. use existing lat/long data to make valid postGIS POINT gemoetry 
    > UPDATE tablename SET point_column_name = ST_SetSRID( ST_MakePoint( lat_col_name, long_col_name), 3035 );

#### good documentation on this : 
http://gis.stackexchange.com/questions/24486/how-to-insert-a-point-into-postgis




### POINTS
-----------------------------------------------------
#### read point data as text…
    > SELECT ST_X(geom), ST_Y(geom) FROM geometries WHERE name = 'Point';



### LINESTRINGS

#### print linestrings
    > SELECT ST_AsText(geom) FROM geometries WHERE name = 'Linestring';

#### LINESTRING FUNCTIONS
    > ST_Length(geometry);
    > ST_StartPoint(geometry);
    > ST_EndPoint(geometry);
    > ST_NPoints(geometry);

#### eg the length of a linestring is … 
    > SELECT ST_Length( geom ) FROM geometries WHERE name = 'Linestring';
        st_length     
    ------------------
     3.41421356237309
    (1 row)

#### get the number of points in a line
    > SELECT ST_NPoints(geom) FROM geometries WHERE name = 'Linestring';
     st_npoints 
    ------------
          4
    (1 row)





### Polygons
-----------------------------------------------------

#### polygon specific FUNCTIONS
    > ST_Area(geometry) returns the area of the polygons
    > ST_NRings(geometry) returns the number of rings (usually 1, more of there are holes)
    > ST_ExteriorRing(geometry) returns the outer ring as a linestring
    > ST_InteriorRingN(geometry,n) returns a specified interior ring as a linestring
    > ST_Perimeter(geometry) returns the length of all the rings


#### print a polygon :) 
    > SELECT ST_AsText( geom ) FROM geometries WHERE name LIKE 'Polygon%';
                            st_astext                         
    ----------------------------------------------------------
     POLYGON((0 0,1 0,1 1,0 1,0 0))
     POLYGON((0 0,10 0,10 10,0 10,0 0),(1 1,1 2,2 2,2 1,1 1))
    (2 rows)

#### Please note, in the above, that
#### - the first polygon is just one polygon
#### - the second polygon has a hole in it… defined by the second group of coordinates.

#### fetch the AREA of a polygon
    > SELECT name, ST_Area(geom) FROM geometries WHERE name LIKE 'Polygon%';
          name       | st_area 
    -----------------+---------
     Polygon         |       1
     PolygonWithHole |      99
    (2 rows)




### Collections
-----------------------------------------------------


#### Collections are collections of previosuly mentioned 'primary' shapes, eg.
    > MultiPoint, a collection of points
    > MultiLineString, a collection of linestrings
    > MultiPolygon, a collection of polygons
    > GeometryCollection, a heterogeneous collection of any geometry (including other collections)


#### listing GEOMETRY COLLECTIONS
    > SELECT name, ST_AsText(geom)
    postgis_test2-#   FROM geometries
    postgis_test2-#   WHERE name = 'Collection';
        name    |                           st_astext                           
    ------------+---------------------------------------------------------------
     Collection | GEOMETRYCOLLECTION(POINT(2 0),POLYGON((0 0,1 0,1 1,0 1,0 0)))
    (1 row)


#### collections have various functions that can be applied to them

    > ST_NumGeometries(geometry) returns the number of parts in the collection
    > ST_GeometryN(geometry,n) returns the specified part
    > ST_Area(geometry) returns the total area of all polygonal parts
    > ST_Length(geometry) returns the total length of all linear parts




### INPUT / EXPORT 
-----------------------------------------------------
( from here : http://workshops.boundlessgeo.com/postgis-intro/geometries.html )

#### postGIS supports export in quite a variety of text, markup and binary formats : 
#### (including geo_json and svg )


#### EXPORTING ( and also quite similar regarding import )
    > ST_GeomFromText(text, srid) returns geometry
    > ST_AsText(geometry) returns text
    > ST_AsEWKT(geometry) returns text
    Well-known binary (WKB)
    > ST_GeomFromWKB(bytea) returns geometry
    > ST_AsBinary(geometry) returns bytea
    > ST_AsEWKB(geometry) returns bytea
    Geographic Mark-up Language (GML)
    > ST_GeomFromGML(text) returns geometry
    > ST_AsGML(geometry) returns text
    Keyhole Mark-up Language (KML)
    > ST_GeomFromKML(text) returns geometry
    > ST_AsKML(geometry) returns text
    > GeoJSON
    > ST_AsGeoJSON(geometry) returns text
    Scalable Vector Graphics (SVG)
    > ST_AsSVG(geometry) returns text



#### PRINT
-----------------------------------------------------
   - print some of the data 

> SELECT timestamp_pretty, ST_AsText( point_data ), ST_X( point_data ), ST_Y( point_data ) FROM z_ais_weeks_large_copy_w_point_col LIMIT 20;


      timestamp_pretty   |         st_astext          |   st_x    |   st_y    
    ---------------------+----------------------------+-----------+-----------
     01/01/2014 18:08:59 | POINT(55.49357 17.431643)  |  55.49357 | 17.431643
     01/01/2014 18:08:59 | POINT(57.599773 11.793926) | 57.599773 | 11.793926
     01/01/2014 18:08:59 | POINT(56.045166 12.687166) | 56.045166 | 12.687166
     01/01/2014 18:08:59 | POINT(55.7031 21.124117)   |   55.7031 | 21.124117
     01/01/2014 18:08:59 | POINT(60.47468 19.203054)  |  60.47468 | 19.203054
     01/01/2014 18:08:59 | POINT(54.466248 12.20047)  | 54.466248 |  12.20047
     01/01/2014 18:09:00 | POINT(55.481834 15.075167) | 55.481834 | 15.075167
     01/01/2014 18:09:00 | POINT(55.8585 12.833167)   |   55.8585 | 12.833167
     01/01/2014 18:09:00 | POINT(54.87151 13.31822)   |  54.87151 |  13.31822
     01/01/2014 18:09:00 | POINT(54.14101 12.096837)  |  54.14101 | 12.096837
     01/01/2014 18:09:00 | POINT(58.766884 18.838072) | 58.766884 | 18.838072
     01/01/2014 18:09:00 | POINT(54.40156 12.003034)  |  54.40156 | 12.003034
     01/01/2014 18:09:00 | POINT(59.7092 28.423058)   |   59.7092 | 28.423058
     01/01/2014 18:09:00 | POINT(56.179996 12.414701) | 56.179996 | 12.414701
     01/01/2014 18:09:00 | POINT(53.954678 14.245459) | 53.954678 | 14.245459
     01/01/2014 18:09:01 | POINT(55.492153 9.497744)  | 55.492153 |  9.497744
     01/01/2014 18:09:01 | POINT(60.012905 27.205582) | 60.012905 | 27.205582
     01/01/2014 18:09:01 | POINT(56.667828 18.205364) | 56.667828 | 18.205364
     01/01/2014 18:09:01 | POINT(54.026516 14.762584) | 54.026516 | 14.762584
     01/01/2014 18:09:01 | POINT(56.036133 12.653822) | 56.036133 | 12.653822
    (20 rows)




##### sample exercise:
#####  - find the length of streets in NYC, ordered by 
#####   the type of street:

    > SELECT type, Sum(ST_Length(geom)) AS length
    FROM nyc_streets
    GROUP BY type
    ORDER BY length DESC;

                           type                       |      length
    --------------------------------------------------+------------------
     residential                                      | 8629870.33786606
     motorway                                         | 403622.478126363
     tertiary                                         | 360394.879051303
     motorway_link                                    | 294261.419479668
     secondary                                        | 276264.303897926
     unclassified                                     | 166936.371604458
     primary                                          | 135034.233017947
     footway                                          | 71798.4878378096
     service                                          |  28337.635038596
     trunk                                            | 20353.5819826076
     cycleway                                         | 8863.75144825929
     pedestrian                                       | 4867.05032825026
     construction                                     | 4803.08162103562
     residential; motorway_link                       | 3661.57506293745
     trunk_link                                       | 3202.18981240201
     primary_link                                     | 2492.57457083536
     living_street                                    | 1894.63905457332
     primary; residential; motorway_link; residential | 1367.76576941335
     undefined                                        |  380.53861910346
     steps                                            | 282.745221342127
     motorway_link; residential                       |  215.07778911517




#### COMPARING geometry !!!
-----------------------------------------------------

 postGIS allows comparing different geometries.
 ie. seeing if they're the same, close, overlapping, etc… 


#### ST_Equals

 tests whether two geometries are the same
 - eg. check whether two shapes are similar


#### ST_Intersects, ST_Disjoint, ST_Crosses and ST_Overlaps

 ST_Intersects, ST_Crosses and ST_Overlaps test whether interiors of geometries intersect
( http://workshops.boundlessgeo.com/postgis-intro/spatial_relationships.html )


        ST_Intersects( geometry_a, geometry_b ) 
        returns true if the two shapes have any space in commong.

#### TESTING the ST_Intersects
##### - get a point
    > SELECT name, ST_AsText(geom) FROM nyc__subway_stations WHERE name = 'Broad St';
    POINT(583571 4506714)
    # - test whether the point is on the line
    > SELECT name, boroname FROM nyc_neighborhoods WHERE ST_Intersects(geom, ST_GeomFromText('POINT(583571 4506714)',26918));

            
            name        | boroname  
    --------------------+-----------
     Financial District | Manhattan
    (1 row)


##### ST_Disjoint( geometry_a, geometry_b )
##### returns true if the two gemetries don't overlap or intersect.


##### ST_Cross( geomtry_a, geometry_b )
##### returns true if the lines/polygons intersect.


##### ST_Overlap( geomtry_a, geometry_b )
##### returns true if the two geometries overlap. 


##### ST_Touches( geometry_a, geometry_b )
##### tests whether two shapes boundaries touch, but don't go inside one another.


##### ST_Contains and ST_Within (geometry_a, geometry_b)
##### both test whether the one geometry is within the other - ST_Contains if the first is within the second, ST_Within if the second is within the first


##### ST_Distance and ST_DWithin
##### ST_Distance( geometry_a, geometry_b ) calculateds the *shortest* distance between two objects.
##### ST_DWithin( geometry_a, geometry_b, radius ) calculates whether objects are within a partiuclar distance of one another.
##### EG. good to find which bits of geometry are within a particular distance of a point.

##### format : ST_DWithin( postgis_point_col_name, circle_centre_point, circle_radius )
    > SELECT count(*) FROM ais_weeks_test5_w_loc_col WHERE ST_DWithin( point_loc, ST_SetSRID( ST_MakePoint( 12, 55 ), 3035), 1 );
     count 
    -------
     85690
    (1 row)




#### SPATIAL JOINS
-----------------------------------------------------
( http://workshops.boundlessgeo.com/postgis-intro/joins.html )

Spatial joins are what make up the most of what GIS applications actually e… 
the bread and butter :) 

It allows using information from two tables/databases to gain more knowledge.
SUMMARIES are also possible. 

##### JOIN and SUMMARISE
the combination of a JOIN and GROUP BY provides the info a GIS system usually provides.
eg. "What is he population and racial make-up of the nieghbourhoods of Manhattan"

##### ( NOTE TO SELF : a join creates a virtual table - and later commands, like WHERE and GROUP BY can filter further, or SUM might aggregate results )


#### insert shapefile into postgresql, with postgis geometry

    > shp2pgsql -s 3035 /Users/miska/Documents/open_something/helcom/_helcom_projects/helcom__SCOPE__ais_explorer/helcom_data/rasterised_data_from_manuel/scope__20160120/helcom_data__rasterised_files/April2014Shapefile/April2014Shapefile.shp | psql -h localhost -U miska





#### SPATIAL INDEXING  
-----------------------------------------------------
( http://workshops.boundlessgeo.com/postgis-intro/indexing.html )

 postGIS does a lot of really great spatial indexing to help 
 speed up searching!

 the spatial index done by pgShapeLoader when data is imported, into a DATA_geom_idx table

 R-Trees are the basic indexing of spatial databases.
 they create create a containing rectangle of the given shape, or subshape.
 Sooo... when the search is performed, first the spatial relation to the rectangle,
 which is quite quick to look up, is performed, 
 later a more detailed search is performed to precisely determine the relevant relation.

#### INDEX ONLY QUERIES
 one can make queries that only use the bounding box, 
 for comparisons, rather than the detailed geometry .
 This is done by using the && operator. 

#### STATISTICS LAG
 postGIS maintains statistics on the makeup of the data, 
 to evaluate whether to do detailed or not so detailed searches. 
 HOWEVER, when big amounts of data have been changed, 
 it's a good plan to updae the statistics, the ANALYZE command,
 to keep the statistics up to date.

#### VACUUMING IS ALSO A GOOD IDEA
 it's like cache cleaning for postGIS/gresql,
 after big changes have happened. 

    > VACUUM tablename ;







































