from django.db import models

class wxapp(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    data = models.TextField()

    def __str__(self):
        return self.name[:20] + ':' + self.data[:200]
