"""
Overrides settings specific to the local environment.
If Backend/Environ/Dev.env file exists.
"""

import os
from Backend.settings import base_settings as bs

if __name__=='Backend.settings.local_settings':

  bs.INSTALLED_APPS.append(
    "django_extensions"
  )

  os.environ['JUPYTER_ALLOW_INSECURE_WRITES'] = 'true'
  os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = 'true'
  os.environ["JUPYTER_PATH"] = str(bs.BASE_DIR)

  SHELL_PLUS = 'notebook'
  NOTEBOOK_ARGUMENTS = ['--no-browser']


__all__ = [i for i in dir() if i.isupper()]
