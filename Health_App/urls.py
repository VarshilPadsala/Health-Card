from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
				path('',views.Home,name="Home"),
				path('Admin_Login/',views.Admin_Login,name="Admin_Login"),
				path('Patient_Login/',views.Patient_Login,name="Patient_Login"),
				path('Patient_Registeration/',views.Patient_Registeration,name="Patient_Registeration"),
				path('Patient_Change_Password/',views.Patient_Change_Password,name="Patient_Change_Password"),
				path('Update_Patient/',views.Update_Patient,name="Update_Patient"),
				path('View_Patients/',views.View_Patients,name="View_Patients"),
				path('Doctor_Login/',views.Doctor_Login,name="Doctor_Login"),
				path('Doctor_Registeration/',views.Doctor_Registeration,name="Doctor_Registeration"),
				path('Doctor_Change_Password/',views.Doctor_Change_Password,name="Doctor_Change_Password"),
				path('Medical_Store_Login/',views.Medical_Store_Login,name="Medical_Store_Login"),
				path('Medical_Store_Registeration/',views.Medical_Store_Registeration,name="Medical_Store_Registeration"),
				path('Medical_Store_Change_Password/',views.Medical_Store_Change_Password,name="Medical_Store_Change_Password"),
				path('Medical_View_Patient/',views.Medical_View_Patient,name="Medical_View_Patient"),
				path('View_Medical_Store/',views.View_Medical_Store,name="View_Medical_Store"),
				path('Add_Medication/',views.Add_Medication,name="Add_Medication"),
				path('Treatment_Details/',views.Treatment_Details,name="Treatment_Details"),
				path('View_Doctor/',views.View_Doctor,name="View_Doctor"),
				path('Manage_Patients/',views.Manage_Patients,name="Manage_Patients"),
				path('Doctor_Profile/',views.Doctor_Profile,name="Doctor_Profile"),
				path('View_Treatment_Details/<int:id>',views.View_Treatment_Details,name="View_Treatment_Details"),
				path('Add_Medical_Details/',views.Add_Medical_Details,name="Add_Medical_Details"),
				path('View_Medical_Details/<int:id>',views.View_Medical_Details,name="View_Medical_Details"),
				path('Add_Medicine/',views.Add_Medicine,name="Add_Medicine"),
				path('Patient_Profile/',views.Patient_Profile,name="Patient_Profile"),
				path('View_Medicine/<int:id>',views.View_Medicine,name="View_Medicine"),
				path('Delete_Patient/<int:id>',views.Delete_Patient,name="Delete_Patient"),
				path('Logout/',views.Logout,name="Logout"),
				

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)