from fpdf import FPDF

class PDF(FPDF):
    def add_header(self):
        self.set_font("Times", "B", 55)
        title = 'CS50 Shirtificate'
        title_width = self.get_string_width(title)
        self.set_xy((210 - title_width) / 2, 20)
        self.text(self.get_x(), self.get_y(), title)

    def add_image(self, image_path):
        self.set_xy(0, 50)
        self.image(image_path, x=(210 - 175) / 2, y=60, w=175)

    def add_name(self, fname):
        self.set_text_color(255, 255, 255)
        if len(fname) > 19 and len(fname) <= 26:
            self.set_font("Times", "B", 27)
        elif len(fname) > 26 and len(fname) <= 30:
            self.set_font("Times", "B", 20)
        else:
            self.set_font("Times", "B", 35)
        text_width = self.get_string_width(fname)
        self.set_xy((210 - text_width) / 2, 130)
        self.text(self.get_x(), self.get_y(), fname)

pdf = PDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.add_header()

image_path = "shirtificate.png"  # Ensure this path is correct
pdf.add_image(image_path)

fname = input("Name: ") + " took CS50"
pdf.add_name(fname)

pdf.output("shirtificate.pdf")



