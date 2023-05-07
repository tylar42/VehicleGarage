# Create an empty list to store the vehicles in the garage
garage = []

# Define a base class for a Vehicle
class Vehicle:

  # Set the make of the Vehicle
  def SetMake(self, make):
    self.make = make

  # Set the model of the Vehicle
  def SetModel(self, model):
    self.model = model

  # Return the make of the Vehicle
  def GetMake(self):
    return self.make

  # Return the model of the Vehicle
  def GetModel(self):
    return self.model

  # Return all the properties of the Vehicle
  def GetProperties(self):
    properties = {"Make": self.make, "Model": self.model}
    return properties


# Define a Car class that inherits from the Vehicle class
class Car(Vehicle):

  # Set the number of doors of the Car
  def SetCarDoor(self, numDoors):
    self.numDoors = numDoors

  # Return the number of doors of the Car
  def GetCarDoor(self):
    return self.numDoors

  # Return all the properties of the Car
  def GetProperties(self):
    properties = super().GetProperties()
    properties["Doors"] = self.numDoors
    return properties


# Define a Truck class that inherits from the Vehicle class
class Truck(Vehicle):

  # Set the bed length of the Truck
  def SetBedLength(self, bedLength):
    self.bedLength = bedLength

  # Return the bed length of the Truck
  def GetBedLength(self):
    return self.bedLength

  # Return all the properties of the Truck
  def GetProperties(self):
    properties = super().GetProperties()
    properties["Bed Length (feet)"] = self.bedLength
    return properties


# Continuously prompt the user to input information about a new vehicle
while True:
  vehicleType = input("Enter the type of vehicle (Car/Truck): ")
  make = input("Enter the make of the vehicle: ")
  model = input("Enter the model of the vehicle: ")

  # If the user entered "Car", prompt for number of doors
  if vehicleType.lower() == "car":
    numDoors = int(input("Enter the number of doors: "))
    new_vehicle = Car()
    new_vehicle.SetCarDoor(numDoors)

  # If the user entered "Truck", prompt for bed length
  elif vehicleType.lower() == "truck":
    bedLength = float(input("Enter the bed length (in feet): "))
    new_vehicle = Truck()
    new_vehicle.SetBedLength(bedLength)

  # If the user entered something else, print an error message and continue to the next iteration
  else:
    print("Invalid vehicle type.")

  # Set the make and model of the vehicle
  new_vehicle.SetMake(make)
  new_vehicle.SetModel(model)

  # Add the vehicle to the garage
  garage.append(new_vehicle)

  # Prompt the user to add another vehicle, or exit
  x = input("Would you like to add another vehicle y/n? ")
  if x.lower() != "y":
    break

print("These are the vehicles in your garage:")
# iterate over the vehicles in the garage and print their properties
for i, vehicle in enumerate(garage):
  print(f"Vehicle {i+1}:")
  for propertyDesc, property in vehicle.GetProperties().items():
    print(f"  {propertyDesc}: {property}")
