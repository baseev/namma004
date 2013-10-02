from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from main.models import UserProfile, UserPost

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
    return render_to_response('profile.html', context, context_instance=RequestContext(request)) 
    

@login_required
def MyPosts(request):
    user    = request.user
    posts   = UserPost.objects.filter(user=user); 
    context = {'posts' : posts, 'a' : 'b'}  
    return render_to_response('posts/my-posts.html', context, context_instance=RequestContext(request))   



@login_required
def ViewMyPost(request):
    user    = request.user
    post   = UserPost.objects.get(id=request.GET['post-id']); 
    context = {'post' : post, 'a' : 'b'}  
    return render_to_response('posts/view-my-post.html', context, context_instance=RequestContext(request))   


@login_required
def EditMyPost(request):
    user    = request.user
    post   = UserPost.objects.get(id=request.GET['post-id']); 
    context = {'post' : post, 'a' : 'b'}  
    return render_to_response('posts/view-my-post.html', context, context_instance=RequestContext(request))   


@login_required
def SaveEditPost(request):
    user    = request.user
    post   = UserPost.objects.get(id=request.GET['post-id']); 
    context = {'post' : post, 'a' : 'b'}  
    return render_to_response('posts/view-my-post.html', context, context_instance=RequestContext(request))   


@login_required
def AddNewPost(request):
    user    = request.user
    post   = UserPost.objects.get(id=request.GET['post-id']); 
    context = {'post' : post, 'a' : 'b'}  
    return render_to_response('posts/view-my-post.html', context, context_instance=RequestContext(request))

@login_required
def SaveNewPost(request):
    user    = request.user
    post   = UserPost.objects.get(id=request.GET['post-id']); 
    context = {'post' : post, 'a' : 'b'}  
    return render_to_response('posts/view-my-post.html', context, context_instance=RequestContext(request))
    
    

@login_required
def DeletePost(request):
    user    = request.user
    post   = UserPost.objects.get(id=request.GET['post-id']); 
    context = {'post' : post, 'a' : 'b'}  
    return render_to_response('posts/view-my-post.html', context, context_instance=RequestContext(request))


    
    