from datetime import date
from abc import ABC, abstractmethod

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

    def train(self):
        pass

    def play_match(self):
        pass

class Coach(Person):
    def __init__(self, person_id, first_name, last_name, date_of_birth, nationality,
                 coach_id, license_level, team_id, role):
        super().__init__(person_id, first_name, last_name, date_of_birth, nationality)
        self.coach_id = coach_id
        self.license_level = license_level
        self.team_id = team_id
        self.role = role

    def conduct_training(self):
        pass

    def select_squad(self):
        pass

class Staff(Person):
    def __init__(self, person_id, first_name, last_name, date_of_birth, nationality,
                 staff_id, club_id, department, role):
        super().__init__(person_id, first_name, last_name, date_of_birth, nationality)
        self.staff_id = staff_id
        self.club_id = club_id
        self.department = department
        self.role = role

    def perform_duties(self):
        pass

class PersonFactory(ABC):
    @abstractmethod
    def create_person(self, *args, **kwargs):
        pass

class PlayerFactory(PersonFactory):
    def create_person(self, person_id, first_name, last_name, date_of_birth, nationality,
                      player_id, jersey_number, market_value, team_id, position, status):
        return Player(person_id, first_name, last_name, date_of_birth, nationality,
                      player_id, jersey_number, market_value, team_id, position, status)

class CoachFactory(PersonFactory):
    def create_person(self, person_id, first_name, last_name, date_of_birth, nationality,
                      coach_id, license_level, team_id, role):
        return Coach(person_id, first_name, last_name, date_of_birth, nationality,
                     coach_id, license_level, team_id, role)

class StaffFactory(PersonFactory):
    def create_person(self, person_id, first_name, last_name, date_of_birth, nationality,
                      staff_id, club_id, department, role):
        return Staff(person_id, first_name, last_name, date_of_birth, nationality,
                     staff_id, club_id, department, role)

class Team:
    def __init__(self, team_id, league, division, club_id, name):
        self.team_id = team_id
        self.league = league
        self.division = division
        self.club_id = club_id
        self.name = name
        self.players = []
        self.coaches = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def schedule_training(self, session):
        pass

class Club:
    def __init__(self, club_id, name, founding_date, budget, league, stadium_id):
        self.club_id = club_id
        self.name = name
        self.founding_date = founding_date
        self.budget = budget
        self.league = league
        self.stadium_id = stadium_id
        self.teams = []
        self.staff = []
        self.sponsors = []
        self.contracts = []

    def manage_budget(self):
        pass

    def sign_sponsor(self, sponsor):
        self.sponsors.append(sponsor)

    def get_teams(self):
        return self.teams

class Sponsor:
    def __init__(self, sponsor_id, name, contact_person, phone, email, contract_value,
                 contract_start_date, contract_end_date):
        self.sponsor_id = sponsor_id
        self.name = name
        self.contact_person = contact_person
        self.phone = phone
        self.email = email
        self.contract_value = contract_value
        self.contract_start_date = contract_start_date
        self.contract_end_date = contract_end_date

    def renew_contract(self, new_date, new_value):
        self.contract_start_date = date.today()
        self.contract_end_date = new_date
        self.contract_value = new_value

class TrainingSession:
    def __init__(self, session_id, session_date, session_time, location, focus_area, team_id):
        self.session_id = session_id
        self.session_date = session_date
        self.session_time = session_time
        self.location = location
        self.focus_area = focus_area
        self.team_id = team_id

    def record_attendance(self, player, present):
        pass

class Match:
    def __init__(self, match_id, match_date, match_time, home_score, away_score,
                 competition, home_team_id, away_team_id, stadium_id, season_id):
        self.match_id = match_id
        self.match_date = match_date
        self.match_time = match_time
        self.home_score = home_score
        self.away_score = away_score
        self.competition = competition
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        self.stadium_id = stadium_id
        self.season_id = season_id

    def record_score(self, home, away):
        self.home_score = home
        self.away_score = away

    def generate_report(self):
        return {
            "home_score": self.home_score,
            "away_score": self.away_score
        }

class Season:
    def __init__(self, season_id, year, league, start_date, end_date):
        self.season_id = season_id
        self.year = year
        self.league = league
        self.start_date = start_date
        self.end_date = end_date
        self.matches = []

    def get_matches(self):
        return self.matches

    def get_standings(self):
        return {}

class Stadium:
    def __init__(self, stadium_id, name, league, capacity, address):
        self.stadium_id = stadium_id
        self.name = name
        self.league = league
        self.capacity = capacity
        self.address = address

    def host_match(self, match):
        pass

class Contract:
    def __init__(self, contract_id, start_date, end_date, salary, clauses, club_id, person_id):
        self.contract_id = contract_id
        self.start_date = start_date
        self.end_date = end_date
        self.salary = salary
        self.clauses = clauses
        self.club_id = club_id
        self.person_id = person_id

    def renew(self):
        pass

    def terminate(self):
        pass

def input_players(team):
    factory = PlayerFactory()
    num = int(input("Berapa banyak pemain yang ingin ditambahkan? "))
    for i in range(num):
        print(f"\nData pemain ke-{i+1}")
        pid = input("ID Person: ")
        fname = input("Nama Depan: ")
        lname = input("Nama Belakang: ")
        dob = input("Tanggal Lahir (YYYY-MM-DD): ")
        nationality = input("Kebangsaan: ")
        player_id = input("Player ID: ")
        jersey = int(input("Nomor Punggung: "))
        value = float(input("Nilai Pasar: "))
        position = input("Posisi: ")
        status = input("Status (Active/Inactive): ")

        birth_date = date.fromisoformat(dob)
        player = factory.create_person(pid, fname, lname, birth_date, nationality,
                                       player_id, jersey, value, team.team_id, position, status)
        team.add_player(player)
    print(f"\nTotal pemain dalam tim {team.name}: {len(team.players)}")
