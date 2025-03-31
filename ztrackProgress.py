from datetime import datetime
import time, os


def trackProgress():
    """Tracks progress and stores it in a local text file."""
    scriptdir = os.path.dirname(os.path.abspath(__file__))
    #print(scriptDir) # for testing
    filename = os.path.join(scriptdir, "trackProgress.txt")
    
    #create the file if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Progress Tracking Over Time - Statistics\n")
        
    #prompt user for today's progress
    print("\n📝 What exercise(s) did you complete today?")
    progress_entry = input(">>> ").strip()

    #capture timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a", encoding="utf-8") as file:
        file.write("\n" + "="*40 + "\n")
        file.write(f"Date: {timestamp}\n")
        file.write(f"Completed: {progress_entry}\n")

    print("✅ Progress logged successfully!")

if __name__ == "__main__":
    trackProgress()

