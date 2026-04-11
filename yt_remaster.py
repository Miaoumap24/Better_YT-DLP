import os
import subprocess
import sys

def check_updates():
    print("--- Checking for Updates ---")
    try:
        subprocess.run(["yt-dlp", "-U"], check=False)
        print("yt-dlp is up to date.")
    except Exception as e:
        print(f"Update check failed: {e}")

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
        custom_fmt = input("Enter custom format (e.g., 137+140): ")
        cmd.extend(["-f", custom_fmt])
    else:
        print("Invalid selection.")
        return

    output_template = os.path.join(os.getcwd(), "%(title)s.%(ext)s")
    cmd.extend(["-o", output_template, url])

    print(f"\nDownloading to: {os.getcwd()}")
    subprocess.run(cmd)

def main():
    print("=== YT-DLP REMASTERED ===\n")
    check_updates()
    
    url = input("\nPaste the URL here: ")
    print("\nSelect Download Option:")
    print("1. Best Audio (MP3)")
    print("2. Best Video (Merged)")
    print("3. Custom Format")
    
    choice = input("\nChoice (1-3): ")
    download_video(url, choice)
    
    input("\nTask complete. Press Enter to exit...")

if __name__ == "__main__":
    main()