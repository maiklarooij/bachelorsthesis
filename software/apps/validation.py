from jschon import JSON, JSONSchema, create_catalog
import jsonschema
import json

def validate_metadata(metadata):
    """
    Validates a metadata dict object against a predefined JSON Schema
    """
    f = open('validation/validationSchema.json')
    validation_schema = json.load(f)

    #create_catalog('2020-12')
    #schema = JSONSchema(validation_schema)

    v = jsonschema.Draft7Validator(validation_schema)
    errors = sorted(v.iter_errors(metadata), key=lambda e: e.path)

    #result = schema.evaluate(JSON(metadata))

    if not errors:
        return True

    return errors
