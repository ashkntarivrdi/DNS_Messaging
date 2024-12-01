# DNS Packet Messaging System

This project demonstrates a messaging system over DNS queries and responses, using the `dnslib` Python library. The system consists of a server and a client that exchange messages by splitting them into DNS-compatible packets. The server acknowledges each packet received, and the client ensures reliable delivery by retransmitting unacknowledged packets.

## Features

- **Message Fragmentation:** Messages are split into multiple DNS packets for transmission.
- **Reliable Communication:** The client retransmits packets until acknowledged by the server.
- **DNS-based Messaging:** The system uses DNS queries and responses to send messages.
- **Multithreaded Server:** The server handles multiple clients simultaneously.

## Requirements

- Python 3.6+
- dnslib library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ashkntarivrdi/DNS_Messaging.git
   cd DNS_Messaging
2. Install the required dependencies using the provided `Makefile`:
   ```bash
   make install

## Usage
**Start the Server**
Run the server script to start listening for incoming DNS messages:
   

**Send a Message**
Run the client script to send a message to the server:
   `bash
   make run-server


**Example Message**
The client sends a message like:



The server reassembles the message from multiple packets and prints:



## File Descriptions
`server.py`: Contains the server-side code for handling DNS messages.
`client.py`: Contains the client-side code for sending DNS messages.
`README.md`: This documentation file.
`Makefile`: A file to automate dependency installation and script execution.
