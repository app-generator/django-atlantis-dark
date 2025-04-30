from django.urls import path

from apps.charts import views

urlpatterns = [
    path("app/", views.index, name="app_charts"),
]