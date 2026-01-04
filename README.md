# Basic Network Sniffer 🕵️‍♂️


**Domain:** Network Security  

This tool is a Python script that captures network packets in real-time. It acts like a digital "listener," analyzing data flowing through your computer to show you where traffic is coming from and where it is going.

It is built to help understand the basics of how data moves across a network (IP addresses, Ports, and Protocols).

## 🚀 Features

* **Real-Time Monitoring:** Watches network traffic as it happens.
* **Protocol Identification:** Automatically detects if a packet is **TCP** (Web/File transfer), **UDP** (Streaming/Gaming), or **ICMP** (Ping).
* **Color-Coded Output:**
    * 🔴 **TCP:** Red
    * 🔵 **UDP:** Blue
    * 🟢 **ICMP:** Green
* **Deep Inspection:** Shows Source IP, Destination IP, Ports, and a snippet of the data payload.

## 🛠️ Requirements

* **Python 3.x** installed on your system.
* **Scapy:** A powerful Python library for packet manipulation.
* **Colorama:** A library to make the terminal output colorful.

## 📦 How to Install

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/rajkumar3887/Prodigy_CS_05.git

    
    ```

2.  **Install Dependencies:**
    Open your terminal and run:
    ```bash
    pip install scapy colorama
    ```

## ▶️ How to Run

**Note:** Network sniffing requires high-level permissions (Administrator or Root) because it accesses the network card directly.

### 🪟 On Windows:
1.  Open Command Prompt or PowerShell as **Administrator**.
2.  Run the command:
    ```bash
    python network_sniffer.py
    ```

### 🐧 On Linux / Mac:
1.  Open your terminal.
2.  Run with `sudo`:
    ```bash
    sudo python3 network_sniffer.py
    ```

## ⚠️ Ethical Disclaimer

This tool is created for **educational purposes only**. It is intended to help learn about network traffic analysis and cybersecurity.

* **Do not** use this tool on networks where you do not have permission.
* **Do not** use this tool to intercept sensitive data of others.






