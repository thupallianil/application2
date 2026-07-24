from rest_framework import serializers
from .models import *

class GeneralSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralSetting
        fields = '__all__'

class BusinessSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessSetting
        fields = '__all__'

class QuotesSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotesSetting
        fields = '__all__'

class InvoicesSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoicesSetting
        fields = '__all__'

class PaymentsSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsSetting
        fields = '__all__'

class TaxSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxSetting
        fields = '__all__'

class EmailsSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailsSetting
        fields = '__all__'

class PdfSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfSetting
        fields = '__all__'

class TranslateSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslateSetting
        fields = '__all__'

class ExtrasSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtrasSetting
        fields = '__all__'

class LicensesSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicensesSetting
        fields = '__all__'
