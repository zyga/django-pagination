#!/usr/bin/env python

import django
import os
import sys

from django.core.management import call_command


def runtests():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'dj_pagination.tests.settings'

    try:
        django.setup()
    except AttributeError:  # for Django 1.6 compatible
        pass

    failures = call_command('test', 'dj_pagination')
    sys.exit(bool(failures))

if __name__ == '__main__':
    runtests()
