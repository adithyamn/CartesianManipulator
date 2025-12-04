import numpy as np
from dynamicsmodel import CartesianManipulator
from simulator import Simulator
from plothelper import PlotHelper


class RunModel:
    def __init__(self):
        self.model = CartesianManipulator(m_x=3.5, m_y=4.5, m_z=5.5, g=9.81)
        self.simulate = Simulator(self.model, dt=0.01)
        self.plothelper = PlotHelper()

    def run(self):
        x0 = np.zeros(6)  # [q; qdot]
        tau = np.array([1.0, 0.5, 60.0])  # constant forces
        result = self.simulate.run(steps=100, x0=x0, tau=tau)

        print("ODE expression f(x,u):", self.model.ode)
        print("Final state:", result.x_final)
        print("q:", result.x_final[:3], "q_dot:", result.x_final[3:])

        self.plothelper.plot(result)


def main():
    file = RunModel()
    file.run()


if __name__ == "__main__":
    main()