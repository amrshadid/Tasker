from django.db import models
from django.contrib.auth import get_user_model
from dashboard.models import panel
User = get_user_model()


# Create your models here.
class ticket(models.Model):
    class status(models.IntegerChoices):
        Wating = 1
        under_process = 2
        done = 3
        total = 4

    title = models.CharField(blank=False,max_length=255,)
    panel = models.ForeignKey(panel, related_name='panel',on_delete=models.CASCADE ,default="" )
    content = models.TextField(blank=False)
    status = models.IntegerField(choices=status.choices, default= 1)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE ,default="")
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    ticket = models.ForeignKey(ticket, related_name='Comment',on_delete=models.CASCADE)
    body = models.CharField(blank=False,max_length=200)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at  = models.DateTimeField()

    def __str__(self):
        return self.body
