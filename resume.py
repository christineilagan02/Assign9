from fpdf import FPDF
import json

title = "CHRISTINE S. ILAGAN     "


class PDF(FPDF):   
    def header(self):
        #Add image
        self.image("2X2.jpg",10, 10, 50, 0)
        # Arial bold 15
        self.set_font('Helvetica', 'B', 30)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((255 - w) / 2)
        self.ln(8)
        self.cell(0, 30, f"{title}" , align = 'R', ln=1)
        # Line break
        self.ln(10)

pdf = PDF('P', 'mm', "Legal")

pdf.add_page()

fh = open('resume.json', 'r') 
jh = fh.read()
info = json.loads(jh)

for information in info:
    pdf.ln(5)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 10, f"{information['header1']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, f"Name: {information['Name']}", align='L', ln=1)
    pdf.cell(0, 5, f"Address: {information['Address']}", align='L', ln=1)
    pdf.cell(0, 5, f"Contact No.: {information['Contact No.']}", align='L', ln=1)
    pdf.cell(0, 5, f"Email: {information['Email']}", align='L', ln=1)
    pdf.ln(5)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 10, f"{information['header2']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, f"{information['Objectives']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Objectives1']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Objectives2']}", align='L', ln=1)
    pdf.ln(5)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 5, f"{information['header3']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', 'B', 14)
    pdf.cell(0, 5, "Tertiary             :  ", align='L')
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 5, f"{information['Tertiary']}", align='R', ln=1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, f"{information['TerAdd']}", align='R', ln=1)
    pdf.cell(0, 5, f"{information['TerYear']}", align='R', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', 'B', 14)
    pdf.cell(0, 5, "Secondary        :  ", align='L')
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 5, f"{information['Secondary']}", align='R', ln=1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, f"{information['SecAdd']}", align='R', ln=1)
    pdf.cell(0, 5, f"{information['SecYear']}", align='R', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', 'B', 14)
    pdf.cell(0, 5, "Primary             :  ", align='L')
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 5, f"{information['Primary']}", align='R', ln=1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, f"{information['PriAdd']}", align='R', ln=1)
    pdf.cell(0, 5, f"{information['PriYear']}", align='R', ln=1)
    pdf.ln(5)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 10, f"{information['header4']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 5, f"{information['Work1']}", align='L', ln=1)
    pdf.ln(1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, f"{information['WorkCompany']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['WorkAdd']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['WorkYear']}", align='L', ln=1)
    pdf.ln(5)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 10, f"{information['header5']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', 'B', 18)
    pdf.cell(0, 2, ". ", align='L')
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, f"{information['Skill1']}", align='R', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', 'B', 18)
    pdf.cell(0, 2, ". ", align='L')
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, f"{information['Skill2']}", align='R', ln=1)
    pdf.ln(5)




pdf.output('ILAGAN_CHRISTINE.pdf')