from django.urls import path
from basic_app import views

## temaplate tagging

app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative_url, name="relative"),
    path('other/', views.other, name="other"),
]