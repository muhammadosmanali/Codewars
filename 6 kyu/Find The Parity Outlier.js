function findOutlier(integers){
  let even = 0;
  let odd = 0;
  for(let i = 0; i < integers.length; i++)
  {
    if(integers[i] % 2 == 0)
    {
      even += 1
    }
    else
    {
      odd += 1
    }
  }
  if(even > odd)
  {
    for(let i = 0; i < integers.length; i++)
    {
      if(integers[i] % 2 != 0)
      {
        return integers[i]
      }
    }
  }
  else
  {
    for(let i = 0; i < integers.length; i++)
    {
      if(integers[i] % 2 == 0)
      {
        return integers[i]
      }
    }
  }
}