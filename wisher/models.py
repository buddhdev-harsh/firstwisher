from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class birthdays(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE , related_name = 'user')
    human = models.CharField(max_length = 15,null = False)
    birthdate = models.DateTimeField(null = False)
    emailtosend = models.EmailField(max_length = 254)
    msg = models.CharField(max_length = 150)
     
    def __str__(self):
        return self.user.username
