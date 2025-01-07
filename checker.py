from pwn import *
host='23.146.248.134'
for i in range(9001, 9010):
    try:
        r=remote(host, i)
        r.close()
    except:
        print(f'[*] Port : {i} DIED')
