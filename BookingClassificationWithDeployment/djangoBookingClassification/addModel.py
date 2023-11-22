from MlAPI.models import MLModel

model_instance = MLModel.objects.create(
    name='clf',
    model_path='./savedModels/clf.joblib'
)

model_instance.save()