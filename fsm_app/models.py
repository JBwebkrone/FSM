from django.db import models
from django_fsm import FSMIntegerField, transition

STATUS_CREATED = 0
STATUS_PAID = 1
STATUS_FULFILLED = 2
STATUS_CANCELLED = 3
STATUS_RETURNED = 4

STATUS_CHOICES = (
    (STATUS_CREATED, 'created'),
    (STATUS_PAID, 'paid'),
    (STATUS_FULFILLED, 'fullfilled'),
    (STATUS_CANCELLED, 'cancelled'),
    (STATUS_RETURNED, 'returned'),
)


class Order(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    product = models.CharField(max_length=128)
    status = FSMIntegerField(choices=STATUS_CHOICES, default=STATUS_CREATED, protected=True)


    @transition(field=status, source=STATUS_CREATED, target=STATUS_PAID)
    def pay(self, amount):
        self.amount = amount
        print(f'Pay amount {self.amount} for the order')
    

    @transition(field=status, source=STATUS_PAID, target=STATUS_FULFILLED)
    def fulfill(self):
        print("Fulfill the order")
    

    @transition(field=status, source=[STATUS_CREATED, STATUS_PAID], target=STATUS_CANCELLED)
    def cancel(self):
        print("Cancel the order")
    
    @transition(field=status, source=STATUS_FULFILLED, target=STATUS_RETURNED)
    def _return(self):
        print("Return the order")


    def __str__(self):
        return self.product