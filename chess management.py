import json
import os
import random
from datetime import datetime
import matplotlib.pyplot as plt
class DataManager:
    def __init__(self, filename="chess_data.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return {"players": []}
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return {"players": []}

    def save_data(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")
class PlayerManager:
    def __init__(self, data_manager):
        self.dm = data_manager

    def register_player(self, name, elo):
        new_id = len(self.dm.data["players"]) + 1
        
        title = "None"
        if elo > 1800:
            print("🌟 High Rating Detected!")
            t_input = input("Enter FIDE Title (GM/IM/NM/FM/CM or 'None'): ").strip().upper()
            
            if t_input == "GM":
                if elo >= 2500:
                    title = "GM"
                    print("✅ GM Title Verified.")
                else:
                    print(f"❌ Rejected: GM title requires minimum 2500 ELO (You have {elo}).")
            
            elif t_input == "IM":
                if elo >= 2200:
                    title = "IM"
                    print("✅ IM Title Verified.")
                else:
                    print(f"❌ Rejected: IM title requires minimum 2200 ELO (You have {elo}).")
            
            elif t_input == "NM":
                if elo >= 2000:
                    title = "NM"
                    print("✅ NM Title Verified.")
                else:
                    print(f"❌ Rejected: NM title requires minimum 2000 ELO (You have {elo}).")
            
            elif t_input in ["FM", "CM"]:
                title = t_input
                print(f"✅ {title} Title Accepted.")
            
            elif t_input != "NONE":
                print("ℹ️ Input ignored or unknown title.")

        new_player = {
            "id": new_id,
            "name": name,
            "elo": elo,
            "title": title,
            "registered_date": datetime.now().strftime("%Y-%m-%d")
        }

        self.dm.data["players"].append(new_player)
        self.dm.save_data()
        print(f"✅ Player Registered! {title if title != 'None' else ''} {name} (ELO: {elo})")

    def admin_view_players(self):
        if not self.dm.data["players"]:
            print("No players registered.")
            return
            
        print("\n--- ♟️ Registered Players Registry (Admin) ---")
        print(f"{'ID':<5} {'Title':<6} {'Name':<20} {'ELO':<6}")
        print("-" * 45)
        for p in self.dm.data["players"]:
            t_str = p['title'] if p['title'] != "None" else ""
            print(f"{p['id']:<5} {t_str:<6} {p['name']:<20} {p['elo']:<6}")
        print("-" * 45)
class TournamentManager:
    def __init__(self, data_manager):
        self.dm = data_manager

    def generate_pairings(self):
        players = self.dm.data["players"]
        if not players:
            print("No players to pair.")
            return

        buckets = {
            "Novice (<1000)": [],
            "Intermediate (1000-1500)": [],
            "Club Player (1500-2000)": [],
            "Expert (2000-2500)": [],
            "Grandmaster (>2500)": []
        }
        for p in players:
            elo = p["elo"]
            if elo < 1000:
                buckets["Novice (<1000)"].append(p)
            elif 1000 <= elo < 1500:
                buckets["Intermediate (1000-1500)"].append(p)
            elif 1500 <= elo < 2000:
                buckets["Club Player (1500-2000)"].append(p)
            elif 2000 <= elo < 2500:
                buckets["Expert (2000-2500)"].append(p)
            else:
                buckets["Grandmaster (>2500)"].append(p)

        print("\n=== ⚔️ TOURNAMENT PAIRINGS GENERATED ⚔️ ===")
        visual_data = []
        
        for category, p_list in buckets.items():
            if not p_list:
                continue

            print(f"\n>> {category} Bracket:")
            random.shuffle(p_list)
            
            i = 0
            while i < len(p_list):
                p1 = p_list[i]
                t1 = f"({p1['title']})" if p1['title'] != "None" else ""
                p1_display = f"{p1['name']} {t1} [{p1['elo']}]"

                if i + 1 < len(p_list):
                    p2 = p_list[i+1]
                    t2 = f"({p2['title']})" if p2['title'] != "None" else ""
                    p2_display = f"{p2['name']} {t2} [{p2['elo']}]"
                    
                    print(f"   {p1_display}  VS  {p2_display}")
                    visual_data.append([category, p1_display, p2_display])
                    i += 2
                else:
                    print(f"   {p1_display} gets a BYE (No Match)")
                    visual_data.append([category, p1_display, "BYE (No Opponent)"])
                    i += 1
        
        print("\n" + "="*45)
        if visual_data:
            self.show_visual_pairings(visual_data)

    def show_visual_pairings(self, data):
        """Displays a Matplotlib Table of the generated pairings"""
        print("📊 Opening Matchmaking Table...")
        
        fig, ax = plt.subplots(figsize=(10, 4 + len(data) * 0.4))
        ax.axis('off')
        ax.set_title("⚔️ Official Tournament Pairings ⚔️", fontsize=16, weight='bold', color='darkred')
        table = ax.table(
            cellText=data,
            colLabels=["Bracket Category", "Player 1 (White)", "Player 2 (Black)"],
            loc='center',
            cellLoc='left',
            colColours=["#dddddd"] * 3
        )

        table.auto_set_font_size(False)
        table.set_fontsize(11)
        table.scale(1.2, 1.8)
        table.auto_set_column_width(col=[0, 1, 2])

        plt.show()
def main():
    dm = DataManager()
    pm = PlayerManager(dm)
    tm = TournamentManager(dm)

    while True:
        print("\n=== ♟️ CHESS TOURNAMENT SYSTEM ===")
        print("1. Register New Player")
        print("2. Generate Match Pairings (Visual Table)")
        print("3. View All Players (Admin Only)")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            try:
                name = input("Enter Player Name: ")
                elo = int(input("Enter ELO Rating: "))
                pm.register_player(name, elo)
            except ValueError:
                print("Invalid ELO rating.")

        elif choice == '2':
            tm.generate_pairings()

        elif choice == '3':
            pwd = input("Enter Admin Password: ")
            if pwd == "3939":
                pm.admin_view_players()
            else:
                print("❌ Access Denied.")

        elif choice == '4':
            print("Exiting...")
            exit()
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
