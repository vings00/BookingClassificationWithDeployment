from joblib import load
from django.db import models

class MLModel(models.Model):
    name = models.CharField(max_length=100)
    model_path = models.CharField(max_length=255)

    def get_model(self):
        return load(self.model_path)