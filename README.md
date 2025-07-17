# COM 3524 – System Tools

This repository contains the source code and documentation for the system tools developed for the COM3524 course. 

This repository contains the source code and documentation for the system tools developed for the COM 3524 course. These tools are designed for educational purposes to demonstrate key system-level concepts.

## Features

- Cross-platform support (Linux, macOS, Windows)
- Modular, extensible design for course assignments

---

## Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- `pip` (Python package manager)
- Git (to clone this repository)
## 🔧 Prerequisites (All Platforms)

Before starting, ensure the following software is installed on your machine:

### ✅ Docker Desktop
Download and install Docker Desktop:  
👉 [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

### ✅ X11 Server
| Platform | Tool     | Link                                      |
|----------|----------|-------------------------------------------|
| Windows  | VcXsrv   | [VcXsrv Download](https://sourceforge.net/projects/vcxsrv/) |
| macOS    | XQuartz  | [XQuartz Download](https://www.xquartz.org/) |
| Linux    | Built-in | Usually pre-installed with the system     |

---

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ac1asana/COM3524.git
cd COM3524
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## Platform-Specific Notes
---


## 🪟 Windows Instructions

### 1. **Install Required Software**
- Install Docker Desktop
- Install [VcXsrv](https://sourceforge.net/projects/vcxsrv/)

### 2. **Run VcXsrv**
Launch VcXsrv with:
- Display number: `0` (NOT `-1`)
- Multiple windows mode
- Start no client
- **Disable access control**

### 3. **Build Docker Image**
```bash
docker build --no-cache -t com3524-toolkit .
```

### 4. **Run Docker Container**
```bash
docker run -it -p 5000:5000 -e DISPLAY=host.docker.internal:0 com3524-toolkit
=======
### 🔹 Linux

No additional configuration is typically required. Make sure you have Python and `pip` installed:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

Run the tools:

```bash
python3 main.py
```

### 🔸 macOS

Ensure Python 3 is installed (macOS may come with Python 2.x by default):

```bash
brew install python
```

Run the tools:

```bash
python3 main.py
```

### 🪟 Windows

Install Python from [python.org](https://www.python.org/downloads/windows/). During installation, make sure to check **“Add Python to PATH”**.

Run the tools in PowerShell or CMD:

```bash
python main.py
>>>>>>> 60cdb4571d8b158f2bb370d109c3156c7c2167b8
```

---

## 🐧 Linux (Ubuntu) Instructions

### 1. **Install Docker**

Follow Docker’s official guide:  
👉 [https://docs.docker.com/engine/install/ubuntu](https://docs.docker.com/engine/install/ubuntu)

### 2. **Set Up Repository and Test Docker**
```bash
sudo docker run hello-world
```

### 3. **Fix Permission Denied Errors (Optional)**  
If you encounter permission errors:  
👉 [Fix Docker Permission Denied](https://hosting.com/tutorials/how-to-fix-docker-permission-denied-error)

### 4. **Run Docker with X11 GUI Support**
```bash
xhost +local:docker  # Allow Docker to access display (run once)

docker run -it   -e DISPLAY=:0   -v /tmp/.X11-unix:/tmp/.X11-unix   com3524-toolkit
```

---

## 🍎 macOS Instructions

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
  - Preferences → Security → Check **"Allow connections from network clients"**

### 4. **Find Your IP Address**
```bash
ipconfig getifaddr en1
```
(Use `en0` if on Ethernet.)

### 5. **Allow Access to X Server**
```bash
xhost +YOUR_IP_ADDRESS
```

### 6. **Build Docker Image**
```bash
docker build -t com3524-toolkit .
```

### 7. **Run Docker Container**
Replace `192.168.1.64` with your actual IP:
```bash
docker run -it   -p 5000:5000   -e DISPLAY=192.168.1.64:0   com3524-toolkit
```

---

## 🐳 Docker Image Info

- Docker image name: `com3524-toolkit`
- Rebuild with:
```bash
docker build --no-cache -t com3524-toolkit .
```

---

## ❗ Troubleshooting

- **GUI doesn't appear?**
  - Ensure X server is running
  - Check that `DISPLAY` is correctly set
  - Verify you’ve run `xhost +` (or added the right IP)

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

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
>>>>>>> 60cdb4571d8b158f2bb370d109c3156c7c2167b8

---

## Author
Ayesha Sana– for COM3524, Department of Computer Science  
=======
Ayesha Sana – for COM3524, Department of Computer Science  
>>>>>>> 60cdb4571d8b158f2bb370d109c3156c7c2167b8
