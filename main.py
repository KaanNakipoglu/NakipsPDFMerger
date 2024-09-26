import PyPDF2
#Author:KaanNakipoglu
#upload the files you want to merge into the project at the same level as main.py to use this format
#or you can just use full directory name to use this program
def merge_pdfs(pdf_list, output_filename):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        with open(pdf, 'rb') as pdf_file:
            pdf_merger.append(pdf_file)

    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)

if __name__ == "__main__":
    pdfs = ['example1.pdf','example2.pdf','example3.pdf']
    merge_pdfs(pdfs, 'mergedPDF.pdf')