#{ postgreSQL , pandas and python }
####( start date : 20160113 )


----------
###learning resources
--------------

######  PostgreSQL.app ( OSX ) - configure PYTHON for POSTGRESQL.APP using SQPAlchemy
http://postgresapp.com/documentation/configuration-python.html

###### Make a FLASK app with POSTFRESQL database ( and deploy to Heroku)
http://blog.sahildiwan.com/posts/flask-and-postgresql-app-deployed-on-heroku/

####### FLASK by example - set up POSTGRESQL, SQLALCHEMY and Alembic
https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/


###### SQLALCHEMY

SQLAlchemy manual
http://docs.sqlalchemy.org/en/latest/core/engines.html

Using SqlAlchemy to reduce memory and server use:
http://www.mobify.com/blog/sqlalchemy-memory-magic/

More SQLAlchemy tutorials from Python Central
http://pythoncentral.io/introductory-tutorial-python-sqlalchemy/


###### PANDAS

Connceting/Reading/Writing dataframes between PANDAS and POSTGRESQL via SQLAlchemy
http://stackoverflow.com/questions/24189150/pandas-writing-dataframe-to-other-postgresql-schema



---------------- 

### notes & code 

-----------------------------------


######  SQLALCHEMY

#### connecting to the postgreSQL database, using SQLAlchemy for python:
    > engine = sqlalchemy.create_engine('postgresql://localhost/postgis_test');
    > conn = engine.connect();

#### make a query and get the result into pandas
    > one = pd.io.sql.read_sql( "select * from ais_weeks limit 10", con=con );
> 




##### import shapefiles into pandas
######		- use pyshp




#### READING shapefiles
#
###### - eg. use the shapefile library

#
#### load shapefile
#
##### - load/open any of the the shapefiles - eg. the .shp or .dbf
    > import shapefile
    > out = shapefile.Reader("path/to/shapefile.shp/or/shapefile.dbf")

#
##### get all the records
    > recs = out.records()
