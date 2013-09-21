from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def Profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    profile    = request.user
    context = {'profile' : profile, 'a' : 'b'}     
    return render_to_response('profile.html', context, context_instance=RequestContext(request)) 
    




    
    
    
    