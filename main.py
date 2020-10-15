import PyPDF4
import img2pdf
import os


def add_pdf_to_final_pdf(file_name):
    with open(f"{file_name}.pdf", "rb") as f:
        pdf_reader = PyPDF4.PdfFileReader(f, strict=False)
        number_of_pages = pdf_reader.getNumPages()
        for i in range(number_of_pages):
            page = pdf_reader.getPage(i)
            pdf_result_writer.addPage(page)
            with open(result_pdf_name, "wb") as file:
                pdf_result_writer.write(file)


def jpg_to_pdf(file_name):
    image = img2pdf.Image.open(f"{file_name}.jpg")
    pdf_bytes = img2pdf.convert(image.filename)
    with open(f"{file_name}.pdf", "wb") as file:
        file.write(pdf_bytes)
        image.close()


if __name__ == "__main__":
    path_to_folder = input('Path to folder containing files: \n')
    file_names = input('file names separated with a comma:\n').replace(" ", "").split(sep=',')

    result_pdf_name = ""
    for file in file_names:
        result_pdf_name = result_pdf_name + file + "_"
    result_pdf_name = path_to_folder + "/" + result_pdf_name[:-1] + ".pdf"

    files_to_merge = [f"{path_to_folder}/{file_to_merge}" for file_to_merge in file_names]

    pdf_result_writer = PyPDF4.PdfFileWriter()
    files_created = []
    for file_name in files_to_merge:
        try:
            jpg_to_pdf(file_name)
            files_created.append(f"{file_name}.pdf")
        except FileNotFoundError:
            pass
        finally:
            add_pdf_to_final_pdf(file_name)

    #with open(result_pdf_name, "wb") as file:
    #    pdf_result_writer.write(file)
    print(f"Created pdf in {result_pdf_name}")
    for file_created in files_created:
        os.remove(file_created)

    input("Press Enter to exit...")
