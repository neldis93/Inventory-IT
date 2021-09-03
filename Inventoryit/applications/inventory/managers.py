from django.db import models
from django.db.models import Q

class InventoryManagers(models.Manager):
    def list_all_filter(self,keyword, acronym):
        result= self.filter(
            Q(nuuma__icontains=keyword) | Q(location__icontains=keyword)
        )
        if acronym is not None:
            return result.filter(
                hostname__startswith= acronym
            )
        
       
        
           
