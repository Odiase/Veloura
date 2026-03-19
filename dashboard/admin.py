from django.contrib import admin
from .models import DashboardStats


@admin.register(DashboardStats)
class DashboardStatsAdmin(admin.ModelAdmin):

    list_display = (
        "total_revenue",
        "total_orders",
        "total_customers",
        "conversion_rate",
        "updated_at"
    )