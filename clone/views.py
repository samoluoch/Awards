from django.shortcuts import render,redirect
from .models import Profile,Project
from django.contrib.auth.models import User
from .forms import RegistrationForm,ProjectForm,EditProfileForm
from django.contrib.auth.decorators import login_required
# from django.contrib.messages.context_processors.messages import
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import MerchSerializer
from rest_framework import status






# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request,'home.html',{"projects":projects})
    # return render(request,'home.html')


def register(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                # user.is_active = False
                user.save()
                # current_site = get_current_site(request)
                # to_email = form.cleaned_data.get('email')
                # activation_email(user, current_site, to_email)
                # return HttpResponse('Please confirm your email')
            return redirect('home.html')

        else:
            form = RegistrationForm()
        return render(request, 'registration/signup.html',{'form':form})



def profile(request,username):
    profile = User.objects.get(username=username)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    projects = Project.get_profile_projects(profile.id)
    title = f'@{profile.username} Projects'

    return render(request, 'profile/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details, 'projects':projects})


@login_required(login_url='/login')
def upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.profile = request.user
            upload.save()
            return redirect('profile',username=request.user)
    else:
        form = ProjectForm()

    return render(request, 'profile/upload_project.html', {'form': form})



def search_profile(request):
    if 'profile' in request.GET and request.GET['profile']:
        search_term = request.GET.get('profile')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Type profile'
        return render(request, 'search.html', {'message':message})


@login_required(login_url='/login')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('profile',username=request.user)
    else:
        form = EditProfileForm()

    return render(request, 'profile/edit_profile.html', {'form':form})


class MerchList(APIView):
    def get_profile(self, request, format=None):
        all_merch_profiles = Profile.objects.all()
        serializers = MerchSerializer(all_merch_profiles, many=True)
        return Response(serializers.data)

    def get_projects(self, request, format=None):
        all_merch_projects = Project.objects.all()
        serializers = MerchSerializer(all_merch_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)






# def register(request):
#     if request.user.is_authenticated():
#         return redirect('home')
#     else:
#         if request.method == 'POST':
#             form = RegistrationForm(request.POST)
#             if form.is_valid():
#                 user = form.save(commit=False)
#                 try:
#                     user.is_active = False
#                     user.save()
#                 except:
#                     messages.errors('Please Verify Email')
#                 # current_site = get_current_site(request)
#                 # to_email = form.cleaned_data.get('email')
#                 # activation_email(user, current_site, to_email)
#                 # return HttpResponse('Please confirm your email')
#             return redirect('home.html')
#
#         else:
#             form = RegistrationForm()
#         return render(request, 'registration/signup.html',{'form':form})
#