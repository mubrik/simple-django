from .base import *

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

# ==========
# EMAIL SETTINGS
# ===========
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = config("SG_API_KEY")
SENDGRID_ECHO_TO_STDOUT = True
