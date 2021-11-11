function deletestudent(id){
	var ok = confirm("Delete this student? => "+id)
	if(ok)
		location.href="/deletestudent?id="+id
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
	document.getElementById('studentmodal').style.display='block';
}
function add_student(){
	document.forms['studentform']['flag'].value = '-'
	document.getElementById('studentmodal').style.display='block';
}