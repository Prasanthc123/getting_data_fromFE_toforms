from django.shortcuts import render
from django.http import HttpResponse

from app.models import *
# Create your views here.
def htmlform(request):
    return render(request,'htmlform.html')

def create_Topic(request):
    if request.method=='POST':
        tname=request.POST['tname']
        to=Topic.objects.get_or_create(tn=tname)[0]
        to.save()
        QLTO=Topic.objects.all()
        d={'Topic':QLTO}
        return render(request,'display_topic.html',d)

    return render(request,'create_Topic.html')

def create_Webpage(request):
    QLTO=Topic.objects.all()
    d={'Topic':QLTO}

    if request.method=='POST':
        n=request.POST['n']
        tname=request.POST['tname']
        u=request.POST['u']
        em=request.POST['em']

        TO=Topic.objects.get(tn=tname)
        WO=Webpage.objects.get_or_create(name=n,tn=TO,url=u,email=em)[0]
        WO.save()

        QLWO=Webpage.objects.all()
        d1={'Webpage':QLWO}
        return render(request,'display_Webpage.html',d1)

    return render(request,'create_Webpage.html',d)


def create_Accessrecord(request):
    QLWO=Webpage.objects.all()
    d={'Webpage':QLWO}

    if request.method=='POST':
        pk=request.POST['pk']
        a=request.POST['a']
        d=request.POST['d']
        

        TO=Webpage.objects.get(pk=pk)
        AO=Accessrecord.objects.get_or_create(name=TO,author=a,date=d)[0]
        AO.save()

        QLAO=Accessrecord.objects.all()
        d1={'Accessrecord':QLAO}
        return render(request,'display_Accessrecord.html',d1)
    return render(request,'create_Accessrecord.html',d)


def display_multiple_Webpage(request):
    QLTO=Topic.objects.all()
    d={'Topic':QLTO}
    if request.method =='POST':
        topiclist=request.POST.getlist('tname')
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(tn=i)
        d1={'Webpage':QLWO}
        return render(request,'display_Webpage.html',d1)
    return render(request,'display_multiple_Webpage.html',d)

def display_multiple_Accessrecord(request):
    QLWO=Webpage.objects.all()
    d={'Webpage':QLWO}
    if request.method=='POST':
        webpagelist=request.POST.getlist('n')
        QLAO=Accessrecord.objects.none()
        for i in webpagelist:
            QLAO=QLAO|Accessrecord.objects.filter(name=i)
        d1={'Accessrecord':QLAO}
        return render(request,'display_Accessrecord.html',d1)
    return render(request,'display_multiple_Accessrecord.html',d)




def checkbox(request):
    QLTO=Topic.objects.all()
    d={'Topic':QLTO}
    if request.method =='POST':
        topiclist=request.POST.getlist('tname')
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(tn=i)
        d1={'Webpage':QLWO}
        return render(request,'display_Webpage.html',d1)
    return render(request,'checkbox.html',d)

def checkbox_Accessrecord(request):
    QLWO=Webpage.objects.all()
    d={'Webpage':QLWO}
    return render(request,'checkbox_Accessrecord.html',d)