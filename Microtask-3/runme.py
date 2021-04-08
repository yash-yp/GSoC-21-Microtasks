import os
from PyPDF2 import PdfFileMerger
import pypandoc



def merge_md(mdfile_list, merged_md_name):
    try:
        print(f"Merging markdown files")
        with open(merged_md_name, 'w') as outfile:
            for md_file in mdfile_list:
                with open(md_file) as infile:
                    print(f"Merging: {md_file}")
                    outfile.write(infile.read())
                outfile.write("\n")
        print(f"Markdown files merged successfully : {merged_md_name}")
    except:
        print("Error: Markdown files could not be merged")
        exit(1)

def convert_md2pdf(md_filename, pdf_filename):

    print(f"Converting {md_filename} file to PDF")
    # using 'gfm' results in page overflow of tables hence 'markdown_github'  used
    output = pypandoc.convert_file(md_filename, 'pdf', outputfile=pdf_filename, extra_args=['-f', 'markdown_github',
                                                                                            '--pdf-engine=xelatex',
                                                                                            '-H', 'header.tex',
                                                                                            '--toc', '--toc-depth= 2',
                                                                                            '-V', 'geometry:a4paper',
                                                                                            '-V', 'geometry:margin=0.8in',
                                                                                            '--highlight-style','zenburn',
                                                                                            '-V', 'fontsize=12pt',
                                                                                            '-V', 'monofont:DejaVuSansMono.ttf',
                                                                                            '-V', 'mathfont:texgyredejavu-math.otf',
                                                                                            '-V', 'colorlinks=true',
                                                                                            '-V', 'linkcolour:blue'
                                                                                            ])
    assert output == ""
    print(f"Created successfully: {pdf_filename}")



def merge_pdf(pdf_list, pdf_filename):

    try:
        print("Merging PDF files")
        merger = PdfFileMerger()
        for pdf in pdf_list:
            print(f"Merging: {pdf}")
            merger.append(pdf)

        merger.write(pdf_filename)
        merger.close()
        print("PDF files merged successfully")
    except:
        print("Error: Unable to merge PDF files")
        exit(3)

def delete_files(file_path_arr):

    for file_path in file_path_arr:
        try:
            if os.path.isfile(file_path):
                print(f"Deleting: {file_path}")
                os.remove(file_path)
                print(f"Deleted Successfully")
        except:
            print(f"Unable to delete {file_path}")

# Driver Code
if __name__ == "__main__":

    mdfile_list = ["project-popularity.md", "project-velocity.md","test.md"]
    inprocess_report_mdfile = "inprocess_report.md"
    inprocess_report_pdffile = "inprocess_report.pdf"
    report_pdf_elements = ["front-matter.pdf", inprocess_report_pdffile]

    # merge the metric markdowns to create a single markdown file
    merge_md(mdfile_list, inprocess_report_mdfile)

    # convert the merged file to pdf
    convert_md2pdf(inprocess_report_mdfile,inprocess_report_pdffile)

    # merge the metrics pdf with front content
    merge_pdf(report_pdf_elements, "sample-report.pdf")

    # delete the intermediate files formed during the process
    delete_files([inprocess_report_mdfile,inprocess_report_pdffile])
