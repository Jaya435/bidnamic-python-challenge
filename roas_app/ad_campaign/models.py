from django.db import models


class StatusChoice(models.Model):
    ENABLED = "ENABLED"
    REMOVED = "REMOVED"
    STATUS_CHOICES = [(ENABLED, "ENABLED"), (REMOVED, "REMOVED")]
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=ENABLED)

    class Meta:
        abstract = True


class SearchTerm(models.Model):
    date = models.DateField()
    ad_group_id = models.BigIntegerField()
    campaign_id = models.ForeignKey("Campaign", on_delete=models.CASCADE)
    clicks = models.IntegerField(default=0)
    cost = models.FloatField()
    conversion_value = models.FloatField(default=0)
    conversions = models.IntegerField(default=0)
    search_term = models.CharField(max_length=255)

    class Meta:
        unique_together = ['date', 'ad_group_id', 'campaign_id', 'search_term']


class AdGroup(StatusChoice):
    ad_group_id = models.BigIntegerField()
    campaign_id = models.ForeignKey("Campaign", on_delete=models.CASCADE)
    alias = models.CharField(max_length=255)

    class Meta:
        unique_together = ['ad_group_id', 'campaign_id', 'alias']


class Campaign(StatusChoice):
    campaign_id = models.BigIntegerField(primary_key=True)
    structure_value = models.CharField(max_length=50)
