# --- INITIAL SETUP ---
hp = 100
inventory = ["Rusty Key"] # Start with one item
current_room = "Hallway"
playing = True
print("Welcome to the Adventure Game!")
print("You find yourself in a dimly lit hallway. You found a Rusty Key on the ground.")
print("You: 'What should I do? Maybe I can use this key somewhere?'")

# --- ROOM: HALLWAY ---
if current_room == "Hallway":
        print("\n[LOCATION: THE STONE HALLWAY]")
        
        # Scenario A: Coin is still there
        if "Gold Coin" not in inventory:
            print("There is a shiny coin on the ground. To the north, you see a path leading into a forest.")
            action = input("Action: [1] Pick up coin, [2] Go North: ").lower()
            
            if action == "1":
                print(">> You picked up the Gold Coin! You can check your inventory to see what you have. (Hint: Type 'i' to check inventory)")
                inventory.append("Gold Coin")
                print("To the north, you see a path leading into a forest. To the south is the entrance you came from.")
                action = input("Action: [1] Go North, [2] Go South, [i] Inventory: ").lower()
            else:
                print("The hallway is empty.")
            action = input("Action: [1] Go North, [2] Go South, [i] Inventory: ").lower()
            
            if action == "1":
                current_room = "Forest"
                print(">> You head north towards the forest.")
                print("LOCATION: THE MYSTERIOUS FOREST")
                print("You: 'Bruh this place is creepy... I feel like there's something interesting here.'")
                action = input("Action: [1] Explore deeper, [2] Go South, [i] Inventory: ").lower()
            elif action == "2":
                current_room = "Entrance"
                print(">> You head back south towards the entrance.")
                print("LOCATION: THE ENTRANCE")
                print("You: 'I guess I can go back to the entrance and see if there's anything else there.'")
                action = input("Action: [1] Explore entrance, [2] Go North, [i] Inventory: ").lower()
            elif action == "i":
                print(f"\n--- YOUR BAG --- \nItems: {inventory}")

        # Scenario B: Coin is ALREADY picked up
elif "Gold Coin" in inventory:
        print("The hallway is empty.")
        action = input("Action: [1] Go North, [2] Go South, [i] Inventory: ").lower()
            
        if action == "1":
                current_room = "Forest"
        elif action == "2":
                current_room = "Entrance"
        elif action == "i":
                print(f"\n--- YOUR BAG --- \nItems: {inventory}")

# --- LOCATION: FOREST ---
if current_room == "Forest":
        print("\n[LOCATION: THE MYSTERIOUS FOREST]")
        print("You enter a dense forest. The trees are tall and the atmosphere is eerie. ")
        action = input("Action: [1] Explore deeper, [2] Go South, [i] Inventory: ").lower()
        
        if action == "1":
            print(">> You venture deeper into the forest and find a hidden cave!")
            current_room = "Cave"
        elif action == "2":
            current_room = "Hallway"
        elif action == "i":
            print(f"\n--- YOUR BAG --- \nItems: {inventory}")