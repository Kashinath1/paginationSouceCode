from django.core.paginator import Paginator
 
def aboutUs(request):
    if request.method == "GET":
        output = request.GET.get('output')
    return render(request,"https://annapurnapost.com/",{'output':output})

def services(request):
    ServiceData = Service.objects.all()
    Paginator = Paginator(ServiceData,30)
    page_number = request.GET.get('page')
    ServiceDataFinal = Paginator.get_page(page_number)
    
    data{
        'ServicesData':ServiceDataFinal,
    }
    return render(request,"services.html",data)