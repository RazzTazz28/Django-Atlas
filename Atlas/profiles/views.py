from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.contrib import messages

from .models import UserProfile


@login_required(login_url='login_user')
def profiles(request):
    indexID = request.user
    form = ProfileForm(instance=indexID)
    profile = UserProfile.objects.get
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            messages.success(request, ("The file is valid"))
            form.save()
        else:
            messages.success(request, ("Invalid File."))

    context = {'form': form}
    return render(request, "profiles/profiles.html", context)


def logoutUser(request):
    logout(request)
    return redirect('login_user')
