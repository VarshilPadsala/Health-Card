from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.db import connection

# Create your views here.

def Home(request):
	return render(request,"Home.html",{})

def Admin_Login(request):
	if request.method == "POST":
		A_username = request.POST['aname']
		A_password = request.POST['apass']
		if AdminDetails.objects.filter(username = A_username,password = A_password).exists():
			ad = AdminDetails.objects.get(username=A_username, password=A_password)
			print('d')
			messages.info(request,'Admin login is Sucessfull')
			request.session['type_id'] = 'Admin'
			request.session['UserType'] = 'Admin'
			request.session['login'] = "Yes"
			return redirect("/")
		else:
			print('y')
			messages.error(request, 'Error wrong username/password')
			return render(request, "Admin_Login.html", {})
	else:
		return render(request, "Admin_Login.html", {})

def Patient_Login(request):
	if request.method == "POST":
		C_name = request.POST['username']
		C_password = request.POST['password']
		if Patient_Details.objects.filter(Username=C_name, Password=C_password).exists():
			users = Patient_Details.objects.all().filter(Username=C_name, Password=C_password)
			messages.info(request,C_name+ ' logged in')
			request.session['UserId'] = users[0].id
			request.session['type_id'] = 'User'
			request.session['UserType'] = C_name
			request.session['login'] = "Yes"
			return redirect("/")
		else:
			messages.error(request, 'Please Register')
			return redirect("/Patient_Registeration")
	else:
		return render(request,'Patient_Login.html',{})
	return render(request,'Patient_Login.html',{})

def Patient_Registeration(request):
	if request.method == "POST":
		Name = request.POST['Name']
		Age= request.POST['Age']
		Gender= request.POST['Gender']
		Phone= request.POST['phone']
		Address= request.POST['Address']
		Medication= request.POST['Medication']
		RFID=request.POST['rfid']
		Username= request.POST['username']
		Password= request.POST['Password']
		obj = Patient_Details(
								Name=Name
								,Age=Age
								,Gender=Gender
								,Phone=Phone
								,Address=Address
								,Medication=Medication
								,RFID=RFID
								,Username=Username
								,Password=Password)
		obj.save()
		messages.info(request,Name +" Registered")
		return redirect("/")
	else:
		return render(request,"Patient_Registeration.html",{})

def Patient_Change_Password(request):
	Userid = request.session['UserId']
	if request.method == "POST":
		newpass = request.POST['new_pass']
		confirm = request.POST['confirm_pass']
		if newpass == confirm:
			Patient_Details.objects.filter(id=Userid).update(Password=newpass)
			messages.info(request,'Password changed')
			details = Patient_Details.objects.filter(id=Userid)
			return render(request,'Patient_Change_Password.html',{'details':details})
		else:
			messages.info(request,'Passwords dont match')
			return redirect('/Patient_Change_Password')
	else:
		Userid = request.session['UserId']
		details = Patient_Details.objects.filter(id=Userid)
		return render(request,'Patient_Change_Password.html',{'details':details})

	return render(request,"Patient_Change_Password.html",{})

def Update_Patient(request):
	if request.method == "POST":
		Patient_Id = request.POST['viewid']
		Name=request.POST['viewname']
		Age=request.POST['viewage']
		Gender=request.POST['viewgender']
		Phone=request.POST['viewphone']
		Address=request.POST['viewadd']
		Medication=request.POST['viewmed']
		Patient_Details.objects.filter(id=Patient_Id).update(
															Name=Name
															,Age=Age
															,Gender=Gender
															,Phone=Phone
															,Address=Address
															,Medication=Medication
			)
		messages.info(request,"Patient Details Updated")
		return redirect('Manage_Patients')
	else:
		return render(request,"Manage_Patients.html",{})

def View_Patients(request):
	if request.method =="POST":
		searched = request.POST['searched']
		searched = str(searched)
		print(searched)
		info =Patient_Details.objects.filter(RFID=searched)
		for i in info:
			Medication = info[0].Medication
			print(Medication)
		if searched:
			details = Patient_Details.objects.filter(RFID__contains=searched)
			return render(request,"View_Patients.html",{'details':details,'searched':searched,'Medication':Medication})
		else:
			return render(request,"View_Patients.html",{})
	else:
	 	return render(request,"View_Patients.html",{})
		
def Medical_View_Patient(request):
	if request.method =="POST":
		searched = request.POST['searched']
		searched = str(searched)
		print(searched)
		info = Medicine.objects.all().filter(RFID = searched)
		if searched:
			details = Patient_Details.objects.filter(RFID__contains=searched)
			return render(request,"Medical_View_Patient.html",{'details':details})
		else:
			return render(request,"Medical_View_Patient.html",{})
	else:
	 	return render(request,"Medical_View_Patient.html",{})

def Doctor_Login(request):
	if request.method == "POST":
		C_name = request.POST['username']
		C_password = request.POST['password']
		if Doctor.objects.filter(username=C_name, password=C_password).exists():
			users = Doctor.objects.all().filter(username=C_name, password=C_password)
			messages.info(request,'Dr. '+C_name+ ' logged in')
			request.session['UserId'] = users[0].id
			request.session['type_id'] = 'Doctor'
			request.session['UserType'] = C_name
			request.session['login'] = "Yes"
			return redirect("/")
		else:
			messages.error(request, 'Please Register')
			return redirect("/Doctor_Registeration")
	else:
		return render(request,'Doctor_Login.html',{})
	return render(request,'Doctor_Login.html',{})

def Doctor_Registeration(request):
	if request.method == "POST":
		Name = request.POST['Name']
		Age= request.POST['Age']
		Gender= request.POST['Gender']
		Phone= request.POST['phone']
		Address= request.POST['Address']
		Speciality= request.POST['Speciality']
		Username= request.POST['username']
		Password= request.POST['Password']
		obj = Doctor(
								Name=Name
								,Age=Age
								,Gender=Gender
								,Phone=Phone
								,Address=Address
								,Speciality=Speciality
								,username=Username
								,password=Password)
		obj.save()
		messages.info(request,Name +" Registered")
		return redirect("/")
	else:
		return render(request,"Doctor_Registeration.html",{})
	

def Doctor_Change_Password(request):
	Userid = request.session['UserId']
	if request.method == "POST":
		newpass = request.POST['new_pass']
		confirm = request.POST['confirm_pass']
		if newpass == confirm:
			Doctor.objects.filter(id=Userid).update(password=newpass)
			messages.info(request,'Password changed')
			details = Doctor.objects.filter(id=Userid)
			return render(request,'Doctor_Change_Password.html',{'details':details})
		else:
			messages.info(request,'Passwords dont match')
			return redirect('/Doctor_Change_Password')
	else:
		Userid = request.session['UserId']
		details = Doctor.objects.filter(id=Userid)
		return render(request,'Doctor_Change_Password.html',{'details':details})

	return render(request,"Doctor_Change_Password.html",{})


def Medical_Store_Login(request):
	if request.method == "POST":
		C_name = request.POST['username']
		C_password = request.POST['password']
		if Medical_Store.objects.filter(username=C_name, password=C_password).exists():
			users = Medical_Store.objects.all().filter(username=C_name, password=C_password)
			messages.info(request,C_name+ ' logged in')
			request.session['UserId'] = users[0].id
			request.session['type_id'] = 'Medical'
			request.session['UserType'] = C_name
			request.session['login'] = "Yes"
			return redirect("/")
		else:
			messages.error(request, 'Please Register')
			return redirect("/Medical_Store_Registeration")
	else:
		return render(request,'Medical_Store_Login.html',{})
	return render(request,'Medical_Store_Login.html',{})

def Medical_Store_Change_Password(request):
	Userid = request.session['UserId']
	if request.method == "POST":
		newpass = request.POST['new_pass']
		confirm = request.POST['confirm_pass']
		if newpass == confirm:
			Medical_Store.objects.filter(id=Userid).update(password=newpass)
			messages.info(request,'Password changed')
			details = Medical_Store.objects.filter(id=Userid)
			return render(request,'Medical_Store_Change_Password.html',{'details':details})
		else:
			messages.info(request,'Passwords dont match')
			return redirect('/Medical_Store_Change_Password')
	else:
		Userid = request.session['UserId']
		details = Medical_Store.objects.filter(id=Userid)
		return render(request,'Medical_Store_Change_Password.html',{'details':details})

	return render(request,"Medical_Store_Change_Password.html",{})



def Medical_Store_Registeration(request):
	if request.method == "POST":
		Name = request.POST['Name']
		Address = request.POST['Address']
		Open = request.POST['open']
		Open = str(Open)+" AM"
		Close = request.POST['close']
		Close = str(Close)+" PM"
		username = request.POST['username']
		password = request.POST['Password']
		obj = Medical_Store(
								Name=Name
								,Address=Address
								,Open=Open
								,Close=Close
								,username=username
								,password=password)
		obj.save()
		messages.info(request,Name +" Registered")
		return redirect("/Medical_Store_Login")
	else:
		return render(request,"Medical_Store_Registeration.html",{})

def View_Medical_Store(request):
	details = Medical_Store.objects.all()
	return render(request,"View_Medical_Store.html",{'details':details})

def Add_Medication(request):
	if request.method == "POST":
		User_Id = request.POST['Addid']
		Medication = request.POST['Addmed']
		RFID = request.POST['Addrfid']
		obj = Medicine(Patient_Id=User_Id
						,RFID=RFID
						,Medicine=Medication)
		obj.save()
		messages.info(request,"Medication for "+str(RFID)+" is added")
		return redirect("/Medical_View_Patient")
	else:
		return render(request,"Medical_View_Patient.html",{})

def Treatment_Details(request):
	if request.method == "POST":
		RFID 					= request.POST['rfid']
		info = Patient_Details.objects.all().filter(RFID=RFID)
		for i in info:
			User_Id = info[0].id
			print(User_Id)
		Treatment_For 			= request.POST['T_For']
		Treatment_Duration 		= request.POST['T_Dur']
		Treatment_Description 	= request.POST['T_Des']
		obj = Treatment(Patient_Id=User_Id
						,RFID=RFID
						,Treatment_For=Treatment_For
						,Treatment_Duration=Treatment_Duration
						,Treatment_Description=Treatment_Description)
		obj.save()
		treatment = Treatment.objects.all()
		return render(request,"View_Patients.html",{'treatment':treatment})
	else:
		return render(request,"View_Patients.html",{})

def View_Treatment_Details(request,id):
	print(id)
	details = Treatment.objects.all().filter(id = id)
	for i in details:
		RFID = details[0].RFID
		print(RFID)
	return render(request,"View_Treatment_Details.html",{'details':details,'RFID':RFID})


def Add_Medical_Details(request):
	if request.method == "POST":
		RFID 					= request.POST['rfid']
		info = Patient_Details.objects.all().filter(RFID=RFID)
		for i in info:
			User_Id = info[0].id
			print(User_Id)
		BP=request.POST['BP']
		Weight=request.POST['Weight']
		Height=request.POST['Height']
		Past=request.POST['Past']
		obj = Medical_Details(
			Patient_Id=User_Id
			,RFID=RFID
			,BP=BP
			,Weight=Weight
			,Height=Height
			,Past=Past)
		obj.save()
		return render(request,"View_Patients.html",{})
	else: 
		return render(request,"View_Patients.html",{})

def Add_Medicine(request):
	if request.method == "POST":
		RFID = request.POST['rfid']
		med = request.POST['med']
		info = Patient_Details.objects.all().filter(RFID=RFID)
		for i in info:
			User_Id = info[0].id
			Present_Medicine = info[0].Medication
		obj = Medicine(Patient_Id=User_Id,RFID=RFID,medicine=med)
		obj.save()
		messages.info(request,"Medicine Added")
		return render(request,"View_Patients.html",{})
	else:
		return render(request,"View_Patients.html",{})

def View_Medicine(request,id):
	details = Medicine.objects.all().filter(Patient_Id=id)
	return render(request,"View_Medicine.html",{'details':details})


def View_Medical_Details(request,id):
	details = Medical_Details.objects.all().filter(Patient_Id = id)
	return render(request,"View_Medical_Details.html",{'details':details})

def View_Doctor(request):
	details = Doctor.objects.all()
	return render(request,"View_Doctor.html",{'details':details})

def Doctor_Profile(request):
	Userid = request.session['UserId']
	details = Doctor.objects.all().filter(id=Userid)
	return render(request,"Doctor_Profile.html",{'details':details})


def Manage_Patients(request):
	details = Patient_Details.objects.all()
	return render(request,"Manage_Patients.html",{'details':details})


def Delete_Patient(request,id):
	Patient_Details.objects.filter(id=id).delete()
	return redirect('Manage_Patients')

def Patient_Profile(request):
	Userid = request.session['UserId']
	details = Patient_Details.objects.all().filter(id=Userid)
	return render(request,"Patient_Profile.html",{'details':details})

def Logout(request):
	Session.objects.all().delete()
	return redirect("/")