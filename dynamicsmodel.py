import casadi as ca
import numpy as np

class CartesianManipulator:
    """3-DOF Cartesian manipulator dynamics."""
    
    def __init__(self, m_x: float = 3.5, m_y: float = 4.5, m_z: float = 5.5, g: float = 9.81):
        self.m_x = m_x
        self.m_y = m_y
        self.m_z = m_z
        self.g = g
        self.model()

    def model(self):
        q = ca.MX.sym('q', 3)
        q_dot = ca.MX.sym('q_dot', 3)
        x = ca.vertcat(q, q_dot)
        tau = ca.MX.sym('tau', 3)
        D = ca.diag(ca.vertcat(self.m_x, self.m_y + self.m_x, self.m_z + self.m_x + self.m_y))
        G = ca.vertcat(0, 0, self.m_z * self.g)

        q_ddot = ca.solve(D, tau - G)
        
        ode = ca.vertcat(q_dot, q_ddot)

        self.x = x
        self.tau = tau
        self.ode = ode
