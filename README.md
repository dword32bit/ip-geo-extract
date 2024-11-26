Here’s the `README.md` in English for your GitHub project:

---

# IP and Geolocation Extractor

**IP and Geolocation Extractor** is a Python program that downloads a file from a provided link, extracts the IP addresses of the servers accessed during the download process, and retrieves geolocation information for each IP.

## Features
- Download files from a provided link using `wget`.
- Extract server IP addresses involved during the download.
- Display geolocation details for each IP using the [ip-api](http://ip-api.com) service.
- Save the video file with a unique name if a file with the same name already exists.

## Requirements
- Python 3.x
- Python packages: 
  - `requests`
- Wget (installed on your system)

## Installation
1. Ensure Python 3.x and Wget are installed on your system.
2. Install the required Python package:
   ```bash
   pip install requests
   ```

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/dword32bit/ip-geo-extract.git
   cd ip-geo-extract
   ```
2. Run the program:
   ```bash
   python3 main.py
   ```
3. Enter the link you want to download:
   ```plaintext
   Input link address : https://example.com/file
   ```
4. The program will:
   - Download the file from the given link.
   - Extract the IP addresses of the servers involved.
   - Display geolocation details for each IP.

5. The downloaded file will be saved with a unique name (e.g., `get`, `get1`, etc.).

## Example Output
```plaintext
Input link address : https://www.tiktok.com/@user/video/47832947839210
IP Addresses:
<ip add>
<ip add>
<ip add>
File saved as get1

Geolocation Information:
IP: <ip add>
Country: United States
Region: California
City: San Jose
Latitude: somewhere
Longitude: somewhere
ISP: indosat
Organization: indosat
...
