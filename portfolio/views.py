from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Project, Experience

# Create your views here.
class IndexView(generic.ListView):
    template_name = ("portfolio/index.html")
    context_object_name = "projects_list"

    def get_queryset(self):
        """Return the list of projects and experiences"""
        return Project.objects.all()

class ProjectsDetailView(generic.DetailView):
    model = Project
    template_name = "portfolio/project/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Project.objects.all()

class ExperienceDetailView(generic.DetailView):
    model = Experience
    template = "portfolio/experience/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Experience.objects.all()

def populate():
    pass