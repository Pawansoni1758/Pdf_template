from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics (1).csv")
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="L", ln=1)
    pdf.line(10,22,200,22)

    for p in range(32, 288, 10):
        pdf.line(10, p, 200, p)

    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=24)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="R", ln=1)


    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(270)
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="R", ln=1)
        for r in range(22, 288, 10):
            pdf.line(10, r, 200, r)
pdf.output("out.pdf")