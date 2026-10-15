# Compare two aligned CDS sequences with the same starting position and no insertions/deletions.
# Paste each sequence on a single line, without FASTA headers, position numbers, or Query labels.
# Enter 1 for a complete CDS, or 181 for the last segment shown in the screenshot.
# A dot (.) in the mutant sequence means the nucleotide is identical to the WT.
# CDS numbering starts at the A of the ATG start codon: c.1.

start_text = input("CDS starting position of this segment (press Enter for 1): ").strip()
if start_text == "":
    start_text = "1"
if not start_text.isdecimal() or int(start_text) < 1:
    raise SystemExit("Error: the starting position must be an integer greater than or equal to 1.")
start = int(start_text)

wt = "".join(input("WT sequence: ").split()).upper()
mut = "".join(input("Mutant sequence (dots allowed): ").split()).upper()

if not wt or len(wt) != len(mut):
    raise SystemExit("Error: both sequences must be non-empty and have the same length. Insertions and deletions are not supported.")
if any(base not in "ACGT" for base in wt):
    raise SystemExit("Error: the WT sequence may only contain A, C, G, and T.")
if any(base not in "ACGT." for base in mut):
    raise SystemExit("Error: the mutant sequence may only contain A, C, G, T, or dots (.).")

# Replace each dot in the mutant sequence with the corresponding WT nucleotide.
mut = "".join(wt[i] if mut[i] == "." else mut[i] for i in range(len(wt)))

found = False
for i in range(len(wt)):
    if wt[i] != mut[i]:
        found = True
        position = start + i             # CDS nucleotide position, starting from 1
        codon = (position - 1) // 3 + 1  # Codon number
        inside = (position - 1) % 3 + 1  # Nucleotide position within the codon
        left = i - (inside - 1)          # Codon's starting index in the input string

        print(f"\nSingle-site change: c.{position}{wt[i]}>{mut[i]}")
        print(f"Codon {codon}, nucleotide {inside} within the codon")
        if 0 <= left and left + 3 <= len(wt):
            print(f"Codon change: {wt[left:left + 3]} -> {mut[left:left + 3]}")
        else:
            print("Part of this codon lies outside the input segment. Please include the adjacent sequence.")

if not found:
    print("No differences found within the input segment.")

# Screenshot example: enter the following three lines in order, without the # symbols.
# 181
# ACAAACTACAATGCTGGAGACAGAAGCACTGATTATGGGATATTTCAGATCAATAGCCGC
# ACAAACTACAATGCTGGAGACAGAAGCACTGATTATGGGACATTTCAGATCAATAGCCGC
# Expected: CDS position 221, T -> C; codon 74, nucleotide 2; ATA -> ACA.
# If multiple differences are present, this program reports each one separately.
# It does not combine them into a complete HGVS variant description.