from django.db import models

class GeneralSetting(models.Model):
    yearStart = models.CharField(max_length=50, default="01 Apr")
    yearEnd = models.CharField(max_length=50, default="31 Mar")
    preDefinedLineItems = models.TextField(blank=True, null=True, default="")
    def __str__(self): return "General Settings"

class BusinessSetting(models.Model):
    logoUrl = models.TextField(blank=True, null=True, default='')
    businessName = models.TextField(blank=True, null=True, default='')
    address = models.TextField(blank=True, null=True, default='')
    extraInfo = models.TextField(blank=True, null=True, default='')
    website = models.TextField(blank=True, null=True, default='')
    def __str__(self): return 'Business Settings'

class QuotesSetting(models.Model):
    prefix = models.TextField(blank=True, null=True, default='')
    suffix = models.TextField(blank=True, null=True, default='')
    autoIncrement = models.BooleanField(default=True)
    nextNumber = models.TextField(blank=True, null=True, default='')
    validity = models.TextField(blank=True, null=True, default='')
    hideAdjustField = models.BooleanField(default=False)
    terms = models.TextField(blank=True, null=True, default='')
    footer = models.TextField(blank=True, null=True, default='')
    acceptQuoteButton = models.BooleanField(default=True)
    acceptedQuoteAction = models.TextField(blank=True, null=True, default='')
    acceptQuoteText = models.TextField(blank=True, null=True, default='')
    acceptedQuoteMessage = models.TextField(blank=True, null=True, default='')
    declineReasonRequired = models.BooleanField(default=True)
    declinedQuoteMessage = models.TextField(blank=True, null=True, default='')
    noticeViewed = models.BooleanField(default=True)
    noticeAccepted = models.BooleanField(default=True)
    template = models.TextField(blank=True, null=True, default='Template 3')
    customCss = models.TextField(blank=True, null=True, default='body {}')
    def __str__(self): return 'Quotes Settings'

class InvoicesSetting(models.Model):
    prefix = models.TextField(blank=True, null=True, default='')
    suffix = models.TextField(blank=True, null=True, default='')
    autoIncrement = models.BooleanField(default=True)
    nextNumber = models.TextField(blank=True, null=True, default='')
    dueDays = models.TextField(blank=True, null=True, default='')
    hideAdjustField = models.BooleanField(default=False)
    terms = models.TextField(blank=True, null=True, default='')
    footer = models.TextField(blank=True, null=True, default='')
    noticeViewed = models.BooleanField(default=False)
    noticePaid = models.BooleanField(default=True)
    template = models.TextField(blank=True, null=True, default='Template 1')
    customCss = models.TextField(blank=True, null=True, default='body {}')
    def __str__(self): return 'Invoices Settings'

class PaymentsSetting(models.Model):
    currencySymbol = models.TextField(blank=True, null=True, default='₹')
    currencyPosition = models.TextField(blank=True, null=True, default='left')
    thousandSeparator = models.TextField(blank=True, null=True, default=',')
    decimalSeparator = models.TextField(blank=True, null=True, default='.')
    numberOfDecimals = models.TextField(blank=True, null=True, default='2')
    paymentPage = models.TextField(blank=True, null=True, default='')
    paymentPageFooter = models.TextField(blank=True, null=True, default='')
    bankDetails = models.TextField(blank=True, null=True, default='')
    genericPayment = models.TextField(blank=True, null=True, default='')
    paypalGateway = models.TextField(blank=True, null=True, default='')
    bankName = models.TextField(blank=True, null=True, default='')
    accountName = models.TextField(blank=True, null=True, default='')
    accountNumber = models.TextField(blank=True, null=True, default='')
    ifsc = models.TextField(blank=True, null=True, default='')
    upi = models.TextField(blank=True, null=True, default='')
    def __str__(self): return 'Payments Settings'

class TaxSetting(models.Model):
    pricesIncludeTax = models.TextField(blank=True, null=True, default='')
    taxRate = models.TextField(blank=True, null=True, default='')
    taxName = models.TextField(blank=True, null=True, default='')
    def __str__(self): return 'Tax Settings'

class EmailsSetting(models.Model):
    emailAddress = models.TextField(blank=True, null=True, default='')
    emailName = models.TextField(blank=True, null=True, default='')
    bccOnClientEmails = models.BooleanField(default=True)
    quoteSubject = models.TextField(blank=True, null=True, default='')
    quoteContent = models.TextField(blank=True, null=True, default='')
    quoteButtonText = models.TextField(blank=True, null=True, default='')
    invoiceSubject = models.TextField(blank=True, null=True, default='')
    invoiceContent = models.TextField(blank=True, null=True, default='')
    invoiceButtonText = models.TextField(blank=True, null=True, default='')
    paymentSubject = models.TextField(blank=True, null=True, default='')
    paymentContent = models.TextField(blank=True, null=True, default='')
    reminderDays = models.JSONField(blank=True, null=True, default=list)
    reminderSubject = models.TextField(blank=True, null=True, default='')
    reminderContent = models.TextField(blank=True, null=True, default='')
    footerContent = models.TextField(blank=True, null=True, default='')
    smtpHost = models.TextField(blank=True, null=True, default='')
    smtpPort = models.TextField(blank=True, null=True, default='')
    username = models.TextField(blank=True, null=True, default='')
    password = models.TextField(blank=True, null=True, default='')
    def __str__(self): return 'Emails Settings'

class PdfSetting(models.Model):
    template = models.TextField(blank=True, null=True, default='')
    paper = models.TextField(blank=True, null=True, default='')
    orientation = models.TextField(blank=True, null=True, default='')
    watermark = models.BooleanField(default=False)
    def __str__(self): return 'Pdf Settings'

class TranslateSetting(models.Model):
    quoteLabel = models.TextField(blank=True, null=True, default='')
    quoteLabelPlural = models.TextField(blank=True, null=True, default='')
    invoiceLabel = models.TextField(blank=True, null=True, default='')
    invoiceLabelPlural = models.TextField(blank=True, null=True, default='')
    hrsQty = models.TextField(blank=True, null=True, default='')
    service = models.TextField(blank=True, null=True, default='')
    ratePrice = models.TextField(blank=True, null=True, default='')
    adjust = models.TextField(blank=True, null=True, default='')
    subTotal = models.TextField(blank=True, null=True, default='')
    discount = models.TextField(blank=True, null=True, default='')
    total = models.TextField(blank=True, null=True, default='')
    totalDue = models.TextField(blank=True, null=True, default='')
    def __str__(self): return 'Translate Settings'

class ExtrasSetting(models.Model):
    darkMode = models.BooleanField(default=False)
    notifications = models.BooleanField(default=False)
    maintenance = models.BooleanField(default=False)
    def __str__(self): return 'Extras Settings'

class LicensesSetting(models.Model):
    company = models.TextField(blank=True, null=True, default='')
    purchaseCode = models.TextField(blank=True, null=True, default='')
    licenseKey = models.TextField(blank=True, null=True, default='')
    expiry = models.TextField(blank=True, null=True, default='')
    def __str__(self): return 'Licenses Settings'
