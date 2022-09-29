from regression_model.config.core import config
from regression_model.processing.features import CombineTowns, ExtractNumericalValue


def test_extract_numerical_value(sample_input_data):
    # Given
    extractor = ExtractNumericalValue(variable=config.model_config.remaining_lease)

    assert sample_input_data["remaining_lease"].iat[4] == "61 years 01 month"

    # When
    subject = extractor.fit_transform(sample_input_data)

    # Then
    assert subject["remaining_lease"].iat[4] == 61.083


def test_combine_towns(sample_input_data):
    # Given
    combiner = CombineTowns(
        variable=config.model_config.town, mappings=config.model_config.town_mappings
    )

    assert sample_input_data["town"].iat[13623] == "YISHUN"

    # When
    subject = combiner.fit_transform(sample_input_data)

    # Then
    assert subject["town"].iat[13623] == "NORTH REGION"
