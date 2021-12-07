function deletestudent(id){
	var ok = confirm("Delete this student? => "+id)
	if(ok){
		location.href="/deletestudent?id="+id
	}
}
function edit_student(id,idno,lastname,firstname,course,level){
	document.forms['studentform']['flag'].value = id;
	document.forms['studentform']['idno'].value = idno;
	document.forms['studentform']['lastname'].value = lastname;
	document.forms['studentform']['firstname'].value = firstname;
	document.forms['studentform']['course'].value = course;
	document.forms['studentform']['level'].value = level;
	/*
	document.getElementById('idno').value=idno;
	document.getElementById('lastname').value=lastname;
	document.getElementById('firstname').value=firstname;
	document.getElementById('course').value=course;
	document.getElementById('level').value=level;
	*/
	document.getElementById('studentmodal').style.display='block'
}
function add_student(){
	document.forms['studentform']['flag'].value = '-'
	document.getElementById('studentmodal').style.display='block'
}

function generate_payroll(id,idno,lastname,firstname,position_desc,daily_rate){
	document.forms['studentform']['flag'].value = id;
	document.forms['studentform']['idno'].value = idno;
	document.forms['studentform']['name'].value = firstname + " " + lastname;
	document.forms['studentform']['rate'].value = daily_rate;
	document.forms['studentform']['d_r'].value = daily_rate;
	/*
	document.getElementById('idno').value=idno;
	document.getElementById('lastname').value=lastname;
	document.getElementById('firstname').value=firstname;
	document.getElementById('course').value=course;
	document.getElementById('level').value=level;
	*/
	document.getElementById('MODAL').style.display='block'

}

function delete_payroll(id){
	var ok = confirm("Delete this payroll? => "+id)
	if(ok){
		location.href="/delete_payroll?id="+id
	}
}
document.getElementById("days").addEventListener("change", function(){
		if (document.getElementById("days").value.length > 0){
			var number_of_days = parseInt(document.getElementById("days").value);
			
			if(number_of_days>=0){
				document.getElementById("salary").value = number_of_days*parseFloat(document.getElementById("rate").value)
			}else{
				document.getElementById("salary").value = "INVALID";
			}
		}

	});

var today = new Date();

var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
document.getElementById("date_to").valueAsDate = today;


// document.getElementById("date_to").addEventListener("change", function(){
// 		var date_from_val = document.getElementById("date_from").valueAsDate;

// 		if(date_from_val!=null){
// 			var date_from_month = parseInt((date_from_val.getMonth()+1));
// 			var date_from_days = parseInt(date_from_val.getDate());
// 			var date_from_year = parseInt(date_from_val.getFullYear());

// 			var date_to_month = parseInt((today.getMonth()+1));
// 			var date_to_days = parseInt(today.getDate());
// 			var date_to_year = parseInt(today.getFullYear());

// 			var new_date = date_from_year+'-'+date_from_month+'-'+date_from_days
// 			if(date_from_month > date_to_month)
// 				new_date = date_from_year+'-'+date_to_month+'-'+date_from_days

// 			document.getElementById("date_from").valueAsDate = new Date(new_date)

// 		}

// 	});

function display_payroll(){
	location.href="/display_payroll"
}
function display_employee(){
	location.href="/employeelist/ok"
}


