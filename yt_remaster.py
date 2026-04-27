import os
import subprocess
from urllib.parse import urlparse

def get_resource_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return filename

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def check_updates():
    # Ajout de -q pour masquer les logs lors de la mise à jour
    subprocess.run(["yt-dlp", "-U", "-q"], check=False)

def download_video(url, choice):
    formats = {
        "1": "bestaudio/best",
        "2": "bestvideo+bestaudio/best",
    }

    cmd = ["yt-dlp"]
    
    if choice == "1":
        cmd.extend(["-f", formats["1"], "--extract-audio", "--audio-format", "mp3"])
    elif choice == "2":
        cmd.extend(["-f", formats["2"]])
    elif choice == "3":
        custom_fmt = input("Enter custom format : ")
        cmd.extend(["-f", custom_fmt])
    else:
        print("Invalid selection.")
        return

    output_template = os.path.join(os.getcwd(), "%(title)s.%(ext)s")
    # Ajout de --progress et -q pour n'afficher que la barre de progression
    cmd.extend(["-o", output_template, "--progress", "-q", url])

    print(f"\nDownloading to: {os.getcwd()}")
    subprocess.run(cmd)

def main():
    print("=== BETTER YT DLP ===\n")
    check_updates()
    
    while True:
        url = input("\nPaste the URL here: ")
        
        if not is_valid_url(url):
            print("Invalid URL")
            continue
            
        print("\nSelect Download Option:")
        print("1. Best Audio")
        print("2. Best Video")
        print("3. Custom Format")
        
        choice = input("\nChoice (1-3): ")
        download_video(url, choice)
        
        again = input("\nDo you want to download another video? (y/n): ").lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()