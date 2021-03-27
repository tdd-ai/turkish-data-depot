import os
from django.core.management.base import BaseCommand
from datasets.models import * 

help_message = f"""
Seed the datasets application dataset
"""

class Command(BaseCommand):
    """
    admin_setup: Command to set-up database for the application
    """
    help = help_message

    def add_arguments(self, parser):
        parser.add_argument('seed_file', type=str)

    def handle(self, *args, **kwargs):
        seed_file = kwargs.get('seed_file')

        try:
            if not os.path.exists(seed_file):
                raise FileNotFoundError("This file doesn't exist: " + seed_file)
            
            # TODO:
            # load json file
            # seed the models

        except Exception as e:
            print(e)