# Project
from .income_models.transactions import Fixed_Cost, Gain, Loss, Economy
from .income_models.variable import Variable_Cost

# Libs
from django.db import models

# Create your models here.
class Save(models.Model):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='ID SAVE', db_column='IDSave')
    name = models.CharField(default='Cofre Novo', max_length=255, verbose_name='Name', db_column='Name')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date', db_column='CreationDate')
    total_amount = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Total Amount', db_column='TotalAmount')
    total_saved = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Total Saved', db_column='TotalSaved')
    # fk_owner_id = models.ForeignKey('Account', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Save'
        verbose_name = 'Save'
        verbose_name_plural = 'Saves'
        ordering = ['created_at']
