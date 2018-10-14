from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile,Project,UsabilityRating,DesignRating,ContentRating
from django.contrib.auth.models import User
from .forms import RegistrationForm,ProjectForm,EditProfileForm,DesignForm,UsabilityForm,ContentForm
from django.contrib.auth.decorators import login_required
# from django.contrib.messages.context_processors.messages import
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import MerchSerializer
from rest_framework import status
import datetime






# Create your views here.
def home(request):
    form=DesignForm()
    projects = Project.objects.all()
    return render(request,'home.html',{"projects":projects, "form":form})


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

def search_project(request):
    if 'title' in request.GET and request.GET['title']:
        search_term = request.GET.get('title')
        projects = Project.search_project(search_term)
        print('projects')

        print(projects)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'projects':projects})
    else:
        message = 'Type project'
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
    def get(self, request, format=None):
        all_merch_profiles = Profile.objects.all()
        serializers = MerchSerializer(all_merch_profiles, many=True)
        return Response(serializers.data)

    def get(self, request, format=None):
        all_merch_projects = Project.objects.all()
        serializers = MerchSerializer(all_merch_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required(login_url='/login')
def add_usability(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = UsabilityForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.project = project
            rate.user_name = request.user
            rate.profile = request.user.profile

            rate.save()
        return redirect('home')

    return render(request, 'home.html')

@login_required(login_url='/login')
def add_design(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = DesignForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.project = project
            rate.user_name = request.user
            rate.profile = request.user.profile

            rate.save()
        return redirect('home')
    else:
        form = DesignForm()

    return render(request, 'home.html',{'form': form})


@login_required(login_url='/login')
def add_content(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.project = project
            rate.user_name = request.user
            rate.profile = request.user.profile

            rate.save()
        return redirect('home')

    return render(request, 'home.html')











# class MerchListProfile(APIView):
#     def get(self, request, format=None):
#         all_merch_profiles = Profile.objects.all()
#         serializers = MerchSerializer(all_merch_profiles, many=True)
#         return Response(serializers.data)
#
#
#
#     def post(self, request, format=None):
#         serializers = MerchSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
#




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