use to filter CPC2 output text into fasta file  
we will further add more script for different tasks for differnt filtering tools and coding and non coding file sepration
# CPC2_Non-Coding_Sequence_Extractor
CPC2_Non-Coding_Sequence_Extractor is a Python-based filtering tool used to extract non-coding sequences from a FASTA file based on classifications provided by a CPC2 output file. The script reads the CPC2 results, identifies non-coding sequences, and creates a new FASTA file with only non-coding sequences for further analysis.

Table of Contents
Requirements
How It Works
Usage
Example
License
Contributing
# Requirements
Python 3.x  
CPC2 Output File: A .txt file with coding and non-coding sequence classifications.  
FASTA File: A .fasta file containing sequences to be filtered.
# How It Works
Input Paths: The script prompts the user to provide file paths for the CPC2 output and the FASTA file.  
Non-coding Filter: It scans the CPC2 file to identify non-coding sequence IDs.  
Extract Sequences: Using these IDs, it searches the FASTA file for matching sequences and writes only the non-coding sequences to a new output file.  
Output File: The new FASTA file is saved in the same directory as the CPC2 file, with _noncoding_sequences.fasta added to the filename.
# Usage
Clone the repository to your local machine:

code
git clone https://github.com/your-username/non-coding-sequence-extractor.git
cd non-coding-sequence-extractor  
Run the script:  code  
python noncoding_sequence_extractor.py  
Provide the paths when prompted:  

CPC2 File: Path to the CPC2 output file, typically with a .txt extension.  
FASTA File: Path to the FASTA file with sequence data.  
Output: The script will create a new FASTA file in the same directory as the CPC2 file, named <cpc2_filename>_noncoding_sequences.fasta.  

# Example
Suppose your CPC2 output is located at:C:\Users\your_user\Documents\cpc2_output.txt  
FASTA file is at:C:\Users\your_user\Documents\sequences.fasta  
The program will output:C:\Users\your_user\Documents\cpc2_output_noncoding_sequences.fasta  
# License
created by Mohammad faiz  
Email-webtech9889@gmail.com.
# Contributing
if any issues leave email  
Contributions are welcome! Please open an issue to discuss any changes or improvements, or submit a pull request if you'd like to contribute directly.

