from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import CMR
from .forms import CMRForm

@user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    users = User.objects.all()
    return render(request, 'cmr_app/dashboard.html', {'users': users})

@user_passes_test(lambda u: u.is_staff)
def user_documents(request, user_id):
    user = get_object_or_404(User, id=user_id)
    documents = CMR.objects.filter(user=user)
    return render(request, 'cmr_app/user_documents.html', {'user': user, 'documents': documents})

@login_required
def upload_cmr(request):
    if request.method == 'POST':
        form = CMRForm(request.POST, request.FILES)
        if form.is_valid():
            cmr = form.save(commit=False)
            cmr.user = request.user
            cmr.save()
            return redirect('cmr_app:dashboard')
    else:
        form = CMRForm()
    return render(request, 'cmr_app/upload_cmr.html', {'form': form})
