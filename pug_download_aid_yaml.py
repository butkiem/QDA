import requests
import json

server = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/"
ext = "assay/aid/1775/description/JSON"

r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})

if not r.ok:
  r.raise_for_status()
  sys.exit()
 
decoded = r.json()
#print decoded


rows = decoded['PC_AssayContainer'][0]['assay']['descr']['xref'][:]
print [row['xref'] for row in rows ]


rows = decoded['PC_AssayContainer'][0]['assay']['descr']['xref']['comment']
print [row['xref'] for row in rows ]


