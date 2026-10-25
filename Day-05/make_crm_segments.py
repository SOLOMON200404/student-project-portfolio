import csv
src=r'outputs\L5-Time-Loop\HubSpot_Import_50.csv'
out=r'outputs\L5-Time-Loop\CRM_Segments_Alternative.csv'
with open(src,newline='',encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
with open(out,'w',newline='',encoding='utf-8-sig') as f:
 w=csv.writer(f); w.writerow(['first_name','email','orders_12m','revenue_12m_usd','last_order_date','segment_formula'])
 for i,r in enumerate(rows,start=2):
  w.writerow([r['first_name'],r['email'],r['orders_12m'],r['revenue_12m_usd'],r['last_order_date'],f'=IF(C{i}>=8,"Champions",IF(AND(C{i}>=3,IFERROR(DATEVALUE(E{i}),E{i})<DATE(2026,7,3)),"At risk","Other"))'])
print(out,len(rows))
