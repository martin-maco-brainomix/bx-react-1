from django.db import models
import json


class Scan(models.Model):
    filename = models.CharField(max_length=255)
    patients = models.TextField(default="[]")
    modalities = models.TextField(default="[]")
    warnings = models.TextField(default="[]")
    notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.filename

    def get_patients(self):
        return json.loads(self.patients)

    def set_patients(self, value):
        self.patients = json.dumps(value)

    def get_modalities(self):
        return json.loads(self.modalities)

    def set_modalities(self, value):
        self.modalities = json.dumps(value)

    def get_warnings(self):
        return json.loads(self.warnings)

    def set_warnings(self, value):
        self.warnings = json.dumps(value)

