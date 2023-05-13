from django.contrib import admin

# Import the models
from ..models import Client, Project

# Import the custom admin classes
from .admin_client import ClientAdmin
from .admin_project import ProjectAdmin

# Register the models with the custom admin classes
admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
