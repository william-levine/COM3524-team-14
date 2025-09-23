# COM 3524 – System Tools

This repository contains the source code and documentation for the system tools developed for the COM3524 course. 

## Features

- Cross-platform support (Linux, macOS, Windows)
- Modular, extensible design for course assignments

---
## 🔧 Prerequisites
Before starting, ensure the following softwares and tools are installed on your machine:

- [Python 3.8+](https://www.python.org/downloads/)
- `pip` (Python package manager for installing necessary dependencies)
- Git (to clone this repository)


###  Docker Desktop
Download and install Docker Desktop:  
👉 [https://www.docker.com/products/docker-desktop/]

###  X11 Server
| Platform | Tool     | Link                                      |
|----------|----------|-------------------------------------------|
| Windows  | VcXsrv   | [VcXsrv Download](https://sourceforge.net/projects/vcxsrv/) |
| macOS    | XQuartz  | [XQuartz Download](https://www.xquartz.org/) |
| Linux    | Built-in | Usually pre-installed with the system     |

---

---

## Installation

### 1. Clone the Repository
Clone this repository and navigate to the COM3524 folder:

```bash
git clone https://github.com/ac1asana/COM3524.git
cd COM3524
```
---

## Platform-Specific Notes
---

## Windows Instructions

### 1. **Install Required Software**
- Install Docker Desktop and VcXsrv as mentioned [above](#Prerequisites)

### 2. **Run Docker and X Server in the background **
After installing VcXsrv software, run the server (Xlaunch)
Set the default display settings as follow:
  - Multiple windows mode
  - Start no client
  - **Disable access control**
 
 
<p align="center">
  <img src="https://github.com/user-attachments/assets/aaef6bd4-151b-4dfa-b957-66b3f91aa650" width="45%" />
  <img src="https://github.com/user-attachments/assets/c83ba456-e844-4454-ae72-5dc283f863fc" width="45%" />
</p>


<img width="612" height="480" alt="image" src="https://github.com/user-attachments/assets/157322a4-18c8-460b-b2b7-773d6bc17a61" /> <br /> 
- Once the configuration is completed, a small X symbol would appear on the bottom right panel of your screen as follow:
  <img width="467" height="192" alt="image" src="https://github.com/user-attachments/assets/c56ef8b4-db6e-419e-8f5b-02251e338761" /> <br /> 

- This confirms that the X server is running in the background.

### 3. **Run the script**
Once you have made sure that the previous steps are done, you are ready to run the script:

```bash
.\windows.bat
```

>[!NOTE]
>Make sure that docker is running in the background 

## Linux (Ubuntu) Instructions

>[!NOTE]
>No additional configuration is typically required. Make sure you have Python and `pip` installed:
>run the command `python3 --version` or `pip --version` to check whether it is installed on your system

### 1. **Install Docker**

Follow Docker’s official guide:  
👉 [https://docs.docker.com/engine/install/ubuntu](https://docs.docker.com/engine/install/ubuntu)

### 2. **Set Up Repository and Test Docker**
```bash
sudo docker run hello-world
```

### 3. **Fix Permission Denied Errors (Optional)**  
If you encounter permission errors:  
[Fix Docker Permission Denied](https://hostinger.com/tutorials/how-to-fix-docker-permission-denied-error)

### 4. **Run the following script**
```bash
./mac.sh 
```
---

## MacOS

Ensure Python 3 is installed (macOS may come with Python 2.x by default):

```bash
brew install python
```

### 1. **Use the Zsh Shell**
Check with:
```bash
echo $SHELL
```
Switch to `zsh` if needed:
```bash
chsh -s /bin/zsh
```

### 2. **Deactivate Conda (if active)**
```bash
conda deactivate
```

### 3. **Install and Launch XQuartz**
- Install from: [https://www.xquartz.org/](https://www.xquartz.org/)
- After installing, **restart your computer**
- Launch XQuartz and enable network connections:
  - Settings → Security → Check **"Allow connections from network clients"**


### 4. **Run the following script**
```bash
./mac.sh 
```
---

---

## ❗ Troubleshooting

- **GUI doesn't appear?**
  - Ensure X server is running
  - Check that `DISPLAY` is correctly set

- **Permission denied**
  - Ensure user is added to Docker group, or run using `sudo`

---

=======
## Usage

After installation, run the main program with:

```bash
python main.py
```

This will display a menu or command-line interface for interacting with the available system tools.

---

## Troubleshooting

- Ensure you’re using **Python 3.8 or higher**.
- For permission errors on Linux/macOS, try using `sudo` if needed.
- On Windows, run the command prompt or PowerShell as Administrator if access is denied.

---
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
---

## Author
Ayesha Sana, Department of Computer Science  
