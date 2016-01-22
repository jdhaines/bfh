function checkInstallation() {
	
	if (document.getElementById("noInstallationIssues").checked) {
		document.getElementById("installationComments").classList.add("hidden");
	}
	else {
		document.getElementById("installationComments").classList.remove("hidden");
	}
}
function checkReason1() {
	
	if (document.getElementById("noreason1Steps").checked) {
		document.getElementById("reason1StepsComments").classList.add("hidden");
	}
	else {
		document.getElementById("reason1StepsComments").classList.remove("hidden");
	}
}
function checkReason2() {
	
	if (document.getElementById("noreason2Steps").checked) {
		document.getElementById("reason2StepsComments").classList.add("hidden");
	}
	else {
		document.getElementById("reason2StepsComments").classList.remove("hidden");
	}
}
function checkStartUp() {
	
	if (document.getElementById("nostartUpIssues").checked) {
		document.getElementById("startUpComments").classList.add("hidden");
	}
	else {
		document.getElementById("startUpComments").classList.remove("hidden");
	}
}
function checkSpecialEvents() {
	
	if (document.getElementById("specialEventsNo").checked) {
		document.getElementById("specialEvents").classList.add("hidden");
	}
	else {
		document.getElementById("specialEvents").classList.remove("hidden");
	}
}
function checkTasPostMortem() {
	
	if (document.getElementById("tasPostMortemNo").checked) {
		document.getElementById("tasPostMortem").classList.add("hidden");
	}
	else {
		document.getElementById("tasPostMortem").classList.remove("hidden");
	}
}