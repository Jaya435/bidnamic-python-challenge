import logging
import os
from csv import DictReader

from ad_campaign.models import Campaigns
from django.core.management import BaseCommand
from tqdm import tqdm

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV files,
run `python manage.py flush` for a new empty
database with tables"""


class Command(BaseCommand):
    help = "Loads data from campaigns.csv"

    def add_arguments(self, parser):
        parser.add_argument("campaigns", nargs="+", help="One or more file paths.")
        parser.add_argument("--search_terms", nargs="+", help="One or more filepaths")

    def handle(self, *args, **options):
        if options["campaigns"]:
            input_files = options["campaigns"]
            for file in input_files:
                with open(os.path.abspath(file)) as csv_file:
                    data = DictReader(csv_file)
                    next(data)
                    campaign_dict = {
                        campaign.campaign_id: campaign
                        for campaign in Campaigns.objects.all()
                    }
                    campaign_list = []
                    for i, row in enumerate(tqdm(data)):
                        campaign_id = row["campaign_id"]
                        campaign = campaign_dict.get(campaign_id)
                        if not campaign:
                            campaign = Campaigns(
                                campaign_id=row["campaign_id"],
                                structure_value=row["structure_value"],
                                status=row["status"],
                            )
                            campaign_dict[campaign.campaign_id] = campaign
                            campaign_list.append(campaign)
                        if len(campaign_list) > 5000:
                            Campaigns.objects.bulk_create(campaign_list)
                            self.stdout.write(
                                self.style.SUCCESS(
                                    "Successfully inserted 5000 rows into Campaigns table."
                                )
                            )
                            campaign_list = []
                    if campaign_list:
                        Campaigns.objects.bulk_create(campaign_list)
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully inserted 5000 rows into Campaigns table."
                )
            )
