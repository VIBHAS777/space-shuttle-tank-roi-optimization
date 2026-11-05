from src.optimizer import ExternalTankOptimizer
from src.materials import MATERIALS

def main():
    print("=" * 70)
    print("  Space Shuttle External Tank Design ROI Optimization")
    print("  Publication: ICAANA 2025, Amrita Vishwa Vidyapeetham")
    print("=" * 70)

    print("[*] Running Numerical SLSQP Optimization across candidate materials:\n")
    
    results = {}
    for mat_key in ["Al-2219", "Al-Li-2195"]:
        opt = ExternalTankOptimizer(material_key=mat_key)
        res = opt.optimize()
        r, l_lox, l_lh2, t_mm = res.x
        
        # Calculate dry mass
        area = (2 * 3.14159 * r * (l_lox + l_lh2)) + (4 * 3.14159 * (r**2))
        dry_mass = area * (t_mm / 1000.0) * MATERIALS[mat_key]["density_kg_m3"]
        total_cost = res.fun
        
        results[mat_key] = {
            "radius_m": r,
            "thickness_mm": t_mm,
            "dry_mass_kg": dry_mass,
            "lifecycle_cost_usd": total_cost
        }
        
        print(f"  [{MATERIALS[mat_key]['name']}]")
        print(f"    - Optimized Radius       : {r:.2f} m (Diameter: {r*2:.2f} m)")
        print(f"    - Optimized Wall Thickness : {t_mm:.2f} mm")
        print(f"    - Total ET Dry Mass        : {dry_mass:.1f} kg")
        print(f"    - Estimated Cost per Flight: ${total_cost/1e6:.2f} Million\n")

    baseline_mass = results["Al-2219"]["dry_mass_kg"]
    opt_mass = results["Al-Li-2195"]["dry_mass_kg"]
    mass_savings = baseline_mass - opt_mass
    roi_percent = ((results["Al-2219"]["lifecycle_cost_usd"] - results["Al-Li-2195"]["lifecycle_cost_usd"]) / results["Al-Li-2195"]["lifecycle_cost_usd"]) * 100

    print("=" * 70)
    print("  OPTIMIZATION SUMMARY & RETURN ON INVESTMENT (ROI)")
    print("=" * 70)
    print(f"  [+] Structural Dry Mass Reduction : {mass_savings:.1f} kg (-{(mass_savings/baseline_mass)*100:.1f}%)")
    print(f"  [+] Additional Payload to LEO     : +{mass_savings:.1f} kg per mission")
    print(f"  [+] Calculated Multi-Mission ROI  : +{roi_percent:.2f}%")
    print("=" * 70)

if __name__ == "__main__":
    main()
