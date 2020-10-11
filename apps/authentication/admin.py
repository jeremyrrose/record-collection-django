from django.contrib import admin
from apps.api.models import Record, Artist, Collection

# Register your models here.
admin.site.register(Record)
admin.site.register(Artist)
admin.site.register(Collection)
