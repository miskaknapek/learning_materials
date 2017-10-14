#{ d3 mapping tutorial notes (aligned left tutorial) }
#####( started: 20150715 )
---------------------------------


###geoJSON
——————————————————————

eg.
Always has a “FeatureCollection”,
within which there’s the “geometry” and “coordinates”.
PLEASE NOTE : LONGITUDE IS LISTED BEFORE LATITUDE, (i.e. y, x????)
contrary to the ‘cultural bias of’ lat/long.
Replacement of GetLatLong - http://teczno.com/squares/

  {
    "type": "FeatureCollection",
    "features": [
       {
         "type": "Feature",
         "id": "01",
         "properties": { "name": "Alabama" },
         "geometry": {
           "type": "Polygon",
           "coordinates": [[[-87.359296,35.00118],
             [-85.606675,34.984749],[-85.431413,34.124869],
             [-85.184951,32.859696],[-85.069935,32.580372],
             [-84.960397,32.421541],[-85.004212,32.322956],
             [-84.889196,32.262709],[-85.058981,32.13674] …
            ]]
        }
      },
      {
           "type": "Feature",
           "id": "02",
           "properties": { "name": "Alaska" },
           "geometry": {
             "type": "MultiPolygon",
             "coordinates": [[[[-131.602021,55.117982],
               [-131.569159,55.28229],[-131.355558,55.183705],
               [-131.38842,55.01392],[-131.645836,55.035827],
               [-131.602021,55.117982]]],[[[-131.832052,55.42469],
               [-131.645836,55.304197],[-131.749898,55.128935],
               [-131.832052,55.189182], …
              ]]]
            }
        } 
  ] }


###Paths 
—————————————


Translation from geojson to paths.
. A (path) translator - d3.geo.path() - is needed to translate geojson data to path data.
var path = d3.geo.path();
Find out more about Geo Paths on the D3 wiki:
https://github.com/mbostock/d3/wiki/Geo-Paths

. The GDAL package can be used to convert different geo data formats to geoJSON.

. The d3.geo.path() generates the a suitable data string for the “d” element of a SVG path element. Similar to some of the other line generators, like d3.svg.line . chc
NOTE: the d3.path class can render directly to <canvas>, which can offer better performance when animating projections.

. d3.geo.path() creates a new geographic path based on default settings - with the albersUSA projection and a point radius of 4.5 pixels.
- path.projection( [projection] ) allows one to retrieve the current map projection used, or change it.

. path.area( feature )
	- computers the area, in pixels, of the given feature.

. path.bounds( feature )
	- computes the bounds box of the given feature.



###Projections
—————————————
Used to convert 3d earth/map coords onto 2d surfaces, eg.…

    var projection = d3.geo.albersUsa()
    			.translate( [w/2, h/2] );   // translates the projection to the center of the image


And then to get the path generator to reference our projection object (above), we do this:


    var path = d3.geo.path()
    		.projection( projection );


We can also affect the calculations of the projection…


    var projection = d3.geo.albersUsa()
    			.translate( [ w/2, h/2] )
    			.scale( [500] );  // the default scale is 500



###Styling
————————

- Map paths can be styled the usual way.




###Loading geo data
—————————————

eg. 


    d3.json( “us-states.json”, function(json){
    	
    	svg.selectAll(“path”)
    		.data( json.features )
    		.enter()
    		.append( “path” )
    		.attr(“d”, path);  	//  <<  note the d3.geo.path() function 
    });





###Choropleth
———————————

Quantize function
It allows one to define destination/output bins for input values… 

// here the output colours are defined ( NOTE: not the input values )


    var color = d3.scale.quantize()
                        .range(["rgb(237,248,233)", "rgb(186,228,179)",
                         "rgb(116,196,118)", "rgb(49,163,84)","rgb(0,109,44)"]);


// after the data’s loaded, one can define the output values like this 
// ( according to the data, using the min/max functions )


    color.domain([
            d3.min(data, function(d) { return d.value; }),
            d3.max(data, function(d) { return d.value; })
    ]);



// if the data comes from an external file, it can be merged like this 


      d3.json("us-states.json", function(json) {

          //Merge the ag. data and GeoJSON
          //Loop through once for each ag. data value
          for (var i = 0; i < data.length; i++) {

              //Grab state name
              var dataState = data[i].state;

              //Grab data value, and convert from string to float
              var dataValue = parseFloat(data[i].value);

              //Find the corresponding state inside the GeoJSON
              for (var j = 0; j < json.features.length; j++) {

              var jsonState = json.features[j].properties.name;

              if (dataState == jsonState) {

                  //Copy the data value into the JSON
                  json.features[j].properties.value = dataValue;

                  //Stop looking through the JSON
                  break;

            }
        }
    }



// And now the whole works, including path colourings, according to the data, as well as a placeholder for missing values… 


                svg.selectAll("path")
                   .data(json.features)
                   .enter()
                   .append("path")
                   .attr("d", path)
                   .style("fill", function(d) {
                                //Get data value
                                var value = d.properties.value;

                                if (value) {
                                        //If value exists…
                                        return color(value);
                                } else {
                                        //If value is undefined…
                                        return "#ccc";
                                }
                   });






###Adding points
————————————

Eg. let’s try adding points, with data about some cities and their populations, onto the map… 

// One can use the projection encoder defined above to plot points too

 
       svg.selectAll("circle")
           .data(data)
           .enter()
           .append("circle")
           .attr("cx", function(d) {
                   return projection([d.lon, d.lat])[0];
           })
           .attr("cy", function(d) {
                   return projection([d.lon, d.lat])[1];
           })
           .attr("r", 5)
           .style("fill", "yellow")
           .style("opacity", 0.75);




###Geocoder
————————————

You can use this to convert place-names to coordinates, so places can be plotted…



###Mapping attributes - eg center, parallels, scale, rotate, etc… 
———————————

    .center([0°, 0°])
. sets the projection’s center, to the specified center.
defaults to ( [0°, 0° ]).

    .rotation( [yaw, pitch, [roll]] )

. set the projection’s rotation, in specified angles, either two or three dimensions can be specified. If only two dimensions are specified, the last third dimension will default to zero.

    .fitExtent( extent, object )
Set the projection’s scale and transform to fit the specified geoJson object in the center of the current extent. The extent is specified in [ [ left, top ], [ right, bottom] ]. Takes care of Transform and Scale. 
Eg. for the German map, this was used ( data was in the geojson data ): 


    var projection = d3.geoMercator()
    		.fitExtent( [[0,0],[1600,1600] ], data);


    .fitSize( size, object )
Equivalent to fitExtent, with a bit of a shorthand. The top left is automatically [0,0], and all one does is set the size and the relevant object… eg…


	var projection = d3.geoMercator()
				.fitSize[ [width,height], data);



_________ geo object functions ___________

    path.centroid( object ) 
Returns the x/y coordinate of the geojson-object - i.e. send it the geo-json object, in various ways, to get the centroid. 
Eg. 


				// make centroid circles 
				window.individual_paths = svg.selectAll("rect")
					.data( data.features )
					.enter()
						.append("rect")
							.attr("class", "centroid")
							.attr("x", function(d){ return window.path.centroid( d )[0]; } )
							.attr("y", function(d){ return window.path.centroid( d )[1]; } )
							.attr("width", 2)
							.attr("height", 2)
							.attr("fill", "orange");



    path.bounds( object ) 
Same as path.centroid but returns bounds as [ [left, top], [right, bottom] ] .

    path.area( object ) 
Same as path.centroid but returns area as a pixel number.

