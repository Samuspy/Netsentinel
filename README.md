NetSentinel is a Python-based network recon utility designed to perform targeted port scans, banner grabs, and TLS certificate analysis with situational awareness.
It's fast, smart, and expandable—built for developers, security students, and curious engineers who want a deeper look into their targets without crossing the ethical line.

- Ping & Reachability Check
Confirms whether a host is alive before scanning.
- Port Scanning (TCP SYN)
Scans a custom port range and flags all open ports.
- Banner Grabbing
Attempts to retrieve service banners from open ports to infer running software.
- TLS Certificate Scanning
For services offering TLS (like HTTPS), it fetches and parses certificates to reveal:
- Issued To / By
- Validity Dates
- Expiry warnings
- Error Handling with Clarity
Catches and reports issues with clean, focused messages.
- Modular & Extensible
Designed to be easily upgraded with threading, logging, WHOIS, GeoIP, and more.

You'll be prompted for:
- IP address or hostname
- Start and end ports to scan
- Optional TLS certificate inspection (if scanning port 443

