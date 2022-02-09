from fpdf import FPDF
import json

title = "CHRISTINE S. ILAGAN"


class PDF(FPDF):   
    def header(self):
        #Add image
        self.image("2X2.jpg",10, 10, 50, 0)
        # Arial bold 15
        self.set_font('helvetica', 'B', 32)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((255 - w) / 2)
        self.cell(0, 30, f"{title}" , align = 'R', ln=1)
        # Line break
        self.ln(15)

pdf = PDF('P', 'mm', "Letter")

pdf.add_page()

fh = open('resume.json', 'r') 
jh = fh.read()
info = json.loads(jh)

for information in info:
    pdf.ln(5)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 10, f"{information['header1']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', '', 12)
    pdf.cell(0, 5, f"NAME: {information['Name']}", align='L', ln=1)
    pdf.cell(0, 5, f"ADDRESS: {information['Address']}", align='L', ln=1)
    pdf.cell(0, 5, f"CONTACT NO.: {information['Contact No.']}", align='L', ln=1)
    pdf.cell(0, 5, f"EMAIL: {information['Email']}", align='L', ln=1)

pdf.output('ILAGAN_CHRISTINE.pdf')