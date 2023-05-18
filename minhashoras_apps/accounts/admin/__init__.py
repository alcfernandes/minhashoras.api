from django.contrib import admin

# Import the models
from ..models import Account, User

# Import the custom admin classes
from .admin_account import AccountAdmin
from .admin_user import UserAdmin

# Register the models with the custom admin classes
admin.site.register(User, UserAdmin)
admin.site.register(Account, AccountAdmin)
