import requests
import schedule
import time

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is online.")
        else:
            print(f"{url} is offline. Status code: {response.status_code}")
    except requests.ConnectionError:
        print(f"Could not connect to {url}. It might be offline.")

# Replace 'https://example.com' with the URL you want to check
website_url = 'https://live.mzoneweb.net/web/'

# Schedule the job to run every 5 minutes (you can adjust the schedule as needed)
schedule.every(10).seconds.do(check_website, website_url)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
