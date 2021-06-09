from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import contactForm

# Create your views here.
def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    context = {'title': title,'form': form,}

    if form.is_valid():
        print ("Send Email")
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from Django'
        message = '%s %s' %(comment, name)
        emailFrom = settings.EMAIL_HOST_USER
        emailTo = [form.cleaned_data['email']]
        send_mail(
            subject,
            message,
            emailFrom,
            emailTo,
            fail_silently=False,
        )
        title = 'Thanks for suscribe!'
        confirm_message='We send you a message.'
        context = {'title': title,'confirm_message': confirm_message,}
    # context = locals()
    template = 'contact.html'
    return render(request, template, context)
