function createPhoneNumber(numbers){
  var phone = "";
  for(let i = 0; i < numbers.length; i++) {
    phone += numbers[i];
  }
  
  var result = "(" + phone.slice(0, 3) + ")" + " " + phone.slice(3, 6) + "-" + phone.slice(6, 10);
  return result;
}