from django.contrib import admin
from .models import Experience, Project, Contact

admin.site.site_header = 'My Portfolio'
admin.site.index_title = 'Opeyemi Adenuga'
admin.site.site_title = 'Opeyemi Adenuga'

class ExperienceAdmin(admin.ModelAdmin):
    display = ("title", "company", "start_date", "end_date", "description")
    
    
class ProjectAdmin(admin.ModelAdmin):
    display = ("title", "description", "link")


class ContactAdmin(admin.ModelAdmin):
    display = ("name", "email", "message")
    fields = ("name", "email", "message")


    

admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Contact, ContactAdmin)
