READ ME:

Python Version used: 3.8.1
LXML Verison used: 4.6.3
Pandas Version used: 1.3.5
CSV Version used: 1.0

Because I was given a week to return the code for the assessment, I decided to solve it multiple ways in order
to see what would be required to code for the desired .xml Template structure using differing methods.

I noticed that the column names in the Claims.csv file did not match all the element names for those columns 
in the .xml Template file, there was an extra element/column, <ClosedDate>, in the .xml Template that was not in the 
Claims.csv file, and there was a column in the Claims.csv file, "Line Of Business Code", that was not an element in the 
.xml Template. I was not clear if that's what the Assessment.pdf instructions meant by "some of the fields won't make 
a direct word for word translation from the CSV to the XML", or if that statement was in reference to the fact that 
the spaces between the words in the column names of the CSV file need to be replaced with '' in order to match the 
format of the element names in the XML Template. I would have inquired as to whether or not this was on purpose and 
how Coterie woud've preferred this be handled before coding to solve the assessment if not for the fact that I 
assumed Coterie would likely be closed and pretty much everyone on PTO for some if not all of the week before 
Christmas, and I wanted to start coding as soon as I got the opportunity rather than await a response, so I coded it 
successfully 3 ways with Python, as described below. 

--CSV_to_XML_via_SQL.sql
I was unable to entirely produce the desired .xml Template results utilizing MSSQL (though I did attach the 
.sql code to the email). Utilizing MSSQL, I was able to produce a .xml with a proper element tree, though it was
missing <ReportingPeriod> and <ClaimsData> elements. However, if MSSQL were to be used and produced the desired
results, the SQL code could be turned into a Stored Procedure and a SQL Server Agent Job created to execute the
Stored Procedure at whatever desired interval in order to automate. Or an SSIS package could be thrown in the mix.

--CSV_to_XML_via_LXML_Lib.py
I coded the assessment successfully, producing the desired .xml Template structure, 3 different ways. I was 
successfully able to utilize the lxml.etree library method. But the column names were hardcoded as headers in
order to match the elements as they are named in the .xml Template. However, using pretty_print=True only tabbed
the resulting .xml file elements by 2 spaces instead of 4. Still, this is likely the most favorable method of 
the 3, though it uses the CSV Library whereas Pandas combined with lxml.etree would likely have been the most 
ideal somehow, seeing as how Pandas has become industry standard, moving away from the BeautifulSoup Library.

--CSV_to_XML_via_Pandas_Lib
I also successfully solved the assessment utilizing the Pandas Library, but rather than use .replace() to
rename the column names in the Claims.csv file with the element/column names in the .xml Template file, I left 
them as they are in the Claims.csv file. The coding methods used in this file are certainly efficient, however, 
there's some hardcoding in the open() function that is probably less than ideal.

--CSV_to_XML_via_CSV_Lib
Another way I successfully solved the assessment was utilizing the Python CSV Library. However, using this method, 
I hardcoded the names of the XML elements to match the names of the XML elements as they are listed in the .xml
Template file, as well as hardcoded the "tabs" and "next lines" with "\t" and "\n". I doubt this is the best way 
to convert CSV to XML, and the method using the LXML Library is likely better.

--Automating .py Files
To automate a .py file on a recurring basis, least good option would be to code it to run at certain intervals
and then have the program continuously running in the background on the laptop. At Allstate, to automate .py 
files, our only option is to convert .py to .exe, then get with a dev who has access to the Allstate Virtual 
Machine, then he codes a 3 line .bat file to trigger the .exe to run, then he adds the .bat file to the automation 
bot on the VM and sets the interval. All of this is bc the SQL Server Agent we use is MSSQL to trigger SSIS packages 
to run will not execute a .py file within the SSIS, even though manually running the SSIS executes the .py file.
I don't know if Coterie uses Airflow, but that, or another similar platform, could be used to automate the .py file.