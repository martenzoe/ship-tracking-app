import tkinter as tk
from tkinter import messagebox, simpledialog
from load_data import load_data

# Daten laden
all_data = load_data()


def show_help():
    messagebox.showinfo("Help", "Available commands:\n"
                                "1. Show Countries\n"
                                "2. Top Countries\n"
                                "3. Exit")


def show_countries():
    unique_countries = set()
    for ship in all_data["data"]:
        country = ship["COUNTRY"]
        unique_countries.add(country)

    sorted_countries = sorted(unique_countries)
    countries_text = "\n".join(sorted_countries)
    messagebox.showinfo("Countries", countries_text)


def top_countries():
    country_count = {}
    for ship in all_data["data"]:
        country = ship["COUNTRY"]
        if country in country_count:
            country_count[country] += 1
        else:
            country_count[country] = 1

    sorted_countries = sorted(country_count.items(), key=lambda item: item[1], reverse=True)

    # Eingabeaufforderung für die Anzahl der angezeigten Länder
    num_countries = simpledialog.askinteger("Input", "How many top countries would you like to see?", minvalue=1)

    if num_countries is None:
        return  # Der Benutzer hat das Dialogfeld abgebrochen

    top_countries_text = "\n".join([f"{country}: {count} ships" for country, count in sorted_countries[:num_countries]])
    messagebox.showinfo("Top Countries", top_countries_text)


# Hauptfenster erstellen
root = tk.Tk()
root.title("Ship Tracking Application")

# Buttons erstellen
help_button = tk.Button(root, text="Help", command=show_help)
help_button.pack(pady=10)

show_countries_button = tk.Button(root, text="Show Countries", command=show_countries)
show_countries_button.pack(pady=10)

top_countries_button = tk.Button(root, text="Top Countries", command=top_countries)
top_countries_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

# Hauptloop starten
root.mainloop()
