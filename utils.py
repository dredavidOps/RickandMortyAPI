# mycli/cli.py
import requests
import csv

def get_character_info(character_id):
    api_url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        character_data = response.json()
        return character_data
    else:
        print(f"Error: Unable to fetch character information for ID {character_id}. Status code: {response.status_code}")
        return None

def save_to_csv(character_info_list, filename):
    keys = character_info_list[0].keys()

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(character_info_list)

def main():
    # Example: Fetch information for characters with IDs 1 to 5
    start_character_id = 1
    end_character_id = 5

    character_info_list = []

    for character_id in range(start_character_id, end_character_id + 1):
        character_info = get_character_info(character_id)
        if character_info:
            character_info_list.append(character_info)

    # Display information for all characters
    print("Character Information:")
    for character_info in character_info_list:
        print(f"Name: {character_info['name']}")
        print(f"Location: {character_info['location']}")
        print(f"Episode: {character_info['episode']}")

    # Save all characters' information to CSV
    csv_filename = 'all_characters_info.csv'
    save_to_csv(character_info_list, csv_filename)
    print(f"All characters' information saved to {csv_filename}")

if __name__ == "__main__":
    main()