var number = function(busStops){
  var into_bus = 0
  var getoff_bus = 0
  for(let i = 0; i < busStops.length; i++)
  {
    into_bus += busStops[i][0];
    getoff_bus += busStops[i][1];
  }
  var result = into_bus - getoff_bus;
  return result;
}