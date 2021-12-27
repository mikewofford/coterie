import pandas as pd

df = pd.read_csv(r'C:\Users\mwoff\Desktop\Claims.csv')
# print(df)
df.columns = df.columns.str.replace(' of ', 'Of')
df.columns = df.columns.str.replace(' ', '') 

#Function to loop through the dataframe and append the field values to the XML skeleton
def xmlSkel(row):
    xml = ['\t<Claim xmlns="SkillsTest">']
    for field in row.index:
        xml.append('\t\t\t<{0}>{1}</{0}>'.format(field, row[field]))
    xml.append('\t\t</Claim>')
    return '\n'.join(xml)

# print('\n'.join(df.apply(func, axis=1)))

#Note: This function doesn't quite accomplish the output the assessment is looking for
# df.to_xml(r'C:\Users\mwoff\Desktop\CSV2XMLviaPandas2.xml', namespaces={"": "SkillsTest"}, pretty_print=True)

#Note: Instead of hardcoding the <ReportingPeriod> input, a function could be written to grab whatever date necessary
with open(r'C:\Users\mwoff\Desktop\CSV_to_XML_via_Pandas_Lib.xml', 'w') as f: f.write('<ClaimsData xmlns="SkillsTest">'+'\n\t'+
'<ReportingPeriod>2021-09-30</ReportingPeriod>'+'\n\t'+'<Claims>'+'\n\t'+'\n\t'.join(df.apply(xmlSkel, axis=1))+'\n\t'+
'</Claims>'+'\n'+'</ClaimsData>')




