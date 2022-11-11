from django.db import models

# Create your models here.

# rovers model
class Rovers(models.Model):
    rover_name = models.TextField()
    rover_landing_date = models.TextField()
    rover_launching_date = models.TextField()
    rover_status = models.TextField()
    max_sol = models.TextField()
    max_date = models.TextField()
    total_photos = models.IntegerField()
    first_photos = models.TextField()

# apod model
class Apod(models.Model):
    title = models.TextField()
    explaination = models.TextField()
    hdurl = models.TextField()
    media_type = models.TextField()
    urli = models.TextField()
    apod_date = models.TextField()

class Cameras(models.Model):
    cam = models.TextField()
    cam_full = models.TextField()
    rover_id = models.ForeignKey(Rovers, on_delete=models.CASCADE)