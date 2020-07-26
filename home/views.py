from django.shortcuts import render
from .models import SkillType, Skill, Company, ProfessionalProject


def home(request):
    return render(request, template_name="home/home.html")

def profile(request):
    return render(request, template_name="home/profile.html")

def skill(request):
    # Skill Starts #
    skill_details = list()

    for skill_type in SkillType.objects.all():
        skills = Skill.objects.all().filter(skill_type = skill_type.id)
        skill_details.append((skill_type.name, skills))

    # Skill Ends #

    context = {"skill_details" : skill_details}

    return render(request, template_name="home/skill.html", context=context)

def professional_experience(request):
    # Project Starts #
    project_details = list()

    for company in Company.objects.all():
        projects = ProfessionalProject.objects.all().filter(company = company.id)
        project_details.append((company, projects))

    # Project Ends #

    context = {"project_details" : project_details}

    return render(request, template_name="home/professional_experience.html", context=context)