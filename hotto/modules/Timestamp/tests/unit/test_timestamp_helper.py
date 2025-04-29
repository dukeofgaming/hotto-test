import pytest
from hotto.modules.timestamp.timestamp_helper import TimestampHelper

class TestTimestampHelper:
    def test_given_iso8601_when_converting_to_unix_then_returns_expected_timestamp(self):
        # Arrange
        iso_str = "2025-04-29T11:24:55Z"
        expected = 1745925895
        
        # Act
        result = TimestampHelper.iso8601_to_unix(iso_str)
        
        # Assert
        assert result == expected

    def test_given_unix_when_converting_to_iso8601_then_returns_expected_string(self):
        # Arrange
        unix_ts = 1745925895
        expected = "2025-04-29T11:24:55Z"
        
        # Act
        result = TimestampHelper.unix_to_iso8601(unix_ts)
        
        # Assert
        assert result == expected

    def test_given_invalid_string_when_converting_to_unix_then_raises_value_error(self):
        # Arrange
        invalid_str = "not-a-date"
        
        # Act & Assert
        with pytest.raises(ValueError):
            TimestampHelper.iso8601_to_unix(invalid_str)

    def test_given_int_when_converting_to_unix_then_returns_same_int(self):
        # Arrange
        ts = 1745925895
        
        # Act
        result = TimestampHelper.iso8601_to_unix(ts)
        
        # Assert
        assert result == ts
