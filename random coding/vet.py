import random
import time

class Clinic:
    def __init__(self, name):
        self.name = name
        self.money = 200
        self.reputation = 50
        self.day = 1
        # Starting medical supplies
        self.inventory = {"Antibiotics": 3, "Bandages": 3}

    def show_status(self):
        print(f"\n{'='*40}")
        print(f"🏥 {self.name} | Day {self.day}")
        print(f"💵 Funds: ${self.money} | ⭐ Reputation: {self.reputation}/100")
        print(f"📦 Inventory: {self.inventory}")
        print(f"{'='*40}")

class Pet:
    def __init__(self):
        names = ["Buddy", "Luna", "Max", "Bella", "Charlie", "Milo", "Daisy"]
        species = ["Dog", "Cat"]
        
        # Dictionary of diseases, their clues, the correct cure, and what you charge
        diseases = {
            "Ear Infection": {
                "symptoms": "scratching ears aggressively and shaking head.", 
                "treatment": "Antibiotics", 
                "revenue": 75
            },
            "Minor Laceration": {
                "symptoms": "limping with a small bleeding cut on the paw.", 
                "treatment": "Bandages", 
                "revenue": 50
            },
            "Healthy": {
                "symptoms": "bright, alert, and wagging tail/purring.", 
                "treatment": "None", 
                "revenue": 20 # Charge for a basic checkup
            }
        }
        
        self.name = random.choice(names)
        self.species = random.choice(species)
        self.disease_name = random.choice(list(diseases.keys()))
        self.data = diseases[self.disease_name]

def game_loop():
    print("🐾 Welcome to Paws & Practice: Vet Tycoon (Console Edition) 🐾")
    clinic_name = input("What do you want to name your clinic? ")
    my_clinic = Clinic(clinic_name)

    while True:
        # Check lose condition
        if my_clinic.reputation <= 0:
            print("\n❌ Game Over! Your reputation dropped to 0 and the veterinary board closed your clinic.")
            break

        my_clinic.show_status()
        patient = Pet()
        
        print(f"\n🔔 *Ding!* A new patient has arrived in the exam room.")
        print(f"It's a {patient.species} named {patient.name}.")
        print(f"Observation: {patient.name} is {patient.data['symptoms']}")
        
        print("\nWhat would you like to do?")
        print("1. Examine and Treat")
        print("2. Turn them away (Too busy)")
        print("3. Close clinic and quit game")
        
        choice = input("> ")
        
        if choice == '3':
            print("\nClosing up shop. Thanks for playing!")
            break
        elif choice == '2':
            print(f"\nYou told {patient.name}'s owner to go to the emergency vet down the street.")
            print("The owner left a 1-star review. (-5 Reputation)")
            my_clinic.reputation -= 5
            my_clinic.day += 1
            time.sleep(1.5)
            continue
        elif choice == '1':
            print("\n--- Treatment Menu ---")
            print("1. Administer Antibiotics")
            print("2. Apply Bandages")
            print("3. Do nothing (Give a clean bill of health)")
            
            treat_choice = input("Choose treatment (1-3): ")
            treatment_given = ""
            
            if treat_choice == '1': treatment_given = "Antibiotics"
            elif treat_choice == '2': treatment_given = "Bandages"
            elif treat_choice == '3': treatment_given = "None"
            else:
                print("Invalid choice! You fumbled your tools.")
                treatment_given = "Error"

            # Check if we have the item in stock (skip check if treatment is None)
            if treatment_given != "None" and treatment_given != "Error":
                if my_clinic.inventory[treatment_given] <= 0:
                    print(f"\nUh oh! You are out of {treatment_given}. You couldn't treat the pet.")
                    print("The owner is furious! (-10 Reputation)")
                    my_clinic.reputation -= 10
                    my_clinic.day += 1
                    time.sleep(2)
                    continue
                else:
                    my_clinic.inventory[treatment_given] -= 1

            # Check if the treatment matches the disease
            if treatment_given == patient.data["treatment"]:
                print(f"\n✅ Success! You correctly treated {patient.name}.")
                print(f"The owner paid you ${patient.data['revenue']}. (+5 Reputation)")
                my_clinic.money += patient.data["revenue"]
                my_clinic.reputation += 5
                
                # Cap reputation at 100
                if my_clinic.reputation > 100:
                    my_clinic.reputation = 100
            else:
                print(f"\n❌ Medical Malpractice! That was the wrong treatment. {patient.name} isn't getting better.")
                print("The owner is demanding a refund. (-15 Reputation)")
                my_clinic.reputation -= 15

        # End of day shop (Restocking)
        if my_clinic.money >= 50:
            print("\n--- End of Day Supply Run ---")
            buy = input("Do you want to buy supplies for $50? (y/n): ").lower()
            if buy == 'y':
                my_clinic.money -= 50
                my_clinic.inventory["Antibiotics"] += 2
                my_clinic.inventory["Bandages"] += 2
                print("Bought +2 Antibiotics and +2 Bandages.")

        my_clinic.day += 1
        time.sleep(1.5) # Pauses the game for a second to make it readable

if __name__ == "__main__":
    game_loop()
