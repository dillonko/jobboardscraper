from django.db import models

from organizations.models import Organization


class Job(models.Model):
    title = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, blank=True, null=True)
    url = models.URLField('URL')
    pub_date = models.DateTimeField()
    scrape_date = models.DateTimeField()

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return self.url
