#!/usr/bin/env python
import os
import sys

"""setup(
    name='mysite',
    version='0.1.0',
    install_requires=[],  # Don't put anything here, just use requirements.txt
    packages=['mysite'],
    package_dir={'mysite': 'src/mysite'},
)
from setuptools import setup, find_packages
import os
"""
setup(
    name='django-project-templates',
    version = "0.11",
    description="Paster templates for creating Django projects",
    author='Gareth Rushgrove',
    author_email='gareth@morethanseven.net',
    url='http://github.com/garethr/django-project-templates/',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    license = "MIT",
    keywords = "django paster",
    install_requires=[
        'setuptools',
        'PasteScript>=1.3',
        'Cheetah',
        'fabric',
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points="""
[paste.paster_create_template]
django_project=django_project_templates.pastertemplates:DjangoProjectTemplate
django_cruisecontrol_project=django_project_templates.pastertemplates:DjangoCruiseControlTemplate
newsapps_project=django_project_templates.pastertemplates:NewsAppsProjectTemplate
cir_project=django_project_templates.pastertemplates:CIRProjectTemplate
heroku_project=django_project_templates.pastertemplates:HerokuProjectTemplate
""",
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)