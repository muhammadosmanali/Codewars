function rowSumOddNumbers(n) {
  var start = 1;
  var power = 1;
  if(n == 1) 
  {
    return n;
  }
  
  for(let i = 1; i < n; i++)
  {
    start = start + (2 * power);
    power += 1;
  }
  var arr = [];
  arr.push(start)
  
  for(let j = 1; j < n; j++) 
  {
    start = start + 2;
    arr.push(start);
  }
  
  const sum = arr.reduce(add);
  return sum;
  
}

function add(accumulator, a) {
    return accumulator + a;
}