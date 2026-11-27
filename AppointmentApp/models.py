from django.db import models
from django.core.validators import FileExtensionValidator
from AccountApp.models import Doctor,Patient
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
class appointment(models.Model):
    reason=models.TextField(max_length=255)
    presciption=models.FileField(
        blank=True ,
        upload_to='prescriptions/',
        validators=[FileExtensionValidator(
            allowed_extensions=['pdf'])],
            help_text="accept uniquement des fichiers pdf"
    )

    status=models.CharField(max_length=20,choices=[('pending','en attente'),('confirmed','Confirme'),('canceled','annule')],default='pending')
    duration_minutes=models.PositiveIntegerField(default=30)
    created_at=models.DateTimeField(auto_now_add=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appointments')
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='appointments')
    appointment_date=models.DateTimeField(blank=False)
    def clean(self):
        modified_date = self._state.adding or (
            appointment.objects.filter(
                pk=self.pk,
                appointment_date=self.appointment_date
            ).exists()
        )
        if self.appointment_date <= timezone.now():
            raise ValidationError("La date du rendez-vous ne peut pas être dans le passé.")
class Meta():
    ordering=['appointment_date']
    constraints=[
        models.UniqueConstraint(
            fields=['doctor','appointment_date'],
            name='unique_appointment_per_doctor',
            violation_error_message="Le docteur a déjà un rendez-vous à cette date et heure."
        )

    ]
def __str__(self):
    return f"{self.reason}"