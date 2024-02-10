from api_docs.spec import spec

spec.tag({"name": "Devices"})

get_devices = {
    "tags": ["Devices"],
    "summary": "Get Devices",
    "responses": {
        "200": {
            "content": {
                "application/json": {
                    "schema": {
                        "type": "array",
                        "items": "Device"
                    }
                }
            }
        }
    }
}

create_device = {
    "tags": ["Devices"],
    "summary": "Create device",
    "requestBody": {
        "content": {
            "application/json": {
                "schema": "Device"
            }
        }
    },
    "responses": {
        "201": {
            "description": "device successfully created"
        },
        "400": {
            "description": "error while creating device"
        }
    }
}

spec.path(
    path="/api/devices",
    operations={
        "get": get_devices,
        "post": create_device,
    },
)

get_device = {
    "tags": ["Devices"],
    "summary": "Get device by uuid",
    "parameters": [
        {
            "in": "path",
            "name": "uuid",
            "schema": {
                "type": "string"
            }
        }
    ],
    "responses": {
        "200": {
            "content": {
                "application/json": {
                    "schema": "Device"
                }
            }
        },
        "404": {
            "description": "NOT FOUND"
        }
    }
}

remove_device = {
    "tags": ["Devices"],
    "summary": "Delete device by uuid",
    "parameters": [
        {
            "in": "path",
            "name": "uuid",
            "schema": {
                "type": "string"
            }
        }
    ],
    "responses": {
        "200": {
            "description": "Device removed successfully"
        },
        "404": {
            "description": "NOT FOUND"
        }
    }
}

spec.path(
    path="/api/devices/{uuid}",
    operations={
        "get": get_device,
        "delete": remove_device,
    },
)

add_format_to_device = {
    "tags": ["Devices"],
    "summary": "Add scan format to device",
    "parameters": [
        {
            "in": "path",
            "name": "device_uuid",
            "schema": {
                "type": "string"
            }
        },
        {
            "in": "path",
            "name": "format_uuid",
            "schema": {
                "type": "string"
            }
        }
    ],
    "responses": {
        "200": {
            "description": "scan format has been added successfully"
        },
        "400": {
            "description": "error while adding scan format to device"
        },
        "404": {
            "description": "device or scan format not found"
        },
    }
}

remove_format_for_device = {
    "tags": ["Devices"],
    "summary": "Remove scan format for device",
    "parameters": [
        {
            "in": "path",
            "name": "device_uuid",
            "schema": {
                "type": "string"
            }
        },
        {
            "in": "path",
            "name": "format_uuid",
            "schema": {
                "type": "string"
            }
        }
    ],
    "responses": {
        "200": {
            "description": "scan format has been removed successfully"
        },
        "400": {
            "description": "error while removing scan format for device"
        },
        "404": {
            "description": "device or scan format not found"
        },
    }
}

spec.path(
    path="/api/devices/{device_uuid}/format/{format_uuid}",
    operations={
        "post": add_format_to_device,
        "delete": remove_format_for_device
    },
)

add_scan_resolution_for_device = {
    "tags": ["Devices"],
    "summary": "Set device scan resolutions",
    "parameters": [
        {
            "in": "path",
            "name": "uuid",
            "schema": {
                "type": "number"
            }
        },
    ],
    "requestBody": {
        "content": {
            "application/json": {
                "schema": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            }
        }
    },
    "responses": {
        "200": {
            "description": "scan resolutions successfully updated"
        },
        "404": {
            "description": "device not not found"
        },
        "400": {
            "description": ""
        }
    }
}

spec.path(
    path="/api/devices/{uuid}/resolutions",
    operations={
        "post": add_scan_resolution_for_device
    },
)
