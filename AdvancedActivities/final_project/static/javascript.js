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
	my_f()

}

function delete_payroll(id){
	var ok = confirm("Delete this payroll? => "+id)
	if(ok){
		location.href="/delete_payroll?id="+id
	}
}

const formatter = new Intl.NumberFormat('en-US', {
                      style: 'currency',
                      currency: 'PHP',
                      minimumFractionDigits: 2
                    })

if(document.getElementById("days")!=null){
	document.getElementById("days").addEventListener("change", function(){
			update_salary();
		});
}
function update_salary(){
			if (document.getElementById("days").value.length > 0){
				var number_of_days = parseInt(document.getElementById("days").value);
				
				if(number_of_days>=0){
					document.getElementById("salary").value = formatter.format(number_of_days*parseFloat(document.getElementById("rate").value))
				}else{
					document.getElementById("salary").value = "INVALID";
				}
			}

		}
function my_f(){
	if(document.getElementById("days")!=null){
		document.getElementById("days").value = 1;
		document.getElementById("salary").value = formatter.format(parseFloat(document.getElementById("rate").value)*1)
	}
}

var today = new Date();

var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();


if(document.getElementById("date_to")!=null){
	document.getElementById("date_to").valueAsDate = today;
	document.getElementById("date_from").valueAsDate = new Date(today.getFullYear()+'-'+(today.getMonth()+1)+'-'+(today.getDate()));
	document.getElementById("date_to").addEventListener("change", function() {
		if(document.getElementById("date_from").valueAsDate!=null){
			date_from = document.getElementById("date_from").valueAsDate;
			date_to = document.getElementById("date_to").valueAsDate;

			if(date_from.getMonth()==date_to.getMonth()){
				day_from = date_from.getDate();
				day_to = date_to.getDate();

				if(day_to > day_from){
					document.getElementById("days").value = parseInt(day_to)-parseInt(day_from);
					update_salary();
				}
			}
		}
	})
}

function display_payroll(){
	location.href="/display_payroll"
}
function display_employee(){
	location.href="/employeelist/ok"
}
