from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ticket,Comment
from dashboard.models import panelMember,panel
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.

def valid(pl,id):
    if panelMember.objects.filter(user=id,panel=pl):
        return True
    else:
        return False


@login_required
def listview(request,pl):
    id=request.user.id
    object = ticket.objects.filter(panel=pl).order_by('created_at')
    object1 = panel.objects.filter (id=pl)
    if valid(pl,id):
        return render(request, 'tasks/list.html',{
        'all_items':object,
        'panel':object1
        })
    else:
        return HttpResponseRedirect('/dashboard')

@login_required
def addTodo(request,pl):
    id=request.user.id
    if valid(pl,id):
        object = ticket(
        content= request.POST['content'],
        title = request.POST['title']
            )
        p= panel.objects.get(id=pl)
        object.panel=p
        time = datetime.now()
        object.created_at = time.strftime("%Y-%m-%d %H:%M:%S")
        object.created_by = request.user
        object.save()
        return HttpResponseRedirect('/task/list/%s'%pl)
    else:
        return HttpResponseRedirect('/dashboard')


@login_required
def deletetodo(request, pk,pl):
    id=request.user.id
    if valid(pl,id):
        object=ticket.objects.get(id=pk)
        object.delete()
        return HttpResponseRedirect('/task/list/%s'%pl)
    else:
        return HttpResponseRedirect('/dashboard')

@login_required
def update(request, pk,pl):
    id=request.user.id
    if valid(pl,id):
        object=ticket.objects.get(id=pk)
        object.status= object.status + 1
        object.save()
        return HttpResponseRedirect('/task/list/%s'%pl)
    else:
        return HttpResponseRedirect('/dashboard')

@login_required
def back(request, pk,pl):
    id=request.user.id
    if valid(pl,id):
        object=ticket.objects.get(id=pk)
        object.status= object.status - 1
        object.save()
        return HttpResponseRedirect('/task/list/%s'%pl)
    else:
        return HttpResponseRedirect('/dashboard')

@login_required
def edit(request,pk,pl):
    id=request.user.id
    if valid(pl,id):
        object=ticket.objects.get(id=pk)
        object.title = request.POST['title']
        object.content = request.POST['content']
        object.save()
        return HttpResponseRedirect('/task/list/%s' %pl)
    else:
        return HttpResponseRedirect('/dashboard')


@login_required
def get(request,pl,pk):
    id=request.user.id
    if valid(pl,id):
        p = panel.objects.filter(id=pl)
        object = ticket.objects.filter(id=pk)
        att= Comment.objects.filter(ticket_id=pk).order_by('created_at')
        return render(request, 'tasks/tickets_details.html',{
        'panel':p,
        'titket':object,
        'comment':att,
        })
    else:
        return HttpResponseRedirect('/dashboard')

@login_required
def addcommant(request,pl,pk):
    id=request.user.id
    if valid(pl,id):
        object = Comment(
        body = request.POST['body']
            )
        name=ticket.objects.get(id=pk)
        object.ticket=name
        time = datetime.now()
        object.created_at = time.strftime("%Y-%m-%d %H:%M:%S")
        object.created_by = request.user
        object.save()
        return HttpResponseRedirect('/task/get/%s/%s' %(pl, pk))
    else:
        return HttpResponseRedirect('/dashboard')

@login_required
def deletecommant(request,pl,pk,com):
    c=Comment.objects.get(id=com)
    c.delete()
    return HttpResponseRedirect('/task/get/%s/%s' %(pk, pl))
