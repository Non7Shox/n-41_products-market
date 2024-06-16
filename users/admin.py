from django.contrib import admin

from users.models import VerificationCodeModel, TeamModel

# Register your models here.
admin.site.register(VerificationCodeModel)
admin.site.register(TeamModel)




