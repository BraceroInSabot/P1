from django.db import models

class Variable_Cost(models.Model):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='ID VC', db_column='IDVariableCost')
    name = models.CharField(max_length=155, verbose_name='Name', db_column='Name')
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Value', db_column='Value')
    variable_type = models.CharField(max_length=2, verbose_name='Type', db_column='Type')
    is_active = models.BooleanField(default=True, verbose_name='Is Active', db_column='IsActive')
    id_transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE, db_column='IDTransaction')

    def __str__(self):
        name = f"{self.name} ($ {self.value})"
        return name
    
    class Meta:
        db_table = 'Variable_Cost'
        verbose_name = 'Variable Cost'
        verbose_name_plural = 'Variable Costs'