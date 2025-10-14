import os
import shutil
import sqlite3
from datetime import datetime, timezone
import sys
import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
from urllib.parse import urlparse


listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 170)



def speek(str):
     a = pyttsx3.init()
     a.say(str)
     a.runAndWait()
     return 
# Domain to track
TRACK_DOMAIN = "youtube.com"

def chrome_history_path():
    home = os.path.expanduser("~")
    if sys.platform.startswith("win"):
        local = os.environ.get("LOCALAPPDATA") or os.path.join(home, "AppData", "Local")
        return os.path.join(local, "Google", "Chrome", "User Data", "Default", "History")
    elif sys.platform == "darwin":
        return os.path.join(home, "Library", "Application Support", "Google", "Chrome", "Default", "History")
    else:
        return os.path.join(home, ".config", "google-chrome", "Default", "History")

def copy_history_db(src_path):
    tmp = src_path + ".copy"
    shutil.copy2(src_path, tmp)
    return tmp

def chrome_time_to_epoch(microseconds_since_1601):
    if microseconds_since_1601 == 0:
        return None
    return microseconds_since_1601 / 1_000_000.0 - 11644473600.0

def count_today_visits(db_path, domain):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = """
        SELECT v.visit_time
        FROM urls u JOIN visits v ON u.id = v.url
        WHERE u.url LIKE ?
    """
    cur.execute(sql, (f"%{domain}%",))
    rows = cur.fetchall()
    conn.close()

    today = datetime.now().date()
    count = 0
    for (visit_time,) in rows:
        epoch = chrome_time_to_epoch(visit_time)
        if epoch:
            visit_date = datetime.fromtimestamp(epoch).date()
            if visit_date == today:
                count += 1
    return count

def main(line):
    src = chrome_history_path()
    if not os.path.exists(src):
        print("Chrome History DB not found. Adjust the path if needed.")
        return

    tmp = copy_history_db(src)
    try:
        count = count_today_visits(tmp, line)
        print(f"{line} visits today: {count}")
        if (count > 3) :
            speek(f"Your are running out of limit in {line}. Stop")
    finally:
        os.remove(tmp)
  
def chrome_history_path():
    home = os.path.expanduser("~")
    return os.path.join(home, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "History")

def copy_history(src):
    import shutil
    tmp = src + ".copy"
    shutil.copy2(src, tmp)
    return tmp

def get_recent_tabs(limit=20):
    path = chrome_history_path()
    tmp = copy_history(path)
    conn = sqlite3.connect(tmp)
    cur = conn.cursor()
    
    # get last N visited URLs
    cur.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT ?", (limit,))
    rows = cur.fetchall()
    conn.close()
    
    tabs = []
    for url, title, visit_time in rows:
        if url.startswith("http"):
            domain = urlparse(url).netloc
            tabs.append((domain, url))
    return tabs
      

def chromeChecker():
    
    tabs = get_recent_tabs(10)
    print(f"Number of recent tabs (approx): {len(tabs)}")
    for d, url in tabs:
        print(f"{d} -> {url}")

    # with open("Brain/WebSite_Tracker/websiteInfo.txt") as file:
    #     for line in file :
    #         line = line.strip()
    #         line = line.lower()
    #         main(line)

chromeChecker()