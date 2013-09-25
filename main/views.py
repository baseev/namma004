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
    profile = UserProfile.objects.get(user=user)
    context = {'profile' : profile, 'a' : 'b'}     
    return render_to_response('profile.html', context, context_instance=RequestContext(request)) 
    

@login_required
def MyPosts(request):
    user    = request.user
    context = {'profile' : user, 'a' : 'b'}  
    return render_to_response('profile.html', context, context_instance=RequestContext(request))   


    
    