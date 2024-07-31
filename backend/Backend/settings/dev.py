import os

from .common import Common

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Dev(Common):
    # INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    DEBUG = True

   

    # SECURITY WARNING: update this when you have the production host
    ALLOWED_HOSTS = ['*']

    CSRF_TRUSTED_ORIGINS = ['https://kuku-rho.vercel.app','https://www.kuku-rho.vercel.app','https://backend.ecelliitr.org','http://127.0.0.1:8000']

    MIDDLEWARE = Common.MIDDLEWARE + ["whitenoise.middleware.WhiteNoiseMiddleware"]

    # STATICFILES_STORAGES = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    STATIC_ROOT=os.path.join(BASE_DIR,'static')
    STATIC_URL = "/static/"

    MEDIA_ROOT = os.path.join(BASE_DIR,'media')
    MEDIA_URL = '/media_files/'

   

    
    STORAGES = {
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
        "media": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
            "LOCATION": os.path.join(BASE_DIR, "media"),
        },
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
            "LOCATION": os.path.join(BASE_DIR, "media"),
        },
        
       
    }