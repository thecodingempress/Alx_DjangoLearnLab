from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

@receiver(post_migrate)
def create_groups_perms(sender, **kwargs):
    if sender.label != 'bookshelf':
        return
    ct = ContentType.objects.get_for_model(Book)
    perms = {
        'can_view': Permission.objects.get(codename='can_view', content_type=ct),
        'can_create': Permission.objects.get(codename='can_create', content_type=ct),
        'can_edit': Permission.objects.get(codename='can_edit', content_type=ct),
        'can_delete': Permission.objects.get(codename='can_delete', content_type=ct),
    }
    editors, _ = Group.objects.get_or_create(name='Editors')
    viewers, _ = Group.objects.get_or_create(name='Viewers')
    admins, _ = Group.objects.get_or_create(name='Admins')

    viewers.permissions.set([perms['can_view']])
    editors.permissions.set([perms['can_view'], perms['can_create'], perms['can_edit']])
    admins.permissions.set([perms['can_view'], perms['can_create'], perms['can_edit'], perms['can_delete']])
