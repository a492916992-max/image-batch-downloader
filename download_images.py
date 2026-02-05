import os
import requests

def download_images(urls, save_dir="images"):
    os.makedirs(save_dir, exist_ok=True)

    for idx, url in enumerate(urls, start=1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            file_path = os.path.join(save_dir, f"image_{idx}.jpg")
            with open(file_path, "wb") as f:
                f.write(response.content)

            print(f"Downloaded: {file_path}")

        except Exception as e:
            print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    image_urls = [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg"
    ]

    download_images(image_urls)
