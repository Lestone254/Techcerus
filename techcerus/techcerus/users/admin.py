from django.contrib import admin
from .models import userMsg, projectPost, clientTestimonials, blogPosts, freeQuote, userServices

# Register your models here.
admin.site.register(userMsg)
admin.site.register(projectPost)
admin.site.register(clientTestimonials)
admin.site.register(blogPosts)
admin.site.register(freeQuote)
admin.site.register(userServices)
