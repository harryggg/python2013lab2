#Ma Tanghao
#24/1/2013
#display result python3.2

import datetime
import time
#read files
file = open('VOTES.DAT','r')

#initialization

dic = {'PAP':0,'WP':0,'RP':0,'SDA':0,'Invalid':0}
total = 0

for line in file.readlines():
    result=line.split(',')
    total += 1
    # check whther valid.
    if result[1] == '0\n': #invalid
        dic['Invalid'] += 1
    else: #valid
        dic[result[0]] += 1

file.close()

#result analyzing
printlist = ['PAP','WP','RP','SDA','Invalid']
resultlist = []
winner=[0,'']
for element in printlist:
    resultlist.append([element,dic[element],str('{0:.2f}'.format(int(dic[element])/total*100))+'%']) #name,amount,percentage
    #find the largest
    if dic[element] > winner[0] and element != 'Invalid' :
        winner = [dic[element] , element]

file = open('RESULTS.TXT','w')
file.write('DATE: '+datetime.date.today().strftime("%d-%m-%y")+' '*17+ 'TIME: '+ time.strftime('%H:%M %p') + '\n')
file.write('RESULTS OF THE 2013 PUNGGOL EAST SMC BY ELECTION \n')
file.write('WARD                PARTY     #VOTES    %VOTES\n')
file.write('--------------------------------------------------\n')
file.write('PUNGGOL EAST SMC    PAP        ' + str(dic['PAP'])+' '*(9-len(str(dic['PAP'])))+resultlist[0][2]+'\n')
file.write('                    RP         '+str(dic['RP'])+' '*(9-len(str(dic['RP'])))+resultlist[2][2]+'\n')
file.write('                    SDA        '+str(dic['SDA'])+' '*(9-len(str(dic['SDA'])))+resultlist[3][2]+'\n')
file.write('                    WP         '+str(dic['WP'])+' '*(9-len(str(dic['WP'])))+resultlist[1][2]+'\n')
file.write('--------------------------------------------------\n')
file.write('WINNER: '+winner[1]+'\n')
file.write('TOTAL VOTES: '+ str(total) + '\n')
file.write('#SPOILT VOTES: ' + str(dic['Invalid'])  + '\n')
file.write(' %SPOLIT VOTES: ' + resultlist[4][2]+'\n')



file.close()
