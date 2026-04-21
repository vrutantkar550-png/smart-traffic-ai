def control_signal(vehicle_count):
    # Basic logic
    if vehicle_count < 5:
        return 10
    elif vehicle_count < 15:
        return 20
    else:
        return 30
