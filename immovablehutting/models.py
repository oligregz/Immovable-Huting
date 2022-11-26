from django.db import models

class Immoble(models.Model):
  title = models.CharField(max_length=255)
  immoble_code = models.PositiveIntegerField(auto_created=True)
  guest_limit = models.IntegerField(max_length=6)
  number_of_bathorroms = models.IntegerField(max_length=3)
  accepted_pet = models.BooleanField(default=False)
  cleaning_price = models.IntegerField(max_length=3)
  date_activation = models.DateTimeField(auto_now_add=True)
  date_time_create = models.DateTimeField(auto_now_add=True)
  date_time_update = models.DateTimeField(auto_now=True)

class Annoucement(models.Model):
  immoble_id = models.ForeignKey(Immoble, on_delete=models.CASCADE)
  publishing_plataform = models.CharField(max_length=50)
  plataform_rate = models.FloatField(help_text="digite a taxa da plataforma. ex: 13.00 R$")
  date_time_create = models.DateTimeField(auto_now_add=True)
  date_time_update = models.DateTimeField(auto_now=True)
  
  
class Reserve(models.Model):
  ...