# PortPulse - Advanced Port Scanner Tool

A powerful and feature-rich port scanner tool with ASCII art interface designed for cybersecurity professionals.

## Features

- **Single Port Scan**: Scan a specific port on a target IP
- **Port Range Scan**: Scan a range of ports with configurable threading
- **Common Ports Scan**: Quick scan of most commonly used ports
- **Full Port Scan**: Comprehensive scan of all 65535 ports
- **Custom Port List**: Scan specific ports of your choice
- **Network Discovery**: Scan multiple IPs in a network range
- **Service Detection**: Identify services running on open ports
- **Export Results**: Save scan results to files
- **Configurable Settings**: Adjust timeout and thread settings

## Requirements

- Python 3.6 or higher
- Built-in Python libraries (no external dependencies)

## Installation

1. Download the `PortPulse.py` file
2. Ensure Python is installed on your system
3. Run the tool using Python

## Usage

### Basic Usage

```bash
python PortPulse.py
```

### Menu Options

1. **Scan Single Port** - Check if a specific port is open
2. **Scan Port Range** - Scan a range of ports (e.g., 1-1000)
3. **Scan Common Ports** - Quick scan of 19 most common ports
4. **Scan All Ports** - Comprehensive scan of all 65535 ports
5. **Custom Port List Scan** - Scan specific ports you specify
6. **Fast Network Discovery** - Scan multiple IPs in a network
7. **Service Detection** - Identify services on open ports
8. **Export Results** - Save scan results to files
9. **Settings** - Configure timeout and thread settings
10. **Exit** - Close the application

### Example Scans

#### Single Port Scan
```
Enter IP Address: 192.168.1.1
Enter Port Number (1-65535): 80
```

#### Port Range Scan
```
Enter IP Address: 192.168.1.1
Enter Start Port (1-65535): 20
Enter End Port (1-65535): 100
Enter number of threads (default 100): 200
```

#### Common Ports Scan
```
Enter IP Address: 192.168.1.1
```
This will automatically scan ports: 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 993, 995, 1723, 3306, 3389, 5900, 8080

## Security Notice

⚠️ **WARNING**: This tool is designed for authorized security testing and network administration only. Always ensure you have proper authorization before scanning any network or system. Unauthorized port scanning may be illegal in many jurisdictions.

## Common Use Cases

- **Network Administration**: Check which services are running on your network
- **Security Auditing**: Identify open ports and potential vulnerabilities
- **Troubleshooting**: Diagnose network connectivity issues
- **Penetration Testing**: Authorized security assessments
- **System Monitoring**: Regular network health checks

## Performance Tips

- Use appropriate thread counts based on your network capacity
- For large scans, consider using the "Scan All Ports" option with high thread counts
- Use "Common Ports Scan" for quick reconnaissance
- Network discovery is useful for mapping entire subnets

## Output Format

The tool provides clear, color-coded output:
- `[+]` - Success/Open ports found
- `[-]` - Failure/Closed ports
- `[*]` - Information/Status updates
- `[!]` - Warnings/Important notices

## Legal Disclaimer

This tool is provided for educational and authorized security testing purposes only. Users are responsible for ensuring compliance with applicable laws and regulations. The author assumes no liability for misuse of this tool.

## Version

PortPulse v1.0

---

**Created by: AymanCharp**
**For authorized security testing and network administration only**

