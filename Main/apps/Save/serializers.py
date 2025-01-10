# Project
from .income_models.transactions import Fixed_Cost, Gain, Loss, Economy
from .income_models.variable import Variable_Cost
from .models import Save

# Libs
from rest_framework import serializers

class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = '__all__'

class Fixed_CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixed_Cost
        fields = '__all__'

class GainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gain
        fields = '__all__'

class LossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loss
        fields = '__all__'

class EconomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Economy
        fields = '__all__'

class Variable_CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variable_Cost
        fields = '__all__'