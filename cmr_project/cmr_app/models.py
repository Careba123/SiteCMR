from django.db import models
from django.contrib.auth.models import User

class CMR(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='cmrs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CMR {self.id} uploaded by {self.user.username}"
