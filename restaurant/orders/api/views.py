from datetime import timedelta

from django.db.models import Sum
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from restaurant.orders.api.serializers import OrderSerializer
from restaurant.orders.filters import OrderFilterSet
from restaurant.orders.models import Order


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilterSet


class DailySaleReport(APIView):
    def get(self, request):
        current_time = timezone.now()
        start_time = current_time - timedelta(hours=24)

        total_price_report = Order.objects.filter(
            created_at__range=(start_time, current_time)
        ).aggregate(total_price=Sum("total_price"))
        total_price = (
            total_price_report["total_price"]
            if total_price_report["total_price"] is not None
            else 0
        )

        return Response({"daily_total_price": total_price})


class WeeklySaleReport(APIView):
    def get(self, request):
        current_time = timezone.now()
        start_time = current_time - timedelta(hours=24 * 7)

        total_price_report = Order.objects.filter(
            created_at__range=(start_time, current_time)
        ).aggregate(total_price=Sum("total_price"))
        total_price = (
            total_price_report["total_price"]
            if total_price_report["total_price"] is not None
            else 0
        )

        return Response({"weekly_total_price": total_price})
