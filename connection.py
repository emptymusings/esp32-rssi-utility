def rssi_quality(rssi):
    if rssi >= -60:
        return 4
    elif rssi >= -70:
        return 3
    elif rssi >= -80:
        return 2
    else:
        return 1