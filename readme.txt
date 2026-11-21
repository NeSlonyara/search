Connect:
Discord: msr.penis
TG: ne_slonyara

Search Script User Guide


Description

This script allows you to perform various information search operations, such as global data searches, searches across specific domains and websites, as well as configuring search settings.

Installation

1. Create an executable script search.sh:sh
nano search.sh

2. Add the following code to the file:bash
#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <option>"
    echo "Options: search 1 | search 2 | search 3"
    exit 1
fi

python3 /path/to/search.py search "$1"

Replace /path/to/search.py with the actual path to your search.py script.
3. Make the script executable:sh
chmod +x search.sh

4. Move the script to a directory accessible from the command line:sh
sudo mv search.sh /usr/local/bin/search


Usage

The script can be run from the command line with one of the following parameters:
• 1 — to search for data globally.
• 2 — to search for data across specific domains and websites.
• 3 — to configure search settings.
Usage examples:
sh
search 1
search 2
search 3


Autostart (Optional)

If you want your script to start automatically when the system boots, you can configure it for autostart.

On Linux

1. Create a service file for your command:sh
sudo nano /etc/systemd/system/search.service

2. Add the following content to the file:ini
[Unit]
Description=Search Script
After=network.target

[Service]
Type=simple
User=your_username
ExecStart=/usr/local/bin/search 1

[Install]
WantedBy=multi-user.target

Replace your_username with your username and /usr/local/bin/search with the actual path to your script.
3. Reload the daemon and start the service:sh
sudo systemctl daemon-reload
sudo systemctl enable search.service
sudo systemctl start search.service


On macOS

On macOS, you can use launchd to automatically run the script at system startup.
1. Create a plist file:
Create a com.example.search.plist file in the ~/Library/LaunchAgents/ directory:sh
nano ~/Library/LaunchAgents/com.example.search.plist

2. Add the following content to the file:xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://apple.com">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.example.search</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/search</string>
        <string>1</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
Используйте код с осторожностью.
3. Load and start the plist file:sh
launchctl load ~/Library/LaunchAgents/com.example.search.plist
launchctl start com.example.search
