function printerError(s) {
    length = s.length;
    var count = 0;
    for(let i = 0; i < length; i++) 
    {
      if(s[i] > 'm')
      {
        count += 1;
      }
    }
    var result = count.toString() + "/" + length.toString();
    return result
}