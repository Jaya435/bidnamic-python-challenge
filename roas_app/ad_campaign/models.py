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
    ad_group_id = models.ForeignKey(
        "AdGroup", on_delete=models.CASCADE, related_name="search_terms"
    )
    campaign_id = models.ForeignKey(
        "Campaign", on_delete=models.CASCADE, related_name="search_terms"
    )
    clicks = models.IntegerField(default=0)
    cost = models.FloatField()
    conversion_value = models.FloatField(default=0)
    conversions = models.IntegerField(default=0)
    search_term = models.CharField(max_length=255)
    roas = models.FloatField(default=0, db_index=True)

    class Meta:
        unique_together = ["date", "ad_group_id", "campaign_id", "search_term"]
        ordering = ["-date"]

    @property
    def get_roas(self):
        """Return on Ad Spend for the search term, conversion value / cost"""
        return self.conversion_value / self.cost

    def save(self, *args, **kwarg):
        self.roas = self.get_roas
        super(SearchTerm, self).save(*args, **kwarg)


class AdGroup(StatusChoice):
    ad_group_id = models.BigIntegerField(primary_key=True)
    campaign_id = models.ForeignKey("Campaign", on_delete=models.CASCADE)
    alias = models.CharField(max_length=255)

    class Meta:
        ordering = ["alias"]


class Campaign(StatusChoice):
    campaign_id = models.BigIntegerField(primary_key=True)
    structure_value = models.CharField(max_length=50)

    class Meta:
        ordering = ["structure_value"]
