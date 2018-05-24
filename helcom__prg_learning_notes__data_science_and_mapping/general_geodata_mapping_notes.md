#{ general notes  : Geodata and Mapping : }
####( started : 20180107 )

-----------
### learning resources
------------------

#### PennState open web mapping course - with lots other related open courseware courses from them avail too 
https://www.e-education.psu.edu/geog883/node/493

#### koordinates : lots of geodata 
https://koordinates.com

#### planet GIS - community
http://gis.stackexchange.com/questions/tagged/postgis

#### lots of remote sensing resources - mostly satellite and GIS data
https://www.e-education.psu.edu/geog883/node/493

#### lots more data
https://freegisdata.rtwilson.com/

#### js coordinate conversion library 
https://github.com/proj4js/proj4js

#### geotiff in leaflet : plugin to allow one to get a geotiff into leaflet!
https://github.com/stuartmatthews/leaflet-geotiff
-- if the geotiffs are very large, you might want to greate map tiles out of it, using gdal, tilmill, etc… EG : http://build-failed.blogspot.fi/2012/11/zoomable-image-with-leaflet.html

#### postGIS : 

##### advanced postGIS tips 
( including doing marching squares and marching triangles with postgis )
https://abelvm.github.io/

##### PennState - advanced GIS - POSTGIS part :)  << good postGIS overview
https://www.e-education.psu.edu/spatialdb/l4.html

##### OSGeo - postGIS material 
http://revenant.ca/www/postgis/workshop/index.html

##### Boundless - PostGIS intro - ( nicely structured )
http://workshops.boundlessgeo.com/postgis-intro/

##### Pedro Racine - common tasks in postGIS ( nice quick overview and cookbook style tips
 https://github.com/pedrogit/postgis_workshop/blob/master/Advanced%20spatial%20analysis%20with%20PostGIS%20-%20Pierre%20Racine%20-%20FOSS4G%202017.pdf

 ##### OSGeo - lots of postGIS tutorials 
 http://trac.osgeo.org/postgis/wiki/UsersWikiMain


## theoretical bits 
-----------

####  ? What goes where : What can be plotted in leaflet?
- Base mapping layer from some service. 
- Some other VMS engine, which allows one to import their tile-maps
    - Vector based such are also becoming commonplace… 
- Geometry 
- Overlay D3 layer


#### ? What creates a slippy map set
- Some tile generator : could be the open source Mapnik, or some commercial thingie, probably also available from ESRI. 

#### ? How to define what's on a slippy map
- With geo-data, described with CartoCSS ( or thereabouts )

#### ? How to add my own content 
- As geometry using Leaflet primitives ( looks a bit bad )
- Add a D3 layer
- Possible add some canvas magic
- Add a own-generated slippy map, based on some server, turned on/off via a layer control.

