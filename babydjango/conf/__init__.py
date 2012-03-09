import os
import sys
import importlib

from babydjango.conf import global_settings

ENVIRONMENT_VARIABLE = "BABYDJANGO_SETTINGS_MODULE"

class Settings(object):
    def __init__(self):
        """
        Initialize settings from the local project.
        """

        # Get all default settings first and set those up
        for setting in dir(global_settings):
            if setting == setting.upper():
                setattr(self, setting, getattr(global_settings, setting))

        try:
            settings_module = os.environ[ENVIRONMENT_VARIABLE]
            if not settings_module:
                raise KeyError
        except KeyError:
            raise ImportError("Settings can't be imported because '%s' environment variable isn't set." % ENVIRONMENT_VARIABLE)

        mod = importlib.import_module(settings_module)

        # Take settings from settings file for the project
        # and set the properties to the current object
        for setting in dir(mod):
            if setting == setting.upper():
                setattr(self, setting, getattr(mod, setting))


settings = Settings()
