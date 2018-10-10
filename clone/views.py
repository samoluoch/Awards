from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.models import User
from .forms import RegistrationForm





# Create your views here.
def home(request):
    # images = Image.objects.all()
    # return render(request,'home.html',{"images":images})
    return render(request,'home.html')


def register(request):
    if request.user.is_authenticated():
        return redirect('instagram')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                # current_site = get_current_site(request)
                # to_email = form.cleaned_data.get('email')
                # activation_email(user, current_site, to_email)
                # return HttpResponse('Please confirm your email')
            return redirect('home.html')

        else:
            form = RegistrationForm()
        return render(request, 'registration/signup.html',{'form':form})



