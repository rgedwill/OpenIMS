from django.db import models
from datetime import datetime
from recurrence.fields import RecurrenceField

# Create your models here.
class DeliveryType(models.Model):
    name = models.CharField(max_length=256)
    
    recurrences = RecurrenceField()

    start_date = models.DateField(auto_now_add=True, blank=True)
    next_delivery_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # save override example https://stackoverflow.com/a/11821832/5877575
        current_recurrences = self.recurrences
        first_delivery = current_recurrences.after(
            # datetime(2023, 9, 9, 0, 0, 0)        
            datetime.now()
        )
        self.next_delivery_date = first_delivery
        super(DeliveryType, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Delivery(models.Model):
    '''
    Delivery Records
    '''
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    delivery_date = models.DateField()
    delivery_type = models.ForeignKey(DeliveryType, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.delivery_date)
    

