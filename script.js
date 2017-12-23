function main() {
  var active = false;
  /*Above variable is wether or not PSR is in service*/
  var active2 = "are not";
  var message = "Sorry :(";
  if (active == true) {
    active2 = "are";
    message = "";
  }
document.getElementById("snowCounter").innerHTML = "We " + active2 + " in service at this time. " + message;
}
setTimeout(main, 1);
