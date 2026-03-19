from django.http import JsonResponse
from django.shortcuts import render
from .models import DashboardStats


def dashboard_page(request):
    stats = DashboardStats.objects.latest("id")
    profit = stats.current_revenue - stats.initial_investment
    roi = round((profit / stats.initial_investment) * 100, 2)

    context = {
        "initial_investment": stats.initial_investment,
        "total_revenue": stats.current_revenue,
        "profit": profit,
        "roi": roi
    }
    return render(request, "dashboard.html", context)


def dashboard_metrics(request):
    stats = DashboardStats.objects.latest("id")

    # Compute category percentages for pie/doughnut charts
    total_category_orders = sum(stats.category_orders.values())
    total_category_revenue = sum(stats.category_revenue.values())

    category_orders_percent = {
        k: round((v / total_category_orders) * 100, 1) 
        for k, v in stats.category_orders.items()
    }

    category_revenue_percent = {
        k: round((v / total_category_revenue) * 100, 1) 
        for k, v in stats.category_revenue.items()
    }

    data = {
        "total_revenue": float(stats.total_revenue),
        "total_orders": stats.total_orders,
        "total_customers": stats.total_customers,
        "conversion_rate": stats.conversion_rate,
        "avg_order_value": float(stats.avg_order_value),
        "business_age": stats.business_age_months,
        "investment": float(stats.initial_investment),
        "current_revenue": float(stats.current_revenue),
        "profit": float(stats.current_revenue - stats.initial_investment),
        "roi": round((stats.current_revenue - stats.initial_investment) / stats.initial_investment * 100, 2),
        "monthly_revenue": stats.monthly_revenue,
        "monthly_orders": stats.monthly_orders,
        "category_orders": stats.category_orders,
        "category_orders_percent": category_orders_percent,
        "category_revenue": stats.category_revenue,
        "category_revenue_percent": category_revenue_percent,
    }

    return JsonResponse(data)