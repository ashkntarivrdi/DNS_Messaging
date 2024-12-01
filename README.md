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

    make run-server

**Send a Message**

Run the client script to send a message to the server:   

    make run-client

**Example Message**

The client sends a message like:

    This is a test message split into DNS packets.

The server reassembles the message from multiple packets and prints:

    Full message received: This is a test message split into DNS packets.

## File Descriptions
`server.py`: Contains the server-side code for handling DNS messages.

`client.py`: Contains the client-side code for sending DNS messages.

`README.md`: This documentation file.

`Makefile`: A file to automate dependency installation and script execution.

## Code Overview

**Server (`server.py`)**
- Listens on port `8533` for incoming UDP DNS packets.
- Handles each client request in a separate thread.
- Reconstructs messages from multiple packets and sends acknowledgments.

**Client (`client.py`)**
- Sends a message by splitting it into DNS-compatible packets.
- Awaits acknowledgment for each packet and retransmits unacknowledged packets.

## Configuration

Modify the following variables in the scripts as needed:

- `SERVER_PORT`: The port number the server listens on (default: `8533`).
- `BUFFER_SIZE`: The maximum size of the DNS packets (default: `512` bytes).
- `ACK_TIMEOUT`: The timeout for acknowledgment in seconds (default: `2` seconds).

## Makefile Usage

The `Makefile` provides the following targets:

`install`: Installs required dependencies (`dnslib`).

`run-server`: Runs the server script (`server.py`).

`run-client`: Runs the client script (`client.py`).

`clean`: Removes Python cache files.

Example:

    make install
    make run-server
    make run-client

## Dependencies

This project uses the following library:

[dnslib](https://pypi.org/project/dnslib/): For creating and parsing DNS packets.

install it with:

    make install

## Author
**Ashkan Tariverdi**

Student Number: `401105753`

## License
This project is for educational purposes and is not intended for production use. Feel free to modify and extend as needed.
