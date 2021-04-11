# GSoC'21-Microtasks

This repository contains the microtasks required to be completed for the automation project of GSoC'21 under [CHAOSS](https://github.com/chaoss).
____

 ## Project Idea
 [Automate Metrics Release and Process Improvement](https://github.com/chaoss/website/issues/537).

## Microtask -1

> Attend the weekly community meeting and monthly web content meeting.


[Link to Microtask -1](Microtask-1)

## Microtask -2

> Familiarize yourself with the website and GitHub repository. Make a pull request (PR) to the website repository - https://github.com/chaoss/website.

In addition to the website repository, I have contributed to other repositories too. The complete list of PRs submitted can be accessed through the link given below.

[Link to Microtask -2](Microtask-2)

## Microtask -3

> Task: Create a repository that contains,
> * Two (2) markdown files (you can start with files CHAOSS created and modify them as needed).
> * A single PDF generated from those markdown files.
> * A description of how you generated the PDF from the markdown files. 


[Link to Microtask -3](Microtask-3)

___

## Additional Project Work
 
In addition to the completing the above microtasks, I have also created some automation systems that can help generate a metrics report for the metrics defined under a particular working group.

- [Automation : Tree Structure of LaTeX files](Automate-LaTeX-Tree)
    - This automation system creates a tree-like structure for the working group repository where the metric files are defined at the bottom level of the tree.
    - All the LaTeX files in the tree get converted to PDF, all at once by including them in the files of upper level which inturn are included in the master file.

- [Automation : Merge Markdowns](Automate-LaTeX-Tree)
    - This system combines the required metric markdowns to create a single merged markdown file.
    - The markdown files thus obtained contains all the required metrics. It is then converted and processed to generate the report.