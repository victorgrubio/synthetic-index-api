from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import List

@dataclass
class DataItem:
    id_security: int
    price: float
    date: datetime = datetime.now()

@dataclass
class SyntheticIndexData:
    values: List[DataItem] = field(default_factory=list)


