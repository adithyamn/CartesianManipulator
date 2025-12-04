import casadi as ca
import numpy as np
import matplotlib.pyplot as plt
from dynamicsmodel import CartesianManipulator


def main():
    model = CartesianManipulator(m_x=3.5, m_y=4.5, m_z=5.5, g=9.81)
    print("ODE expression f(x,u):", model.ode)

    dt = 0.01
    F = ca.integrator(
        'F', 'cvodes',
        {'x': model.x, 'p': model.tau, 'ode': model.ode},
        0.0,
        dt
    )

    # Initial state and constant input
    x = np.zeros(6)              # [q; qdot]
    tau = np.array([1.0, 0.5, 60.0])  # simple constant forces

    # Logs
    q_log = []
    qdot_log = []
    t_log = []

    # Run 100 steps
    for k in range(100):
        result = F(x0=x, p=tau)
        x = np.array(result['xf']).flatten()
        q_log.append(x[:3])
        qdot_log.append(x[3:])
        t_log.append((k+1) * dt)

    print("Final state:", x)
    print("q:", x[:3], "q_dot:", x[3:])

    q_log = np.array(q_log)
    qdot_log = np.array(qdot_log)

    # Plot
    fig, axes = plt.subplots(2, 1, figsize=(10, 6)) 
    axes[0].plot(t_log, q_log[:, 0], 'r', label='x')
    axes[0].plot(t_log, q_log[:, 1], 'g', label='y')
    axes[0].plot(t_log, q_log[:, 2], 'b', label='z')
    axes[0].set_title('Position vs Time'); axes[0].grid(True); axes[0].legend()

    axes[1].plot(t_log, qdot_log[:, 0], 'r', label='x_dot')
    axes[1].plot(t_log, qdot_log[:, 1], 'g', label='y_dot')
    axes[1].plot(t_log, qdot_log[:, 2], 'b', label='z_dot')
    axes[1].set_title('Velocity vs Time'); axes[1].grid(True); axes[1].legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
