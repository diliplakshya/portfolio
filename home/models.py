from django.db import models


class SkillType(models.Model):
    name                =           models.CharField(max_length=100)

    def __str__(self):
        return (self.name)


class Skill(models.Model):
    skill_type          =           models.ForeignKey(SkillType, on_delete=models.CASCADE)
    name                =           models.CharField(max_length=50)
    experience          =           models.CharField(max_length=50)
    proficiency         =           models.IntegerField()
    remarks             =           models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return (self.name)


class Company(models.Model):
    name                =           models.CharField(max_length=100)
    from_date           =           models.DateField()
    to_date             =           models.DateField()
    location            =           models.CharField(max_length=100)

    def __str__(self):
        return (self.name)


class ProfessionalProject(models.Model):
    company             =           models.ForeignKey(Company, on_delete=models.CASCADE)
    designation         =           models.CharField(max_length=50, verbose_name="Designation")
    title               =           models.CharField(max_length=100)
    client              =           models.CharField(max_length=100)
    team_size           =           models.IntegerField()
    description         =           models.TextField()
    role                =           models.CharField(max_length=100)
    responsibilities    =           models.TextField()
    environment         =           models.CharField(max_length=200)
    remarks             =           models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.company) + '_' + str(self.title)