//return the total number of smiling faces in the array
function countSmileys(arr) {
  length = arr.length;
  var count = 0;
  if(length == 0) 
  {
    return 0;
  }
  for(let i = 0; i < length; i++) 
  {
    if(arr[i].length == 3) 
    {
      if(arr[i][0] == ':' || arr[i][0] == ';')
      {
        if(arr[i][1] == '-' || arr[i][1] == '~') 
        {
          if(arr[i][2] == ')' || arr[i][2] == 'D')
          {
            count += 1;
          }
        }
      }
    }
    else if(arr[i].length == 2)
    {
      if(arr[i][0] == ':' || arr[i][0] == ';')
      {
        if(arr[i][1] == ')' || arr[i][1] == 'D') 
        {
          count += 1;
        }
      }
    }
  }
  return count;
}