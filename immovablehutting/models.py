from django.db import models

class Immoble(models.Model):
  guests = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
  ]
  title = models.CharField(max_length=255)
  immoble_code = models.PositiveIntegerField(auto_created=True, unique=True, blank=True)
  guest_limit = models.IntegerField(max_length=1, choices=guests)
  number_of_bathorroms = models.IntegerField(max_length=3)
  accepted_pet = models.BooleanField(default=False)
  cleaning_price = models.IntegerField(max_length=3)
  date_activation = models.DateTimeField(auto_now_add=True)
  date_time_create = models.DateTimeField(auto_now_add=True)
  date_time_update = models.DateTimeField(auto_now=True)

class Annoucement(models.Model):
  immoble_id = models.ForeignKey(Immoble, on_delete=models.CASCADE)
  publishing_plataform = models.CharField(max_length=50)
  plataform_rate = models.FloatField(help_text="digite a taxa da plataforma. ex: 13.00")
  date_time_create = models.DateTimeField(auto_now_add=True)
  date_time_update = models.DateTimeField(auto_now=True)
 
class Reserve(models.Model):
  guests = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
  ]
  reserve_code = models.PositiveIntegerField(auto_created=True, unique=True)
  annoucement_id = models.ForeignKey(Annoucement, on_delete=models.SET_NULL, related_name="id_annoucement", null=True)
  total_price = models.FloatField(help_text="digite o valor da reserva total da reserva(ex: 952.38)")
  comment_field = models.CharField(max_length=255)
  number_of_guests = models.IntegerField(max_length=1, choices=guests)
  check_in_date = models.DateField(auto_now_add=True)
  check_out_date = models.DateField(auto_now=True)
  date_time_create = models.DateTimeField(auto_now_add=True)
  date_time_update = models.DateTimeField(auto_now=True)
