from django.contrib import admin
from .models import Topics, Remarks, Homework, Submission, Project, Reminder, TimeTable

admin.site.register(Topics)
admin.site.register(Remarks)
admin.site.register(Homework)
admin.site.register(Submission)
admin.site.register(Project)
admin.site.register(Reminder)
admin.site.register(TimeTable)

