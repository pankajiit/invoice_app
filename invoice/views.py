from django.shortcuts import render
from rest_framework import viewsets
from .models import InvoiceHeader, InvoiceItem, BillSundry
from .serializers import InvoiceHeaderSerializer, InvoiceItemSerializer, BillSundrySerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = InvoiceHeader.objects.all()
    serializer_class = InvoiceHeaderSerializer