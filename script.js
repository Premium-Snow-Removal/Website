var minuteToSecond = 60;
//Do NOT change the value of this variable. 1 minute is always 60 seconds.
var SecondToMillisecond = 1000;
//Do NOT change the value of this variable. 1 second is always 1000 milliseconds.
var updateTimeMinutes = 30;
var updateTimeFinal = updateTimeMinutes * minuteToSecond * SecondToMillisecond;

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
document.getElementById("snowCounter").innerHTML = "We " + active2 + " in service at this time. " + message;
//message for uers on availability

}
setTimeout(main, 1);
function action() {
	var apointment = document.getElementById("select").value;
	if (apointment == 2 && active == false) {
		alert("ERROR: This action could not be completed because Premium Snow Removal Crew are unavailible at this time")
	}
	if (apointment == 1) {
		alert("PLEASE NOTE: All appointments with times on weekdays before 4:15PM or on Tuesday or Thursday are usually unavailable and times before 9:00AM or after 5:00 will alaways be denied because Premium Snow Removal Crew are unavailible at these times. Friday times can usually be after 2:15PM or before 4:30PM")
	}
	if (apointment == 1||apointment == 2) {
		while (true) {
          var time = "";
          var name = prompt("What is your name?");
          var location = prompt("Where would you like our services?");
          if (apointment == 1) {
             time = " at " + prompt("When would you like us to start?");
          }
          var subject = "Apointment for " + name + " at " + location + time;
          var body = prompt("What exactly would you like?");
   
          if (subject == null||subject == null||name == null||location == null||time == null) {
				alert("One or more catagory was cancelled");
          }else {
            break;
          }
        }
		var popupBlockerChecker = {
			check: function(popup_window) {
          var _scope = this;
            if (popup_window) {
                if(/chrome/.test(navigator.userAgent.toLowerCase())){
                    setTimeout(function () {
                        _scope._is_popup_blocked(_scope, popup_window);
                     },200);
                }else{
                    popup_window.onload = function () {
                        _scope._is_popup_blocked(_scope, popup_window);
                    };
                }
            }else {
                _scope._displayError();
            }
        },
        _is_popup_blocked: function(scope, popup_window) {
            if ((popup_window.innerHeight > 0)== false){ scope._displayError(); }
        },
        _displayError: function(){
            alert("Popup Blocker is enabled! Please add this site to your exception list.");
        }
    };
var popup = window.open("mailto:wesbob12@gmail.com" + "?subject=" + subject + "&body=" + body);
popupBlockerChecker.check(popup);
        }
}
//The section below is a hidden function developed for update team to use to determine if a customer is loyal
function loyalty(search) {
    var loyal = ["Rebecca Howden", "Vince Greco"]
	var stink = 0;
	var message1 = "not loyal";
    for (var i = 1; i <= loyal.length(); i = i + 1) {
        stink = loyal[i-1];
		if (stink == search) {
			var ifLoyal = true;
			message1 = "loyal";
			break;
		}
    }
	alert("This customer is " + message1);
}
