# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article,tags,NewsLetterRecipients

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)


# Register your models here.
admin.site.register(Article)
admin.site.register(tags)
admin.site.register(NewsLetterRecipients)
