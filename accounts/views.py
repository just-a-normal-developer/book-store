from django.http import JsonResponse
from django.views import generic
from django.urls import reverse_lazy

# api's
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import CustomUserSerializer
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class UserProfileTemplateView(generic.TemplateView):
    template_name = "accounts/user_profile.html"


# response_schema_dict = {
#     "200": openapi.Response(
#         description="custom 200 description",
#         examples={
#             "application/json": {
#                 "200_key1": "200_value_1",
#                 "200_key2": "200_value_2",
#             }
#         }
#     ),
#     "205": openapi.Response(
#         description="custom 205 description",
#         examples={
#             "application/json": {
#                 "205_key1": "205_value_1",
#                 "205_key2": "205_value_2",
#             }
#         }
#     ),
# }

# def swagger_auto_schema_class(request_body=None, responses=None, **kwargs):
#     def decorator(cls):
#         for method in ['get', 'post', 'put', 'patch', 'delete']:
#             if hasattr(cls, method):
#                 method_func = getattr(cls, method)
#                 decorated_method = swagger_auto_schema(
#                     request_body=request_body, responses=responses, **kwargs
#                 )(method_func)
#                 setattr(cls, method, decorated_method)
#         return cls
#     return decorator
#
#
# @swagger_auto_schema_class(
#     operation_summary='User Profile API',
#     operation_description='API to retrieve and update user profile',
#     request_body=CustomUserSerializer,
#     responses={
#         200: openapi.Response(
#             description="Profile retrieved successfully",
#             schema=CustomUserSerializer
#         ),
#         400: openapi.Response(
#             description="Bad Request",
#             schema=openapi.Schema(
#                 type=openapi.TYPE_OBJECT,
#                 properties={
#                     'error': openapi.Schema(type=openapi.TYPE_STRING)
#                 }
#             )
#         )
#     }
# )


class UserProfileView(APIView):
    """
    showing the user information by GET method and if wanted update the information as they like with the patch method.

    1. send a request with the authorized user to see the information
    2. Send the request with a valid email or other information shown below:
        ```json
        {
          "email": <email parameter with the string value>,
          "first_name": <firstname parameter with string value>,
          "last_name": <lastname parameter with string value>,
          "age": <age parameter with integer value>
        }
        ```
    3. You will get the response with the specified schema.
    """

    permission_classes = [IsAuthenticated]

    # @swagger_auto_schema(responses=response_schema_dict)
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "param1",
                openapi.IN_QUERY,
                description="Parameter 1",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "param2",
                openapi.IN_QUERY,
                description="Parameter 2",
                type=openapi.TYPE_INTEGER,
            ),
        ],
        responses={
            200: openapi.Response(
                description="Successful response",
                examples={
                    "application/json": {
                        "id": 1,
                        "username": "johndoe",
                        "email": "johndoe@example.com",
                    }
                },
            ),
            400: openapi.Response(
                description="Bad request",
                examples={"application/json": {"error": "Invalid input"}},
            ),
        },
    )
    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)
        return JsonResponse(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Email address"
                ),
                "first_name": openapi.Schema(
                    type=openapi.TYPE_STRING, description="First name"
                ),
                "last_name": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Last name"
                ),
            },
            required=["email"],
        ),
        responses={
            200: openapi.Response(
                description="Profile updated successfully",
                examples={
                    "application/json": {
                        "id": 1,
                        "username": "johndoe",
                        "email": "newemail@example.com",
                        "first_name": "John",
                        "last_name": "Doe",
                    }
                },
            ),
            400: openapi.Response(
                description="Bad request",
                examples={"application/json": {"error": "Invalid input"}},
            ),
        },
    )
    def patch(self, request):
        user = request.user
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
