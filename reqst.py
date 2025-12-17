import requests
import threading
import os

def download_file(url, destination):
    response = requests.get(url, stream=True)
    total_length = response.headers.get('content-length')

    if total_length is None:
        with open(destination, 'wb') as f:
            f.write(response.content)
    else:
        with open(destination, 'wb') as f:
            for data in response.iter_content(chunk_size=4096):
                f.write(data)
    print(f"Download completed: {destination}")

def download_multiple_files(urls, download_folder):
    threads = []
    for url in urls:
        file_name = os.path.join(download_folder, os.path.basename(url))
        thread = threading.Thread(target=download_file, args=(url, file_name))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()

# Example usage
# urls = ["https://example.com/file1.zip", "https://example.com/file2.zip"]
# download_folder = "./downloads"
# download_multiple_files(urls, download_folder)
