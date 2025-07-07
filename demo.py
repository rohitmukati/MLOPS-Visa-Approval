from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
import os 

url = MONGODB_URL_KEY
if url is None:
    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")

print(f"MongoDB URL: {url}")