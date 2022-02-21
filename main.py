import re
import time
import datetime

def parse_health_data_test(file_name):    
    start_time = time.time()    
   
    PATTERN_ROW = r'(?:<tr\s*/>)|(?:<tr\b[^>]*>(?P<arow>.+?)</tr>)'    
    PATTERN_CELL = r'(?:<(?:th|td)\s*/>)|(?:<(?P<element>th|td)\b[^>]*>(?P<col>.+?)</(?P=element)>)'
    PATTERN_CLEANUP = r'\s+|&#160;'
    
    html_content = open(file_name,'r', encoding='utf-8').read()
    
    # Cleanup: Replaces all extra spaces, new lines, tabs etc with a single space.    
    html_content = re.sub(PATTERN_CLEANUP,' ', html_content)    
    
    with open(file_name + '.csv','w', encoding='utf-8') as wr:
        
        # For each row
        row_iter = re.finditer(PATTERN_ROW, html_content)
        
        for row_match in row_iter:
            # Skip empty rows. Process only if group arow matched.        
            if row_match.group('arow'):
                # For each cell in a row
                col_iter = re.finditer(PATTERN_CELL,row_match.group('arow'))
                line = []
                for col_match in col_iter:
                    if col_match.group('col'):
                        line.append(col_match.group('col').replace(',',''))
                    else:
                        line.append('')
                        
                wr.write(','.join(line))
                wr.write('\n')
                
    print ('Elapsed Time : {0:.2f}s'.format(time.time()-start_time))

files =[r"C:\Users\ios\Desktop\Python\Python_Codes\Health Care\problems.html",
        r"C:\Users\ios\Desktop\Python\Python_Codes\Health Care\labresults.html"]
for file_name in files:
    print('****{0}'.format(file_name))
    parse_health_data_test(file_name)
