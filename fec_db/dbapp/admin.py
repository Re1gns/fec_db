from django.contrib import admin
from .models import MemberInformation

class MemberInformationAdmin(admin.ModelAdmin):
    list_display = ('reference_id', 'surname', 'timestamp', 'image_tag')

admin.site.register(MemberInformation, MemberInformationAdmin)
