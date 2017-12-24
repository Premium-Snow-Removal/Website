var minuteToSecond = 60;
var SecondToMillisecond = 1000;
var updateTimeMinutes = 30;
var updateTimeFinal = updateTimeMinutes * minuteToSecond * SecondToMillisecond;

function timedRefresh() {
	setTimeout("location.reload(true);", updateTimeFinal);
 //1800000 is equal to 30m, which is the time frame for updates on stats like report
}

window.onload = timedRefresh();
//Above is code used for refreshing the page every 30m

var active = true;
 //Above variable is wether or not PSR is in service
function main() {
  var active2 = "are not";
  var message = "Sorry :(";
  if (active == true) {
    active2 = "are";
    message = ":)";
  }
document.getElementById("snowCounter").innerHTML = "We " + active2 + " in service at this time. " + message;
}
setTimeout(main, 1);
