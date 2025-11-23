from django.urls import path

from . import views

app_name = "portfolio"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("project/<int:pk>", views.ProjectsDetailView.as_view(), name="project"),
    path("project/populate/<int:project_id>", views.populate, name="populate"),
    path("experience/<int:pk>", views.ExperienceDetailView.as_view(), name="experience")
]