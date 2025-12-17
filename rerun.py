import requests

def resume_download(url, destination, resume_byte_pos=0):
    headers = {"Range": f"bytes={resume_byte_pos}-"}
    response = requests.get(url, headers=headers, stream=True)
    with open(destination, "ab") as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    print(f"Download resumed and completed: {destination}")

def pause_downlaod(url, destinantion, pause_byte_pos):
    headers = {"Range": f"bytes={pause_byte_pos}-"}

# Example usage
# url = "https://example.com/file.zip"
# destination = "./file.zip"
# resume_download(url, destination, 1024 * 1024)  # Resume from 1MB
