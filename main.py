from superhero import Superhero, FlyingSuperhero

def main():
    # Create a regular superhero
    spidey = Superhero("Spider-Man", "web-slinging")
    spidey.reveal_identity()
    spidey.get_status()
    spidey.use_power()
    spidey.get_status()
    spidey.rest()
    spidey.get_status()

    print("\n" + "="*40 + "\n")

    # Create a flying superhero
    superman = FlyingSuperhero("Superman", "super strength", flight_speed=500)
    superman.reveal_identity()
    superman.get_status()
    superman.use_power()
    superman.get_status()
    superman.soar()
    superman.rest()
    superman.get_status()

if __name__ == "__main__":
    main()