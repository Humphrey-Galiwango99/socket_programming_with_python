import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()

port = 12345

s.connect((host,port))

rec_data = s.recv(1024).decode("utf-8")
print(rec_data)

rec_key = s.recv(1024).decode("utf-8")

print(rec_key)
rec_keys = []
for i in rec_key:
    rec_keys.append(i)

print(rec_keys)

# List of received packets
received_packets = []
for i in range(0,len(rec_data),5):
    received_packets.append(rec_data[i:i+5])

print(received_packets)

# Attaching the distorted data to its respective index.
distorted_dict = {rec_keys[i]:received_packets[i] for i in range(len(rec_keys))}
print(distorted_dict)

# Organizing the distorted dictionary
organized_dict={}
for i in sorted(distorted_dict):
   organized_dict[i]=distorted_dict[i]
print(organized_dict)

# # Creating a list of organized_keys of the dictionary
organized_keys = list(organized_dict.keys())
print(organized_keys)

# # Creating a list of the values of the dictionary (Organized packets)
organized_data = list(organized_dict.values())
print(organized_data)

# # Combining the distorted data packets in a Striing
data_received = ''.join(organized_data)
print(data_received)

s.close()