from django.shortcuts import render
from .models import SkillType, Skill, Company, ProfessionalProject, HobbyProject


def home(request):
    # Project Starts #
    professional_projects = list()

    for company in Company.objects.all():
        for project in ProfessionalProject.objects.all().filter(company = company.id):
            professional_projects.append(project)

    # Project Ends #

    hobby_projects = HobbyProject.objects.all()

    context = {"works" : Company.objects.all(), "professional_projects" : professional_projects, "hobby_projects" : hobby_projects}
    
    return render(request, template_name="home/home.html", context=context)

def project(request, project_id):
    professional_projects = ProfessionalProject.objects.filter(id = project_id)

    context = {"projects" : professional_projects}
    
    return render(request, template_name="home/project.html", context=context)

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

def about(request):
    return render(request, template_name="home/about.html")

def contact(request):
    return render(request, template_name="home/contact.html")