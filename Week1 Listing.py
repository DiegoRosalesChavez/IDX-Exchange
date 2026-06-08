import pandas as pd

df202401 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202401.csv", encoding="ISO-8859-1")
df202402 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202402.csv", encoding="ISO-8859-1")
df202403 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202403.csv", encoding="ISO-8859-1")
df202404 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202404.csv", encoding="ISO-8859-1")
df202405 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202405.csv", encoding="ISO-8859-1")
df202406 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202406.csv", encoding="ISO-8859-1")
df202407 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202407.csv", encoding="ISO-8859-1")
df202408 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202408.csv", encoding="ISO-8859-1")
df202409 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202409.csv", encoding="ISO-8859-1")
df202410 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202410.csv", encoding="ISO-8859-1")
df202411 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202411.csv", encoding="ISO-8859-1")
df202412 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202412.csv", encoding="ISO-8859-1")

df202501 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202501.csv", encoding="ISO-8859-1")
df202502 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202502.csv", encoding="ISO-8859-1")
df202503 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202503.csv", encoding="ISO-8859-1")
df202504 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202504.csv", encoding="ISO-8859-1")
df202505 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202505.csv", encoding="ISO-8859-1")
df202506 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202506.csv", encoding="ISO-8859-1")
df202507 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202507.csv", encoding="ISO-8859-1")
df202508 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202508.csv", encoding="ISO-8859-1")
df202509 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202509.csv", encoding="ISO-8859-1")
df202510 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202510.csv", encoding="ISO-8859-1")
df202511 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202511.csv", encoding="ISO-8859-1")
df202512 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202512.csv", encoding="ISO-8859-1")

df202601 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202601.csv", encoding="ISO-8859-1")
df202602 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202602.csv", encoding="ISO-8859-1")
df202603 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202603.csv", encoding="ISO-8859-1")
df202604 = pd.read_csv(r"C:/Users/Admin/Desktop/raw/CRMLSListing202604.csv", encoding="ISO-8859-1")

frames=[df202401,df202402,df202403,df202404,df202405, df202406, df202407, df202408, df202409, df202410, df202411, df202412, df202501, df202502, df202503, df202504, df202505,df202506, df202507, df202508, df202509,df202510,df202511,df202512, df202601, df202602, df202603, df202604]
combine = pd.concat(frames, ignore_index=True)

print("Rows before Residential filter:", len(combine))
main = combine[combine["PropertyType"] == "Residential"].copy()
print("Rows after Residential filter:", len(main))
main.to_csv(r"C:\Users\Admin\Documents\IDX Exchange\newlistings.csv",index=False)


print("Week 1 listings dataset created successfully!")