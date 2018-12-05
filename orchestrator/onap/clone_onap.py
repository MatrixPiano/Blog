# clone all onap codes from gerrit as anonymous user
# pip install pandas
# pip install lxml

import pandas as pd
import os
import sys

if len(sys.argv)>=2 :
   local_path = sys.argv[1]
else:
   local_path = os.path.abspath('.')
   
talbes = pd.read_html("https://git.onap.org/")
i=1
while i< len(talbes[2][0]):
    r_path = talbes[2][0][i]
    if ('.' not in r_path):
       GIT_COMMAND='git clone https://gerrit.onap.org/r/'+r_path+' "'+local_path+'/'+r_path+'"'
       print GIT_COMMAND
       os.system(GIT_COMMAND)
    i=i+1
