#Ma Tanghao
#24/1/2013
#count votes

#read files
file = open('VOTES.DAT','r')

#initialization
dic = {'PAP':0,'WP':0,'RP':0,'SDA':0,'Invalid':0}
total = 0

for line in file.readlines():
    result=line.split(',')
    total += 1
    # valid?
    if result[1] == '0\n': #invalid
        dic['Invalid'] += 1
    else: #valid
        dic[result[0]] += 1

file.close()

#format result
printlist = ['PAP','WP','RP','SDA','Invalid']
for element in printlist:
    print(element,dic[element],str('{0:.2f}'.format(int(dic[element])/total*100))+'%') #name,amount,percentage
