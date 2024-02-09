from flask import Blueprint, request, Response, abort, jsonify
from marshmallow.exceptions import ValidationError
from piScan.models import Device, ScanFormat
from piScan.schemas.device import DeviceSchema
from piScan import db


blueprint = Blueprint("devices", __name__)


@blueprint.route("/", methods=["GET"])
def get_devices():
    schema = DeviceSchema(many=True)
    printers = schema.dump(db.session.query(Device).all())

    return printers


@blueprint.route("/", methods=["POST"])
def add_device():
    try:
        schema = DeviceSchema().load(request.get_json())
        device = Device(**schema)

        db.session.add(device)
        db.session.commit()

        return Response(status=201)

    except ValidationError as e:
        return jsonify(error=str(e)), 400


@blueprint.route("/<uuid>", methods=["GET"])
def get_device(uuid):
    device = db.session.query(Device).filter_by(uuid=uuid).first()

    if not device:
        abort(404)

    schema = DeviceSchema()
    dumped_device = schema.dump(device)

    return dumped_device


@blueprint.route("/<uuid>", methods=["DELETE"])
def remove_device(uuid):
    device = db.session.query(Device).filter_by(uuid=uuid).first()

    if not device:
        abort(404)

    db.session.delete(device)
    db.session.commit()

    return Response(status=200)


@blueprint.route("/<device_uuid>/format/<format_uuid>", methods=["POST"])
def add_scan_format_to_device(device_uuid, format_uuid):
    device = db.session.query(Device).filter_by(uuid=device_uuid).first()
    scan_format = db.session.query(ScanFormat).filter_by(uuid=format_uuid).first()

    if not device or not scan_format:
        abort(404)

    if scan_format not in device.scan_formats:
        device.scan_formats.append(scan_format)
        db.session.commit()

        return Response(status=200)

    abort(400)


@blueprint.route("/<device_uuid>/format/<format_uuid>", methods=["DELETE"])
def remove_scan_format_for_device(device_uuid, format_uuid):
    device = db.session.query(Device).filter_by(uuid=device_uuid).first()
    scan_format = db.session.query(ScanFormat).filter_by(uuid=format_uuid).first()

    if not device or not scan_format:
        abort(404)

    if scan_format in device.scan_formats:
        device.scan_formats.remove(scan_format)
        db.session.commit()

        return Response(status=200)

    abort(400)


@blueprint.route("/<uuid>/resolutions", methods=["POST"])
def add_scan_resolution_for_device(uuid):
    device = db.session.query(Device).filter_by(uuid=uuid).first()

    if not device:
        abort(404)

    data = request.get_json()
    is_valid = device.validate_resolutions(data)

    if not is_valid:
        abort(400)

    device.resolutions = data
    db.session.commit()

    return Response(status=200)
