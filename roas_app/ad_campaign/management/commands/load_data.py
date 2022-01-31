import logging
import os
from csv import DictReader, reader, writer

from ad_campaign.models import Campaigns, SearchTerms, AdGroups
from django.core.management import BaseCommand
from tqdm import tqdm

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


class Command(BaseCommand):
    help = "Loads data from campaigns.csv"

    def add_arguments(self, parser):
        parser.add_argument("campaigns", nargs="+", help="One or more file paths.")
        parser.add_argument("--search_terms", nargs="+", help="One or more filepaths")
        parser.add_argument("--ad_groups", nargs="+", help="One or more filepaths")

    def handle(self, *args, **options):
        if options["campaigns"]:
            input_files = options["campaigns"]
            for file in input_files:
                self.load_data(Campaigns, 'campaign_id', file)
        if options["search_terms"]:
            input_files = options["search_terms"]
            for file in input_files:
                self.load_data(SearchTerms, 'ad_group_id', file)
        if options["ad_groups"]:
            input_files = options["ad_group"]
            for file in input_files:
                self.load_data(AdGroups, 'ad_group_id', file)

    def load_data(self, model, pk_str, file):
        """Inserts CSV data into a specific database object.

        Args:
            model (model.Model): The database model that data will be inserted into.
            pk_str (str): The name of the primary key column of the database object.
            file (str): The CSV containing the data to loaded.

        """
        object_dict = {obj.pk: obj for obj in model.objects.all()}

        with open(os.path.abspath(file)) as csv_file:
            data = DictReader(csv_file)
            next(data)
            unique_rows = 0
            object_list = []
            for i, row in enumerate(tqdm(data)):
                pk_id = int(row[pk_str])
                object_ref = object_dict.get(pk_id)
                if not object_ref:
                    object_instance = model(**row)
                    object_dict[int(object_instance.pk)] = object_instance
                    object_list.append(object_instance)
                    unique_rows += 1

            if object_list:
                model.objects.bulk_create(object_list)
                msg = f"Successfully inserted {unique_rows} rows into {model._meta.db_table} table."
            else:
                msg = f"{os.path.abspath(file)} is already saved in the {model._meta.db_table} table."

        self.stdout.write(self.style.SUCCESS(msg))
