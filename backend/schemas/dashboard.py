from pydantic import BaseModel,ConfigDict
from  typing import List,Dict


class DashboardStats(BaseModel):
    total_students : int 
    total_rooms:int
    occupied_rooms :int 
    available_rooms : int 
    pending_complaints :int 
    total_complaints :int

# For the Chart.js graphs
class ChartData(BaseModel):
    occupancy_ratio: Dict[str, int] # e.g., {"occupied": 15, "available": 5}
    monthly_complaints: List[Dict[str, object]] # e.g., [{"month": "2026-08", "count": 12}]