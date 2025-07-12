from datetime import date
from typing import List

class Person:
    def __init__(self, person_id, first_name, last_name, date_of_birth, nationality):
        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.nationality = nationality

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Player(Person):
    def __init__(self, person_id, first_name, last_name, date_of_birth, nationality,
                 player_id, jersey_number, market_value, team_id, position, status):
        super().__init__(person_id, first_name, last_name, date_of_birth, nationality)
        self.player_id = player_id
        self.jersey_number = jersey_number
        self.market_value = market_value
        self.team_id = team_id
        self.position = position
        self.status = status

    def __str__(self):
        return f"{self.get_full_name()} - #{self.jersey_number} - {self.position}"

class Coach(Person):
    def __init__(self, person_id, first_name, last_name, date_of_birth, nationality,
                 coach_id, license_level, team_id, role):
        super().__init__(person_id, first_name, last_name, date_of_birth, nationality)
        self.coach_id = coach_id
        self.license_level = license_level
        self.team_id = team_id
        self.role = role

    def __str__(self):
        return f"{self.role}: {self.get_full_name()} (License: {self.license_level})"

class Team:
    def __init__(self, team_id, league, division, club_id, name):
        self.team_id = team_id
        self.league = league
        self.division = division
        self.club_id = club_id
        self.name = name
        self.players: List[Player] = []
        self.coaches: List[Coach] = []

    def add_player(self, player: Player):
        self.players.append(player)

    def add_coach(self, coach: Coach):
        self.coaches.append(coach)

    def display_team(self):
        print(f"\nTeam: {self.name} ({self.division})")
        print("Coaches:")
        for coach in self.coaches:
            print(" -", coach)
        print("\nPlayers:")
        for player in self.players:
            print(" -", player)

class Stadium:
    def __init__(self, stadium_id, name, league, capacity, address):
        self.stadium_id = stadium_id
        self.name = name
        self.league = league
        self.capacity = capacity
        self.address = address

class Club:
    def __init__(self, club_id, name, founding_date, budget, league, stadium: Stadium):
        self.club_id = club_id
        self.name = name
        self.founding_date = founding_date
        self.budget = budget
        self.league = league
        self.stadium = stadium
        self.teams: List[Team] = []

    def add_team(self, team: Team):
        self.teams.append(team)

    def display_info(self):
        print(f"\nClub: {self.name}")
        print(f"League: {self.league}, Budget: {self.budget}")
        print(f"Stadium: {self.stadium.name}, Capacity: {self.stadium.capacity}")
        for team in self.teams:
            team.display_team()

def input_date(prompt):
    raw = input(prompt + " (YYYY-MM-DD): ")
    y, m, d = map(int, raw.split("-"))
    return date(y, m, d)

def main():
    print("=== FC Cakrawala Setup ===")
    club_id = input("Club ID: ")
    club_name = input("Club Name: ")
    founding = input_date("Founding Date")
    budget = float(input("Budget: "))
    league = input("League Name: ")

    print("\n-- Stadium Info --")
    stadium_id = input("Stadium ID: ")
    stadium_name = input("Stadium Name: ")
    capacity = int(input("Capacity: "))
    address = input("Address: ")
    stadium = Stadium(stadium_id, stadium_name, league, capacity, address)

    club = Club(club_id, club_name, founding, budget, league, stadium)

    print("\n-- Team Setup --")
    team_id = input("Team ID: ")
    team_name = input("Team Name: ")
    division = input("Division (e.g. U-23): ")
    team = Team(team_id, league, division, club_id, team_name)
    club.add_team(team)

    print("\n-- Add Coaches --")
    for role in ["Head Coach", "Assistant Coach"]:
        print(f"\nEntering {role}")
        pid = input("Person ID: ")
        fname = input("First Name: ")
        lname = input("Last Name: ")
        dob = input_date("Date of Birth")
        nat = input("Nationality: ")
        cid = input("Coach ID: ")
        license = input("License Level: ")
        coach = Coach(pid, fname, lname, dob, nat, cid, license, team_id, role)
        team.add_coach(coach)

    print("\n-- Add 15 Players --")
    for i in range(1, 16):
        print(f"\nPlayer #{i}")
        pid = input("Person ID: ")
        fname = input("First Name: ")
        lname = input("Last Name: ")
        dob = input_date("Date of Birth")
        nat = input("Nationality: ")
        plid = input("Player ID: ")
        jersey = int(input("Jersey Number: "))
        value = float(input("Market Value: "))
        pos = input("Position: ")
        status = input("Status (Active/Injured): ")
        player = Player(pid, fname, lname, dob, nat, plid, jersey, value, team_id, pos, status)
        team.add_player(player)

    print("\n=== DATA RINGKASAN ===")
    club.display_info()

if __name__ == "__main__":
    main()
