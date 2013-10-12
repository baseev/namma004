# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.core import serializers
import json
from django.template.loader import render_to_string


from django.contrib.auth.decorators import login_required

from activity.models import UserPost


@login_required
def MyPosts(request):
    user    = request.user
    posts   = UserPost.objects.filter(user=user); 
    context = {'posts' : posts, 'a' : 'b'}  
    return render_to_response('activity/my-posts.html', context, context_instance=RequestContext(request))   



#@login_required
def ViewMyPost(request):
   # user    = request.user
   # post   = UserPost.objects.get(id=request.GET['post-id']); 
    context = {'post' : 'P', 'a' : 'b'}  
    return render_to_response('activity/view-my-post.html', context, context_instance=RequestContext(request))   


@login_required
def Test(request):
    user    = request.user
    post   = UserPost.objects.get(id=request.GET['post-id']); 
    context = {'post' : post, 'a' : 'b'}  
    d = render_to_string('activity/view-my-post.html', context);
    data = {'html': d}    
    return HttpResponse(json.dumps(data), mimetype="text/html")
    #return HttpResponse(json.dumps(data), mimetype="application/json")


@login_required
def EditMyPost(request):
    user    = request.user
    post   = UserPost.objects.get(id=request.GET['post-id']); 
    context = {'post' : post, 'a' : 'b'}  
    return render_to_response('activity/view-my-post.html', context, context_instance=RequestContext(request))   


@login_required
def SaveEditPost(request):
    user    = request.user
    post   = UserPost.objects.get(id=request.POST['post-id']) 
    post.content = request.POST['post-content']
    post.post_type = request.POST['post-type']
    post.save()
    context = {'post' : post, 'a' : 'b'}  
    return render_to_response('activity/view-my-post.html', context, context_instance=RequestContext(request))   


@login_required
def AddNewPost(request):
    user    = request.user
    post   = UserPost.objects.get(id=request.GET['post-id']); 
    context = {'post' : post, 'a' : 'b'}  
    return render_to_response('activity/view-my-post.html', context, context_instance=RequestContext(request))

@login_required
def SaveNewPost(request):
    user    = request.user
    post   = UserPost.objects.get(id=request.GET['post-id']); 
    context = {'post' : post, 'a' : 'b'}  
    return render_to_response('activity/view-my-post.html', context, context_instance=RequestContext(request))
    
    

@login_required
def DeletePost(request):
    user    = request.user
    post   = UserPost.objects.get(id=request.GET['post-id']); 
    context = {'post' : post, 'a' : 'b'}  
    return render_to_response('activity/view-my-post.html', context, context_instance=RequestContext(request))


    
    