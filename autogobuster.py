from colorama import Fore
import argparse
import subprocess


parser = argparse.ArgumentParser()

parser.add_argument('-u', help='Provide the url to scan', required=True, metavar='URL')
parser.add_argument('-w', help='Provide the wordlist to use', required=True, metavar='WORDLIST')

wordlist = parser.parse_args().w
url = parser.parse_args().u

times = 0
cmd = ["gobuster", "dir", "-u", url, "-q", "-w", wordlist, "-t", "50"]
print(f"Running command: {' '.join(cmd)}")

scan = subprocess.run(cmd, capture_output=True, text=True)

times += 1
print(f"Ran {times} time for {url}")


scan = scan.stdout


list = []
queue = []

for line in scan.split('\n'):
    words = line.split()
    if len(words) > 0 and int(words[2][:-1]) in range(200, 400):
        queue.append(url+words[0][5:]+'/')
        list.append(
            Fore.YELLOW+url+words[0][5:] + '\t'*3 + Fore.GREEN+f"(Status: {words[2][:-1]})"+'/')


while (len(queue)):

    new_url = queue.pop(0)
    queue = queue[1:]
    new_cmd = ["gobuster", "dir", "-u", new_url,
               "-q", "-w", wordlist, "-t", "50"]
    scan = subprocess.run(new_cmd, capture_output=True, text=True)

    times += 1
    print(f"Ran {times} time for {new_url}")
    print(f"Te size of the queue is {len(queue)} now...")
    if len(queue) == 0:
        print("The queue is empty, exiting...")
        break
    scan = scan.stdout

    for line in scan.split('\n'):
        words = line.split()
        if len(words) > 0 and int(words[2][:-1]) in range(200, 400):
            if new_url+words[0][5:] not in list:
                if new_url+words[0][5:] not in queue:
                    queue.append(new_url+words[0][5:]+'/')
                if new_url+words[0][5:] + '\t'*3 + f"(Status: {words[2][:-1]})" not in list:
                    list.append(
                        Fore.YELLOW+new_url+words[0][5:] + '\t'*3 + Fore.GREEN+f"(Status: {words[2][:-1]})"+'/')


def removeDuplicates(listofElements):
    uniqueList = []
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)
    return uniqueList

file=open("gobuster.txt","w+")
for i in removeDuplicates(list):
    url = i.split()[0][5:]

    status = subprocess.run(["wget", "-O-", url],
                            capture_output=True, text=True)
    status = status.stdout
    if len(status) > 30:
        file.write(i[:-1]+'\n')
        print(i[:-1])
file.close()
       
