function findOdd(A) {
  length = A.length;
  
  if(length == 1)
  {
    return A[0];
  }
  
  var count = 0;
  for(let i = 0; i < length; i++)
  {
    for(let j = 0; j < length; j++)
    {
      if(A[i] == A[j]) 
      {
        count += 1;
      }  
    }
    if(count % 2 != 0)
    {
      return A[i];
    }
    else 
    {
      count = 0;
    }
  }
  return 0;
}