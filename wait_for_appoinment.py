import requests
import time
import os  # For macOS sound signal

URL = "https://z-lode.vot.by/getTicketsByWorker?workerId=2076&lastData=2025-05-21T23:59:59.999Z"
POLL_INTERVAL = 10  # Time in seconds between each poll

def play_sound():
	"""Plays a sound signal."""
	os.system('say "Doctor Mistukevich appointment available!"')

def play_error_sound():
		"""Plays a sound signal for errors."""
		os.system('say "Error occurred while polling!"')

def poll_url():
	"""Polls the URL and checks if the returned data is not an empty JSON array."""
	while True:
		try:
			response = requests.get(URL, timeout=10)
			response.raise_for_status()
			data = response.json()
			dataFiltered = [item for item in data if item.get('date') > '2025-04-07']
			
			if dataFiltered != []:
				print("Data found:", dataFiltered)
				play_sound()
			else:
				print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - No appropriate data found: {data}. Retrying...")
		except requests.RequestException as e:
			print(f"Error while polling URL: {e}")
			play_error_sound()
		
		time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
	poll_url()