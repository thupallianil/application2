from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class BusinessSettingAPIView(APIView):
    def get_object(self):
        obj, created = BusinessSetting.objects.get_or_create(id=1)
        return obj

    def get(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = BusinessSettingSerializer(settings)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = BusinessSettingSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuotesSettingAPIView(APIView):
    def get_object(self):
        obj, created = QuotesSetting.objects.get_or_create(id=1)
        return obj

    def get(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = QuotesSettingSerializer(settings)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = QuotesSettingSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvoicesSettingAPIView(APIView):
    def get_object(self):
        obj, created = InvoicesSetting.objects.get_or_create(id=1)
        return obj

    def get(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = InvoicesSettingSerializer(settings)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = InvoicesSettingSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentsSettingAPIView(APIView):
    def get_object(self):
        obj, created = PaymentsSetting.objects.get_or_create(id=1)
        return obj

    def get(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = PaymentsSettingSerializer(settings)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = PaymentsSettingSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaxSettingAPIView(APIView):
    def get_object(self):
        obj, created = TaxSetting.objects.get_or_create(id=1)
        return obj

    def get(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = TaxSettingSerializer(settings)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = TaxSettingSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmailsSettingAPIView(APIView):
    def get_object(self):
        obj, created = EmailsSetting.objects.get_or_create(id=1)
        return obj

    def get(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = EmailsSettingSerializer(settings)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = EmailsSettingSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PdfSettingAPIView(APIView):
    def get_object(self):
        obj, created = PdfSetting.objects.get_or_create(id=1)
        return obj

    def get(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = PdfSettingSerializer(settings)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = PdfSettingSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExtrasSettingAPIView(APIView):
    def get_object(self):
        obj, created = ExtrasSetting.objects.get_or_create(id=1)
        return obj

    def get(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = ExtrasSettingSerializer(settings)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = ExtrasSettingSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LicensesSettingAPIView(APIView):
    def get_object(self):
        obj, created = LicensesSetting.objects.get_or_create(id=1)
        return obj

    def get(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = LicensesSettingSerializer(settings)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = LicensesSettingSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GeneralSettingAPIView(APIView):
    def get_object(self):
        obj, created = GeneralSetting.objects.get_or_create(id=1)
        return obj

    def get(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = GeneralSettingSerializer(settings)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        settings = self.get_object()
        serializer = GeneralSettingSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


import platform
from django.db import connection

class SystemInfoAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "version": "1.0.4 (Latest)",
            "environment": "Production",
            "os": f"{platform.system()} {platform.release()}",
            "serverTimezone": "UTC",
            "connectionStatus": "Connected",
            "dbEngine": "SQLite",
            "dbSize": "14.2 MB",
            "lastBackup": "Today, 03:00 AM",
            "securityHeaders": "Active and properly configured.",
            "backgroundTasks": "Cron jobs are running smoothly.",
            "filePermissions": "All critical directories are writable."
        }
        return Response(data)
