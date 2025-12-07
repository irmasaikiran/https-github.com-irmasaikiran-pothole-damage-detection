# --------------------------------------------
# COST ESTIMATION MODELS
# --------------------------------------------

# Model 2 – Road Type Based Cost
def estimate_cost_model2(area_m2, road_type):
    """
    Model 2:
        Asphalt  = ₹500 / m²
        Concrete = ₹800 / m²
    """
    if road_type == "Asphalt":
        rate = 500
    else:
        rate = 800
    
    return area_m2 * rate


# Model 3 – PWD Standard Government Cost
def estimate_cost_model3(area_m2):
    """
    Model 3 — PWD-Based Cost:
        Material   = ₹350 / m²
        Labor      = ₹200 / m²
        Machinery  = ₹150 / m²
        Overheads  = ₹100 / m²
    """
    material = 350
    labor = 200
    machinery = 150
    overhead = 100

    total_rate = material + labor + machinery + overhead
    return area_m2 * total_rate
