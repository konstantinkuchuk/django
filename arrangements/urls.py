
from django.urls import path
from .views import current_datetime, greeting

#маршрутизатор
urlpatterns = [
    path('now_time', current_datetime),
    path('greeting/<str:name>/', greeting)
]