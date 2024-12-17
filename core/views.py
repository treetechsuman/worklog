from django.shortcuts import render
def home(request):
    #return HttpResponse("this is home page")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("this is about page")
    return render(request, 'about.html')