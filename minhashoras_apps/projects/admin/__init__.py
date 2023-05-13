from django.contrib import admin

# Import the models
from ..models import Client

# Import the custom admin classes
from .admin_client import ClientAdmin

# Register the models with the custom admin classes
admin.site.register(Client, ClientAdmin)
