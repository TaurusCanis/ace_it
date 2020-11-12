//https://stackoverflow.com/questions/20851709/how-to-pause-stop-a-timer
//https://stackoverflow.com/questions/24724852/pause-and-resume-setinterval
var seconds = new Date().getTime();
var last = seconds;
var mins = document.getElementsByClassName("mins");
var secs = document.getElementsByClassName("secs");
// var pause_timer = document.getElementsByClassName("pause-timer-btn");
var form_timer_hidden_value = document.getElementsByClassName("remaining_time");
var seconds_elapsed_before = form_timer_hidden_value[0].value;
var paused = false;
var interval;
var timeRemainingMins = Number(document.querySelector("#time_remaining_mins").value);
var timeRemainingSecs = document.querySelector("#time_remaining_secs").value;
var clock_minutes;
var clock_seconds;
var seconds_elapsed_now;

if (timeRemainingSecs == 0o0) {
	timeRemainingSecs = 60;
}



// console.log("seconds_elapsed_before: " + form_timer_hidden_value[0].value);
// console.log("seconds: " + (seconds));



//try {
//	timer[0].addEventListener("click", function() {
//		timer[0].innerHTML = "clicked";
//	});
//}
//catch (e) {
//    console.log("Error", e.stack);
//    console.log("Error", e.name);
//    console.log("Error", e.message);
//}


//console.log(timer);
//
//var mins = 24;
//var secs = 1;

function start_timer() {

	paused = false;
	interval = setInterval(function() {
	var now = new Date().getTime();
	// console.log("now: " + now);
//	last = now;
//	if ((now - seconds) / 1000 == seconds * mins) {
//		mins--;
//		secs = 1;
//		mins[0].innerHTML = mins;
//	}
//	if ((now - seconds) / 1000 == seconds * mins) {
//
//	}

	clock_minutes = Math.floor((timeRemainingMins - seconds_elapsed_before / 1000 / 60) - (now - seconds) / 1000 / 60);
	clock_seconds = Math.round((timeRemainingSecs - seconds_elapsed_before / 1000 % 60) - (now - seconds) / 1000 % 60);

	// console.log(clock_minutes, clock_seconds);

	seconds_elapsed_now = (now - seconds) + Number(seconds_elapsed_before);

	// console.log("seconds: " + seconds);
	// console.log("now - seconds: " + (now - seconds));
	// console.log("now - seconds + seconds_elapsed_before: " + seconds_elapsed_now);


  if (clock_minutes < 0) {
    console.log("endsession");
    clearInterval(interval);
    endSession();
  }
  else if (clock_minutes == 0 && clock_seconds == 0) {
    console.log("endsession");
    clearInterval(interval);
    endSession();
  }
  else if (clock_seconds == 0) {
		mins[0].innerHTML = clock_minutes;
		secs[0].innerHTML = "00";
    if (clock_minutes <= 0) {
      console.log("endsession");
      clearInterval(interval);
      endSession();
    }
	} else {
  
		mins[0].innerHTML = clock_minutes;
		if (clock_seconds < 10) {
			secs[0].innerHTML = "0" + clock_seconds;
		} else {
			secs[0].innerHTML = clock_seconds;
		}

	}

//	for (i in form_timer_hidden_value) {
//		i.value = now - seconds;
//		console.log("hidden value: " + i);
//		console.log("i.value: " + i.value);
//	}

	for (i = 0; i < form_timer_hidden_value.length; i++) {

		form_timer_hidden_value[i].value = seconds_elapsed_now;
		// console.log("seconds_elapsed: " + form_timer_hidden_value[i].value);
//		console.log(now - seconds - seconds_elapsed);
	}



}, 1000);
}

function endSession() {
  pauseTimer();
  saveFinalAnswer();
}


function pauseTimer() {
	if (paused == false) {
		clearInterval(interval);
		paused = true;
		seconds_elapsed_before = seconds_elapsed_now;
	}
	else {
		seconds = new Date().getTime();
		start_timer(); //How to resume?
	}
};

window.addEventListener("load", start_timer);

// export { clock_minutes, clock_seconds }
