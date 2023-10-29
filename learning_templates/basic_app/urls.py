from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('relative_url/', views.relative_url, name='relative_url'),
]