from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    # images = Image.objects.all()
    # return render(request,'home.html',{"images":images})
    return render(request,'home.html')


