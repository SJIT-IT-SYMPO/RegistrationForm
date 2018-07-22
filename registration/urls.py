from django.urls import path
from registration import views

urlpatterns = [
    path('api/', views.user_profile_data.as_view()	),
    path('',views.list),
    path('download/',views.download_csv),
]