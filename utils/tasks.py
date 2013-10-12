import hashlib
import random

from urlparse import parse_qs
from twython import Twython
from celery.task import task
from kisaa.settings import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET
from registration.models import RegistrationProfile





def welcome_new_user(backend, user, social_user, is_new=False, new_association=False, *args, **kwargs):
    """
        Part of SOCIAL_AUTH_PIPELINE. Works with django-social-auth==0.7.21 or newer
        @backend - social_auth.backends.twitter.TwitterBackend (or other) object
        @user - User (if is_new) or django.utils.functional.SimpleLazyObject (if new_association)
        @social_user - UserSocialAuth object
    """
    
    if is_new:
        #create_registration_profile.delay(user)
        create_registration_profile(user)
        #send_welcome_email.delay(user.email, user.first_name)



    if backend.name == 'twitter':
        if is_new or new_association:
            access_token = social_user.extra_data['access_token']
            parsed_tokens = parse_qs(access_token)
            oauth_token = parsed_tokens['oauth_token'][0]
            oauth_secret = parsed_tokens['oauth_token_secret'][0]
            #tweet_on_join.delay(oauth_token, oauth_secret)
            tweet_on_join(oauth_token, oauth_secret)
    return None




@task
def tweet_on_join(oauth_token, oauth_secret):
    """
        Tweet when the user is logged in for the first time or
        when new Twitter account is associated.

        @oauth_token - string
        @oauth_secret - string
    """
    twitter = Twython(app_key=TWITTER_CONSUMER_KEY,
                         app_secret=TWITTER_CONSUMER_SECRET,
                         oauth_token=oauth_token,
                         oauth_token_secret=oauth_secret
                         )
    
    twitter.update_status(status='Started following open source changes!')


"""
Registration profile added
"""
def create_registration_profile(user):
    
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    username = user.username
    if isinstance(username, unicode):
        username = username.encode('utf-8')
    activation_key = hashlib.sha1(salt+username).hexdigest()
    RegistrationProfile(user=user,
                           activation_key=activation_key).save()