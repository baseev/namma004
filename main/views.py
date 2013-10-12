from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from main.models import UserProfile


@login_required
def Home(request):
    user    = request.user
    context = {'profile' : user, 'a' : 'b'}  
    return render_to_response('home.html', context, context_instance=RequestContext(request)) 


@login_required
def Profile(request):
    user    = request.user
    profile = None
    try:
        profile = UserProfile.objects.get(user=user)
    except:
        pass
    context = {'profile' : profile, 'a' : 'b'}     
    return render_to_response('main/profile.html', context, context_instance=RequestContext(request)) 
    

