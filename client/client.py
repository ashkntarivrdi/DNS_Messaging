import socket
from dnslib import DNSRecord, DNSHeader, DNSQuestion, QTYPE, DNSLabel, TXT

SERVER_ADDRESS = "localhost"
SERVER_PORT = 8533
BUFFER_SIZE = 512
ACK_TIMEOUT = 2  # Seconds


def build_dns_packet(transaction_id, seq_num, total_packets, payload):
    # Split payload into DNS-compatible labels
    labels = [str(seq_num), str(total_packets)] + [
        payload[i:i+63] for i in range(0, len(payload), 63)
    ]
    qname = DNSLabel(".".join(labels))
    
    # Create the DNS request using DNSQuestion
    question = DNSQuestion(qname, QTYPE.TXT)
    request = DNSRecord(DNSHeader(id=transaction_id, qr=0), q=question)
    return request



def send_message(message, server_address, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    transaction_id = 1234  # Random transaction ID
    total_packets = (len(message) - 1) // (BUFFER_SIZE - 8) + 1  # 8 bytes for headers

    for seq_num in range(total_packets):
        start_index = seq_num * (BUFFER_SIZE - 8)
        end_index = start_index + (BUFFER_SIZE - 8)
        payload = message[start_index:end_index]

        dns_packet = build_dns_packet(transaction_id, seq_num, total_packets, payload)
        ack_received = False

        while not ack_received:
            
            client_socket.sendto(dns_packet.pack(), (server_address, server_port))
            client_socket.settimeout(ACK_TIMEOUT)

            try:
                ack_data, _ = client_socket.recvfrom(BUFFER_SIZE)
                ack_record = DNSRecord.parse(ack_data)
                
                # Process all answers in the 'a' section
                for answer in ack_record.rr:
                    if isinstance(answer.rdata, TXT):
                        ack_seq_num = int(answer.rdata.data[0].decode().split(":")[1])  # Extract sequence number
                        if ack_seq_num == seq_num:
                            ack_received = True
                            break
            except socket.timeout:
                print(f"Retransmitting packet {seq_num}...")

    client_socket.close()

if __name__ == "__main__":
    message = "This is a test message split into DNS packets."
    send_message(message, SERVER_ADDRESS, SERVER_PORT)
