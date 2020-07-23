from django.shortcuts import render
from .models import Project


def projects(request):
    projects = Project.objects.all()
    context = {"projects" : projects}
    return render(request, template_name='projects/project_index.html', context=context)
