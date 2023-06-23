from dataclasses import dataclass
import numpy as np


@dataclass(init=False)
class System:
    time: float
    busy: bool
    num_in_q: int
    time_next_event: np.ndarray
    time_last_event: float
    time_arrival: np.ndarray
    next_event_type: int
    num_customers_delayed: int
    num_customers_rejected: int
    total_of_delays: int
    time_num_in_q: Dict[int, float]
    time_busy: float


@dataclass(frozen=True)
class Parameters:
    mean_interarrival: float
    mean_service: float
    num_delays_required: int
    q_limit: int