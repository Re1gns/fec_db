from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import MemberInformationForm
from .models import MemberInformation
from django.db.models import Q
from django.http import HttpResponseBadRequest

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('member_list')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

@login_required
def form_view(request):
    if request.method == 'POST':
        form = MemberInformationForm(request.POST, request.FILES)
        if form.is_valid():
            member_info = form.save(commit=False)
            member_info.reference_id = MemberInformation.generate_reference_id()
            member_info.save()
            return redirect('success_view')
    else:
        form = MemberInformationForm(initial={'reference_id': MemberInformation.generate_reference_id()})
    return render(request, 'form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def redirect_to_form(request):
    return redirect('form_view')

def member_list(request):
    query = request.GET.get('query')
    if query:
        members = MemberInformation.objects.filter(Q(surname__icontains=query) | Q(reference_id__icontains=query))
    else:
        members = MemberInformation.objects.all()
    return render(request, 'member_list.html', {'members': members})

def edit_member(request, pk):
    member = get_object_or_404(MemberInformation, id=pk)
    if request.method == 'POST':
        form = MemberInformationForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            print(request.FILES)
            form.save()
            return redirect('member_list')
    else:
        form = MemberInformationForm(instance=member)
    return render(request, 'edit_member.html', {'form': form})

def confirm_delete(request):
    ids = request.GET.getlist('ids')
    if not ids:
        return HttpResponseBadRequest("No member IDs provided.")
    
    if request.method == 'POST':
        
        for id in ids:
            member = get_object_or_404(MemberInformation, pk=id)
            member.delete()
        return redirect('member_list')
    
    return render(request, 'delete_member.html')