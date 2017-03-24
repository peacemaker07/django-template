from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

decorators = [login_required]


@method_decorator(decorators, name='get')
class HtmlCssList(TemplateView):
	template_name = 'html_css/list.html'
	
	def get(self, request, *args, **kwargs):
		""""""
		user = request.user
		
		context = super(HtmlCssList, self).get_context_data(**kwargs)
		
		return self.render_to_response(context)
