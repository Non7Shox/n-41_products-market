from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
UserModel = get_user_model()


class VerificationCodeModel(models.Model):
    objects = None
    code = models.CharField(max_length=6, unique=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='verification_codes')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('Verification Code')
        verbose_name_plural = _('Verification Codes')


class TeamModel(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _('name')
        verbose_name_plural = _('names')



