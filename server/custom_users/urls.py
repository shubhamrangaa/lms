from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from custom_users import views
from custom_users.views import UserProfileAPI

urlpatterns = [
    # path('list/<int:pk>/',views.snippet_list),
    # path('new_list/',views.new_snippet_list),

    # path('create/',views.create_user),
    # path('detail/',views.user_detail),
    # path('listed/',views.user_list),
    # path('update/',views.update_user),
    # path('delete/',views.delete_user),

    path('' ,UserProfileAPI.as_view()),
    path('<int:id>/' ,views.user_details),
    ]
# urlpatterns = format_suffix_patterns(urlpatterns)
    # {"uuid": "8ff01722-a73d-4a08-b57a-18f68091bf52", "user_name": 1, "email": "admin123@gmail.com", "mobile": "99999999", "first_name": "Prachi", "last_name": "Mohnot"}