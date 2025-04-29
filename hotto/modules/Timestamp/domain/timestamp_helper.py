from datetime import datetime, timezone
from typing import Union

class TimestampHelper:
    @staticmethod
    def iso8601_to_unix(value: Union[str, int]) -> int:
        if isinstance(value, int):
            return value
        if isinstance(value, str):
            try:
                dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
                return int(dt.timestamp())
            except Exception:
                pass
        raise ValueError(f"Cannot convert {value} to Unix timestamp")

    @staticmethod
    def unix_to_iso8601(timestamp: int) -> str:
        dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
        return dt.isoformat().replace('+00:00', 'Z')
