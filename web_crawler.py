import threading
import time
import csv
import requests
from bs4 import BeautifulSoup
from queue import Queue
from tqdm import tqdm

# Configuration des paramètres
NUM_THREADS = int(input("Entrez le nombre de threads : "))
MAX_URLS = int(input("Entrez le nombre de url a visité : "))
DELAY = 1
url_queue = Queue()
visited_urls = set()
initial_urls = [
    'https://www.wikipedia.org',
    'https://www.reddit.com',
    'https://www.bbc.com',
    'https://www.cnn.com',
    'https://www.github.com',
    'https://www.stackoverflow.com',
    'https://www.medium.com',
    'https://www.quora.com',
    'https://www.nytimes.com',
    'https://www.theguardian.com'
]

output_file = 'crawl_results.csv'

# Verrous pour protéger l'accès aux ressources partagées
csv_lock = threading.Lock()
visited_urls_lock = threading.Lock()

def crawl(url, pbar):
    try:
        print(f"Début du traitement pour {url}")  # Message avant le traitement
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No title'

        # Écriture sécurisée dans le fichier CSV
        with csv_lock:
            with open(output_file, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([url, title])
        print(f'Titre de {url}: {title}')

        # Mise à jour sécurisée de la liste des URLs visitées
        with visited_urls_lock:
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('http') and href not in visited_urls and len(visited_urls) < MAX_URLS:
                    visited_urls.add(href)
                    url_queue.put(href)

        pbar.update(1)

        print(f"Traitement terminé pour {url}")  # Message après le traitement

    except requests.RequestException as e:
        print(f'Erreur lors du crawling de {url}: {e}')

def worker(pbar):
    while True:
        url = url_queue.get()
        if url is None:
            break
        crawl(url, pbar)
        time.sleep(DELAY)
        url_queue.task_done()

def main():
    start_time = time.time()

    # Initialisation du fichier CSV
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Title'])

    with tqdm(total=MAX_URLS, desc="Progression du crawling") as pbar:
        threads = []
        for _ in range(NUM_THREADS):
            t = threading.Thread(target=worker, args=(pbar,))
            t.start()
            threads.append(t)

        for url in initial_urls:
            url_queue.put(url)
            visited_urls.add(url)

        url_queue.join()

        for _ in range(NUM_THREADS):
            url_queue.put(None)
        for t in threads:
            t.join()

    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes, seconds = divmod(elapsed_time, 60)
    print(f"Temps d'exécution total : {int(minutes)} minutes et {seconds:.2f} secondes")

if __name__ == "__main__":
	main()
