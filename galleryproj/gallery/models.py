from django.db import models
from django.contrib.auth import get_user_model

class Photo(models.Model):
    owner = models.ForeignKey(get_user_model(), editable = False,
        on_delete=models.CASCADE, default=None)
    label = models.CharField(max_length=200)
    s3url = models.URLField(default='')
    upload_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label+":"+self.s3url
    
