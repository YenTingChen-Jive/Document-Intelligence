# Document Intelligence

## Abstract
Collaborated with the Financial Supervisory Commission to develop an generative interactive AI for retrieving data from annual financial reports for major companies based on user queries.

NOTE: This research is in its initial stage (Stage A), awaiting further development toward a larger scaled system by others.


## Installation

```bash
conda create -n docint python=3.11
conda activate docint
conda install -c conda-forge ghostscript
pip install -r requirements.txt
```

## Target

Create an artificial intelligence that searching in which table in the given pdf files has the desired information.  

#### Input

1. pdf files with only tables inside
2. the searching keywords

#### Output

**the hole table with desired information in it**

#### Example

The given pdf file:  
![image](https://github.com/Stage-A/Document-Intelligence/blob/main/images/example1.png)
Keyword of searching:  

```commandline
非監督是學習的學習目標
```

Output:
![image](https://github.com/Stage-A/Document-Intelligence/blob/main/images/example2.png)

## How to contribute

* Every one finishes the whole project and pulls the requests , do not edit the main branch
* if your code is useful, we will add it into the main branch

## Background Knowledge

[Azure Document Intelligence]( https://azure.microsoft.com/en-us/products/ai-services/ai-document-intelligence
)

## Test Document

[Document 1](https://docs.google.com/document/d/1Di5oVYhUF6p-zj2y0DEBBeTvhC91KhX8/edit?usp=sharing&ouid=107784913306655694785&rtpof=true&sd=true)
[Document 2](https://docs.google.com/document/d/1HiZrgIyvwY8Fi4eLS0QGUkkycngtD6XJ/edit?usp=sharing&ouid=107784913306655694785&rtpof=true&sd=true)
