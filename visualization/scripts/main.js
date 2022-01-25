const Day = {
	day: function () {this.Day},
	time: function () {this.Time},
	capacity: function () {this.Capacity}
};
const days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];
const weekdayTimes = ["05:00 AM","05:30 AM","06:00 AM","06:30 AM","07:00 AM","07:30 AM"];
const weekendTimes = ["07:00 AM","07:30 AM","08:00 AM","08:30 AM","09:00 AM","09:30 AM","10:00 AM","10:30 AM","11:00 AM","11:30 AM","12:00 PM","12:30 PM","01:00 PM","01:30 PM","02:00 PM","02:30 PM","03:00 PM","03:30 PM","04:00 PM","04:30 PM","05:00 PM","05:30 PM","06:00 PM","06:30 PM"]

// pull in csv data once the DOM loads
$(document).ready(function () {
	// need to use ).then(fx) rather than ", fx()" so that it reads it all into an array
	// rather than perform the action on each and be unable to grab pieces
	d3.csv("/data/viscapacitylog.csv").then(function (data) {
		// the actual stuff will go here but for now just prove csv read is working
		averages = averageData(data);
		//console.log(averages);
	});
});

function averageData (data) {
	let dayArray = filterByDays(data);
	let averages = grabTimeAverages(dayArray);
	//console.log(dayArray);
	//filteredFull = dayArray.filter(filterTimes);
}

// create a nested array for each day of the week to group datapoints
function filterByDays (data) {
	let dayArray = [[],[],[],[],[],[],[]];
	for (datapoint of data) {
		// create a new object instance
		let thisDay = Object.create(Day);
		thisDay.day = datapoint.Day;
		thisDay.time = datapoint.Time;
		thisDay.capacity = datapoint.Capacity;
		// add the new object to the appropriate day array index
		let i = days.indexOf(thisDay.day);
		dayArray[i][dayArray[i].length].push(thisDay);
	}
	return dayArray;
}

// create array of avg capacity for each time
function grabTimeAverages (dayArray) {
	let i = 0;
	let allTimes = [];
	//console.log(dayArray);
	for (thisDay of dayArray) {
		for (let j = 0; j < thisDay.length; j++) {
			let thisTime = thisDay[j].time;
			if ((i == 0) || (i == 6)) {
				k = weekendTimes.indexOf(thisTime);
			}
			else {
				k = weekdayTimes.indexOf(thisTime);
			}
			// so how do I do this without creating a massive array of [[[],[]],[[],[]],etc]
			allTimes[i][k].push(thisTime);
			console.log(allTimes[i][k]);
		}
		i++;
		//console.log(thisDay);
	}
}