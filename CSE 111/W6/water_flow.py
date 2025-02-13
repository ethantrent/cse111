"""In your function, use the following formulas for calculating
h = t + 3w/4

h is height of the water column
t is the height of the tower
w is the height of the walls of the tank that is on top of the tower

P = pgh/1000

P is the pressure in kilopascals
p is the density of water (998.2 kilogram / meter3)
g is the acceleration from Earths gravity (9.80665 meter / second2)
h is the height of the water column in meters

P = -fLpv2/2000d

P is the lost pressure in kilopascals
f is the pipe's friction factor
L is the length of the pipe in meters
p is the density of water (998.2 kilogram / meter3)
v is the velocity of the water flowing through the pipe in meters / second
d is the diameter of the pipe in meters

P = -0.04pv2n/2000
P is the lost pressure in kilopascals
p is the density of water (998.2 kilogram / meter3)
v is the velocity of the water flowing through the pipe in meters / second
n is the quantity of fittings

R = pdv/μ
R is the Reynolds number
p is the density of water (998.2 kilogram / meter3)
d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter.
v is the velocity of the water flowing through the pipe in meters / second
μ is the dynamic viscosity of water (0.0010016 Pascal seconds)

k = (0.1 + 50/R)((D/d)^4 - 1)
P = -kpv^2n/2000

k is a constant computed by the first formula and used in the second formula
R is the Reynolds number that corresponds to the pipe with the larger diameter
D is the diameter of the larger pipe in meters
d is the diameter of the smaller pipe in meters
P is the lost pressure kilopascals
p is the density of water (998.2 kilogram / meter3)
v is the velocity of the water flowing through the larger diameter pipe in meters / second
"""

# Inside the functions of your water_flow.py program, you may have typed numbers for Earth’s acceleration of gravity, 
# the density of water, and the dynamic viscosity of water. Instead of using the numbers inside your functions, 
# define the following constants outside your functions. Then use the constant names in place of the numbers inside your functions.

earth_acceleration_of_gravity = 9.80665
density_of_water = 998.2
dynamic_viscosity_of_water = 0.0010016

def water_column_height(tower_height, tank_height):
    # Calculate the height of the water column
    height = tower_height + (3 * tank_height) / 4
    return height

def pressure_gain_from_water_height(height):
    # Calculate the pressure gain from the height of the water column
    pressure = density_of_water * earth_acceleration_of_gravity * height / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    # Calculate the pressure loss from the pipe
    pressure_loss = -friction_factor * pipe_length * density_of_water * fluid_velocity**2 / (2000 * pipe_diameter)
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    # Calculate the pressure loss from the fittings
    pressure_loss = -0.04 * density_of_water * fluid_velocity**2 * quantity_fittings / 2000
    return pressure_loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    # Calculate the Reynolds number
    reynolds_number = density_of_water * hydraulic_diameter * fluid_velocity / dynamic_viscosity_of_water
    return reynolds_number

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    # Calculate the pressure loss from the pipe reduction
    constant = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter)**4 - 1)
    pressure_loss = -constant * density_of_water * fluid_velocity**2 / 2000
    return pressure_loss

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()