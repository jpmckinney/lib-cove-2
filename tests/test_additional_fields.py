import json
import pytest

from libcove2.common import get_additional_fields_info
from libcove2.common import schema_dict_fields_generator

@pytest.fixture
def bods_data_0_3():
    """Data for BODS 0.3"""
    with open("tests/fixtures/bods-data-0-3-0.json", "r") as read_file:
        return json.load(read_file)

@pytest.fixture
def schema_fields_0_3():
    """Schema fields for BODS 0.3"""
    with open("tests/fixtures/schema-0-3-0.json", "r") as read_file:
        return set(schema_dict_fields_generator(json.load(read_file)))

@pytest.fixture
def bods_data_0_4():
    """Data for BODS 0.4"""
    with open("tests/fixtures/bods-data-0-4-0.json", "r") as read_file:
        return json.load(read_file)

@pytest.fixture
def schema_fields_0_4():
    """Schema fields for BODS 0.4"""
    with open("tests/fixtures/schema-0-4-0.json", "r") as read_file:
        return set(schema_dict_fields_generator(json.load(read_file)))

def test_additional_fields_0_3(bods_data_0_3, schema_fields_0_3):

    additional_fields = get_additional_fields_info(bods_data_0_3, schema_fields_0_3)

    assert len(additional_fields) == 0

def test_additional_fields_0_4(bods_data_0_4, schema_fields_0_4):
    print(schema_fields_0_4)

    additional_fields = get_additional_fields_info(bods_data_0_4, schema_fields_0_4)

    print(additional_fields)

    assert len(additional_fields) == 0