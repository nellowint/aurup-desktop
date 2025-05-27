# Aurup Desktop

[![License](https://img.shields.io/badge/license-GNU-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/platform-Arch%20Linux%20%26%20derivatives-lightgrey.svg)]()

A graphical application for Arch Linux users that simplifies searching and installing packages from the AUR (Arch User Repository).

![Aurup Desktop Screenshot](screenshot.png) 

## Features

🔍 **Search packages** - Find AUR packages quickly  
📦 **View details** - Check version, maintainer, and dependencies  
⚡ **Manage installations** - Clone, build, and install with ease  
🔄 **Update checking** - Get notified about available updates  

## Installation

### From AUR (Coming Soon)
```bash
yay -S aurup-desktop
```
### From Git
```
git clone https://github.com/yourusername/aurup-desktop.git
cd aurup-desktop
pip install -r requirements.txt
python main.py
```
### Technologies

- Backend: Python 3.13 and [Aurweb RPC Interface](https://aur.archlinux.org/rpc/swagger)
- Frontend: Flet Framework [More info](https://flet.dev/)
- Compatibility: Arch Linux, Manjaro, EndeavourOS, and other Arch-based distros

## Contributing
✨ Contributions are welcome! Please:

1) Fork the repository
2) Create a feature branch (git checkout -b feature/your-feature)
3) Commit your changes (git commit -am 'Add some feature')
4) Push to the branch (git push origin feature/your-feature)
5) Open a Pull Request

# License
This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the LICENSE file for details.
