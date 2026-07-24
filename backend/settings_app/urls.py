from django.urls import path
from .views import (
    BusinessSettingAPIView,
    QuotesSettingAPIView,
    InvoicesSettingAPIView,
    PaymentsSettingAPIView,
    TaxSettingAPIView,
    EmailsSettingAPIView,
    PdfSettingAPIView,
    TranslateSettingAPIView,
    ExtrasSettingAPIView,
    LicensesSettingAPIView,
    GeneralSettingAPIView,
    SystemInfoAPIView
)

urlpatterns = [
    path('general/', GeneralSettingAPIView.as_view(), name='general-settings'),
    path('business/', BusinessSettingAPIView.as_view(), name='business-settings'),
    path('quotes/', QuotesSettingAPIView.as_view(), name='quotes-settings'),
    path('invoices/', InvoicesSettingAPIView.as_view(), name='invoices-settings'),
    path('payments/', PaymentsSettingAPIView.as_view(), name='payments-settings'),
    path('tax/', TaxSettingAPIView.as_view(), name='tax-settings'),
    path('emails/', EmailsSettingAPIView.as_view(), name='emails-settings'),
    path('pdf/', PdfSettingAPIView.as_view(), name='pdf-settings'),
    path('translate/', TranslateSettingAPIView.as_view(), name='translate-settings'),
    path('extras/', ExtrasSettingAPIView.as_view(), name='extras-settings'),
    path('licenses/', LicensesSettingAPIView.as_view(), name='licenses-settings'),
    path('system/', SystemInfoAPIView.as_view(), name='system-info'),
]
