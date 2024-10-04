import dolfinx

import numpy as np

import ufl 
class EshelbyDisk:
    def __init__(self, V, γ, χ, ν_i, ν_m):
        self.V = V
        self.u = dolfinx.fem.Function(V,name="exact_solution")
        self.x = ufl.SpatialCoordinate(V.mesh)
        self.γ = γ
        self.χ = χ
        self.ν_i = ν_i
        self.ν_m = ν_m

    def create_lhs(self):
        return np.array(
            [
                [2, 2 * self.γ ** 2, 2 * self.γ ** 4, 2 * self.γ ** 6, 0, 0],
                [
                    2 * self.ν_m * (self.ν_m - 1),
                    -(self.γ ** 2) * self.ν_m * (2 * self.ν_m - 1),
                    -2 * self.γ ** 4 * self.ν_m * (self.ν_m - 1),
                    self.γ ** 6 * (self.ν_m - 1) * (2 * self.ν_m - 3),
                    0,
                    0,
                ],
                [1, 1, 1, 1, -1, -1],
                [
                    2 * self.ν_i * self.ν_m * (self.ν_m - 1),
                    -self.ν_i * self.ν_m * (2 * self.ν_m - 1),
                    -2 * self.ν_i * self.ν_m * (self.ν_m - 1),
                    self.ν_i * (self.ν_m - 1) * (2 * self.ν_m - 3),
                    2 * self.ν_i * self.ν_m * (self.ν_m - 1),
                    -self.ν_m * (2 * self.ν_i - 3) * (self.ν_m - 1),
                ],
                [
                    3 * (self.ν_i + 1) * (self.ν_m - 1),
                    -self.ν_i - 1,
                    -(self.ν_i + 1) * (self.ν_m - 1),
                    0,
                    self.χ * (self.ν_m - 1) * (self.ν_m + 1),
                    0,
                ],
                [
                    -6 * self.ν_i * self.ν_m * (self.ν_i + 1) * (self.ν_m - 1),
                    self.ν_i * self.ν_m * (self.ν_i + 1),
                    -2 * self.ν_i * self.ν_m * (self.ν_i + 1) * (self.ν_m - 1),
                    -3 * self.ν_i * (self.ν_i + 1) * (self.ν_m - 1),
                    2 * self.χ * self.ν_i * self.ν_m * (self.ν_m - 1) * (self.ν_m + 1),
                    3 * self.χ * self.ν_m * (self.ν_m - 1) * (self.ν_m + 1),
                ],
            ]
        )

    def create_rhs(self):
        return np.array(
            [2 * self.γ ** 4, -2 * self.γ ** 4 * self.ν_m * (self.ν_m - 1), 0, 0, 0, 0]
        )

    def compute_integration_constants(self):
        return np.linalg.solve(self.create_lhs(), self.create_rhs())

    def to_expression(self, a=1.0):
        A_m3, A_m1, A_1, A_3, C_1, C_3 = self.compute_integration_constants()
        ρ = ufl.sqrt(self.x[0]**2 + self.x[1]**2) / a
        θ = ufl.atan2(self.x[1],self.x[0])
        B_m3 = - A_m3
        B_m1 = (1 - 2 * self.ν_m) / 2 / (1 - self.ν_m) * A_m1
        B_1 = A_1
        B_3 = (3 - 2 * self.ν_m) / 2 / self.ν_m * A_3
        D_1 = C_1
        D_3 =  (3 - 2 * self.ν_i) / 2 / self.ν_i * C_3
        rho = ρ
        theta = θ

        F = ufl.conditional(rho > 1, A_m3 * rho ** -3 + A_m1/rho + A_1 * rho + A_3 * rho ** 3,            C_1 * rho + C_3 * rho ** 3)
        G = ufl.conditional(rho > 1, B_m3 * rho ** -3 + B_m1/rho + B_1 * rho + B_3 * rho ** 3,            D_1 * rho + D_3 * rho ** 3)
        u_r =  - F * ufl.sin(2*theta)
        u_θ =  - G * ufl.cos(2*theta)
        u_expr_ = ufl.as_vector([u_r*ufl.cos(theta)-u_θ*ufl.sin(theta), u_r*ufl.sin(theta)+u_θ*ufl.cos(theta)])
        u_expr = dolfinx.fem.Expression(u_expr_, self.V.element.interpolation_points())
        #self.u.interpolate(u_expr)
        #dolfin.Expression(
        #    ("u_r*cos(theta)-u_theta*sin(theta)", "u_r*sin(theta)+u_theta*cos(theta)"),
        #    degree=degree,
        #    theta=θ,
        #    u_r=u_r,
        #    u_theta=u_θ,
        #grad_expr1(x):
        #return np.vstack((2.0 * x[0], 4.0 * x[1]))
        return u_expr
    
    def to_function(self, a=1.0):
        self.u.interpolate(self.to_expression(a=a))
        return self.u

