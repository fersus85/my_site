from django.http import BadHeaderError, HttpResponse
from django.views.generic import ListView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.db.models import Sum

from .forms import ContactForm
from config.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from run.models import Year


class MainPage(ListView):
    model = Year
    template_name = "system/index.html"

    def get_context_data(self):
        context = super().get_context_data()
        total = Year.objects.aggregate(Sum('total'))
        context["total"] = f"Run: {str(total['total__sum'])} km"
        return context


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = DEFAULT_FROM_EMAIL
            message = form.cleaned_data['message']
            message += f"\tEmail from: {form.cleaned_data.get('from_email')}"
            try:
                send_mail(f'{subject}', message,
                          from_email, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Error subject')
            return redirect('success')
    else:
        return HttpResponse('invalid request')
    return render(request, "system/feedback.html", {'form': form})


def success_view(request):
    return render(request, "system/success.html",)


def tr_handler403(request, exception=None, msg=None):
    """
    Обработка ошибки 403
    """
    message = 'Доступ к этой странице ограничен.'
    if msg:
        message = msg
    return render(
        request=request,
        template_name='system/error_page.html',
        status=403,
        context={
            'title': 'Ошибка доступа: 403',
            'error_message': message,
            })


def tr_handler404(request, exception):
    """
    Обработка ошибки 404
    """
    return render(
        request=request,
        template_name='system/error_page.html',
        status=404,
        context={
            'title': 'Страница не найдена: 404',
            'error_message': 'К сожалению, такая страница не найдена.',
        })


def tr_handler500(request):
    """
    Обработка ошибки 500
    """
    return render(
        request=request,
        template_name='system/error_page.html',
        status=500,
        context={
            'title': 'Ошибка сервера: 500',
            'error_message': '''Внутренняя ошибка сайта,
                                вернитесь на главную страницу,
                                отчет мы направим администрации сайта.''',
        })
