from getresponse_api_wrapper import helper


def test_intersect_fields(fields, data_fields):
    assert helper.data_has_invalid_fields(fields, data_fields)