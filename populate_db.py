# # populate_db.py
# import os
# import django
# import time
# from datetime import datetime

# # הגדרת משתנה סביבה עבור הגדרות Django (אם לא מוגדר)
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maxBreak.settings')
# django.setup()

# from oneFourSeven.scraper import get_ranking, get_season_events, get_players_m,get_players_w,get_a_players_m, get_upcoming_matches

# # הגדרת מגבלת קצב (10 בקשות בדקה)
# REQUESTS_PER_MINUTE = 10
# SECONDS_PER_MINUTE = 60
# DELAY_BETWEEN_REQUESTS = SECONDS_PER_MINUTE / REQUESTS_PER_MINUTE

# last_request_time = None

# def make_api_request(api_function, *args, **kwargs):
#     global last_request_time
#     now = datetime.now()

#     if last_request_time:
#         time_since_last_request = (now - last_request_time).total_seconds()
#         if time_since_last_request < DELAY_BETWEEN_REQUESTS:
#             sleep_time = DELAY_BETWEEN_REQUESTS - time_since_last_request
#             print(f"Waiting for {sleep_time:.2f} seconds to respect API rate limit.")
#             time.sleep(sleep_time)

#     last_request_time = now
#     return api_function(*args, **kwargs)

# if __name__ == "__main__":
#     print("Populating database...")

#     # Fetch and save season events
#     print("Fetching and saving season events...")
#     make_api_request(get_season_events)

#     # Fetch and save men players
#     print("Fetching and saving men players...")
#     make_api_request(get_players_m)

#     # Fetch and save women players
#     print("Fetching and saving women players...")
#     make_api_request(get_players_w)

#     # Fetch and save amateur players
#     print("Fetching and saving women players...")
#     make_api_request(get_a_players_m)

#     # Fetch and save rankings
#     print("Fetching and saving rankings...")
#     make_api_request(get_ranking)

#     # Fetch and save upcoming matches
#     print("Fetching and saving upcoming matches...")
#     make_api_request(get_upcoming_matches)

#     print("Database population finished.")


import os
import django
import time
from datetime import datetime
import logging

# הגדרת משתנה סביבה עבור הגדרות Django (אם לא מוגדר)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maxBreak.settings')
django.setup()

from oneFourSeven.scraper import get_ranking, get_season_events, get_players_m, get_players_w, get_a_players_m, get_upcoming_matches, matches_of_an_event

# הגדרת לוגינג
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# הגדרת מגבלת קצב (10 בקשות בדקה)
REQUESTS_PER_MINUTE = 10
SECONDS_PER_MINUTE = 60
DELAY_BETWEEN_REQUESTS = SECONDS_PER_MINUTE / REQUESTS_PER_MINUTE

last_request_time = None

def make_api_request(api_function, *args, **kwargs):
    global last_request_time
    now = datetime.now()

    if last_request_time:
        time_since_last_request = (now - last_request_time).total_seconds()
        if time_since_last_request < DELAY_BETWEEN_REQUESTS:
            sleep_time = DELAY_BETWEEN_REQUESTS - time_since_last_request
            logging.info(f"Waiting for {sleep_time:.2f} seconds to respect API rate limit.")
            time.sleep(sleep_time)

    last_request_time = now
    try:
        return api_function(*args, **kwargs)
    except Exception as e:
        logging.error(f"Error calling {api_function.__name__}: {e}")
        return None

def selective_update():
    # logging.info("Performing selective update...")

    # # Fetch and save season events (selective update)
    # logging.info("Fetching and saving season events (selective update)...")
    # make_api_request(get_season_events)

    # # Fetch and save rankings (selective update)
    # logging.info("Fetching and saving rankings (selective update)...")
    # make_api_request(get_ranking)

    # # Fetch and save upcoming matches (selective update)
    # logging.info("Fetching and saving upcoming matches (selective update)...")
    # make_api_request(get_upcoming_matches)

    logging.info("Fetching and saving active tour matches (selective update)...")
    make_api_request(matches_of_an_event)

    logging.info("Selective update finished.")

def full_update():
    logging.info("Performing full update...")

    # Fetch and save players (full update)
    logging.info("Fetching and saving players (full update)...")
    make_api_request(get_players_m)
    make_api_request(get_players_w)
    make_api_request(get_a_players_m)

    logging.info("Full update finished.")

if __name__ == "__main__":
    logging.info("Starting database update...")

    # Perform selective update (every hour)
    selective_update()

    # Perform full update (every day)
    now = datetime.now()
    if now.hour == 0:  # Perform full update at midnight
        full_update()

    logging.info("Database update finished.")