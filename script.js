var minuteToSecond = 60;
//Do NOT change the value of this variable. 1 minute is always 60 seconds.
var SecondToMillisecond = 1000;
//Do NOT change the value of this variable. 1 second is always 1000 milliseconds.
var updateTimeMinutes = 30;
var updateTimeFinal = updateTimeMinutes * minuteToSecond * SecondToMillisecond;
var read = new FileReader();
function timedRefresh() {
	setTimeout("location.reload(true);", updateTimeFinal);
	//1800000 is equal to 30m, which is the time frame for updates on stats like report
}

window.onload = timedRefresh();
//Above is code used for refreshing the page every 30m

var active = false;
//Above variable is wether or not PSR is in service
function main() {
	var active2 = "are not";
	var message = "Sorry :(";
	if (active == true) {
		active2 = "are";
		message = ":)";
//Above variables are used for message and are reversed from negative to positive if PSR is active	  
  }
document.getElementById("report").innerHTML = "We " + active2 + " in service at this time. " + message;
}
setTimeout(main, 1);
