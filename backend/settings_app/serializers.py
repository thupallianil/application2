from rest_framework import serializers
from .models import *

class BusinessSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessSetting
        fields = ['logoUrl', 'businessName', 'address', 'extraInfo', 'website']

class QuotesSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotesSetting
        fields = ['prefix', 'nextNumber', 'validity', 'terms', 'notes']

class InvoicesSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoicesSetting
        fields = ['prefix', 'nextNumber', 'dueDays', 'footer', 'notes']

class PaymentsSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsSetting
        fields = ['bankName', 'accountName', 'accountNumber', 'ifsc', 'upi']

class TaxSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxSetting
        fields = ['taxName', 'taxRate', 'taxNumber']

class EmailsSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailsSetting
        fields = ['mailFrom', 'smtpHost', 'smtpPort', 'username', 'password']

class PdfSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfSetting
        fields = ['template', 'paper', 'orientation', 'watermark']

class ExtrasSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtrasSetting
        fields = ['darkMode', 'notifications', 'maintenance']

class LicensesSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicensesSetting
        fields = ['company', 'purchaseCode', 'licenseKey', 'expiry']

class GeneralSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralSetting
        fields = ['yearStart', 'yearEnd', 'preDefinedLineItems']
