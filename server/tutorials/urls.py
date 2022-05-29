from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tutorials import views


urlpatterns = [
    path('' ,views.TutorialProfileAPI.as_view()),
    path('category/' ,views.ContentTypeAPI.as_view()),
    ]