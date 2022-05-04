#settings.py
import os
DEBUG = True
if DEBUG:
    from MAIN.local_settings import *
else:
    from MAIN.production_settings import *
