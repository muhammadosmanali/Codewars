using System.Text.RegularExpressions;

public static class Kata
{
  public static string AlphabetPosition(string text)
  {
    string[] lower_alphabets = { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" };
    string[] digits = { "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26" };

    text = text.Replace(" ", "");
    text = text.ToLower();
    int length = text.Length;

    var store_numbers = new string[1000];
    int i = 0;
    foreach (var x in text)
    {
      
      for (int j = 0; j < 26; j++)
      {
        if (x.ToString() == lower_alphabets[j])
        {
          store_numbers[i] = digits[j];
          i = i + 1;
       }
      }
     }
     
     string result = ConvertStringArrayToStringJoin(store_numbers);
     string[] number = Regex.Split(result, @"\D+");
     string result1 = string.Join(" ", number);
     result1 = result.TrimEnd();
     return result1;
  }
  
  static string ConvertStringArrayToStringJoin(string[] array)
  {
      // Use string Join to concatenate the string elements.
      string result = string.Join(" ", array);
      return result;
  }
}