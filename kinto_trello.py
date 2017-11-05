import logging

import requests
from pyramid.authentication import CallbackAuthenticationPolicy
from pyramid.interfaces import IAuthenticationPolicy
from zope.interface import implementer

logger = logging.getLogger(__name__)

TRELLO_METHOD = 'trello'

@implementer(IAuthenticationPolicy)
class TrelloAuthenticationPolicy(CallbackAuthenticationPolicy):
    def __init__(self, realm='Realm'):
        self.realm = realm

    def unauthenticated_userid(self, request):
        user_id = self._get_credentials(request)
        return user_id

    def forget(self, request):
        return [('WWW-Authenticate', '%s realm="%s"' % (TRELLO_METHOD, self.realm))]

    def _get_credentials(self, request):
        authorization = request.headers.get('Authorization', '')
        try:
            authmeth, token = authorization.split(' ', 1)
            authmeth = authmeth.lower()
        except ValueError:
            return None
        if authmeth != TRELLO_METHOD.lower():
            return None
        try:
            headers = {"Authorization": "token %s" % token}
            resp = requests.get("https://api.trello.com/1/members/me", headers=headers)
            resp.raise_for_status()
            userinfo = resp.json()
            user_id = userinfo['id']
            return user_id
        except Exception as e:
            logger.warn(e)
            return None
