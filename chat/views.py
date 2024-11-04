from django.shortcuts import render

from .models import Group , Message
# Create your views here.
def index(request,group_name=None):
    group,created=Group.objects.get_or_create(name=group_name)
    print('group name is ', group)
    messages= group.messages.all()
    return render(request, 'index.html',{'group_name':group_name,'messages':messages})