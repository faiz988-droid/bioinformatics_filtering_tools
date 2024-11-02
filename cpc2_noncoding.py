# Take file path inputs from the user
cpc2_file = input("Enter the path to the CPC2 output file: ")
fasta_file = input("Enter the path to the FASTA file: ")

# Define the output file path based on the CPC2 file location
output_file = cpc2_file.replace(".txt", "_noncoding_sequences.fasta")

def read_fasta(file_path):
    """Reads sequences from a FASTA file and returns a dictionary with sequence IDs as keys."""
    sequences = {}
    with open(file_path, 'r') as fasta_file:
        header = None
        sequence_lines = []
        for line in fasta_file:
            line = line.strip()
            if line.startswith('>'):
                if header:  # Store the previous sequence if it exists
                    sequences[header] = ''.join(sequence_lines)
                header = line[1:].split()[0]  # Get the ID only, excluding '>'
                sequence_lines = []
            else:
                sequence_lines.append(line)
        if header:  # Store the last sequence after exiting loop
            sequences[header] = ''.join(sequence_lines)
    return sequences

def filter_noncoding_sequences(cpc2_file, fasta_file, output_file):
    """
    Reads the IDs of non-coding sequences from a CPC2 output file, 
    finds the corresponding sequences in a FASTA file, and writes them to an output file.
    """
    # Read sequences from the FASTA file
    fasta_sequences = read_fasta(fasta_file)

    # Read non-coding sequence IDs from the CPC2 output file
    noncoding_ids = set()
    with open(cpc2_file, 'r') as cpc2:
        next(cpc2)  # Skip header line
        for line in cpc2:
            parts = line.strip().split('\t')
            if len(parts) > 1 and parts[-1] == "noncoding":  # Check if the last column is "noncoding"
                noncoding_ids.add(parts[0])  # Add the sequence ID to the set

    # Write matching non-coding sequences to the output FASTA file
    with open(output_file, 'w') as output:
        written_count = 0
        for nc_id in noncoding_ids:
            if nc_id in fasta_sequences:
                output.write(f">{nc_id}\n{fasta_sequences[nc_id]}\n")
                written_count += 1
                print(f"Writing non-coding sequence for ID: {nc_id}")  # Debug output

    # Inform if no sequences were written
    if written_count == 0:
        print("No non-coding sequences were written to the output file.")
    else:
        print(f"Total non-coding sequences written: {written_count}")


# Execute the function
filter_noncoding_sequences(cpc2_file, fasta_file, output_file)
