
from fpdf import FPDF

title = "CHRISTINE S. ILAGAN"
fn="ILAGAN_CHRISTINE.pdf"
jsonFile = "resume.json"

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('helvetica', 'B', 32)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((255 - w) / 2)
        # Colors of frame, background and text
        # self.set_draw_color(0, 80, 180)
        self.set_fill_color(250, 250, 250)
        self.set_text_color(0, 0, 0)
        # Thickness of frame (1 mm)
        # self.set_line_width(1)
        # Title
        self.cell(w, 48, title)
        # Line break
        self.ln(10)
    
    def add_image(self):
        #Add image
        self.image("2X2 PIC.jpg",10, 10, 50, 0)
    
    def chapter_body(self, name):
        # Read text file
        with open(jsonFile) as fh:
            jh = fh.read()
        # Times 12
        self.set_font('helvetica', '', 12)
        # Output justified text
        self.multi_cell(0, 5, jh)
        # Line break
        self.ln(5)
        # Mention in italics
        self.set_font('', 'I')

    def print_chapter(self, num, title, name):
        self.add_page()
        # self.chapter_title(num, title)
        self.chapter_body(name)
        self.add_image()


pdf = PDF()
pdf.set_title(title)
pdf.print_chapter(1, "", str(jsonFile))

pdf.output(fn)


from PyPDF2 import PdfFileWriter, PdfFileReader

def add_encryption(input_pdf, output_pdf, password):

    pdf_writer = PdfFileWriter()

    pdf_reader = PdfFileReader(input_pdf)

    for page in range(pdf_reader.getNumPages()):

        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, 

                       use_128bit=True)

    with open(output_pdf, 'wb') as fh:

        pdf_writer.write(fh)

if __name__ == '__main__':

    add_encryption(input_pdf='ILAGAN_CHRISTINE.pdf',

                   output_pdf='ILAGAN_CHRISTINE.pdf',

                   password='Cuteko02')