from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import MLModel
import pandas as pd

@api_view(['POST'])
def predictor(request):
    if request.method == 'POST':
        input_data = pd.DataFrame([request.data], index=[0])
        name = 'clf'
        model_instance = MLModel.objects.get(name=name)
        model = model_instance.get_model()
        prediction = model.predict(input_data)

        return Response({'prediction': prediction}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)