"""
Aerospace Material Database for External Tank Structural Analysis
"""
MATERIALS = {
    "Al-2219": {
        "name": "Aluminium-Copper Alloy 2219-T87 (Standard ET)",
        "density_kg_m3": 2840.0,
        "yield_strength_mpa": 390.0,
        "ultimate_strength_mpa": 450.0,
        "raw_cost_per_kg_usd": 45.0,
        "manufacturing_multiplier": 3.2
    },
    "Al-Li-2195": {
        "name": "Aluminium-Lithium Alloy 2195 (Super Lightweight Tank - SLWT)",
        "density_kg_m3": 2710.0,
        "yield_strength_mpa": 550.0,
        "ultimate_strength_mpa": 600.0,
        "raw_cost_per_kg_usd": 120.0,
        "manufacturing_multiplier": 4.8
    },
    "CFRP-Overwrap": {
        "name": "Carbon Fiber Reinforced Polymer Overwrap",
        "density_kg_m3": 1550.0,
        "yield_strength_mpa": 850.0,
        "ultimate_strength_mpa": 1200.0,
        "raw_cost_per_kg_usd": 210.0,
        "manufacturing_multiplier": 5.5
    }
}
