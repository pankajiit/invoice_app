from rest_framework import serializers
from .models import InvoiceHeader, InvoiceItem, BillSundry


class InvoiceItemSerializer(serializers.ModelSerializer):
   def save(self, *args, **kwargs):
      self.amount = self.quantity * self.price
       
   
   def validation(self, data):
        if data['quantity'] <= 0:
                raise serializers.ValidationError("Quantity must be graterthen zero")
        
        if data["price"] <= 0:
                raise serializers.ValidationError("Price must be grater then zero")
        
        if data['amount'] <= 0:
            raise serializers.ValidationError("Amount must be graterthen zero")

        return data
        
   class Meta:
      model = InvoiceItem
      fields = "__all__"


class BillSundrySerializer(serializers.ModelSerializer):
   class Meta:
      model = BillSundry
      fields = "__all__"


class InvoiceHeaderSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True)
    billSundry = BillSundrySerializer(many=True)
    
    class Meta:
      model = InvoiceHeader
      fields = "__all__"

    def validate(self, data):
        total_item_amount = sum(item['amount'] for item in data['items'])
        total_sundry_amount = sum(sundry['amount'] for sundry in data[BillSundry])
        
        if data['amount'] != total_item_amount + total_sundry_amount:
            raise serializers.ValidationError("Total amount must be equal total item amount and total sundry amount")
    

    def create(self, validated_data):
        item_data = validated_data.pop("items")
    
    