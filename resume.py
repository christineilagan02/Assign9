from fpdf import FPDF

title = 'CHRISTINE ILAGAN'
fn='ILAGAN_CHRISTINE.pdf'
jsonFile = "resume.json"

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('arial', 'B', 32)
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
    
    def chapter_body(self, name):
        # Read text file
        with open(jsonFile) as fh:
            txt = fh.read()
        # Times 12
        self.set_font('helvetica', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln(5)
        # Mention in italics
        self.set_font('', 'I')

    def print_chapter(self, num, title, name):
        self.add_page()
        # self.chapter_title(num, title)
        self.chapter_body(name)



pdf = PDF()
pdf.set_title(title)
pdf.print_chapter(1, "", str(jsonFile))

pdf.output(fn)