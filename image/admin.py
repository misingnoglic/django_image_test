from django.contrib import admin
from models import X

# Register your models here.

@admin.register(X)
class PlotLinkAdmin(admin.ModelAdmin):
    readonly_fields = ('mugshot',)
