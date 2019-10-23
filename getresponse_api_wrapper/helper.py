from typing import List


def data_has_invalid_fields(
    schema_fields: List[str] = None, data_fields: List[str] = None
) -> set:
    return set(data_fields).difference(schema_fields)
