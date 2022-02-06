import os
from csv import DictReader

from ad_campaign.models import AdGroup, Campaign, SearchTerm
from django.core.management import BaseCommand
from tqdm import tqdm


class Command(BaseCommand):
    help = "Loads data from campaigns.csv"

    def add_arguments(self, parser):
        parser.add_argument("campaigns", nargs="+", help="One or more file paths.")
        parser.add_argument("--search_terms", nargs="+", help="One or more filepaths")
        parser.add_argument("--ad_groups", nargs="+", help="One or more filepaths")

    def handle(self, *args, **options):
        campaign_dict = None
        adgroup_dict = None
        if options["campaigns"]:
            input_files = options["campaigns"]
            for file in input_files:
                campaign_dict = self.load_data(Campaign, "campaign_id", file)
            if options["ad_groups"]:
                input_files = options["ad_groups"]
                for file in input_files:
                    adgroup_dict = self.load_data(
                        AdGroup, "ad_group_id", file, campaign_dict
                    )
                if options["search_terms"]:
                    input_files = options["search_terms"]
                    for file in input_files:
                        self.load_data(
                            SearchTerm, "ad_group_id", file, campaign_dict, adgroup_dict
                        )

    def load_data(self, model, pk_str, file, campaign_dict=None, adgroup_dict=None):
        """Inserts CSV data into a specific database object.

        Args:
            model (model.Model): The database model that data will be inserted into.
            pk_str (str): The name of the primary key column of the database object.
            file (str): The CSV containing the data to loaded.
            campaign_dict (dict):
            adgroup_dict (dict):

        """
        object_dict = {obj.pk: obj for obj in model.objects.all()}

        with open(file) as csv_file:
            data = DictReader(csv_file)
            next(data)
            unique_rows = 0
            object_list = []
            for i, row in enumerate(tqdm(data)):
                pk_id = int(row[pk_str])
                object_ref = object_dict.get(pk_id)
                if not object_ref:
                    if campaign_dict and adgroup_dict:
                        row["campaign_id"] = campaign_dict[int(row["campaign_id"])]
                        row["ad_group_id"] = adgroup_dict[int(row["ad_group_id"])]
                        try:
                            row["roas"] = float(row["conversion_value"]) / float(
                                row["cost"]
                            )
                        except ZeroDivisionError:
                            row["roas"] = 0
                        object_instance = model(**row)
                    elif campaign_dict and not adgroup_dict:
                        row["campaign_id"] = campaign_dict[int(row["campaign_id"])]
                        object_instance = model(**row)
                        object_dict[int(object_instance.pk)] = object_instance
                    else:
                        object_instance = model(**row)
                        object_dict[int(object_instance.pk)] = object_instance
                    object_list.append(object_instance)
                    unique_rows += 1
                if len(object_list) == 5000:
                    model.objects.bulk_create(object_list, ignore_conflicts=True)
                    msg = (
                        f"Successfully inserted 5000 "
                        f"rows into {model._meta.db_table} table."
                    )
                    self.stdout.write(self.style.SUCCESS(msg))
                    object_list = []
            if object_list:
                model.objects.bulk_create(object_list, ignore_conflicts=True)
                msg = (
                    f"Successfully inserted {unique_rows} "
                    f"rows into {model._meta.db_table} table."
                )
            else:
                msg = (
                    f"{os.path.abspath(file)} is already saved in the "
                    f"{model._meta.db_table} table."
                )

        self.stdout.write(self.style.SUCCESS(msg))

        return object_dict
