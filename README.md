#  YT-DLP Remastered

An enhanced, standalone version of `yt-dlp` designed for speed and simplicity. This tool automates dependency updates and provides a clean interface for high-quality media downloads.

---

##  Features

* **Auto-Update:** Checks and updates `yt-dlp` and `ffmpeg` core every time you launch.
* **One-Click Presets:**
    1.  **Best Audio:** Automatically extracts and converts to high-quality MP3.
    2.  **Best Video:** Merges the highest available video and audio streams.
    3.  **Custom:** Enter your own `yt-dlp` format codes for full control.
* **Portable:** Everything is bundled into a single `.exe`. No Python or manual FFmpeg installation required for the end-user.
* **Auto-Routing:** Downloads are automatically saved in the same folder as the application.

---

##  Built With

* **Language:** Python 3.14
* **Core:** [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* **Processing:** [FFmpeg](https://ffmpeg.org/)
* **Compiler:** PyInstaller

---

##  How to Use (Pre-compiled Version)

1.  Go to the [Releases](https://github.com/Miaoumap24/Better_YT-DLP/releases) section.
2.  Download `BetterYTDLP_x.x.x.exe`.
3.  Run the file.
4.  Paste your URL, choose your format, and you're done!

---

##  For Developers (Running from Source)

If you want to run the script manually:

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/Miaoumap24/Better_YT-DLP.git](https://github.com/Miaoumap24/Better_YT-DLP.git)
    cd Better_YT-DLP
    ```

2.  **Install dependencies:**
    Make sure you have `yt-dlp.exe`, `ffmpeg.exe`, and `ffprobe.exe` in the root folder.

3.  **Run the script:**
    ```bash
    python yt_remaster.py
    ```

4.  **Build your own EXE:**
    ```bash
    pyinstaller --onefile --add-binary "yt-dlp.exe;." --add-binary "ffmpeg.exe;." --add-binary "ffprobe.exe;." yt_remaster.py
    ```

---

##  Author

**Lixiod Technologies** - *Engineered for the Common Good*  |  Yt-Dlp : https://github.com/yt-dlp/yt-dlp

---

##  License

Distributed under the MIT License. See `LICENSE` for more information.
