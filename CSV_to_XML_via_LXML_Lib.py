import lxml.etree as ET
import csv

#Hardcoded in order to match .xml Template element names minus the extra one plus to missing one
headers = ['PolicyNumber', 'ClaimNumber', 'LineOfBusiness', 'LineOfBusinessCode', 'AccidentState', 'ClaimantName',
'ClaimStatus', 'DateOfLoss', 'ReportedDate', 'OpenDate', 'TypeOfLoss', 'DescriptionOfLoss', 'SubrogationRecovered', 
'SubrogationAdjustingandOtherExpensesRecovered', 'IndemnityPaid', 'IndemnityReserve', 'MedicalPaid', 'MedicalReserve', 
'AdjustingandOtherExpensePaid', 'AdjustingandOtherExpenseReserve']

ns = 'SkillsTest'

# INITIALIZING XML FILE
claimsData = ET.Element("ClaimsData", nsmap = {None: ns})
repPer = ET.SubElement(claimsData, "ReportingPeriod")
repPer.text = '2021-11-30' 
claimsData.insert(0, repPer)

# READING CSV FILE AND BUILD TREE
with open(r'C:\Users\mwoff\Desktop\Claims.csv') as f:
    next(f)                             # SKIP HEADER
    csvreader = csv.reader(f)

    claims = ET.SubElement(claimsData, "Claims")
    for row in csvreader:        
        data = ET.SubElement(claims, "Claim")
        data.set('xmlns', ns)
        for col in range(len(headers)):
            node = ET.SubElement(data, headers[col]).text = str(row[col])

# SAVE XML TO FILE
tree_out = (ET.tostring(claimsData, xml_declaration=True, pretty_print=True, encoding="UTF-8"))

#print(tree_out)

# OUTPUTTING XML CONTENT TO FILE
with open(r'C:\Users\mwoff\Desktop\CSV_to_XML_via_LXML_Lib.xml', 'wb') as f: f.write(tree_out)


