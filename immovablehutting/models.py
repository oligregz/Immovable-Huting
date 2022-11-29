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
  immoble_code = models.BigIntegerField(max_length=10, blank=True, null=True)
  guest_limit = models.IntegerField(max_length=1, choices=guests, blank=True, null=True)
  number_of_bathorroms = models.IntegerField(max_length=3, blank=True, null=True)
  accepted_pet = models.BooleanField(default=False)
  cleaning_price = models.IntegerField(max_length=3, blank=True, null=True)
  activation = models.DateField(auto_now_add=True, blank=True)
  create = models.DateTimeField(default="2006-02-15 05:03:42")
  update = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.title

class Annoucement(models.Model):
  immoble_id = models.ForeignKey(Immoble, on_delete=models.CASCADE, blank=True, null=True)
  publishing_plataform = models.CharField(max_length=50, blank=True, null=True)
  plataform_rate = models.FloatField(help_text="digite a taxa da plataforma. ex: 13.00", blank=True, null=True)
  create = models.DateTimeField(auto_now_add=True)
  update = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.publishing_plataform
  
  def get_actions(self, request):
    actions = super(models, self).get_actions(request)
    del actions['delete_selected']
    return actions
  
  def has_delete_permission(self, request, obj=None):
    return False
 
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
  total_price = models.FloatField(help_text="digite o valor da reserva total da reserva(ex: 952.38)", blank=True, null=True)
  comment_field = models.CharField(max_length=255, blank=True, null=True)
  number_of_guests = models.IntegerField(max_length=1, choices=guests, blank=True, null=True)
  check_in_date = models.DateField(auto_now_add=True)
  check_out_date = models.DateField(auto_now=True)
  create = models.DateTimeField(auto_now_add=True)
  update = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f'code:{self.reserve_code} | {self.comment_field} | {self.total_price}'