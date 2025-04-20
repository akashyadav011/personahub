from django.shortcuts import render
from .models import Profile, Education, SoftSkill, TechSkill, Project, Certification

def index(request):
    context = {
        'profile': Profile.objects.first(),
        'education_list': Education.objects.all(),
        'soft_skills': SoftSkill.objects.all(),
        'tech_skills': TechSkill.objects.all(),
        'projects': Project.objects.order_by('-completed_date'),
        'certifications': Certification.objects.all(),
    }
    return render(request, 'portfolio_app/index.html', context)