from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from rest_framework.routers import DefaultRouter
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from backend.clients.views import ClientViewSet
from backend.invoices.views import InvoiceViewSet
from backend.payments.views import PaymentViewSet
from backend.quotations.views import QuoteViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Invoice Management API",
        default_version="v1",
        description="API endpoints for Invoice Management System",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r"clients", ClientViewSet, basename="client")
router.register(r"invoices", InvoiceViewSet, basename="invoice")
router.register(r"payments", PaymentViewSet, basename="payment")
router.register(r"quotes", QuoteViewSet, basename="quote")

urlpatterns = [
    path("", RedirectView.as_view(url="/swagger/", permanent=False)),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/settings/", include("backend.settings_app.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]