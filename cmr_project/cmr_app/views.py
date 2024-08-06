from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import CMR
from .forms import CMRForm

@login_required
def dashboard(request):
    if request.user.is_staff:
        users = User.objects.all()
        cmrs = CMR.objects.all()  # Adaugat pentru a vizualiza toate documentele
    else:
        users = None
        cmrs = CMR.objects.filter(user=request.user)
    return render(request, 'cmr_app/dashboard.html', {'users': users, 'cmrs': cmrs})

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
