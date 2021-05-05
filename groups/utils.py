from django.shortcuts import redirect

from .filter import GroupsFilter
from .models import *


def create_group_request(request, form):
    user = request.user
    if form.is_valid():
        form.save()
        return redirect('groups_index')


def get_group_members(group_id, is_approved):
    members = Group.objects.get(id=group_id).members.filter(membership__approved=is_approved)
    my_members_id = [ids[0] for ids in members.values_list('id')]
    users = User.objects.filter(pk__in=my_members_id)
    return users


def get_index_context(request):
    memberships = [group[0] for group in request.user.group_set.all().values_list('id')]
    groups = Group.objects.all()
    user_query = request.GET.get('search_name')
    my_filter = GroupsFilter(request.GET, queryset=groups)
    if request.GET and user_query:
        print("yes")
        groups = my_filter.qs
        context = {'groups': groups, 'memberships': memberships, "filter": my_filter, }
    else:
        print("no")
        context = {'groups': groups, 'memberships': memberships, "filter": my_filter, }
    print(groups)
    return context
