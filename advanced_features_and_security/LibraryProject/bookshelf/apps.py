from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        post_migrate.connect(create_groups_and_permissions, sender=self)

def create_groups_and_permissions(sender, **kwargs):
    from .models import Book
    
    # Define groups
    group_permissions = {
        "Editors": ["can_create", "can_edit"],
        "Viewers": ["can_view"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"]
    }

    for group_name, perms in group_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm_codename in perms:
            perm = Permission.objects.get(codename=perm_codename, content_type__app_label="bookshelf")
            group.permissions.add(perm)


class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

