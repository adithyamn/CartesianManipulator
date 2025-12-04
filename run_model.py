
from dynamicsmodel import CartesianManipulator


def main():
    model = CartesianManipulator(m_x=3.5, m_y=4.5, m_z=5.5, g=9.81)
    print("ODE expression f(x,u):", model.ode)


if __name__ == "__main__":
    main()
