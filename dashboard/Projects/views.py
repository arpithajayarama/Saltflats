# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return HttpResponse("Hello. You're at the dashboard .")



def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.groups.filter(name="admins").exists():
        # user is an admin
        return redirect("admin")
    else:
        return redirect("other_view")
