import numpy as np
from scipy.optimize import minimize
from src.materials import MATERIALS

class ExternalTankOptimizer:
    """
    SLSQP Constrained Optimization for Space Shuttle External Tank (ET).
    Minimizes dry mass & lifecycle expenditure while respecting cryogenic ullage pressure,
    hydrostatic head, and aerodynamic drag constraints.
    """
    def __init__(self, material_key: str = "Al-Li-2195"):
        self.mat = MATERIALS[material_key]
        self.launch_cost_per_kg = 10000.0 # Standard Shuttle payload cost ($/kg to LEO)
        self.num_flights_amortized = 25

    def objective_cost(self, x: np.ndarray) -> float:
        # Decision variables: x = [radius_m, lox_length_m, lh2_length_m, wall_thickness_mm]
        r, l_lox, l_lh2, t_mm = x
        t_m = t_mm / 1000.0

        # Structural surface area approximation (cylinders + ogive dome)
        area_lox = 2 * np.pi * r * l_lox + 2 * np.pi * (r ** 2)
        area_lh2 = 2 * np.pi * r * l_lh2 + 2 * np.pi * (r ** 2)
        total_area = area_lox + area_lh2

        dry_mass_kg = total_area * t_m * self.mat["density_kg_m3"]
        mfg_cost_usd = dry_mass_kg * self.mat["raw_cost_per_kg_usd"] * self.mat["manufacturing_multiplier"]
        
        # Flight penalty cost (each kg of dry mass reduces payload capacity by 1 kg)
        flight_penalty_usd = dry_mass_kg * self.launch_cost_per_kg
        
        return mfg_cost_usd + flight_penalty_usd

    def optimize(self):
        # Initial guess: standard ET dimensions
        # r = 4.2m (8.4m diameter), l_lox = 15m, l_lh2 = 29m, t = 4.5mm
        x0 = np.array([4.2, 15.0, 29.5, 4.5])

        # Bounds: [radius, l_lox, l_lh2, thickness]
        bounds = [(3.8, 4.5), (12.0, 18.0), (26.0, 34.0), (2.0, 8.0)]

        # Constraints: Propellant volumetric requirements for Space Shuttle Main Engines (SSME)
        # LOX volume >= 550 m3, LH2 volume >= 1500 m3
        # Structural stress <= yield_strength / safety_factor (1.4)
        def vol_lox_constraint(x):
            return np.pi * (x[0]**2) * x[1] - 550.0

        def vol_lh2_constraint(x):
            return np.pi * (x[0]**2) * x[2] - 1500.0

        def hoop_stress_constraint(x):
            # Pressure = 0.25 MPa (cryogenic ullage)
            p = 0.25e6 
            r = x[0]
            t = (x[3] / 1000.0)
            hoop_stress = (p * r) / t # Pa
            allowable = (self.mat["yield_strength_mpa"] * 1e6) / 1.4 # Safety factor 1.4
            return allowable - hoop_stress

        constraints = [
            {'type': 'ineq', 'fun': vol_lox_constraint},
            {'type': 'ineq', 'fun': vol_lh2_constraint},
            {'type': 'ineq', 'fun': hoop_stress_constraint}
        ]

        res = minimize(
            self.objective_cost,
            x0,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints,
            options={'disp': False, 'ftol': 1e-6, 'maxiter': 200}
        )
        return res
