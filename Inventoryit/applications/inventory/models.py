from django.db import models

from .managers import InventoryManagers

class Inventory(models.Model):

    LAPTOPS='0'
    DESKTOP='1'
    SURFACE='2'

    MODEL_TEAM=[
        (LAPTOPS,'Laptops'),
        (DESKTOP,'Desktop'),
        (SURFACE,'Surface'),
    
    ]


    location = models.CharField('Location', max_length=100)
    direction = models.CharField('Direction', max_length=150)
    hostname = models.CharField('Hostanme', max_length=50)
    nuuma = models.CharField('Nuuma', max_length=70)
    serial_number = models.CharField('Serial number', max_length=50)
    product_number = models.CharField('Product number', max_length=50,blank= True)
    mac_address= models.CharField('MAC',max_length=50)
    mac_wifi = models.CharField('MAC WIFI', max_length=50, blank=True)
    manufacturer = models.CharField('Manufacturer', max_length=50)
    name = models.CharField('Name', max_length=50)
    model = models.CharField('Model', max_length=1, choices=MODEL_TEAM)
    observations= models.CharField('Observations', max_length=70)
    warranty= models.CharField('Warranty', max_length=50, blank=True)

    objects= InventoryManagers()

    class Meta:
        verbose_name='Inventory'
        verbose_name_plural='Inventories'
        ordering=['id']

    def __str__(self):
        return self.nuuma + ' - ' + self.hostname

"""Change control"""


class ChangeControl(models.Model):  
    
    tracing_number= models.IntegerField()
    date= models.DateField()
    field_host= models.CharField('Hostname/NºSerial',max_length=50,blank=True)
    ticket = models.CharField('IM or RF', max_length=50,blank=True)
    comments = models.CharField('Comments', max_length=100, blank=True)

    class Meta:
        verbose_name='Change control'
        ordering=['tracing_number']

    def __str__(self):
        return str(self.id) + '-' + self.ticket + ' - ' + self.field_host


