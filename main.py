from fpdf import FPDF
import pandas as pd

# to create a pdf instance/object from PDF class
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# read .csv file as dataframe object
df = pd.read_csv("topics.csv")

# create for-loop for each instance of row object
for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
             ln=1, border=0)
    pdf.line(10, 21, 200, 21)

    # to set the footer - pgs with topic title
    pdf.ln(268)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=0, txt=row["Topic"], align="R",
             ln=1, border=0)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # to set the footer - pgs added after title
        pdf.ln(280)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=0, txt=row["Topic"], align="R",
                 ln=1, border=0)

pdf.output("output.pdf")
