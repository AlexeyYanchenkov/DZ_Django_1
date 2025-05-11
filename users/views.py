from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import CustomUserCreationForm
from .models import CustomUser

class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_mail(
            'Добро пожаловать!',
            'Спасибо за регистрацию на нашем сайте.',
            'from@example.com',
            [form.cleaned_data['email']],
            fail_silently=False,
        )
        return response