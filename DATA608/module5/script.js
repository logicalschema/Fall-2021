function reverseString(str) {
	var inputString = document.getElementById("inputString").value;
	var printMe = "";

    if(document.getElementById("inputString").value.length == 0){
    	printMe = "The input string is empty.";
    } else {
    	printMe = inputString.split('').reverse().join('');

    }

	document.getElementById("reverseText").innerHTML = printMe;
}


function matrixMultiple(){

// Assigning the variable to the user input
	var inputNumber = parseInt(document.getElementById("inputNumber").value);
	var printMe = "";
	var count = 1;

	if (!isNaN(inputNumber)){
		for (let row = 0; row < 5; row++) {
			let line = "<tr>"
			for (let column = 0; column < 4; column++){
				line = line.concat("<td>" + String(inputNumber * count) + "</td>");
				count += 1;
			}
			line = line.concat("</tr>");
			printMe = printMe.concat(line);
		} 

	} else {
		printMe = "<tr><td>Invalid input for multiples. You need to input an integer.</td></tr>";
	}


// Print the Multiples
document.getElementById("function1").innerHTML = printMe;
}


//https://gist.github.com/jfreels/6814721
var tabulate = function (data,columns) {
  var table = d3.select('#load-csv').append('table')
  var thead = table.append('thead')
  var tbody = table.append('tbody')


    table.attr("id", "csv-table")

	thead.append('tr')
	  .selectAll('th')
	    .data(columns)
	    .enter()
	  .append('th')
	    .text(function (d) { return d })

	var rows = tbody.selectAll('tr')
	    .data(data)
	    .enter()
	  .append('tr')

	var cells = rows.selectAll('td')
	    .data(function(row) {
	    	return columns.map(function (column) {
	    		return { column: column, value: row[column] }
	      })
      })
      .enter()
    .append('td')
      .text(function (d) { return d.value })

  return table;
}