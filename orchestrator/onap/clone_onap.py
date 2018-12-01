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
    NAME = talbes[2][0][i]
    if ('.' not in NAME):
       DIRS = NAME.split('/')
       GIT_COMMAND='git clone https://gerrit.onap.org/r/'+NAME+' "'+local_path+'/'+NAME+'"'
       print GIT_COMMAND
       os.system(GIT_COMMAND)
    i=i+1
