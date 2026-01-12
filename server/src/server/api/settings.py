from common import EnvBaseSettings
from pydantic import Field
from typing import Optional

class ApiSettings(EnvBaseSettings):
    api_debug: bool = Field(True, description="디버그 모드 여부")