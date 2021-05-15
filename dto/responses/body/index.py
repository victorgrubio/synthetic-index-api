from dataclasses import dataclass
from dataclasses import asdict, replace
from dataclasses import field
from uuid import uuid4
from typing import List

@dataclass
class SynteticIndexReponse:
    name: str = "Legend of Zelda: BOTW"
    game_id: int = 3242223
    genre: str = "RPG"