#{ general notes  : Geodata and Mapping : MAPPING IN D3 }
####( started : 20180107 )

-----------
### learning resources
------------------

- some nice link 

- some nice other link 

*Tests :*
- leaflet_with_d3_content__basic_test__03.html // plotting luftdaten - leaflet + d3 

## theoretical bits 
-----------

####  ? How can one map with d3? 
- Add a d3 layer in a leaflet sketch.
- Use d3's tile bits to get a slippy map in d3 +++ PLUS +++ add a svg layer using D3
- Use d3's tile bits to get a slippy map in d3 +++ PLUS +++ add a CANVAS layer using D3




## practical bits 
-----------



#### Basics of plotting with D3 on D3 ( not quite same as with leaflet )
-----------
( …When using d3 with leaflet, one doesn't use the standard projection, behaviour and zoom objects. However, the zoom still needs implementing, but slightly differently. More on that later ).

But, one does need to pay extra attention when mapping between screen and map coordinates. … eg w)

**Preface** : One always needs certain components to create a map : 

    - ** Projection ** : to choose how the map is displayed
        - described here : (v3) https://www.youtube.com/watch?v=L2SJMqbFzPs&t=226s

    - ** Zoom ** : if there's zooming involved, this partly catches zooming events and updates the projection/transformation stuff, to suit the desired zoom level.
            - in d3 **v4**, a d3.event.transform gives one the relevant scale and translation settings for the curent zoom level 
                .eg:

                    ////// ** earlier, in initial setup **
                    var zoom = d3.zoom()
                        .scaleExtent([1 << 11, 1 << 14])
                        .on("zoom", zoomed);

                    ////// ** in the zoomed function **
                    // make the transform object 
                    var transform = d3.event.transform;
                    //
                    var tiles = tile
                      .scale(transform.k)
                      .translate([transform.x, transform.y])
                      ();
                    //
                    projection
                      .scale(transform.k / tau)
                      .translate([transform.x, transform.y]);
                    //
                    geo path… d…
                    -

            - in d3 **v3** one uses a d3.behaviour.zoom object instead of d3.zoom, as in v4 

                    ////// ** earlier, in initial setup **
                    var projection = d3.geo.mercator()
                        .scale((1 << 24) / 2 / Math.PI)
                        .translate([-width / 2, -height / 2]); // just temporary
                    //
                    var zoom = d3.behavior.zoom()
                        .scale(projection.scale() * 2 * Math.PI)
                        .scaleExtent([1 << 9, 1 << 25])
                        .translate(projection([-73.975536, 40.691674]).map(function(x) { return -x; }))
                        .on("zoom", zoomed);

                    ////// ** in zoomed function 
                    //
                    var tiles = tile
                      .scale(zoom.scale())
                      .translate(zoom.translate())
                      ();
                    //
                    projection
                      .scale(zoom.scale() / 2 / Math.PI)
                      .translate(zoom.translate());                        




#### Various bits & pieces
-----------

** How to get geographic coordinate positions from the mouse position on the map : ** … on a d3.tile map… ( or, I guess, could be any map using suggested projection )
-->> projection.invert
( described here: https://github.com/d3/d3-3.x-api-reference/blob/master/Geo-Projections.md )
note : "Not all projections implement invert; for noninvertible projections, this method is undefined."
eg 
( from here : http://bl.ocks.org/mbostock/4132797 )

    var projection = d3.geo.mercator();
    // and then : 
        function mousemoved() {
          info.text(formatLocation(projection.invert(d3.mouse(this)), zoom.scale()));
        }











