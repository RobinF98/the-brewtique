from django.shortcuts import render, redirect, reverse

from profiles.models import UserProfile
from .forms import NewsletterForm
from django.contrib.auth.decorators import login_required


@login_required
def newsletter(request):
    '''View and submit newsletter subscription details'''

    if request.method == "POST":

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
        }
        newsletter_form = NewsletterForm(form_data)
        if newsletter_form.is_valid():
            newsletter_form.save()
        return redirect(reverse('newsletter_success'))

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            newsletter_form = NewsletterForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
            })
        except UserProfile.DoesNotExist:
            newsletter_form = NewsletterForm()
    else:
        newsletter_form = NewsletterForm()

    template = 'newsletter/newsletter.html'

    context = {
        'form': newsletter_form,
    }

    return render(request, template, context)


def newsletter_success(request):
    template = 'newsletter/newsletter_success.html'

    return render(request, template)
