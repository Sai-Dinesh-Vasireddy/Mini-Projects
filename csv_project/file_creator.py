import csv



with open('HPC_SNOW_Report.csv' , 'w+' , newline = "") as c:
        w = csv.writer(c)
        w.writerow(['Request Incident Number' , 'Requested User' , 'Assigned To' , 'Request Open Date','State' , 'Request Closed Date','Time worked','Description','Note'])

with open('HPC_JIRA_Report.csv' , 'w+' , newline = "") as cs:
        wr = csv.writer(cs)
        wr.writerow(['Task Number' , 'Sprint Number' , 'Sprint Date From' ,'Sprint Date To', 'Assigned To','Worklog Date' , 'Number of Hours','Deployed Date','Impediments','Reason','Description','Comments'])

