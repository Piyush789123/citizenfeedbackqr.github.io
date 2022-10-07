from django.db import models

# Create your models here.
class Feedback(models.Model):
    rating = (
        (1,'very bad'),
        (2,'Bad'),
        (3,'Okay'),
        (4,'Good'),
        (5,'Excellent')
    )
    type = (('positive','positive'),('negative','negative'))

    reason_to_come = models.CharField("How did you come to the police station",max_length=100, null=True)
    waiting_time = models.CharField(max_length=30)
    overall = models.IntegerField(choices=rating,default=3)
    behaviour = models.IntegerField(choices=rating,default=3)
    servicing = models.IntegerField(choices=rating,default=3)
    type_feedback = models.CharField(max_length=11,choices=type,null=True, blank=True)
    city = models.CharField(max_length=30)
    police_name = models.CharField(max_length=50,null=True)
    feedback = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f"Feedback for {self.police_name}"

class VerificationCodes(models.Model):
    phone = models.CharField(max_length=12, null=True, blank=True)
    otp = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)