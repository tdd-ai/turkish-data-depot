import os
import json
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
            
            with open(seed_file, "r", encoding="utf-8") as fi:
                print("Reading seed file...")
                data = json.loads(fi.read())
                for _type in data["types"]:
                    _t = Type.objects.get_or_create(name=_type["value"], description=_type["description"], catalog_acronym=_type["catalog_acronym"])

                for data_type in data["data_types"]:
                    _td = DataType.objects.get_or_create(name=data_type["value"], description=data_type["description"])

                for annotation in data["annotations"]:
                    _an = Annotation.objects.get_or_create(name=annotation["value"], description=annotation["description"])

                for source in data["sources"]:
                    _s  = Source.objects.get_or_create(name=source["value"], description=source["description"])

                for compression in data["compressions"]:
                    _c = Compression.objects.get_or_create(name=compression["value"], description=compression["description"])

                for _format in data["formats"]:
                    _f = Format.objects.get_or_create(name=_format["value"], description=_format["description"])

                for _license in data["licenses"]:
                    _l = License.objects.get_or_create(name=_license["value"], description=_license["description"], catalog_acronym=_license["catalog_acronym"])
        except Exception as e:
            print(e)