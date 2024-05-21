from django.db import models

class InvoiceHeader(models.Model):
    id = models.UUIDField(primary_key=True)
    invoiceNumber = models.IntegerField()
    customerName =  models.CharField(max_length=30)
    billingAddress =  models.CharField(max_length=50)
    shippingAddress = models.CharField(max_length=50)
    GSTIN = models.CharField(max_length=30)
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)



class InvoiceItem(models.Model):
    id = models.UUIDField(primary_key=True)
    itemName = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2) 


class BillSundry(models.Model):
    id = models.UUIDField(primary_key=True)
    billSundryName = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)














 
    
