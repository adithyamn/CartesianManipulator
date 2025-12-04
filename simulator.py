from dataclasses import dataclass
import numpy as np
import casadi as ca
from dynamicsmodel import CartesianManipulator

@dataclass
class SimulationResult:
    t: np.ndarray
    q: np.ndarray
    qdot: np.ndarray
    x_final: np.ndarray


class Simulator:
    def __init__(self, model: CartesianManipulator, dt: float = 0.01):
        self.model = model
        self.dt = dt
        self.integrator = ca.integrator(
            'F', 'cvodes',
            {'x': self.model.x, 'p': self.model.tau, 'ode': self.model.ode},
            0.0,
            self.dt
        )

    def run(self, steps: int, x0: np.ndarray, tau: np.ndarray) -> SimulationResult:
        x = np.array(x0, dtype=float).flatten()
        q_log = []
        qdot_log = []
        t_log = []

        for k in range(steps):
            result = self.integrator(x0=x, p=tau)
            x = np.array(result['xf']).flatten()
            q_log.append(x[:3])
            qdot_log.append(x[3:])
            t_log.append((k + 1) * self.dt)

        q_log = np.array(q_log)
        qdot_log = np.array(qdot_log)
        t = np.array(t_log)

        return SimulationResult(t=t, q=q_log, qdot=qdot_log, x_final=x)