from django.shortcuts import render
from mainapp.models import Arch_photo,Arch_projects,Architects_supervision,Paragraphs_AS,Architecture,Paragraphs_Arch_SD,Paragraphs_Arch_DD,Paragraphs_Arch_CD,Interior_design,Paragraphs_ID,Product_design,Paragraphs_PD

def index(request):
    return render(request, 'home.html')

def architecture(request):
    xcontent = {
        'Arch_projects' : Arch_projects.objects.all().order_by('id'),
        'Arch_photo' : Arch_photo.objects.all(),
    }
    return render(request, 'architecture.html', xcontent)

def design(request):
    return render(request, 'design.html')

def slideshow(request, pk):
    photos = {
        'Arch_photo' : Arch_photo.objects.all().filter(project_id=pk),
    }
    return render(request, 'slideshow.html', photos)

def services(request):
    content = {
        'Architects_supervision' : Architects_supervision.objects.all(),
        'Paragraphs_AS' : Paragraphs_AS.objects.all(),
        'Architecture' : Architecture.objects.all(),
        'Paragraphs_Arch_SD' : Paragraphs_Arch_SD.objects.all(),
        'Paragraphs_Arch_DD' : Paragraphs_Arch_DD.objects.all(),
        'Paragraphs_Arch_CD' : Paragraphs_Arch_CD.objects.all(),
        'Interior_design' : Interior_design.objects.all(),
        'Paragraphs_ID' : Paragraphs_ID.objects.all(),
        'Product_design' : Product_design.objects.all(),
        'Paragraphs_PD' : Paragraphs_PD.objects.all(),
    }
    return render(request, 'services.html', content)

def contact(request):
    return render(request, 'contact.html')


#### RU ####

def ruindex(request):
    return render(request, 'ruhome.html')

def ruarchitecture(request):
    return render(request, 'ruarchitecture.html')

def rudesign(request):
    return render(request, 'rudesign.html')

def ruservices(request):
    content = {
        'Architects_supervision' : Architects_supervision.objects.all(),
        'Paragraphs_AS' : Paragraphs_AS.objects.all(),
        'Architecture' : Architecture.objects.all(),
        'Paragraphs_Arch_SD' : Paragraphs_Arch_SD.objects.all(),
        'Paragraphs_Arch_DD' : Paragraphs_Arch_DD.objects.all(),
        'Paragraphs_Arch_CD' : Paragraphs_Arch_CD.objects.all(),
        'Interior_design' : Interior_design.objects.all(),
        'Paragraphs_ID' : Paragraphs_ID.objects.all(),
        'Product_design' : Product_design.objects.all(),
        'Paragraphs_PD' : Paragraphs_PD.objects.all(),
    }
    return render(request, 'ruservices.html', content)

def rucontact(request):
    return render(request, 'rucontact.html')

def ukdesign(request):
    return render(request, 'ukdesign.html')
