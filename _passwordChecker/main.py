import hashlib
import requests
import sys


def request_API(hashed):
	url = "https://api.pwnedpasswords.com/range/" + hashed
	responce = requests.get(url)
	if responce.status_code != 200:
		raise Exception(f"Flawed API: Please Check API Status {responce}")
	return responce

def hashing(password):
	shaKey = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
	head, tail = shaKey[:5], shaKey[5:]
	return (_acquiringData(request_API(head), tail))

def _acquiringData(k, tail):
	hashes = (line.split(':') for line in k.text.splitlines())
	for i, count in hashes:
		if(i == tail):
			return (count)
	return (0)

def __main__(key):
	result = hashing(key)
	if result == 0:
		print("Your password is Strong enough!!!")
	else:
		print(f'Your password has been breached about {result}')
	return "Done!!"

exit(__main__(input("Enter your Password:")))