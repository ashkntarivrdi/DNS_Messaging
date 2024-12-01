import socket
import threading
from dnslib import DNSRecord, DNSHeader, RR, QTYPE, TXT, DNSQuestion

SERVER_PORT = 8533
BUFFER_SIZE = 512

def handle_client(sock, addr, data):
    print(f"Handling request from {addr}")
    message_parts = {}

    while True:
        # Parse the DNS packet
        dns_record = DNSRecord.parse(data)
        transaction_id = dns_record.header.id
        labels = dns_record.q.qname.label
        seq_num = int(labels[0].decode())
        total_packets = int(labels[1].decode())
        payload = "".join(label.decode() for label in labels[2:])

        # Simulate ACK response
        ack_packet = build_dns_ack(transaction_id, seq_num)
        sock.sendto(ack_packet.pack(), addr)

        # Store the payload in the correct sequence
        message_parts[seq_num] = payload

        # If all packets are received, reconstruct the message
        if len(message_parts) == total_packets:
            full_message = "".join(message_parts[i] for i in sorted(message_parts.keys()))
            print(f"Full message received: {full_message}")
            break

        # Wait for the next packet
        data, addr = sock.recvfrom(BUFFER_SIZE)

def build_dns_ack(transaction_id, seq_num):
    # Build a valid DNS acknowledgment response
    qname = f"ack.{seq_num}."
    question = DNSQuestion(qname, QTYPE.TXT)
    response = DNSRecord(
        DNSHeader(id=transaction_id, qr=1, aa=1, ra=1),  # Response header
        q=question,  # Include the question section
        a=RR(qname, QTYPE.TXT, ttl=0, rdata=TXT(f"ACK:{seq_num}"))  # Answer section
    )
    return response


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("0.0.0.0", SERVER_PORT))
    print(f"Server listening on port {SERVER_PORT}...")

    while True:
        # Wait for a request
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        threading.Thread(target=handle_client, args=(server_socket, addr, data)).start()

if __name__ == "__main__":
    start_server()
