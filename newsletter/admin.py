from django.contrib import admin

from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
    )


admin.site.register(Newsletter, NewsletterAdmin)
