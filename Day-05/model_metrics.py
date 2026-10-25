import csv
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, recall_score, confusion_matrix
p=r'C:\Users\stell\Downloads\doomsday_d5_churn_practice.csv'
with open(p, newline='', encoding='utf-8-sig') as f:
    rows=list(csv.DictReader(f))
features=['tenure_months','plan','monthly_fee_usd','support_tickets_90d','sessions_last_30d','days_since_last_login','payment_failures_90d','joined_on_discount']
num=['tenure_months','monthly_fee_usd','support_tickets_90d','sessions_last_30d','days_since_last_login','payment_failures_90d','joined_on_discount']
cat=['plan']
X=[]; y=[]
for r in rows:
    X.append([float(r[c]) if c in num else r[c] for c in features])
    y.append(1 if r['churned'].strip().lower()=='yes' else 0)
X=np.array(X,dtype=object); y=np.array(y)
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.30,random_state=42,stratify=y)
pre=ColumnTransformer([('num',Pipeline([('impute',SimpleImputer(strategy='median')),('scale',StandardScaler())]),[0,2,3,4,5,6,7]),('cat',OneHotEncoder(handle_unknown='ignore'),[1])],verbose_feature_names_out=False)
models={'Logistic regression':LogisticRegression(max_iter=2000,random_state=42),'Decision tree':DecisionTreeClassifier(random_state=42)}
for name,clf in models.items():
    pipe=Pipeline([('prep',pre),('model',clf)])
    pipe.fit(Xtr,ytr); pred=pipe.predict(Xte); proba=pipe.predict_proba(Xte)[:,1]
    cm=confusion_matrix(yte,pred,labels=[1,0]); tp,fn,fp,tn=cm.ravel()
    print(name, 'train',len(ytr),'test',len(yte),'AUC',round(roc_auc_score(yte,proba),4),'CA',round(accuracy_score(yte,pred),4),'Precision',round(precision_score(yte,pred,zero_division=0),4),'Recall',round(recall_score(yte,pred,zero_division=0),4),'TP/FN/FP/TN',tp,fn,fp,tn)
    names=pipe.named_steps['prep'].get_feature_names_out(); vals=pipe.named_steps['model'].coef_[0] if name.startswith('Logistic') else pipe.named_steps['model'].feature_importances_
    agg={}
    for n,v in zip(names,vals):
        key='plan' if n.startswith('x1_') else {'x0':'tenure_months','x2':'monthly_fee_usd','x3':'support_tickets_90d','x4':'sessions_last_30d','x5':'days_since_last_login','x6':'payment_failures_90d','x7':'joined_on_discount'}.get(n,n)
        agg[key]=agg.get(key,0)+abs(float(v))
    print('top features',sorted(agg.items(),key=lambda x:-x[1])[:5])

