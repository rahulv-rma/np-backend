from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig as BaseAdminConfig


class CustomAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_admin'


class CustomAdminConfigSite(BaseAdminConfig):
    default_site = 'custom_admin.sites.AdminSite'
