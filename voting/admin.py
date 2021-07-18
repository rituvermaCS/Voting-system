from django.contrib import admin
from .models import Feedback
from .models import Contact
from .models import Registration
from .models import Candidate
from .models import News

# Register your models here.

admin.site.register(Feedback)
admin.site.register(Contact)
admin.site.register(Registration)
admin.site.register(Candidate)
admin.site.register(News)
