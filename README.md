# Code_Aplha_Cyber_security_Projects-1
This project is a basic network sniffer built in Python, leveraging the Scapy library to capture and analyze network traffic. It captures packets on a specified network interface, extracting useful information such as source/destination IP, MAC addresses, port numbers, and even HTTP data when available.




Here's a `README.md` file to describe your network sniffer project. This provides an overview, installation instructions, usage examples, and other relevant details.

---

# Basic Network Sniffer

This project is a basic network sniffer built in Python, leveraging the Scapy library to capture and analyze network traffic. It captures packets on a specified network interface, extracting useful information such as source/destination IP, MAC addresses, port numbers, and even HTTP data when available. This tool provides insight into data flow on a network and how network packets are structured.

## Features

- Capture packets on a specified network interface.
- Display detailed packet information, including IP and MAC addresses, protocols, and port numbers.
- Detect and display HTTP GET/POST requests and their data payloads.
- Designed to analyze network traffic for educational and debugging purposes.

## Requirements

- **Python 3.6+**
- **Scapy library** for packet sniffing and parsing

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/network-sniffer.git
   cd network-sniffer
   ```

2. Install the required libraries:
   ```bash
   pip install scapy
   ```

## Usage

Run the network sniffer with:
```bash
python sniffer.py
```

### Parameters

- **Interface**: Specify the network interface (e.g., `eth0`, `wlan0`) to capture packets.
- **Count**: Set the number of packets to capture.

By default, the interface is set to `eth0` and captures 10 packets. Modify these values in the script or pass them as arguments to customize behavior.

### Output

The output will include packet-level details, such as:
- **Source and Destination IP addresses**
- **Source and Destination MAC addresses**
- **Protocol type** (e.g., HTTP, TCP, etc.)
- **HTTP request data** (if available)

Sample output:
```plaintext
Packet Info:
  Source IP: 192.168.1.5
  Destination IP: 192.168.1.8
  Protocol: TCP
  Length: 64 bytes

HTTP Packet:
  Source IP: 192.168.1.5
  Destination IP: 192.168.1.8
  Source Port: 53820
  Destination Port: 80
  HTTP Request: GET /index.html HTTP/1.1
```

 Contributing

Feel free to open issues or submit pull requests if you would like to contribute. All contributions are welcome!

 Disclaimer

This project is intended for educational purposes only. Use responsibly and ensure you have permission to capture traffic on the network you are analyzing.

 License

This project is licensed under the MIT License.

---

This `README.md` file provides a concise yet comprehensive overview of the project, installation instructions, usage examples, and a clear warning about responsible usage.
