import os
import json
import re
from pathlib import Path

CRED_PATH = Path(__file__).parent / ".alphazero_user"


def normalize_team_name(team_name):
    """
    Convert team name to lowercase and remove spaces/special characters
    Examples: "The Monkeys" -> "themonkeys", "Team Alpha-1" -> "teamalpha1"
    """
    if not team_name:
        return ""
    # Convert to lowercase and keep only alphanumeric characters
    normalized = re.sub(r'[^a-zA-Z0-9]', '', team_name.lower())
    return normalized


def prompt_for_alias(old_alias=None):
    if old_alias:
        print(f"Your last alias was '{old_alias}'.")
        use_old = input("Would you like to use this alias again? (y/n): ").strip().lower()
        if use_old == 'y':
            print(f"Continuing as {old_alias}.")
            return old_alias
    # Else
    alias = input("Enter a new alias (username): ").strip()
    while not alias:
        alias = input("Alias cannot be empty. Please enter a new alias: ").strip()
    return alias


def prompt_for_team(old_team_id=None):
    if old_team_id:
        print(f"Your last team was '{old_team_id}'.")
        use_old = input("Would you like to stay with this team? (y/n): ").strip().lower()
        if use_old == 'y':
            print(f"Staying with team {old_team_id}.")
            return old_team_id
    # Else
    team_name = input("Enter your team name (e.g., 'The Monkeys'): ").strip()
    while not team_name:
        team_name = input("Team name cannot be empty. Please enter your team name: ").strip()
    
    # Normalize the team name
    normalized_team = normalize_team_name(team_name)
    print(f"Team name '{team_name}' will be saved as '{normalized_team}'.")
    return normalized_team


def main():
    old_alias = None
    old_team_id = None
    
    # Load existing data
    if CRED_PATH.exists():
        try:
            with CRED_PATH.open("r") as f:
                data = json.load(f)
                old_alias = data.get("alias")
                old_team_id = data.get("team_id")
        except Exception:
            old_alias = None
            old_team_id = None

    # Step 1: Get alias
    alias = prompt_for_alias(old_alias)
    
    # Step 2: Get team name
    team_id = prompt_for_team(old_team_id)

    # Always overwrite file with current alias and team_id
    with CRED_PATH.open("w") as f:
        json.dump({"alias": alias, "team_id": team_id}, f)

    print(alias)  # print the chosen alias (for shell/parent backward compatibility)

if __name__ == "__main__":
    main()
