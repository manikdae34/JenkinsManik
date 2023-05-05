from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from .models import *

# Create your views here.
def main(request):
    ##### FOR IP ADDRESS COLLECTION #####
    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip = get_ip(request)
    u = Visitor(visitor=ip)
    result = Visitor.objects.filter(Q(visitor__icontains=ip))
    if len(result) == 1:
        print("Visitor Exit")
    elif len(result) > 1:
        print("visitor exist more........")
    else:
        u.save()
    countdata = Visitor.objects.all().count()

    aboutdata = About.objects.all()[0]
    sliderdata = SliderItem.objects.all()
    academicdata = Academic.objects.all()
    experiencedata = Experience.objects.all()
    affiliationdata = Affiliation.objects.all()
    context = {
        'about' : aboutdata,
        'slider': sliderdata,
        'count': countdata,
        'academic': academicdata,
        'experience': experiencedata,
        'affiliation': affiliationdata,
    }

    return render(request, 'base.html', context)