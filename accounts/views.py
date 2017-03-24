from django.core.urlresolvers import reverse_lazy
from django.views import generic
from accounts.forms import *


class CreateUserView(generic.CreateView):

    template_name = 'accounts/create.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')
