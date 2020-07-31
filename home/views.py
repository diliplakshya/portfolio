from django.shortcuts import render
from .models import SkillType, Skill, Company, ProfessionalProject, HobbyProject
from django.core.mail import send_mail
from decouple import config, Csv        # Please update .env file or config vars on Heroku
from lib.portfolio.forms import ContactForm
from django.contrib import messages


def home(request):
    contact = None
    context = None
    professional_projects = list()
    hobby_projects = None

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request
        contact = ContactForm(request.POST)

        # check whether it's valid
        if contact.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
    
            sender          =   contact.cleaned_data['email']
            subject         =   contact.cleaned_data['subject']
            message         =   contact.cleaned_data['message']
            
            recipients = config('EMAIL_RECIPIENTS', cast=Csv())

            send_mail(subject, message, sender, recipients)

            messages.success(request, "Thank You. Message is sent successfully.")
        else:
            messages.error(request, f"Failed to send message.")
    else:
        # Project Starts #
        
        for company in Company.objects.all():
            for project in ProfessionalProject.objects.all().filter(company = company.id):
                professional_projects.append(project)

        # Project Ends #

        hobby_projects = HobbyProject.objects.all()

    contact = ContactForm()

    context = {"works" : Company.objects.all(), "professional_projects" : professional_projects, "hobby_projects" : hobby_projects, "contact" : contact}
        
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