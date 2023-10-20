from AbstractEvent import AbstractEvent
import json
from datetime import datetime

class StockIncreased(AbstractEvent):
    id : int
    
    def __init__(self):
        super().__init__()
        self.id = None

