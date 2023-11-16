from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # Get the fields from teh incoming data (if available)
        incoming_fields = kwargs.pop('fields', None)

        # Call the parent __init__ method
        super().__init__(*args, **kwargs)

        # If incoming fields are specified, filter the fields based on them
        if incoming_fields:
            allowed_fields = set(incoming_fields) & set(self.fields.keys())
            self.fields = {field: self.fields[field] for field in allowed_fields}