import matplotlib.pyplot as plt
from simulator import SimulationResult


class PlotHelper:
    def plot(self, result: SimulationResult):
        fig, axes = plt.subplots(2, 1, figsize=(10, 6))
        axes[0].plot(result.t, result.q[:, 0], 'r', label='x')
        axes[0].plot(result.t, result.q[:, 1], 'g', label='y')
        axes[0].plot(result.t, result.q[:, 2], 'b', label='z')
        axes[0].set_title('Position vs Time'); axes[0].grid(True); axes[0].legend()

        axes[1].plot(result.t, result.qdot[:, 0], 'r', label='x_dot')
        axes[1].plot(result.t, result.qdot[:, 1], 'g', label='y_dot')
        axes[1].plot(result.t, result.qdot[:, 2], 'b', label='z_dot')
        axes[1].set_title('Velocity vs Time'); axes[1].grid(True); axes[1].legend()

        plt.tight_layout()
        plt.show()
