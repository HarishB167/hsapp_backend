from django.db import models

# Create your models here.

class Mindmap(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    revisions = models.PositiveIntegerField()
    image_link = models.TextField()

    def __str__(self):
        return self.title

class Branch(models.Model):
    title = models.CharField(max_length=255)
    mindmap = models.ForeignKey(Mindmap, on_delete=models.CASCADE, related_name='branches')
    sort_number = models.PositiveIntegerField()

    class Meta:
        unique_together = [['mindmap', 'sort_number']]

    def __str__(self):
        return self.title

class BranchLine(models.Model):
    content = models.TextField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='content_line')
    sort_number = models.PositiveIntegerField()

    class Meta:
        unique_together = [['branch', 'sort_number']]

    def __str__(self):
        return self.content[:10]

