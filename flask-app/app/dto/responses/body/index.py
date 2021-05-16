from dataclasses import dataclass
from dataclasses import asdict, replace
from dataclasses import field
from uuid import uuid4
from typing import List

@dataclass
class SyntheticIndexReponse:
    values: List[float] = field(default_factory=list)