from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.inspectors.base import call_view_method
from drf_yasg.utils import no_body, force_real_str, is_list_view
from rest_framework import exceptions


class BimebazarAutoSchema(SwaggerAutoSchema):
    def get_default_response_serializer(self):
        """Return the default response serializer for this endpoint. This is derived from either the ``request_body``
        override or the request serializer (:meth:`.get_view_serializer`).

        :return: response serializer, :class:`.Schema`, :class:`.SchemaRef`, ``None``
        """
        body_override = self._get_request_body_override()
        if body_override and body_override is not no_body:
            return body_override

        return call_view_method(self.view, "get_read_serializer")

    def get_generic_error_schema(self):
        return openapi.Schema(
            "Generic API Error",
            type=openapi.TYPE_OBJECT,
            properties={
                "errors": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING, description="Error details"
                        ),
                    },
                ),
                "message": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Message"
                ),
                "message_code": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Message Code"
                ),
                "status": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Status"
                ),
            },
            required=["errors", "status"],
        )

    def get_validation_error_schema(self):
        return openapi.Schema(
            "Validation Error",
            type=openapi.TYPE_OBJECT,
            properties={
                "errors": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="Error messages for each field that triggered a validation error",
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING, description="Error details"
                        ),
                    },
                    additional_properties=openapi.Schema(
                        description="A list of error messages for the field",
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                ),
                # api_settings.NON_FIELD_ERRORS_KEY: openapi.Schema(
                #     description="List of validation errors not related to any field",
                #     type=openapi.TYPE_ARRAY,
                #     items=openapi.Schema(type=openapi.TYPE_STRING),
                # ),
                "message": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Message"
                ),
                "message_code": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Message Code"
                ),
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="Error Data",
                ),
                "status": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Status"
                ),
            },
        )

    def get_response_serializers(self):
        responses = super().get_response_serializers()
        definitions = self.components.with_scope(
            openapi.SCHEMA_DEFINITIONS
        )  # type: openapi.ReferenceResolver

        definitions.setdefault("GenericError", self.get_generic_error_schema)
        definitions.setdefault("ValidationError", self.get_validation_error_schema)
        definitions.setdefault("APIException", self.get_generic_error_schema)

        if self.get_request_serializer() or self.get_query_serializer():
            responses.setdefault(
                exceptions.ValidationError.status_code,
                openapi.Response(
                    description=force_real_str(
                        exceptions.ValidationError.default_detail
                    ),
                    schema=openapi.SchemaRef(definitions, "ValidationError"),
                ),
            )

        security = self.get_security()
        if security is None or len(security) > 0:
            responses.setdefault(
                exceptions.AuthenticationFailed.status_code,
                openapi.Response(
                    description="Authentication credentials were invalid, absent or insufficient.",
                    schema=openapi.SchemaRef(definitions, "GenericError"),
                ),
            )
        if not is_list_view(self.path, self.method, self.view):
            responses.setdefault(
                exceptions.PermissionDenied.status_code,
                openapi.Response(
                    description="Permission denied.",
                    schema=openapi.SchemaRef(definitions, "APIException"),
                ),
            )
            responses.setdefault(
                exceptions.NotFound.status_code,
                openapi.Response(
                    description="Object does not exist or caller has insufficient permissions to access it.",
                    schema=openapi.SchemaRef(definitions, "APIException"),
                ),
            )

        return responses
