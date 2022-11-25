from django.urls import path
import paladiy.views

urlpatterns = [
    path('status', paladiy.views.index)
]