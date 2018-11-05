import csv
from collections import Counter

filename='H-1B_FY14_Q4.csv'
#output=[]
employer_state = Counter()
employer_certified = Counter()
employer_certified1 = Counter()
employer_occupation =Counter()

with open(filename, encoding='utf8', errors='ignore') as csv_file:
#with open(filename) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        employer_state[row[10]] += 1
        if row[1] == "CERTIFIED":
            employer_certified[row[10]] += 1
        employer_occupation[row[14]] += 1
        if row[1] == "CERTIFIED":
        	employer_certified1[row[14]] += 1

for employer_state in employer_state.most_common(10):
	print(str(employer_state[0]) + " had " + str(employer_certified.get(employer_state[0])) + "("  + str(round((float(employer_certified.get(employer_state[0]))/float(employer_state[1]) * 100),2)) +  "% )" + " certified employees\n")
	file=open("top_10_states.txt","a")
	file.write(str(employer_state[0])+';'+str(employer_certified.get(employer_state[0]))+';'+str(round((float(employer_certified.get(employer_state[0]))/float(employer_state[1]) * 100),2))+'% \n')
	file.close()
for employer_occupation in employer_occupation.most_common(10):
	print(str(employer_occupation[0])+ " had " + str(employer_certified1.get(employer_occupation[0])) + "("  + str(round((float(employer_certified1.get(employer_occupation[0]))/float(employer_occupation[1]) * 100),2)) +  "% )" + " certified employees \n")
	file=open("top_10_occupations.txt","a")
	#file.write(str(employer_state[0])+';'+str(employer_certified.get(employer_state[0]))+';'+str(round((float(employer_certified.get(employer_state[0]))/float(employer_state[1]) * 100),2))+'\n')
	file.write(str(employer_occupation[0])+";"+str(employer_certified1.get(employer_occupation[0]))+'\n')
	file.close()