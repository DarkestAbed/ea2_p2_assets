# db/initialize.py

from db.setup import main as db_setup
from db.load_initial_data import main as db_load_data


def main():
    db_setup()
    db_load_data()
    return None


if __name__ == "__main__":
    main()
else:
    pass
