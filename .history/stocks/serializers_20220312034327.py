from .models import Stock,Mysector
from rest_framework import serializers
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        s = Stock('appl')
        f = []
        f = s.get_model_fields()
        fl=[]
        for m in f:
            fl.append(m.name)
        model = Stock
        fields=fl
class SectorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Mysector

        fields=['name','ave']
