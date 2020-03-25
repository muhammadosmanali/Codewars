using System;

public class NthSeries {
  
  public static string seriesSum (int n) {
  
    if(n == 0) {
      return "0.00";
    }
    
    decimal sum = 1;
    decimal den = sum + 3;
    for(int i = 0; i < n - 1; i++) {
      sum = sum + (1 / den);
      den = den + 3;
    }
    decimal result = decimal.Round(sum, 2, MidpointRounding.AwayFromZero);
    string r = result.ToString();
    return r;
  }
}