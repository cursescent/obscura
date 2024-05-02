from django.core import serializers

def get_source_json(data):
    jsonob_raw = [{"code": 0, "name": "Obscura", "url": "none"}]
    for i in data.split("\n"):
        jsonob_raw.append({"code": 1, "name": "Unknown source", "url": i})
    return jsonob_raw
