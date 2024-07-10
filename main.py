from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto= False,margin = 0)
df = pd.read_csv('topics.csv')
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family ='Times', style = "B", size=24)
    pdf.set_text_color(100, 100, 110 )
    pdf.cell(w = 0, h = 12, txt = row['Topic'], border = 1, ln = 1, aling = "L" )
    pdf.line(10, 21, 201, 21)
    pdf.ln(255)
    pdf.set_text_color(177, 178, 179)
    pdf.set_font(family='Times', style ="I", size = 8)

    for i in range(row["pages"]):
        pdf.add_page()
        pdf.ln(255)
        pdf.set_text_color(177, 178, 179)
        pdf.set_font(family='Times', style="I", size=8)f

    pdf.output('output.pdf')