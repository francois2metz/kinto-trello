import logging
import requests

from pyramid.authentication import CallbackAuthenticationPolicy
from pyramid.interfaces import IAuthenticationPolicy
from zope.interface import implementer

logger = logging.getLogger(__name__)

TRELLO_METHOD = 'trello'

def trello_apikey(request):
    return request.registry.settings['trello.apikey']


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

        if not hasattr(request.registry, 'cache'):
            return fetch_trello(request, token)

        cache = request.registry.cache
        cache_key = "token_trello:" + token
        user_id = cache.get(cache_key)

        if not user_id:
            user_id = fetch_trello(request, token)
            cache.set(cache_key, user_id, ttl=3600*24)

        return user_id

    def fetch_trello(self, request, token)
        try:
            params = {"token": token, "key": trello_apikey(request)}
            resp = requests.get("https://api.trello.com/1/members/me", params=params)
            resp.raise_for_status()
            userinfo = resp.json()
            user_id = userinfo['id']
            return user_id
        except Exception as e:
            logger.warn(e)
            return None
