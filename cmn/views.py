from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView

decorators = [login_required]


@method_decorator(decorators, name='get')
class CmnList(TemplateView):
	template_name = 'cmn/list.html'
	
	def get(self, request, *args, **kwargs):
		""""""
		user = request.user
		
		context = super(CmnList, self).get_context_data(**kwargs)
		
		return self.render_to_response(context)
