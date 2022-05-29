from django.contrib import admin
from tutorials.apps import TutorialsConfig

from tutorials.models import ContentType, Images, Keywords, Videos, Tutorial

# Register your models here.
admin.site.register(Images)
admin.site.register(Videos)
admin.site.register(Keywords)
admin.site.register(ContentType)
admin.site.register(Tutorial)


