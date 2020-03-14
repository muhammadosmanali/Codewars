function sqInRect(lng, wdth){
  var arr = [];
  if(lng == wdth) {
    return null;
  }
  while(wdth != lng) {
    if(wdth > lng) {
      wdth -= lng;
      arr.push(lng);
    }
    else if(lng > wdth) {
      lng -= wdth;
      arr.push(wdth);
    }
  }
  arr.push(wdth);
  return arr
}