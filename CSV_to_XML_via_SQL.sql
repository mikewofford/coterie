create table claim (
	Policy_Number  varchar(255),
	Claim_Number varchar(255),
	Line_of_Business varchar(255),
	Line_of_Business_Code varchar(255),
	Accident_State varchar(255),
	Claimant_Full_Name varchar(255),
	Claim_Status varchar(255),
	Date_of_Loss varchar(255),
	Date_Reported varchar(255),
	Open_Date varchar(255),
	Type_of_Loss varchar(255),
	Loss_Description varchar(max),
	Total_Recovery varchar(255),
	Deductible_Recovery varchar(255),
	Indemnity_Paid varchar(255),
	Indemnity_Reserve varchar(255),
	Medical_Paid varchar(255),
	Medical_Reserve varchar(255),
	Expense_Paid varchar(255),
	Expense_Reserve varchar(255)
   )

--Could turn everything below into a stored procedure and dump the .xml file to a folder using SQL Server Agent to run the procedure at an interval
bulk insert claim
from 'C:\Mike\Resumes\Coterie\claims.csv'
with
  (Fieldterminator = ',',
   RowTerminator = '\n',
   FIRSTROW = 2)

--Works, generates .xml file with link in execution results, 
--but can't figure out how to create <ClaimsData> and <ReportingPeriod> elements
SELECT * 
FROM Claim
FOR XML AUTO, TYPE, --XMLSCHEMA('SkillsTest'), 
ROOT('Claims'), ELEMENTS XSINIL -- PATH('C:\Mike\Resumes\Coterie') --Unclear if ROOT is contributing



