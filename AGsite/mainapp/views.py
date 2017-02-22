from django.shortcuts import render
from mainapp.models import Architects_supervision,Paragraphs_AS,Architecture,Paragraphs_Arch_SD,Paragraphs_Arch_DD,Paragraphs_Arch_CD,Interior_design,Paragraphs_ID,Product_design,Paragraphs_PD

def index(request):
    return render(request, 'home.html')

def architecture(request):
    return render(request, 'architecture.html')

def design(request):
    return render(request, 'design.html')

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
