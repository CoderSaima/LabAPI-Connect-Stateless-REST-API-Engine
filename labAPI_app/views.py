from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SecAuthSerializer
from .models import labapi_model
from django.contrib.auth.hashers import check_password

@api_view(['POST'])
def api_register_view(request):
    """
    Stateless REST API Endpoint: Ingests raw JSON payloads across networks,
    validates the dictionary parameters using our Serializer engine,
    and returns uniform data envelopes mapping precise HTTP status codes.
    """
    serializer = SecAuthSerializer(data= request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            {
            "status": "success",
            "message": "API user profile generated successfully inside the security core.",
            "user_data": serializer.data}, status=status.HTTP_201_CREATED
        )
    return Response(
        {
            "status": "error",
            "message": "Validation constraints breach. Account creation rejected.",
            "errors": serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
def api_login_view(request):
    user_email = request.data.get('email', '').strip()
    user_password = request.data.get('password', '')

    if not user_email or not user_password:
        return Response(
            {
                "status": "error",
                "message": "Both fields are required",
            }, 
            status = status.HTTP_400_BAD_REQUEST
        )
    try:
        user_record = labapi_model.objects.get(email = user_email)

        if check_password(user_password, user_record.password):
            return Response({
                "status":"success",
                "message":" Access granted successfully.",
                "user_profile":{
                    "name":user_record.name,
                    "email":user_record.email
                }
            },status=status.HTTP_200_OK
        )
        else:
            return Response({
                "status": "error",
                "message":"Access Denied, enter correct data"
            },status=status.HTTP_400_BAD_REQUEST)
    except labapi_model.DoesNotExist:
        return Response({
            "status":"error",
            "message":"Invalid authentication access!"
        },status=status.HTTP_400_BAD_REQUEST)