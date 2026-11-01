# adventure game

hp = 100
current_room = "Dark Forest"
inventory = ["Torch"]
attack_power = 5
defense = 5
playing = True

print("Welcome to the your journey!")
print("You find yourself in a dark forest. You see a light from a tree.")
print("You: It's so dark in here. I could use this torch. \nYou picked up the torch")
print("Inventory: Torch added.")
# --- ROOM: DARK FOREST ---
if current_room == "Dark Forest":
    print("\n[LOCATION: DARK FOREST]")

# --- Scenario A: Key found
if "Rusty Key" not in inventory:
    print("There is a key on the ground. You see a path leading to a more darkness, and a path to a cabin")