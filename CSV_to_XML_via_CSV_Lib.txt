import csv

f = open(r'C:\Users\mwoff\Desktop\claims.csv')
csv_f = csv.reader(f)   
data = []

for row in csv_f: 
    data.append(row)
f.close()

#print (data[1:])

def convert_row(row):
    return """\t<Claim xmlns="SkillsTest">
    \t\t<PolicyNumber>%s</PolicyNumber>
    \t\t<ClaimNumber>%s</ClaimNumber>
    \t\t<LineOfBusiness>%s</LineOfBusiness>
    \t\t<LineOfBusinessCode>%s</LineOfBusinessCode>
    \t\t<AccidentState>%s</AccidentState>
    \t\t<ClaimantName>%s</ClaimantName>
    \t\t<ClaimStatus>%s</ClaimStatus>
    \t\t<DateOfLoss>%s</DateOfLoss>
    \t\t<ReportedDate>%s</ReportedDate>
    \t\t<OpenDate>%s</OpenDate>
    \t\t<TypeOfLoss>%s</TypeOfLoss>
    \t\t<DescriptionOfLoss>%s</DescriptionOfLoss>
    \t\t<SubrogationRecovered>%s</SubrogationRecovered>
    \t\t<SubrogationAdjustingandOtherExpensesRecovered>%s</SubrogationAdjustingandOtherExpensesRecovered>
    \t\t<IndemnityPaid>%s</IndemnityPaid>
    \t\t<IndemnityReserve>%s</IndemnityReserve>
    \t\t<MedicalPaid>%s</MedicalPaid>
    \t\t<MedicalReserve>%s</MedicalReserve>
    \t\t<AdjustingandOtherExpensePaid>%s</AdjustingandOtherExpensePaid>
    \t\t<AdjustingandOtherExpenseReserve>%s</AdjustingandOtherExpenseReserve>
\t\t</Claim>""" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], 
row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19])

#print ('\n'.join([convert_row(row) for row in data[1:]]))

#Note: Instead of hardcoding the <ReportingPeriod> input, a function could be written to grab whatever date necessary
with open(r'C:\Users\mwoff\Desktop\CSV_to_XML_via_CSV_Lib.xml', 'w') as f: f.write('<ClaimsData xmlns="SkillsTest">'+'\n\t'+
'<ReportingPeriod>2021-09-30</ReportingPeriod>'+'\n\t'+'<Claims>'+'\n\t'+'\n\t'.join([convert_row(row) for row in data[1:]])+'\n\t'+
'</Claims>'+'\n'+'</ClaimsData>')

