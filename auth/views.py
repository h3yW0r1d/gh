from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.response import Response

class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client


    def complete_login(self, request, app, token, **kwargs) :
        # Call the base class complete_login method
        response = super().complete_login(request, app, token, **kwargs)
        # Get the extra_data from the GitHub account
        extra_data = response.user.socialaccount_set.get(provider='github').extra_data
        # Set the user's username to their GitHub login
        response.user.username = extra_data['login']
        # Save the user
        response.user.save()
        return response

    