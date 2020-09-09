from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class panel(models.Model):
    name = models.CharField(blank=False,max_length=255,)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name

class panelMember(models.Model):
    panel = models.ForeignKey(panel,related_name='panel_member',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_panel',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("panel", "user")
