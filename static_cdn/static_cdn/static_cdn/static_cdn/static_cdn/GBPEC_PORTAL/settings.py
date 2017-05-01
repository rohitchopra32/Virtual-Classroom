"""
Django settings for GBPEC_PORTAL project.

Generated by 'django-admin startproject' using Django 1.9.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_l*d3b)ioe*4!!ig8ro@fu@5-@3for0rbzgg5zrcg@y++(6la!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rohitchopra32@gmail.com'
EMAIL_HOST_PASSWORD = 'awsdlumia'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True

LOGIN_URL = '/'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pagination',
    'postman',
    'mailer',
    'pagedown',
    'student',
    'teacher',
    'classroom',
    'posts',
    'comments',
    'fourms',
    'background',
    
]


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'mobileesp.middleware.MobileDetectionMiddleware',
]

ROOT_URLCONF = 'GBPEC_PORTAL.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "postman.context_processors.inbox",
                'django.contrib.messages.context_processors.messages',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'GBPEC_PORTAL.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'portal',
        # 'USER': 'admin',
        # 'PASSWORD': 'awsdlumia',
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'portal',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/


STATIC_URL = '/static/'

STATICFILES_DIRS=[
    os.path.join(BASE_DIR)

]

STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn")
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media_cdn")

SITE_ID = 1


POSTMAN_AUTO_MODERATE_AS = True
POSTMAN_MAILER_APP = None
POSTMAN_NOTIFIER_APP = None

FILE_UPLOAD_HANDLERS = ("django_excel.ExcelMemoryFileUploadHandler",
                        "django_excel.TemporaryExcelFileUploadHandler")


# CRISPY_TEMPLATE_PACK = 'bootstrap3'

# COMMENTS_APP = 'threadedcomments'

# FLUENT_COMMENTS_FORM_CLASS = 'fluent_comments.forms.FluentCommentForm'

# FLUENT_COMMENTS_FORM_CSS_CLASS = 'comments-form form-horizontal'
# FLUENT_COMMENTS_LABEL_CSS_CLASS = 'col-sm-2'
# FLUENT_COMMENTS_FIELD_CSS_CLASS = 'col-sm-10'

# FLUENT_COMMENTS_USE_EMAIL_NOTIFICATION = True
