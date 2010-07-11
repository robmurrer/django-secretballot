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
        try:
            return request.META['REMOTE_ADDR']
        except:
            return None
            
class SecretBallotIpUseragentMiddleware(SecretBallotMiddleware):
    def generate_token(self, request):
        try:
            if request.user.is_authenticated():
                s = request.user.username
            else:                     
                s = ''.join((request.META['REMOTE_ADDR'], request.META['HTTP_USER_AGENT']))
            
            return md5(s).hexdigest()
                    
        except:
            return None
        

