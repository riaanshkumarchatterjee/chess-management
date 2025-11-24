# Chess Tournament Management System
A specialized Python-based application designed to streamline the organization of chess tournaments. This system digitizes the entire workflow, from player registration with strict title validation to automated, algorithmic matchmaking. It replaces manual spreadsheet pairings with an intelligent system that ensures fair play by grouping competitors into specific skill bands.
Key Features
## Smart Title Verification: The system maintains the integrity of player titles by validating self-proclaimed titles against ELO ratings.
o	GM (Grandmaster): Requires 2500+ ELO.
o	IM (International Master): Requires 2200+ ELO.
o	NM (National Master): Requires 2000+ ELO.
o	If a player claims a title without the required rating, the system automatically rejects it.
## 	Visual Matchmaking Table: Generates professional-grade pairings using matplotlib. Instead of text output, the system launches a graphical popup window displaying a clear, color-coded table of who plays whom (White vs. Black).
## Algorithmic Skill Bucketing: Ensures fair matches by automatically categorizing players into five distinct skill levels:
o	Novice (<1000)
o	Intermediate (1000-1500)
o	Club Player (1500-2000)
o	Expert (2000-2500)
o	Grandmaster (>2500)
## Automated "Bye" Handling: Intelligently handles odd numbers of players within a bracket by automatically assigning a "Bye" (a free pass to the next round) to the unmatched player.
## 	Secure Admin Registry: Includes a password-protected administrative view (Password: 3939) that allows tournament directors to audit the full list of registered players and their IDs.
## 	Zero-Config Persistence: All player data is automatically saved to a local chess_data.json file, ensuring the tournament roster is preserved even if the application is closed.
## Technologies Used
## Language: Python 3.x
## Visualization: matplotlib (for generating the pairings table)
## Data Handling: json (for persistent storage), random (for shuffling pairings)
## Steps to Install & Run
1.	Clone the Repository:
2.	git clone [https://github.com/yourusername/chess-tournament-system.git](https://github.com/yourusername/chess-tournament-system.git)
3.	cd chess-tournament-system
4.	Install Required Libraries: This project uses matplotlib for the visual tables.
5.	pip install matplotlib
6.	Run the Application:
7.	python chess_main.py
## Instructions for Testing
 To verify the system's logic, perform the following test scenarios:
 ### Scenario A: Title Validation Logic
     1.	Register a Player: Select option 1.
     2.	Attempt Fraud: Enter Name "Test User", ELO 1900, and claim title "GM".
     3.	Expected Result: System should display ❌ Rejected: GM title requires minimum 2500 ELO.
 ### Scenario B: Fair Matchmaking
       1.	Populate Roster: Register 4 players:
        o	Player A (ELO 800)
        o	Player B (ELO 900)
        o	Player C (ELO 2600)
        o	Player D (ELO 2700)
    2.	Generate Pairings: Select option 2.
    3.	Verify Visual Table: A window should pop up showing two separate brackets. Player A should play Player B (Novice Bracket), and Player C should play Player D (Grandmaster Bracket). They should not cross-pair.
### Scenario C: Admin Access
      1.	Select Admin View: Choose option 3.
2.	Enter Password: Type 3939.
3.	Verify Output: Ensure the full list of players and IDs is displayed in the terminal.
