import socket
import random as r

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()

port = 12345

s.bind((host,port))

s.listen(5)

while True:
    c,addr = s.accept()

    print('Got connection from',addr)

    # Entering the File path
    file = input("Enter the file to open: ")
    file1 = open(file,'r')
    data = file1.read()
    file1.close()

    # Displaying the Read data from the File
    print(data)
        
    # Creating Packets of 5 characters Long
    chucked_list = []
    for i in range(0,len(data),5):
        chucked_list.append(data[i:i+5])

    #Displaying the created packets 
    print(chucked_list)

    # Obtaining the indices of the packets
    indices = []
    for i in range(len(chucked_list)):
        indices.append(i)
    print(indices)

    # Creating a dictionary (Attaching the index to its respective data packet)
    result1 = {indices[i]:chucked_list[i] for i in range(len(indices))}
    print(result1)

    # Converting the items of the dictionary into a list
    result2 = list(result1.items())
    print(result2)

    # Shuffling the list 
    r.shuffle(result2)
    print(result2)

    # Converting the shufffled list into a dictionary
    result3 = dict(result2)
    print(result3)

    # Creating a list of keys of the dictionary
    key_list = list(result3.keys())
    print(key_list)

    sent_keys1 = [str(i) for i in key_list]
    print(sent_keys1)

    sent_keys = ''.join(sent_keys1)
    print(sent_keys)

    # Creating a list of the values of the dictionary (Distorted packets)
    values_list = list(result3.values())
    # print(values_list)

    # Combining the distorted data packets in a Striing
    sent_str = ''.join(values_list)
    # print(sent_str)

    # c.send(bytes('Thanks for Connecting',"utf-8"))
    c.send(bytes(sent_str,"utf-8"))
    c.send(bytes(sent_keys,"utf-8"))


    c.close()