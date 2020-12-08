## miRcorrNet
This tool allows you to make an integrated mRNA - miRNA profiles analysis. Via using this document you can easily execute the steps and you can obtain the results. Using this document you can easily repeat the experiments.

## Data Preparation
miRcorrNet uses 2 different data sheets with same control-case column. It means you should have same samples in one column which should be both in mRNA and miRNA data sheet. In this study we used KNIME analytics platform. Therefore, the data is stored in ".table" extension files.

## mRNA Data (Gene Expression)
In mRNA data one should have samples in the rows and gene names in the columns but the type of the genes should be double. The "class" column represents the sample whether control or case. The type of class column should be String and there can be only 2 classes. Below one can see the some chunk of the mRNA data.
 
 ![alt text](https://github.com/gokhangoy/miRcorrNet/blob/master/Data%20Graphics/README%20Figures/mRNA_Data.JPG)
 
## microRNA Data
In miRNA data one should have samples in the rows and microRNA names in the columns but the type of the genes should be String. The "class" column represents the sample whether control or case. The type of class column should be String and there can be only 2 classes. Below one can see the some chunk of the miRNA data.

 ![alt text](https://github.com/gokhangoy/miRcorrNet/blob/master/Data%20Graphics/README%20Figures/miRNA_Data.JPG)

## Set up Parameters

miRcorrNet allows you to set some parameter values. These parameters :
- Negative Correlation Value (Default :  -0.6)
- Positive Correlation Value (Default :  +1.0)
- Number of Iterations       (Default :  100)

To be able to change these parameters one need to use SetParameters node in the workflow.

## Usage of miRcorrNet and Environment Settings

The only thing one should do is install KNIME Analytics platform. The workflow for miRcorrNet is available. One just download and import that workflow into KNIME. The miRcorrNet workflow contains python and R scripts in it so to avoid any error one need to set up the KNIME Python settings following this path inside KNIME : 
- File -> Preferences -> KNIME(left side of the pop-up) -> Python <br />
And your R server needs to be (open) running simultaneously when the execution starts. To be able to open this please use following commands in your R / RStudio:
- library(Rserve);
- Rserve(args = "--vanilla") <br />
If you set all of this environment settings you'll never encounter any error with this stable version of the workflow.

## KNIME WORKFLOW
 ![alt text](https://github.com/gokhangoy/miRcorrNet/blob/master/Data%20Graphics/README%20Figures/Latest_miRcorrNet_Workflow(v10).JPG)
 
 - List Files Node("Node 223"): One need to give the path of directory which contains mRNA and miRNA data
 - Table Reader("Read mRNA data") : This node finds the "mRNA .table" file in given directory and read those values and put it into a table.
 - SetParameters Node : Via using this node one can set the parameters for the workflow.
 - Java Edit Variable("get the corresponding miRNA name") Node : This nodes adds 'i' letter to the mRNA file(ie. A_mRNA.table -> A_miRNA.table)
 - Table Reader("Read miRNA data") : This node finds the "miRNA .table" file in given directory and read those values and put it into a table.
 - Row Filter("remove 5.0") Node( X2(Both mRNA and miRNA) ): If there is other than a value except two classes one need to remove that value from the class column.
 - Column Auto Type Cast("Node 466,467") Node : Assign the columns data type automatically.
 - Normalizer Node("Node 464,465") Node : Normalize the values via using z-score normalization.
 - miRcorrNet Meta-Node : This metanode's task is making integrated mRNA-miRNA analysis.

## Solution Approach Steps
1. Import data and set the parameters
2. Normalize mRNA and miRNA expression data
3. Find Differentially Expressed mRNAs and miRNAs
4. Compute the Pearson correlation coeeficient between mRNAs and miRNAs in a pairwise manner
5. Detect mRNAs and miRNAs target groups
6. Rank the target gene groups
7. Test on top ranked clusters
8. Write Results to the output files

![alt text](https://github.com/gokhangoy/miRcorrNet/blob/master/Data%20Graphics/README%20Figures/miRcorrNet_v2.jpg)
