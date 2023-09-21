from django.contrib import admin
from .models import Posts
from .models import Author
from .models import Tag

# Register your models here.
admin.site.register(Posts)
admin.site.register(Author)
admin.site.register(Tag)