import requests
from tqdm import tqdm

def download_with_progress(url, destination):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('Content-Length', 0))
    with open(destination, 'wb') as file, tqdm(
        desc=destination,
        total=total_size,
        unit='B',
        unit_scale=True,
    ) as bar:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
                bar.update(len(chunk))

# Example usage
# url = "https://example.com/file.zip"
# destination = "./file.zip"
# download_with_progress(url, destination)
