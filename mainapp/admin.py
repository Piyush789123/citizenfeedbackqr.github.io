from django.contrib import admin
from .models import Feedback, VerificationCodes
# Register your models here.
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['reason_to_come','waiting_time','overall','behaviour','servicing','type_feedback','city','police_name','feedback']

@admin.register(VerificationCodes)
class VerificationCodesAdmin(admin.ModelAdmin):
    list_display = ['email',
    'phone',
    'otp',]