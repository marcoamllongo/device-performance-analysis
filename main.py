import csv

with open("data/battery_readings.csv", newline="") as file:
    readings = list(csv.DictReader(file))

initial = int(readings[0]["battery_level"])
second_measurement = int(readings[1]["battery_level"])
final = int(readings[-1]["battery_level"])

print(f"Total measurements: {len(readings)}")
print(f"Initial battery: {initial}%")
print(f"Second Measurement battery: {second_measurement}%")
print(f"Final battery: {final}%")
print(f"Battery drop: {initial - final} percentage points")