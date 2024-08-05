from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CMR
from .forms import CMRForm

@login_required
def upload_cmr(request):
    if request.method == 'POST':
        form = CMRForm(request.POST, request.FILES)
        if form.is_valid():
            cmr = form.save(commit=False)
            cmr.user = request.user
            cmr.save()
            return redirect('dashboard')
    else:
        form = CMRForm()
    return render(request, 'cmr_app/upload_cmr.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.is_staff:
        cmrs = CMR.objects.all()
    else:
        cmrs = CMR.objects.filter(user=request.user)
    return render(request, 'cmr_app/dashboard.html', {'cmrs': cmrs})
