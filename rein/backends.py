from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user): #note the absence of request which was neded in older version
        return ('core:create')
