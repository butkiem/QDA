import requests
import json

server = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/"
#ext = "compound/cid/2244/sids/JSON"
ext = "assay/aid/1775/concise/JSON"

r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})

if not r.ok:
  r.raise_for_status()
  sys.exit()
 
decoded = r.json()

#rows = decoded['Table']['Row'][:]

#print len( [ row['Cell'][2] for row in decoded['Table']['Row'][:] if row['Cell'][4] == 'Active' ])
#print len( [ row['Cell'][2] for row in decoded['Table']['Row'][:] if row['Cell'][4] == 'Inactive' ])

print decoded

