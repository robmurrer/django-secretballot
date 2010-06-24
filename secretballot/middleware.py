try:
    from hashlib import md5
except ImportError:
    from md5 import md5

class SecretBallotMiddleware(object):
    def process_request(self, request):
        request.secretballot_token = self.generate_token(request)

    def generate_token(self, request):
        raise NotImplementedError


class SecretBallotIpMiddleware(SecretBallotMiddleware):
    def generate_token(self, request):
        return request.META['REMOTE_ADDR']

class SecretBallotIpUseragentMiddleware(SecretBallotMiddleware):
    def generate_token(self, request):
        try:
            s = ''.join((request.META['REMOTE_ADDR'], request.META['HTTP_USER_AGENT']))
        except:
            return None
        return md5(s).hexdigest()
