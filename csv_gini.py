import pandas as pd
from pandas import DataFrame
import csv
import datetime


df = pd.read_csv('gini.csv')
print csv.reader(df)
df.index = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','0','p']        # given new name to every index
#print df.loc[["c","d"],["gender","age"]]   # loc to print as an object of row
#df.iloc[[1,2]]


spe_it = df.speciality == 'it'
spe_medicine = df.speciality == 'medicine'
spe_sociology = df.speciality == 'sociology'
spe_engineering = df.speciality == 'engineering'

result_yes = df.result == 'yes'
result_no = df.result == 'no'

age_greater = df.age < 25 
age_less = df.age >= 25

gender_f = df.gender == 'f'
gender_m = df.gender == 'm'


with open('gender.csv', 'w') as writeFileGender:
	writer = csv.writer(writeFileGender,delimiter=',')
	writer.writerow(['','yes','no','total'])
	writer.writerow(['female',len(df.loc[gender_f & result_yes]),len(df.loc[gender_f & result_no]),len(df.loc[gender_f & result_yes])+len(df.loc[gender_f & result_no])])
	writer.writerow(['male',len(df.loc[gender_m & result_yes]),len(df.loc[gender_m & result_no]),len(df.loc[gender_m & result_yes])+len(df.loc[gender_m & result_no])])

with open('speciality.csv','w') as writeFileSpeciality:
	writer = csv.writer(writeFileSpeciality,delimiter=',')
	writer.writerow(['','yes','no','total'])
	writer.writerow(['it',len(df.loc[spe_it & result_yes]),len(df.loc[spe_it & result_no]),len(df.loc[spe_it & result_yes])+len(df.loc[spe_it & result_no])])
	writer.writerow(['medicine',len(df.loc[spe_medicine & result_yes]),len(df.loc[spe_medicine & result_no]),len(df.loc[spe_medicine & result_yes])+len(df.loc[spe_medicine & result_no])])
	writer.writerow(['engineering',len(df.loc[spe_sociology & result_yes]),len(df.loc[spe_sociology & result_no]),len(df.loc[spe_sociology & result_yes])+len(df.loc[spe_sociology & result_no])])
	writer.writerow(['sociology',len(df.loc[spe_engineering & result_yes]),len(df.loc[spe_engineering & result_no]),len(df.loc[spe_engineering & result_yes])+len(df.loc[spe_engineering & result_no])])

with open('age.csv','w') as writeFileAge:
	writer = csv.writer(writeFileAge,delimiter=',')
	writer.writerow(['','yes','no','total'])
	writer.writerow(['less',len(df.loc[age_less & result_yes]),len(df.loc[age_less & result_no]),len(df.loc[age_less & result_yes])+len(df.loc[age_less & result_no])])
	writer.writerow(['greater',len(df.loc[age_greater & result_yes]),len(df.loc[age_greater & result_no]),len(df.loc[age_greater & result_yes])+len(df.loc[age_greater & result_no])])




def FirstMath(filename):
	df2 = pd.read_csv(filename)
	f = []
	#print csv.reader(df2)
	#print(len(df2))
	for i in range(0,len(df2)):
		ff = 1 - ( ((float(df2.yes[i])/float(df2.total[i]))**2) ) - ( ((float(df2.no[i])/float(df2.total[i]))**2) )
		f.append(ff)
	print f
	for i in range(0,len(f)):
		p = (float(df2.total[i])/16 * f[i])

	print (float(df2.total[0])/16 * f[0]) + (float(df2.total[1])/16 * f[1])


	#print   1 - ( ((float(df2.yes[0])/float(df2.total[0]))**2) ) - ( ((float(df2.no[0])/float(df2.total[0]))**2) )
	#print   ( ((float(df2.yes[0])/float(df2.total[0]))**2) , ((float(df2.no[0])/float(df2.total[0]))**2) )
	#print   1 - ( ((float(df2.yes[1])/float(df2.total[1]))**2) ) - ( ((float(df2.no[1])/float(df2.total[1]))**2) )
	#print   ( ((float(df2.yes[1])/float(df2.total[1]))**2) , ((float(df2.no[1])/float(df2.total[1]))**2) )
	print('\n')
print('....................')
#FirstMath('gender.csv')
FirstMath('age.csv')
#FirstMath('speciality.csv')


