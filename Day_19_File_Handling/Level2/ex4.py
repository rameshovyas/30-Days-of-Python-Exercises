# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
f = open("email_exchanges_big.txt", "r")
lines = f.readlines()
email_address = []
for line in lines:
    if(line.startswith("From")):        
        email_address.append(line.split()[1])

print(email_address)