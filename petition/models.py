from django.utils import timezone
from django.db import models
from login.models import User

# Create your models here.

class AbstractPetition(models.Model):
    states = [
    ('pendiente', 'Pendiente'),
    ('aprobado', 'Aprobado'),
    ('en_proceso', 'En Proceso'),
    ('rechazado', 'Rechazado'),]
    petitionDate = models.DateField(default=timezone.now)
    startDate = models.DateField()
    endDate = models.DateField()
    state = models.CharField(max_length = 20, choices = states)
    cenco = models.CharField(max_length = 20)
    fullName = models.CharField(max_length = 255)
    identityDocument = models.CharField(max_length = 20)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length = 15)
    user = models.ForeignKey(User, related_name='petitionUser', on_delete=models.CASCADE)
    class Meta:
        abstract = True
    
class Petition(AbstractPetition):
    pass
        
class Observation(models.Model):
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    author = models.CharField(max_length = 50)
    
    petition = models.ForeignKey(Petition, related_name='observations', on_delete=models.CASCADE)
    

class Monitoring(Petition):
    monitoringTypeChoices = [
    ('academica', 'Academica'),
    ('oficina', 'Oficina'),]
    hasMoneyInCenco = models.BooleanField(default = False)
    cencoResponsible = models.CharField(max_length = 255)
    monitoringType = models.CharField(max_length = 20, choices = monitoringTypeChoices)
    studentCode = models.CharField(max_length = 20)
    daviPlata = models.CharField(max_length = 20)
    projectOrCourse = models.CharField(max_length = 255)
    monitoringDescription = models.TextField()
    hoursPerWeek = models.PositiveIntegerField()
    totalPaymentAmount = models.DecimalField(max_digits = 10, decimal_places = 2)
    isOneTimePayment = models.BooleanField(default = False)
    def yesOrNoCenco(self):
        if self.hasMoneyInCenco:
            return "Si"
        else:
            return "No"
    def yesOrNoPayment(self):
        if self.isOneTimePayment:
            return "Si"
        else:
            return "No"
    
    def getPetitionType(self):
        return "Monitoria"
    
    def __str__(self):
        return f"Full Name: {self.fullName}\nStudent Code: {self.studentCode}\nIdentity Document: {self.identityDocument}\nEmail Address: {self.email}\nPhone Number: {self.phoneNumber}\nDAVI Plata: {self.daviPlata}\nProject or Course: {self.projectOrCourse}\nMonitoring Description: {self.monitoringDescription}\nStart Date: {self.startDate}\nEnd Date: {self.endDate}\nHours Per Week: {self.hoursPerWeek}\nTotal Payment Amount: {self.totalPaymentAmount}\nMonitoring Type: {self.monitoringType}\nCenco: {self.cenco}\nHas Money in Cenco: {self.hasMoneyInCenco}\nCenco Responsible: {self.cencoResponsible}\nIs One-Time Payment: {self.isOneTimePayment}"
    
class Other(Petition):
    petitionType = [('serviceProvision', 'ServiceProvision'), ('practicing', 'Practicing')]
    bankTypeAccount = [
        ('Ahorro', 'Ahorro'),
        ('Corriente', 'Corriente'),]
    personType = models.CharField(max_length=50, choices=petitionType)
    requesterName = models.CharField(max_length=255)
    requesterFaculty = models.CharField(max_length=255)
    
    motive = models.CharField(max_length=255)
    bankEntity = models.CharField(max_length=255)
    bankAccountType = models.CharField(max_length=50, choices=bankTypeAccount)
    bankAccountNumber = models.CharField(max_length=50)
    eps = models.CharField(max_length=255)
    pensionFund = models.CharField(max_length=255)
    arl = models.CharField(max_length=255)
    contractValue = models.DecimalField(max_digits=10, decimal_places=2)
    paymentInfo = models.TextField()
    rutAttachment = models.FileField(upload_to="data/")
    
    def getPetitionType(self):
        if self.personType == 'serviceProvision':
            return "Prestación de Servicios"
        else:
            return "Practicante"
    
    def __str__(self):
        return f"Requester Name: {self.requesterName}\nRequester Faculty: {self.requesterFaculty}\nContractor Full Name: {self.fullName}\nContractor Identity Number: {self.identityDocument}\nContractor Phone Number: {self.phoneNumber}\nContractor Email: {self.email}\nCENCO: {self.cenco}\nMotive: {self.motive}\nStart Date: {self.startDate}\nEnd Date: {self.endDate}\nBank Entity: {self.bankEntity}\nBank Account Type: {self.bankAccountType}\nBank Account Number: {self.bankAccountNumber}\nEPS: {self.eps}\nPension Fund: {self.pensionFund}\nARL: {self.arl}\nRUT Attachment: {self.rutAttachment}\nContract Value: {self.contractValue}\nPayment Info: {self.paymentInfo}"
    