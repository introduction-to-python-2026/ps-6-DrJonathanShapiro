def create_codon_dict(file_path):
    cta = {}

    with open(file_path, "r") as f:
        for line in f:
            cells = line.strip().split('\t')
            codon = cells[0]
            amino_acid = cells[1]  # one-letter code
            cta[codon] = amino_acid

    return cta
