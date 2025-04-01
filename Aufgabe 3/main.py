from my_functions import build_person, build_experiment

def main():
    first_name = input("Vorname: ")
    last_name = input("Nachname: ")
    sex = input("Geschlecht (male/female): ").lower()
    age = int(input("Alter: "))

    person = build_person(first_name, last_name, sex, age)

    experiment_name = input("Experiment-Name: ")
    date = input("Datum (DD-MM-YYYY): ")
    supervisor = input("Versuchsleiter: ")

    experiment = build_experiment(experiment_name, date, supervisor, person)

    print("\nVersuchsperson:", person)
    print("Experiment:", experiment)

if __name__ == "__main__":
    main()