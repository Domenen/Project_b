from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("hello/", views.hello),
    path("hello/<str:name>/", views.hello, name="hello"),
    path("feedback/", views.FeedbackView.as_view()),
    path('admin/', admin.site.urls),
]
