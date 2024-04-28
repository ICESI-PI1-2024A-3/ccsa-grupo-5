from django.utils import timezone
from django.db import models
from login.models import User

# Create your models here.


class AbstractPetition(models.Model):
    """
    Abstract model representing a petition.
    """
    states = [
        ("pendiente", "Pendiente"),
        ("aprobado", "Aprobado"),
        ("en_proceso", "En Proceso"),
        ("rechazado", "Rechazado"),
    ]
    petitionDate = models.DateField(
        default=timezone.now, verbose_name="Fecha de solicitud"
    )
    percentage = models.IntegerField(default=0, verbose_name="Porcentaje")
    startDate = models.DateField(verbose_name="Fecha de inicio")
    endDate = models.DateField(verbose_name="Fecha de fin")
    state = models.CharField(max_length=20, choices=states, verbose_name="Estado")
    cenco = models.CharField(max_length=20, verbose_name="Centro de Costo")
    fullName = models.CharField(max_length=255, verbose_name="Nombre completo")
    identityDocument = models.CharField(
        max_length=20, verbose_name="Documento de identidad"
    )
    email = models.EmailField(verbose_name="Correo electrónico")
    phoneNumber = models.CharField(max_length=15, verbose_name="Número de teléfono")
    
    userAsigner = models.ForeignKey(
        User,
        related_name="userAsigner",
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Usuario Asignador",
    )
    
    user = models.ForeignKey(
        User,
        related_name="petitionUser",
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Usuario",
    )
    
    def getPercentage(self):
        petition = Petition.objects.get(pk=self.id)
        tasks = Task.objects.filter(petition=petition)
        tasks_count = petition.tasks.count()
        completed_tasks_count = petition.tasks.filter(isComplete=True).count()

        # Calculate the percentage of tasks completed
        if tasks_count > 0:
            completion_percentage = round((completed_tasks_count / tasks_count) * 100)
        else:
            completion_percentage = 0
        return completion_percentage

    def getState(self):
        """
        Method to get the state of the petition.
        """
        if self.state == "aprobado":
            return "Aprobado"
        elif self.state == "pendiente":
            return "Pendiente"
        elif self.state == "en_proceso":
            return "En Proceso"
        elif self.state == "rechazado":
            return "Rechazado"
        else:
            return "Estado Desconocido"

    def getUser(self):
        """
        Method to get the user associated with the petition.
        """
        if self.user is None:
            return "Sin Asignar"
        else:
            return self.user.first_name + " " + self.user.last_name

    getUser.short_description = "Gestor asignado"

    def __str__(self):
        """
        String representation of the petition.
        """
        userInfo = (
            f" Gestor asignado: {self.user.first_name} {self.user.last_name}"
            if self.user
            else "Gestor: Sin Asignar"
        )
        return f"ID solicitud: {self.id} | {userInfo}"

    class Meta:
        abstract = True
        verbose_name = "Petición Abstracta"
        verbose_name_plural = "Peticiones Abstractas"


class Petition(AbstractPetition):
    class Meta:
        verbose_name = "Petición"
        verbose_name_plural = "Peticiones"


class Observation(models.Model):
    """
    Model representing an observation.
    """
    description = models.TextField(verbose_name="Descripción")
    date = models.DateField(verbose_name="Fecha")
    time = models.TimeField(verbose_name="Hora")
    author = models.CharField(max_length=50, verbose_name="Autor")
    petition = models.ForeignKey(
        Petition,
        related_name="observations",
        on_delete=models.CASCADE,
        verbose_name="Petición",
    )
    class Meta:
        verbose_name = "Observación"
        verbose_name_plural = "Observaciones"


class TaskPredeterminate(models.Model):
    description = models.TextField(verbose_name="Descripción")
    isComplete = models.BooleanField(
        default=False, verbose_name=""
    )
    admin = models.ForeignKey(User, related_name="taskAdmin", on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Tarea Predeterminada"
        verbose_name_plural = "Tareas Predeterminadas"

class Task(models.Model):
    description = models.TextField(verbose_name="Descripción")
    isComplete = models.BooleanField(
        default=False, verbose_name=""
    )
    petition = models.ForeignKey(Petition, related_name="tasks", on_delete=models.CASCADE, verbose_name="Petición")
    
    def yesOrNoComplete(self):
        """
        Method to return Yes or No based on isComplete field.
        """
        if self.isComplete:
            return "✔️"
        else:
            return "❌"
        
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"



class Monitoring(Petition):
    """
    Model representing a monitoring petition.
    """
    monitoringTypeChoices = [
        ("academica", "Académica"),
        ("oficina", "Oficina"),
    ]
    hasMoneyInCenco = models.BooleanField(
        default=False, verbose_name="¿Tiene dinero en CENCO?"
    )
    cencoResponsible = models.CharField(
        max_length=255, verbose_name="Responsable de CENCO"
    )
    monitoringType = models.CharField(
        max_length=20, choices=monitoringTypeChoices, verbose_name="Tipo de Monitoreo"
    )
    studentCode = models.CharField(max_length=20, verbose_name="Código de estudiante")
    daviPlata = models.CharField(max_length=20, verbose_name="DaviPlata")
    projectOrCourse = models.CharField(max_length=255, verbose_name="Proyecto o Curso")
    monitoringDescription = models.TextField(verbose_name="Descripción del monitoreo")
    hoursPerWeek = models.PositiveIntegerField(verbose_name="Horas por semana")
    totalPaymentAmount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Monto total de pago"
    )
    isOneTimePayment = models.BooleanField(
        default=False, verbose_name="Es un pago único"
    )

    def yesOrNoCenco(self):
        """
        Method to return Yes or No based on hasMoneyInCenco field.
        """
        if self.hasMoneyInCenco:
            return "Si"
        else:
            return "No"

    def yesOrNoPayment(self):
        """
        Method to return Yes or No based on isOneTimePayment field.
        """
        if self.isOneTimePayment:
            return "Si"
        else:
            return "No"

    def getPetitionType(self):
        """
        Method to get the type of petition.
        """
        return "Monitoria"

    getPetitionType.short_description = "Tipo de solicitud"

    def __str__(self):
        """
        String representation of the monitoring petition.
        """
        return f"Nombre Completo: {self.fullName}\nCódigo de Estudiante: {self.studentCode}\nDocumento de Identidad: {self.identityDocument}\nCorreo Electrónico: {self.email}\nNúmero de Teléfono: {self.phoneNumber}\nDAVI Plata: {self.daviPlata}\nProyecto o Curso: {self.projectOrCourse}\nDescripción del Monitoreo: {self.monitoringDescription}\nFecha de Inicio: {self.startDate}\nFecha de Fin: {self.endDate}\nHoras por Semana: {self.hoursPerWeek}\nMonto Total de Pago: {self.totalPaymentAmount}\nTipo de Monitoreo: {self.monitoringType}\nCentro de Costo: {self.cenco}\n¿Tiene Dinero en CENCO?: {self.hasMoneyInCenco}\nResponsable de CENCO: {self.cencoResponsible}\nEs un Pago Único: {self.isOneTimePayment}"

    class Meta:
        verbose_name = "Monitoria"
        verbose_name_plural = "Monitorias"


class Other(Petition):
    """
    Model representing other types of petitions.
    """
    petitionType = [
        ("serviceProvision", "Prestación de Servicios"),
        ("practicing", "Practicante"),
    ]
    bankTypeAccount = [
        ("Ahorro", "Ahorro"),
        ("Corriente", "Corriente"),
    ]
    personType = models.CharField(
        max_length=50, choices=petitionType, verbose_name="Tipo de Petición"
    )
    requesterName = models.CharField(
        max_length=255, verbose_name="Nombre del solicitante"
    )
    requesterFaculty = models.CharField(
        max_length=255, verbose_name="Facultad del solicitante"
    )

    motive = models.CharField(max_length=255, verbose_name="Motivo")
    bankEntity = models.CharField(max_length=255, verbose_name="Entidad Bancaria")
    bankAccountType = models.CharField(
        max_length=50, choices=bankTypeAccount, verbose_name="Tipo de Cuenta Bancaria"
    )
    bankAccountNumber = models.CharField(
        max_length=50, verbose_name="Número de Cuenta Bancaria"
    )
    eps = models.CharField(max_length=255, verbose_name="EPS")
    pensionFund = models.CharField(max_length=255, verbose_name="Fondo de Pensiones")
    arl = models.CharField(max_length=255, verbose_name="ARL")
    contractValue = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Valor del Contrato"
    )
    paymentInfo = models.TextField(verbose_name="Información de Pago")
    rutAttachment = models.FileField(upload_to="rut/", verbose_name="Adjunto RUT")

    def getPetitionType(self):
        """
        Method to get the type of petition.
        """
        if self.personType == "serviceProvision":
            return "Prestación de Servicios"
        else:
            return "Practicante"

    getPetitionType.short_description = "Tipo de solicitud"

    def __str__(self):
        """
        String representation of the Other petition.
        """
        return f"Requester Name: {self.requesterName}\nRequester Faculty: {self.requesterFaculty}\nContractor Full Name: {self.fullName}\nContractor Identity Number: {self.identityDocument}\nContractor Phone Number: {self.phoneNumber}\nContractor Email: {self.email}\nCENCO: {self.cenco}\nMotive: {self.motive}\nStart Date: {self.startDate}\nEnd Date: {self.endDate}\nBank Entity: {self.bankEntity}\nBank Account Type: {self.bankAccountType}\nBank Account Number: {self.bankAccountNumber}\nEPS: {self.eps}\nPension Fund: {self.pensionFund}\nARL: {self.arl}\nRUT Attachment: {self.rutAttachment}\nContract Value: {self.contractValue}\nPayment Info: {self.paymentInfo}"

    class Meta:
        verbose_name = "Otro tipo"
        verbose_name_plural = "Otros tipos"
