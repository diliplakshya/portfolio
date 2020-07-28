from django.contrib import admin
from .models import Skill, SkillType, Company, ProfessionalProject, HobbyProject


# Register your models here.
admin.site.register(Skill)
admin.site.register(SkillType)
admin.site.register(Company)
admin.site.register(ProfessionalProject)
admin.site.register(HobbyProject)
