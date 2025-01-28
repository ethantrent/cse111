# OPEN THE FILE
# READ IT LINE BY LINE
# SPLIT EACH LINE ON "," TO GET THE FIELDS DATA
# GET EACH FIELD OF THE SPLITTED LINE AND APPEND TO A RESPECTIVE LIST
# AT THIS POINT YOU WILL HAVE THE TELEMETRY DATA IN 5 DIFFERENT LISTS
# USING THE LISTS THAT YOU CREATED, PRINT THE ANSWER OF FOLLOWING QUESTIONS:
# 1-IN WHICH INTERVAL DOES THE ALTITUDE CHANGES MOST RAPIDLY?
# 2-WHAT IS THE MAXIMUM ALTITUDE CHANGE RATE?
# 3-WHAT IS THE ALTITUDE AT THIS POINT?
# 4-IN WHICH INTERVAL DOES THE SPEED CHANGE MOST RAPIDLY?
# 5-WHAT IS THE SPEED AT THIS POINT?
 # *CONSIDER THE CHANGE RATE AS: (ACTUAL - PREVIOUS) / INTERVAL

timestamps = []
altitudes = []
speeds = []
stages = []

with open('falcon9_launch_telemetry.cvs') as f:
    # Skip header
    # next (f)
    for line in f:
        line_parts = line.split(',')
        measurement = int(line_parts[0]).strip()
        timestamp = float(line_parts[1]).strip()
        timestamps.append(timestamp)
        altitude = float(line_parts[2]).strip()
        altitudes.append(altitude)
        speed = float(line_parts[3]).strip()
        speeds.append(speed)
        stage = int(line_parts[4].strip())
        stages.append(stage)

for i in range(len(1, len(timestamps))):
    altitude_change_rate = (altitudes[i] - altitudes[i-1]) / (timestamps[i] - timestamps[i-1])
    if altitude_change_rate > max_altitude_change_rate:
        max_altitude_change_rate = altitude_change_rate
        max_altitude_change_rate_interval = i
        max_altitude_change_rate_altitude = altitudes[i]

    speed_change_rate = (speeds[i] - speeds[i-1]) / (timestamps[i] - timestamps[i-1])
    if speed_change_rate > max_speed_change_rate:
        max_speed_change_rate = speed_change_rate
        max_speed_change_rate_interval = i
        max_speed_change_rate_speed = speeds[i]