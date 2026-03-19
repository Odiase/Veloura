from django.db import models
from django.db.models import JSONField

class DashboardStats(models.Model):
    total_revenue = models.DecimalField(max_digits=12, decimal_places=2)
    total_orders = models.IntegerField()
    total_customers = models.IntegerField()
    conversion_rate = models.FloatField()
    avg_order_value = models.DecimalField(max_digits=10, decimal_places=2)
    business_age_months = models.IntegerField()
    initial_investment = models.DecimalField(max_digits=12, decimal_places=2)
    current_revenue = models.DecimalField(max_digits=12, decimal_places=2)
    
    monthly_revenue = JSONField(default=list)  # [month1, month2, ...]
    monthly_orders = JSONField(default=list)   # [month1, month2, ...]
    
    # Category data
    category_revenue = JSONField(default=dict)  # {"Makeup": 1200, "Skincare": 800, "Haircare": 500}
    category_orders = JSONField(default=dict)   # {"Makeup": 40, "Skincare": 30, "Haircare": 20}
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Veloura Dashboard Stats"