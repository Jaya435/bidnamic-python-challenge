from django.db import models


class StatusChoices(models.Model):
    ENABLED = 'EN'
    REMOVED = 'RE'
    STATUS_CHOICES = [
        (ENABLED, 'ENABLED'),
        (REMOVED, 'REMOVED')
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=ENABLED
    )

    class Meta:
        abstract = True


class SearchTerms(models.Model):
    date = models.DateField()
    ad_group_id = models.BigIntegerField()
    campaign_id = models.ForeignKey('Campaigns', on_delete=models.CASCADE)
    clicks = models.IntegerField(default=0)
    cost = models.FloatField()
    conversion_value = models.IntegerField(default=0)
    conversions = models.IntegerField(default=0)
    search_term = models.CharField(max_length=255)


class AdGroups(StatusChoices):
    ad_group_id = models.BigIntegerField()
    campaign_id = models.ForeignKey('Campaigns', on_delete=models.CASCADE)
    alias = models.CharField(max_length=255)


class Campaigns(StatusChoices):
    campaign_id = models.IntegerField()
    structure_value = models.CharField(max_length=15)


