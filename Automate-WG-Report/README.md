# Automated Report Generation for WG

This README describes the process of automated generation of report for working groups. 

## Pre-Requisites

- [Pandoc](https://pandoc.org/installing.html)
- [PyPandoc](https://pypi.org/project/pypandoc/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [Git-Python](https://pypi.org/project/GitPython/)
- LaTeX Distribution

## Files

- Script used to clone the required repository : [clone-repo.py](clone-repo.py)
- Script used to generate the report : [generate-report.py](generate-report.py)
- Front matter of the report: [front-matter.pdf](front-matter.pdf)
- File used for formatting: [header.tex](header.tex)
- Cloned Repository : [wg-common](wg-common)

## Report Generation Process

The process followed by the automated system to generate the report for working group from it's remote repository has been described below.

### Cloning the Remote Repository

- The [wg-common](https://github.com/chaoss/wg-common) was selected as the test repository for this process.
- The repository was cloned using the [clone-repo.py](clone-repo.py) script.
- Minor changes were made to the markdown files of the repository after cloning such as adding proper line-spacing, removal of unnecessary line breaks, etc.
- These edits ensure that the markdown files are displayed correctly in the report. (These edits can be made permanently in remote repositories.)

### Extraction of Files & Merger of Markdowns

- From the cloned version of the repository the required metric markdown files for each focus area were extracted.
- These files were merged to form a single markdown file for each focus area sorted alphabetically.
- The files for each focus area were once again sorted alphabetically and merged to form a single markdown file.
- Note:-  The extraction of these files is done assuming that repositories follow the [standard template](https://docs.google.com/document/d/1chPzgJa49sO_f3wVqp_NLJupSVyKHSVyuFuwzl4m4KI/). 

### Conversion to PDF & Front Content Incorporation

- The process of conversion was unaltered and the same as described in [Microtask -3](./Microtask-3).
- The [front-content](front-matter.pdf) was then prepended to the generated PDF to create the final report.
- [Link to Final report](Final-Release.pdf)

### Removal of Inessential Files

- The report generation created some intermediate markdown files and process.
- These files are removed automatically once they're no longer needed.

### Execution

- To test the process of cloning, run [clone-repo.py](clone-repo.py) script in any folder.
- To test the process of report generation, run [generate-report.py](generate-report.py) script in this folder itself.


