from django.contrib import admin
from ToDo_App.models import Task

# Register your models here.
admin.site.register(Task)


admin.site.site_header = "A_A_K - ToDo Panel"
admin.site.site_title = "A_A_K - Site"


