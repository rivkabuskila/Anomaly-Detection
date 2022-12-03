import pandas as pd
import numpy as np
import joblib 
from sklearn.covariance import EllipticEnvelope


f_path = "conn_attack.csv"
df = pd.read_csv(f_path,names=["record ID","duration_", "src_bytes","dst_bytes"], header=None)
X = list(zip(df["duration_"],df["src_bytes"],df["dst_bytes"]))
cov = EllipticEnvelope(contamination=0.025).fit(X)
print(df)

def predict(a):
	#test_name = [a]
	# predict returns 1 for an inlier and -1 for an outlier
	pred1 = cov.predict(a)
	return pred1
	
EllipticEnvelope = open("model/anomalyModel.pkl","wb")
joblib.dump(cov,EllipticEnvelope)
EllipticEnvelope.close()
