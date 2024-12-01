# Makefile for DNS Packet Messaging System

.PHONY: all install clean run-server run-client

# Variables
PYTHON = python
PIP = pip
DEPS = dnslib
SERVER_SCRIPT = server.py
CLIENT_SCRIPT = client.py

all: install

# Install dependencies
install:
	$(PIP) install $(DEPS)

# Run the server
run-server:
	$(PYTHON) $(SERVER_SCRIPT)

# Run the client
run-client:
	$(PYTHON) $(CLIENT_SCRIPT)

# Clean up environment (if needed)
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
