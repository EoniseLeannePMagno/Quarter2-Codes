destinations = int(input("How many destinations are you going to visit?"))
print(f"Please enter your {destinations} travel destinations: ")
travel_plan = []
for i in range(destinations):
    destination = input(f"Destination {i + 1}: ")
    travel_plan.append(destination)
print("Original Travel Itinerary:")
for idx, place in enumerate(travel_plan, start=1):
    print(f"{idx}. {place}")
reply = input("Do you want to update your travel itinerary? (yes/no): ").strip().lower()
if reply == 'yes':
    new_destinations = int(input("How many destinations do you want to update? "))
    for i in range(new_destinations):
        new_destination = input(f"Enter new destination for stop {i + 1}: ")
        travel_plan[i] = new_destination
    print("Updated Travel Itinerary:")
    for idx, place in enumerate(travel_plan, start=1):
        print(f"{idx}. {place}")
elif reply == 'no':
    print("No changes made to the travel itinerary.")
    str()