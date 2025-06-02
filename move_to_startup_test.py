import json
import os
from shutil import move

def main():
    with open("config_copy.json", 'r', encoding='utf-8') as f:
        config = json.load(f)
        if config["firstRun"]:
            config["firstRun"] = False
            if input("Would you like to run the program at boot? (Y/N): ").lower() == "y":
                config["wantsToBeInstalled"] = True
                path = os.getcwd()
                modified_path = os.path.join(path, "battery_notifs.py")
                config["pathName"] = modified_path
            else:
                config["wantsToBeInstalled"] = False

    with open("config_copy.json", 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)

    if config["wantsToBeInstalled"]:
        create_bat()

def create_bat():
    bat_path = "autorun_battery_notifs.bat"

    with open(bat_path, "w") as batch_file:
        with open("config_copy.json", 'r', encoding='utf-8') as f:
            config = json.load(f)
            script_path = config["pathName"]

            batch_file.write(
                "@echo off\n"
                f"cd /d {os.path.dirname(script_path)}\n"
                f"pythonw {os.path.basename(script_path)}\n"
            )

    print(f"[INFO] Batch file created at {os.path.abspath(bat_path)}")

def move_to_startup_folder():
    ...


if __name__ == "__main__":
    main()