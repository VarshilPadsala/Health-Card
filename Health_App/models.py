from django.db import models


# Create your models here.

class AdminDetails(models.Model):
	username = models.CharField(max_length=100,default=None)
	password = models.CharField(max_length=100,default=None)
	class Meta:
		db_table = 'AdminDetails'

class Patient_Details(models.Model):
	Name 		= models.CharField(max_length=100,default=None)
	Age 		= models.CharField(max_length=100,default=None)
	Gender 		= models.CharField(max_length=100,default=None)
	Phone 		= models.CharField(max_length=100,default=None)
	Address 	= models.CharField(max_length=100,default=None)
	Medication 	= models.CharField(max_length=100,default=None,null=True)
	Treatment 	= models.CharField(max_length=100,default=None,null=True)
	Medical 	= models.CharField(max_length=100,default=None,null=True)
	RFID 		= models.CharField(max_length=100,default=None)
	Username 	= models.CharField(max_length=100,default=None)
	Password 	= models.CharField(max_length=100,default=None)
	class Meta:
		db_table='Patient_Details'

class Medical_Store(models.Model):
	Name = models.CharField(max_length=100,default=None)
	Address = models.CharField(max_length=100,default=None)
	Open = models.CharField(max_length=100,default=None)
	Close = models.CharField(max_length=100,default=None)
	username = models.CharField(max_length=100,default=None)
	password = models.CharField(max_length=100,default=None)
	class Meta:
		db_table = 'Medical_Store'

class Doctor(models.Model):
	Name 		= models.CharField(max_length=100,default=None)
	username 	= models.CharField(max_length=100,default=None)
	password 	= models.CharField(max_length=100,default=None)
	Age 		= models.CharField(max_length=100,default=None)
	Gender 		= models.CharField(max_length=100,default=None)
	Phone 		= models.CharField(max_length=100,default=None)
	Address 	= models.CharField(max_length=100,default=None)
	Speciality 	= models.CharField(max_length=100,default=None)
	class Meta:
		db_table = 'Doctor'

class Medicine(models.Model):
	Patient_Id =models.CharField(max_length=100,default=None)
	RFID = models.CharField(max_length=100,default=None)
	medicine = models.CharField(max_length=100,default=None)
	class Meta:
		db_table = 'Medicine'

class Treatment(models.Model):
	Patient_Id = models.CharField(max_length=100,default=None,null=True)
	RFID = models.CharField(max_length=100,default=None)
	Treatment_For = models.CharField(max_length=100,default=None)
	Treatment_Duration= models.CharField(max_length=100,default=None)
	Treatment_Description = models.CharField(max_length=500,default=None)
	class Meta:
		db_table = 'Treatment'

class Medical_Details(models.Model):
	Patient_Id = models.CharField(max_length=100,default=None,null=True)
	RFID = models.CharField(max_length=100,default=None)
	BP= models.CharField(max_length=100,default=None)
	Weight= models.CharField(max_length=100,default=None)
	Height= models.CharField(max_length=100,default=None)
	Past= models.CharField(max_length=100,default=None)
	class Meta:
		db_table = 'Medical_Details'

		
		
