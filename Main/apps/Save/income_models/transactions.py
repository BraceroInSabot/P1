from django.db import models

class Fixed_Cost(models.Model):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='ID FC', db_column='IDFixedCost')
    expected_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Expected Value', db_column='ExpectedValue')
    real_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Real Value', db_column='RealValue') 
    id_save = models.ForeignKey('Save', on_delete=models.CASCADE)

    def __str__(self):
        name = f"{self.id_save.name} - FIXED COST - ${round(self.real_value, 2)}"
        return name
    
    class Meta:
        db_table = 'Fixed_Cost'
        verbose_name = 'Fixed Cost'
        verbose_name_plural = 'Fixed Costs'
        ordering = ['created_at']        

class Gain(models.Model):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='ID Gain', db_column='IDGain')
    expected_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Expected Value', db_column='ExpectedValue')
    real_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Real Value', db_column='RealValue') 
    id_save = models.ForeignKey('Save', on_delete=models.CASCADE)

    def __str__(self):
        name = f"{self.id_save.name} - GAIN - ${round(self.real_value, 2)}"
        return name
    
    class Meta:
        db_table = 'Gain'
        verbose_name = 'Gain'
        verbose_name_plural = 'Gains'
        ordering = ['created_at']

class Loss(models.Model):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='ID Loss', db_column='IDLoss')
    expected_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Expected Value', db_column='ExpectedValue')
    real_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Real Value', db_column='RealValue')
    id_save = models.ForeignKey('Save', on_delete=models.CASCADE)

    def __str__(self):
        name = f"{self.id_save.name} - LOSS - ${round(self.real_value, 2)}"
        return name
    
    class Meta:
        db_table = 'Loss'
        verbose_name = 'Loss'
        verbose_name_plural = 'Losses'
        ordering = ['created_at']

class Economy(models.Model):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='ID Economy', db_column='IDEconomy')
    expected_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Expected Value', db_column='ExpectedValue')
    real_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Real Value', db_column='RealValue')
    id_save = models.ForeignKey('Save', on_delete=models.CASCADE)

    def __str__(self):
        name = f"{self.id_save.name} - ECONOMY - ${round(self.real_value, 2)}"
        return name
    
    class Meta:
        db_table = 'Economy'
        verbose_name = 'Economy'
        verbose_name_plural = 'Economies'
        ordering = ['created_at']