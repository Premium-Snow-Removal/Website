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
	if (apointment == 1) {
		while (true) {
		var name = prompt("What is your name?");
		var location == prompt("Where would you like our services?");
		var subject = "Apointment for " + name + " at " + location;
		var body = prompt("What exactly would you like?");
		if (subject == null||subject == null||name == null||location == null) {
				alert("One or more catagory was cancelled");
		}
		else {
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
            if ((popup_window.innerHeight > 0)==false){ scope._displayError(); }
        },
        _displayError: function(){
            alert("Popup Blocker is enabled! Please add this site to your exception list.");
        }
    };
var popup = window.open("mailto:wesbob12@gmail.com" + "?subject=" + subject + "&body=" + body);
popupBlockerChecker.check(popup);
}
	}
}
