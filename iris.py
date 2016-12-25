import pandas as pd

import scipy.sparse as ss


# custcode = pd.read_csv("custcode.csv")
# cusdes = pd.read_csv("cusdes.csv")
# testcus = pd.read_csv("testcus.csv")
# prodata = pd.read_csv("prodata.csv")
cusdes = pd.read_csv("/Users/VeraZhou1/Documents/PycharmProjects/Santander/sanprodata.csv", index_col=False)
cusdes.drop("Unnamed: 0",axis = 1,inplace = True)

# for i in ["employeeInd","resiCountry","sex","primary","provinceName","activeIndex","segmentation"]:
#     cusdes = pd.concat([cusdes,pd.get_dummies(cusdes[i],prefix = i,drop_first=True)],axis = 1)
#     cusdes.drop(i,axis = 1, inplace = True)
cusdes.loc[:,"fecha_dato"] = pd.to_datetime(cusdes["fecha_dato"])
groups = cusdes["fecha_dato"].apply(lambda x: x.strftime('%Y')+x.strftime('%j'))
groups_X = ss.csr_matrix(groups.astype(float)).T
# date.loc[:,"age"] = pd.to_numeric(test["age"],errors = "coerce") # change age to number
cusdes.drop("fecha_dato",axis = 1,inplace = True)

x =ss.csr_matrix(cusdes.values)
x = ss.hstack([x,groups_X]).tocsr()

