# IPv4
- Stored as 4 seperate 8 bit characters e.g. 255.255.255.255 is 11111111 11111111 11111111 11111111
- The first 2 sections specify which network the IP address belong to
- The last 2 sections specify which Class the network belongs to
- When you connect to a new router you create a new IP address

# Classes/CIDR (Classless-Inter-Domain-Routing)
## Classes
- Class systems existed until 1990 where all four digits were used to assign the IP address
- Go from A-E where A class can connect millions of devices, lower Classes get progressively smaller in size
- The top three bits determined the class used
- Uses netmasks (subnet masks) to identify classes e.g. Class A: 255.0.0.0, Class C: 255.255.255.0 this defines how many addresses the given class can host

## CIDR
- Based on variable length subnet masking
- Specify the number of bits assigned to network the ip at the end in a /n format (up to 32)
- An IP address is said to match the CIDR if the initial n bits and /n match
- The first /n bits identify the network or subnet and are named the Network Prefix
- The last /32 - n bits form the Host Identifier
- Your VPC should have more bits assigned to it than the subnet
- 2^32 - n is how many IPv4 addresses can match a given n-bit CIDR prefix
- All binary zero in the Host Identifiers refers to the network e.g. 192.168.0.0
- All binary one is reserved for the Broadcast Address which is used to send data to all connected hosts
- e.g. 192.168.255.255 ^ ^ ^

# Public Vs Private
- There are 4 billion IPv4 networks on the internet, this is what your public ip, your routers IP
- Each network distributes private ips

# Ports
- Used by [[TCP]] and [[UDP]] they are a 16-bit unsigned integer as a sort of address of the packet
- The first 1024 are reserved and are the Well-Known Ports
- Your ports are dynamically assigned to your IPv4 when you send a packet and foreign addresses assign a port to their IP address (typically 80 or 443)
- Your dynamically assigned port is called an Ephemeral Port 
- You can specify a port after a website's name http://www.example.com:500/path will connect on port 500
