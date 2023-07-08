import pytest
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


@pytest.mark.parametrize(
    "path,expected_status,expected_response",
    [
        ("/api_route", 200, {"message": "Hello World"}),
        ("/non_decorated_route", 200, {"message": "Hello World"}),
        ("/nonexistent", 404, {"detail": "Not Found"}),
    ],
)
def test_get_path(path, expected_status, expected_response):
    response = client.get(path)
    assert response.status_code == expected_status
    assert response.json() == expected_response


def test_swagger_ui():
    response = client.get("/docs")
    assert response.status_code == 200, response.text
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "swagger-ui-dist" in response.text
    assert (
        "oauth2RedirectUrl: window.location.origin + '/docs/oauth2-redirect'"
        in response.text
    )


def test_swagger_ui_oauth2_redirect():
    response = client.get("/docs/oauth2-redirect")
    assert response.status_code == 200, response.text
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "window.opener.swaggerUIRedirectOauth2" in response.text


def test_redoc():
    response = client.get("/redoc")
    assert response.status_code == 200, response.text
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "redoc@next" in response.text


def test_enum_status_code_response():
    response = client.get("/enum-status-code")
    assert response.status_code == 201, response.text
    assert response.json() == "foo bar"


def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/api_route": {
                "get": {
                    "summary": "Non Operation",
                    "operationId": "non_operation_api_route_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            },
            "/non_decorated_route": {
                "get": {
                    "summary": "Non Decorated Route",
                    "operationId": "non_decorated_route_non_decorated_route_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            },
            "/text": {
                "get": {
                    "summary": "Get Text",
                    "operationId": "get_text_text_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            },
            "/path/{item_id}": {
                "get": {
                    "summary": "Get Id",
                    "operationId": "get_id_path__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {"title": "Item Id"},
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/str/{item_id}": {
                "get": {
                    "summary": "Get Str Id",
                    "operationId": "get_str_id_path_str__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "string", "title": "Item Id"},
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/int/{item_id}": {
                "get": {
                    "summary": "Get Int Id",
                    "operationId": "get_int_id_path_int__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "integer", "title": "Item Id"},
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/float/{item_id}": {
                "get": {
                    "summary": "Get Float Id",
                    "operationId": "get_float_id_path_float__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "number", "title": "Item Id"},
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/bool/{item_id}": {
                "get": {
                    "summary": "Get Bool Id",
                    "operationId": "get_bool_id_path_bool__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "boolean", "title": "Item Id"},
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param/{item_id}": {
                "get": {
                    "summary": "Get Path Param Id",
                    "operationId": "get_path_param_id_path_param__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-minlength/{item_id}": {
                "get": {
                    "summary": "Get Path Param Min Length",
                    "operationId": "get_path_param_min_length_path_param_minlength__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "string",
                                "minLength": 3,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-maxlength/{item_id}": {
                "get": {
                    "summary": "Get Path Param Max Length",
                    "operationId": "get_path_param_max_length_path_param_maxlength__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "string",
                                "maxLength": 3,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-min_maxlength/{item_id}": {
                "get": {
                    "summary": "Get Path Param Min Max Length",
                    "operationId": "get_path_param_min_max_length_path_param_min_maxlength__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "string",
                                "minLength": 2,
                                "maxLength": 3,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-gt/{item_id}": {
                "get": {
                    "summary": "Get Path Param Gt",
                    "operationId": "get_path_param_gt_path_param_gt__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "number",
                                "exclusiveMinimum": 3,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-gt0/{item_id}": {
                "get": {
                    "summary": "Get Path Param Gt0",
                    "operationId": "get_path_param_gt0_path_param_gt0__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "number",
                                "exclusiveMinimum": 0,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-ge/{item_id}": {
                "get": {
                    "summary": "Get Path Param Ge",
                    "operationId": "get_path_param_ge_path_param_ge__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "number",
                                "minimum": 3,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-lt/{item_id}": {
                "get": {
                    "summary": "Get Path Param Lt",
                    "operationId": "get_path_param_lt_path_param_lt__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "number",
                                "exclusiveMaximum": 3,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-lt0/{item_id}": {
                "get": {
                    "summary": "Get Path Param Lt0",
                    "operationId": "get_path_param_lt0_path_param_lt0__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "number",
                                "exclusiveMaximum": 0,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-le/{item_id}": {
                "get": {
                    "summary": "Get Path Param Le",
                    "operationId": "get_path_param_le_path_param_le__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "number",
                                "maximum": 3,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-lt-gt/{item_id}": {
                "get": {
                    "summary": "Get Path Param Lt Gt",
                    "operationId": "get_path_param_lt_gt_path_param_lt_gt__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "number",
                                "exclusiveMaximum": 3,
                                "exclusiveMinimum": 1,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-le-ge/{item_id}": {
                "get": {
                    "summary": "Get Path Param Le Ge",
                    "operationId": "get_path_param_le_ge_path_param_le_ge__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "number",
                                "maximum": 3,
                                "minimum": 1,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-lt-int/{item_id}": {
                "get": {
                    "summary": "Get Path Param Lt Int",
                    "operationId": "get_path_param_lt_int_path_param_lt_int__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "integer",
                                "exclusiveMaximum": 3,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-gt-int/{item_id}": {
                "get": {
                    "summary": "Get Path Param Gt Int",
                    "operationId": "get_path_param_gt_int_path_param_gt_int__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "integer",
                                "exclusiveMinimum": 3,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-le-int/{item_id}": {
                "get": {
                    "summary": "Get Path Param Le Int",
                    "operationId": "get_path_param_le_int_path_param_le_int__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "integer",
                                "maximum": 3,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-ge-int/{item_id}": {
                "get": {
                    "summary": "Get Path Param Ge Int",
                    "operationId": "get_path_param_ge_int_path_param_ge_int__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "integer",
                                "minimum": 3,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-lt-gt-int/{item_id}": {
                "get": {
                    "summary": "Get Path Param Lt Gt Int",
                    "operationId": "get_path_param_lt_gt_int_path_param_lt_gt_int__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "integer",
                                "exclusiveMaximum": 3,
                                "exclusiveMinimum": 1,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/path/param-le-ge-int/{item_id}": {
                "get": {
                    "summary": "Get Path Param Le Ge Int",
                    "operationId": "get_path_param_le_ge_int_path_param_le_ge_int__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "integer",
                                "maximum": 3,
                                "minimum": 1,
                                "title": "Item Id",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/query": {
                "get": {
                    "summary": "Get Query",
                    "operationId": "get_query_query_get",
                    "parameters": [
                        {
                            "name": "query",
                            "in": "query",
                            "required": True,
                            "schema": {"title": "Query"},
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/query/optional": {
                "get": {
                    "summary": "Get Query Optional",
                    "operationId": "get_query_optional_query_optional_get",
                    "parameters": [
                        {
                            "name": "query",
                            "in": "query",
                            "required": False,
                            "schema": {"title": "Query"},
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/query/int": {
                "get": {
                    "summary": "Get Query Type",
                    "operationId": "get_query_type_query_int_get",
                    "parameters": [
                        {
                            "name": "query",
                            "in": "query",
                            "required": True,
                            "schema": {"type": "integer", "title": "Query"},
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/query/int/optional": {
                "get": {
                    "summary": "Get Query Type Optional",
                    "operationId": "get_query_type_optional_query_int_optional_get",
                    "parameters": [
                        {
                            "name": "query",
                            "in": "query",
                            "required": False,
                            "schema": {
                                "anyOf": [{"type": "integer"}, {"type": "null"}],
                                "title": "Query",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/query/int/default": {
                "get": {
                    "summary": "Get Query Type Int Default",
                    "operationId": "get_query_type_int_default_query_int_default_get",
                    "parameters": [
                        {
                            "name": "query",
                            "in": "query",
                            "required": False,
                            "schema": {
                                "type": "integer",
                                "default": 10,
                                "title": "Query",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/query/param": {
                "get": {
                    "summary": "Get Query Param",
                    "operationId": "get_query_param_query_param_get",
                    "parameters": [
                        {
                            "name": "query",
                            "in": "query",
                            "required": False,
                            "schema": {"title": "Query"},
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/query/param-required": {
                "get": {
                    "summary": "Get Query Param Required",
                    "operationId": "get_query_param_required_query_param_required_get",
                    "parameters": [
                        {
                            "name": "query",
                            "in": "query",
                            "required": True,
                            "schema": {"title": "Query"},
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/query/param-required/int": {
                "get": {
                    "summary": "Get Query Param Required Type",
                    "operationId": "get_query_param_required_type_query_param_required_int_get",
                    "parameters": [
                        {
                            "name": "query",
                            "in": "query",
                            "required": True,
                            "schema": {"type": "integer", "title": "Query"},
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/query/sequence-params": {
                "get": {
                    "summary": "Get Sequence Query Params",
                    "operationId": "get_sequence_query_params_query_sequence_params_get",
                    "parameters": [
                        {
                            "name": "query",
                            "in": "query",
                            "required": False,
                            "schema": {
                                "type": "object",
                                "additionalProperties": {
                                    "type": "array",
                                    "items": {"type": "integer"},
                                },
                                "default": {},
                                "title": "Query",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/query/mapping-params": {
                "get": {
                    "summary": "Get Mapping Query Params",
                    "operationId": "get_mapping_query_params_query_mapping_params_get",
                    "parameters": [
                        {
                            "name": "queries",
                            "in": "query",
                            "required": False,
                            "schema": {
                                "type": "object",
                                "additionalProperties": {"type": "string"},
                                "default": {},
                                "title": "Queries",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/query/mapping-sequence-params": {
                "get": {
                    "summary": "Get Sequence Mapping Query Params",
                    "operationId": "get_sequence_mapping_query_params_query_mapping_sequence_params_get",
                    "parameters": [
                        {
                            "name": "queries",
                            "in": "query",
                            "required": False,
                            "schema": {
                                "type": "object",
                                "additionalProperties": {
                                    "type": "array",
                                    "items": {"type": "integer"},
                                },
                                "default": {},
                                "title": "Queries",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/query/mixed-params": {
                "get": {
                    "summary": "Get Mixed Mapping Query Params",
                    "operationId": "get_mixed_mapping_query_params_query_mixed_params_get",
                    "parameters": [
                        {
                            "name": "sequence_mapping_queries",
                            "in": "query",
                            "required": False,
                            "schema": {
                                "type": "object",
                                "additionalProperties": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                },
                                "default": {},
                                "title": "Sequence Mapping Queries",
                            },
                        },
                        {
                            "name": "mapping_query",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "object",
                                "additionalProperties": {"type": "string"},
                                "title": "Mapping Query",
                            },
                        },
                        {
                            "name": "query",
                            "in": "query",
                            "required": True,
                            "schema": {"type": "string", "title": "Query"},
                        },
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/query/mixed-type-params": {
                "get": {
                    "summary": "Get Mixed Mapping Mixed Type Query Params",
                    "operationId": "get_mixed_mapping_mixed_type_query_params_query_mixed_type_params_get",
                    "parameters": [
                        {
                            "name": "sequence_mapping_queries",
                            "in": "query",
                            "required": False,
                            "schema": {
                                "type": "object",
                                "additionalProperties": {
                                    "type": "array",
                                    "items": {"type": "integer"},
                                },
                                "default": {},
                                "title": "Sequence Mapping Queries",
                            },
                        },
                        {
                            "name": "mapping_query_str",
                            "in": "query",
                            "required": False,
                            "schema": {
                                "type": "object",
                                "additionalProperties": {"type": "string"},
                                "default": {},
                                "title": "Mapping Query Str",
                            },
                        },
                        {
                            "name": "mapping_query_int",
                            "in": "query",
                            "required": False,
                            "schema": {
                                "type": "object",
                                "additionalProperties": {"type": "integer"},
                                "default": {},
                                "title": "Mapping Query Int",
                            },
                        },
                        {
                            "name": "query",
                            "in": "query",
                            "required": True,
                            "schema": {"type": "integer", "title": "Query"},
                        },
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/enum-status-code": {
                "get": {
                    "summary": "Get Enum Status Code",
                    "operationId": "get_enum_status_code_enum_status_code_get",
                    "responses": {
                        "201": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            },
            "/query/frozenset": {
                "get": {
                    "summary": "Get Query Type Frozenset",
                    "operationId": "get_query_type_frozenset_query_frozenset_get",
                    "parameters": [
                        {
                            "name": "query",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "array",
                                "uniqueItems": True,
                                "items": {"type": "integer"},
                                "title": "Query",
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            },
        },
        "components": {
            "schemas": {
                "HTTPValidationError": {
                    "properties": {
                        "detail": {
                            "items": {"$ref": "#/components/schemas/ValidationError"},
                            "type": "array",
                            "title": "Detail",
                        }
                    },
                    "type": "object",
                    "title": "HTTPValidationError",
                },
                "ValidationError": {
                    "properties": {
                        "loc": {
                            "items": {
                                "anyOf": [{"type": "string"}, {"type": "integer"}]
                            },
                            "type": "array",
                            "title": "Location",
                        },
                        "msg": {"type": "string", "title": "Message"},
                        "type": {"type": "string", "title": "Error Type"},
                    },
                    "type": "object",
                    "required": ["loc", "msg", "type"],
                    "title": "ValidationError",
                },
            }
        },
    }
