def rssi_quality(rssi):
    if rssi >= -55:
        return 4
    elif rssi >= -75:
        return 3
    elif rssi >= -85:
        return 2
    else:
        return 1