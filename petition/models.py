from django.utils import timezone
from django.db import models
from login.models import User

# Create your models here.


class AbstractPetition(models.Model):
    states = [
        ("pendiente", "Pendiente"),
        ("aprobado", "Aprobado"),
        ("en_proceso", "En Proceso"),
        ("rechazado", "Rechazado"),
    ]
    petitionDate = models.DateField(
        default=timezone.now, verbose_name="Fecha de solicitud"
    )
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

    def getUser(self):
        if self.user is None:
            return "Sin Asignar"
        else:
            return self.user.first_name + " " + self.user.last_name

    getUser.short_description = "Gestor asignado"

    def __str__(self):
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


class Monitoring(Petition):
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

    getPetitionType.short_description = "Tipo de solicitud"

    def __str__(self):
        return f"Nombre Completo: {self.fullName}\nCódigo de Estudiante: {self.studentCode}\nDocumento de Identidad: {self.identityDocument}\nCorreo Electrónico: {self.email}\nNúmero de Teléfono: {self.phoneNumber}\nDAVI Plata: {self.daviPlata}\nProyecto o Curso: {self.projectOrCourse}\nDescripción del Monitoreo: {self.monitoringDescription}\nFecha de Inicio: {self.startDate}\nFecha de Fin: {self.endDate}\nHoras por Semana: {self.hoursPerWeek}\nMonto Total de Pago: {self.totalPaymentAmount}\nTipo de Monitoreo: {self.monitoringType}\nCentro de Costo: {self.cenco}\n¿Tiene Dinero en CENCO?: {self.hasMoneyInCenco}\nResponsable de CENCO: {self.cencoResponsible}\nEs un Pago Único: {self.isOneTimePayment}"

    class Meta:
        verbose_name = "Monitoria"
        verbose_name_plural = "Monitorias"


class Other(Petition):
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
        if self.personType == "serviceProvision":
            return "Prestación de Servicios"
        else:
            return "Practicante"

    getPetitionType.short_description = "Tipo de solicitud"

    def __str__(self):
        return f"Requester Name: {self.requesterName}\nRequester Faculty: {self.requesterFaculty}\nContractor Full Name: {self.fullName}\nContractor Identity Number: {self.identityDocument}\nContractor Phone Number: {self.phoneNumber}\nContractor Email: {self.email}\nCENCO: {self.cenco}\nMotive: {self.motive}\nStart Date: {self.startDate}\nEnd Date: {self.endDate}\nBank Entity: {self.bankEntity}\nBank Account Type: {self.bankAccountType}\nBank Account Number: {self.bankAccountNumber}\nEPS: {self.eps}\nPension Fund: {self.pensionFund}\nARL: {self.arl}\nRUT Attachment: {self.rutAttachment}\nContract Value: {self.contractValue}\nPayment Info: {self.paymentInfo}"

    class Meta:
        verbose_name = "Otro tipo"
        verbose_name_plural = "Otros tipos"
