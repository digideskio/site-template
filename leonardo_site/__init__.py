from django.apps import AppConfig


default_app_config = 'leonardo_site.ProjectConfig'


class Default(object):

    apps = ['leonardo_site']


class ProjectConfig(AppConfig, Default):
    name = 'leonardo_site'
    verbose_name = "{{ project_name }}"


default = Default()
