# import camelot
# from tabulate import tabulate

# df = camelot.read_pdf('data/5d03dc8b8621ea5e53ad6fe7b44c8533_bijlage-4-inventarislijst-deelbesluit-1.pdf', pages='all')
# print(df[0].df)
import pdfplumber
import pandas as pd

pdf = pdfplumber.open("data/2c4079ccaad78e8d2cb494681ae79928_inventarislijst-wob-verzoek-notities-besluitvorming-coronacrisis.pdf")

df = pd.DataFrame()
for page in pdf.pages:
    table=page.extract_table()
    df = df.append(pd.DataFrame(table[1::],columns=pdf.pages[0].extract_table()[0]))

print(df)