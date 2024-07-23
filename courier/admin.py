from django.contrib import admin
from courier.models import TrackingNumber
from import_export.admin import ImportExportModelAdmin



admin.site.register(TrackingNumber)
