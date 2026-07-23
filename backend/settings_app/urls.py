from django.urls import path
from .views import BusinessSettingAPIView
from .views import QuotesSettingAPIView
from .views import InvoicesSettingAPIView
from .views import PaymentsSettingAPIView
from .views import TaxSettingAPIView
from .views import EmailsSettingAPIView
from .views import PdfSettingAPIView
from .views import ExtrasSettingAPIView
from .views import LicensesSettingAPIView
from .views import GeneralSettingAPIView

urlpatterns = [
    path('general/', GeneralSettingAPIView.as_view(), name='general-settings'),
    path('business/', BusinessSettingAPIView.as_view(), name='business-settings'),
    path('quotes/', QuotesSettingAPIView.as_view(), name='quotes-settings'),
    path('invoices/', InvoicesSettingAPIView.as_view(), name='invoices-settings'),
    path('payments/', PaymentsSettingAPIView.as_view(), name='payments-settings'),
    path('tax/', TaxSettingAPIView.as_view(), name='tax-settings'),
    path('emails/', EmailsSettingAPIView.as_view(), name='emails-settings'),
    path('pdf/', PdfSettingAPIView.as_view(), name='pdf-settings'),
    path('extras/', ExtrasSettingAPIView.as_view(), name='extras-settings'),
    path('licenses/', LicensesSettingAPIView.as_view(), name='licenses-settings'),
]
