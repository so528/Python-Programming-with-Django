from .forms import MyForm
from django.views.generic.edit import FormView

class MyFormView(FormView):
    form_class = MyForm
    template_name = 'form_template.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        # cleaned_data로 관련 로직 처리
        return super().form_valid(form)
