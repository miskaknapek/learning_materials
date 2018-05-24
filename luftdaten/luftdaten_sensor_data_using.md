### Sonstiges LuftDaten daten plotting info … 
( start datum : 20180128 )

---------------------------------


##### Various resources : 

OpenSense.net API 
https://www.opensense.network/beta/apidocs/#!/Values/get_api_v1_0_values







###### Getting data from LuftDaten
---------------

////// GET /api/v1.0/values : 
////     - The following area, in OpenSense/Luftdaten seems to allow one to get sensor data FROM A SPECIIFC LAT/LONG COORDINATE position AND RADIUS 
NOTE : alas, it is about getting data from a specific radius… - remember that min-distance needs to be set… 
NOTE : Max/min time limits are possible to set… 

//// URL for teching data generally
// *Note* min radius and no time limit )
https://www.opensense.network/beta/api/v1.0/values?measurandId=11&refPoint=41.765%2C%2026.204&maxDistance=1



////// GET /api/v1.0/sensors : 
////        - Get all the sensor units, of a specific sensor type 
( also allows bounding boxes and the like … )
https://www.opensense.network/beta/apidocs/#!/Sensors/get_api_v1_0_sensors
//
// eg fetch all sensors of sensor type 11 ( PM 2.5 methinks )
https://www.opensense.network/beta/api/v1.0/sensors?measurandId=11


// eg Fetch the data of a specific sensor ( id #8970 ) 
//  between specific time-strings
// NOTE : doesn't retrieve values if there are no values… 
https://www.opensense.network/beta/api/v1.0/sensors/8970/values?minTimestamp=2017-01-27T22:00:00.000Z&maxTimestamp=2017-01-28T22:00:00.000Z

// eg. as above, but fetch all values of sensor ( id #12826 )
// - possible settings include setting timestamps 
// NOTE : only fetches values if they're fewer than 50k values… 
https://www.opensense.network/beta/api/v1.0/sensors/12826/values
