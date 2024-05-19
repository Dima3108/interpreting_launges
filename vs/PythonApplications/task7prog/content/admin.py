from django.contrib import admin
from .models import Question
from .models import iatp
from .models import type_of_painting
from .models import authors
admin.site.register(Question)
admin.site.register(type_of_painting)
admin.site.register(iatp)
admin.site.register(authors)
# Register your models here.
