from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import panel,panelMember
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.

def valid(pk,id):
    if panelMember.objects.filter(user=id,panel=pk):
        return True
    else:
        return False


@login_required
def home(request):
    object = panelMember.objects.filter(user=request.user.id)
    return render(request, 'dashboard/dashboard.html',{'all_items':object})

@login_required
def setting(request,pk):
    object1 = get_list_or_404(panel, id=pk)
    object2 = get_list_or_404(panelMember, panel=pk)
    if valid(pk,request.user.id):
        return render(request, 'dashboard/dashboard-setting.html',{
        'panel_setting':object1,
        'panel_member':object2,
        })
    else:
        return HttpResponseRedirect('/dashboard')


@login_required
def addpanel(request):
    object = panel(
        name= request.POST['name'],
        )
    time = datetime.now()
    object.created_at = time.strftime("%Y-%m-%d %H:%M:%S")
    object.created_by = request.user
    object.save()
    admin = panelMember(
        panel=object,
        user=request.user
    )
    admin.save()
    return HttpResponseRedirect('/dashboard')

def delete(request,pk):
    p = panel.objects.get(id=pk)
    queryset = panelMember.objects.filter(panel=p,user=request.user.id)
    check=get_object_or_404(queryset)
    check.delete()
    return HttpResponseRedirect('/dashboard')

@login_required
def addmermber(request,pk):
    queryset = panel.objects.get(id=pk)
    u = User.objects.filter(email=request.POST['username'])
    user=get_object_or_404(u)
    object = panelMember(
    panel=panel.objects.get(id=pk),
    user=user
    )
    object.save()
    return HttpResponseRedirect('/dashboard/setting/%s'%pk)


@login_required
def deletemamber(request,pk,userid):
    p = panel.objects.get(id=pk)
    queryset = panelMember.objects.filter(panel=p,user=userid)
    check=get_object_or_404(queryset)
    check.delete()
    return HttpResponseRedirect('/dashboard/setting/%s'%pk)
