#ma tanghao
#genearate votes
#24/1/2013
import random
file=open('VOTES.DAT','w')
for i in range(33000):
    result=''
    #party?
    n=random.randint(0,100)
    if (-1) < n < 3 : result += 'SDA'
    if 2 < n < 8 : result += 'RP'
    if 7 < n <41 : result += 'WP'
    if 40 < n < 101 : result += 'PAP'
    m = random.randint(0,100)
    #spoil?
    if m < 3 :
        result += (',0\n')
    else:
        result += (',1\n')
    #output
    file.write(result)
file.close()

    
       
