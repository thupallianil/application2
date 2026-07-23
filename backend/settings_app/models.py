from django.db import models

class BusinessSetting(models.Model):
    logoUrl = models.TextField(blank=True, null=True, default='')
    businessName = models.TextField(blank=True, null=True, default='')
    address = models.TextField(blank=True, null=True, default='')
    extraInfo = models.TextField(blank=True, null=True, default='')
    website = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return 'Business Settings'

class QuotesSetting(models.Model):
    prefix = models.TextField(blank=True, null=True, default='')
    nextNumber = models.TextField(blank=True, null=True, default='')
    validity = models.TextField(blank=True, null=True, default='')
    terms = models.TextField(blank=True, null=True, default='')
    notes = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return 'Quotes Settings'

class InvoicesSetting(models.Model):
    prefix = models.TextField(blank=True, null=True, default='')
    nextNumber = models.TextField(blank=True, null=True, default='')
    dueDays = models.TextField(blank=True, null=True, default='')
    footer = models.TextField(blank=True, null=True, default='')
    notes = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return 'Invoices Settings'

class PaymentsSetting(models.Model):
    bankName = models.TextField(blank=True, null=True, default='')
    accountName = models.TextField(blank=True, null=True, default='')
    accountNumber = models.TextField(blank=True, null=True, default='')
    ifsc = models.TextField(blank=True, null=True, default='')
    upi = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return 'Payments Settings'

class TaxSetting(models.Model):
    taxName = models.TextField(blank=True, null=True, default='')
    taxRate = models.TextField(blank=True, null=True, default='')
    taxNumber = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return 'Tax Settings'

class EmailsSetting(models.Model):
    mailFrom = models.TextField(blank=True, null=True, default='')
    smtpHost = models.TextField(blank=True, null=True, default='')
    smtpPort = models.TextField(blank=True, null=True, default='')
    username = models.TextField(blank=True, null=True, default='')
    password = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return 'Emails Settings'

class PdfSetting(models.Model):
    template = models.TextField(blank=True, null=True, default='')
    paper = models.TextField(blank=True, null=True, default='')
    orientation = models.TextField(blank=True, null=True, default='')
    watermark = models.BooleanField(default=False)

    def __str__(self):
        return 'Pdf Settings'

class ExtrasSetting(models.Model):
    darkMode = models.BooleanField(default=False)
    notifications = models.BooleanField(default=False)
    maintenance = models.BooleanField(default=False)

    def __str__(self):
        return 'Extras Settings'

class LicensesSetting(models.Model):
    company = models.TextField(blank=True, null=True, default='')
    purchaseCode = models.TextField(blank=True, null=True, default='')
    licenseKey = models.TextField(blank=True, null=True, default='')
    expiry = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return 'Licenses Settings'


class GeneralSetting(models.Model):
    yearStart = models.CharField(max_length=50, default="01 Apr")
    yearEnd = models.CharField(max_length=50, default="31 Mar")
    preDefinedLineItems = models.TextField(blank=True, default="")
    def __str__(self): return "General Settings"
