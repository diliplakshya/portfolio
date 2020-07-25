from django.shortcuts import render
from .models import SkillType, Skill, Company, ProfessionalProject


def home(request):
    return render(request, template_name="home/home.html")

def profile(request):
    # Skill Starts #
    skill_details = list()

    for skill_type in SkillType.objects.all():
        skills = Skill.objects.all().filter(skill_type = skill_type.id)
        skill_details.append((skill_type.name, skills))

    # Skill Ends #

    # Project Starts #
    project_details = list()

    for company in Company.objects.all():
        projects = ProfessionalProject.objects.all().filter(company = company.id)
        project_details.append((company.name, projects))

    # Project Ends #

    context = {"skill_details" : skill_details, "project_details" : project_details}

    return render(request, template_name="home/profile.html", context=context)