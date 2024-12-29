from load_data import load_data

all_data = load_data()

print("Welcome, this is a ship tracking application.")
print("Here, you can view information about various ships, including their names, countries, and current statuses.")
print("Type 'help' to show all commands or 'exit' to quit the program")

def help():
    print("Available commands:")
    print()
    print("help - Displays this help message")
    print("show_countries - Displays a list of all the countries of the ships")
    print("top_countries - Displays the top countries with the most ships")
    print("exit - Exits the program")

def show_countries():
    unique_countries = set()
    for ship in all_data["data"]:
        country = ship["COUNTRY"]
        unique_countries.add(country)

    sorted_countries = sorted(unique_countries)
    for country in sorted_countries:
        print(country)

def top_countries():
    country_count = {}
    for ship in all_data["data"]:
        country = ship["COUNTRY"]
        if country in country_count:
            country_count[country] += 1
        else:
            country_count[country]  = 1

    sorted_countries = sorted(country_count.items(), key=lambda item: item[1], reverse=True)

    for country, count in sorted_countries[:5]:
        print(f"{country}: {count} ships")

def main():
    while True:

        user_command = input("Which command do you want to use?")
        if user_command == "help":
            help()
        elif user_command == "show_countries":
            show_countries()
        elif user_command == "top_countries":
            top_countries()
        elif user_command == "exit":
            break
        print("Unknown command. Type 'help' for a list of commands.")


if __name__ == "__main__":
    main()
