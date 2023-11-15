import os
from .base import *
from ..celery import *
enviroment = os.getenv('ENV', 'local')

if enviroment == 'prod':
    from .production import *
else:
    from .local import *
