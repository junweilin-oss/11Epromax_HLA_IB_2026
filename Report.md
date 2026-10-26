# HLC DISEASE
Abril César, Marina Cabredo, Juan Ricaurte, Junwei Lin

Intoduction to bioinformatics, UPC
## Abstract
### Background.
Hereditary lysozyme amyloidosis (HLA) is a rare autosomal dominant disease caused by variants of the lysozyme gene (LYZ) that lead to the deposition of amyloid fibrils in several organs. Here we characterise one disease-associated variant at the gene, protein and structural levels and compare it with orthologs.

### Results. 
The wild-type (WT) and mutant coding sequences differ at a single nucleotide, c.221T>C, which changes codon 74 from ATA to ACA and produces the substitution p.Ile74Thr (Ile56Thr in the mature protein). Ile74 is conserved in the dog (Canis lupus familiaris) and in the giant panda (Ailuropoda melanoleuca), which share 80 % sequence identity and 89 % similarity with the human protein. The human and dog structures are very similar (global RMSD 1.54 Å), and the variant position shows a very low backbone displacement between WT and mutant (0.225 Å; global WT–mutant RMSD 0.253 Å).

### Conclusions.
The variant replaces a conserved hydrophobic residue by a polar one without distorting the backbone, so its effect is probably chemical rather than structural.

## Keywords
hereditary lysozyme amyloidosis, LYZ, p.Ile74Thr, sequence conservation, structural superposition

## Backround
Amyloidosis is the name given to a group of diseases linked by abnormal protein folding and deposition of amyloid, whose deposits displace normal tissue and disrupt its function (National Library of Medicine, date last accessed). Hereditary lysozyme amyloidosis (HLA) is one of them: it is inherited in an autosomal dominant manner, mainly affects the gastrointestinal tract, liver, and kidneys, and usually progresses slowly (Sattianayagam 2012). The first disease-causing variants of the lysozyme gene (LYZ) were described in 1993 (Pepys 1993), and variants such as Ile56Thr, Trp64Arg, Asp67His, and Asp67Gly have been reported since (Sattianayagam 2012).

Lysozyme (also called muramidase, EC 3.2.1.17) is an antibacterial enzyme present in saliva, tears, and other body fluids. It hydrolyzes the bonds between N-acetylmuramic acid and N-acetylglucosamine in bacterial peptidoglycan (National Library of Medicine, date last accessed). The human protein is synthesized as a precursor of 148 amino acids that includes an 18-residue signal peptide. For this reason, the variant studied here is called Ile56Thr in the mature protein and Ile74Thr in the precursor (74 − 18 = 56). We use the precursor numbering throughout this report.

In their review, "Lysozyme amyloidosis: report of 4 cases and a review of the literature" by Brigitte Granel , Sophie Valleix, Jacques Serratrice, Patrick Chérin, Antonio Texeira, Patrick Disdier, Pierre-Jean Weiller, Gilles Grateau (PubMed PMID: 16523055), the authors describe clinical manifestations of hereditary lysozyme amyloidosis in four unrelated families, including renal and gastrointestinal symptoms, as well as a severe bleeding event. They also highlight that the disease may be underdiagnosed and can be mistaken for other forms of amyloidosis, emphasizing the importance of identifying the specific amyloid-forming protein to ensure appropriate treatment.
This project asks two questions: (i) how can changes in gene and protein sequence and structure explain the molecular basis of the disease, and (ii) what can the comparison of genes and proteins across species tell us about the affected biological function. To answer them, we analysed the WT and mutant sequences of human LYZ, compared the human protein with the lysozymes of the dog and the giant panda, and examined the structure of the variant.
## Results
### Identification of the gene and protein
To determine the gene and protein associated with the wild-type (WT) coding DNA sequence (CDS) and amino acid FASTA files, we performed sequence similarity analyses using BLAST (Basic Local Alignment Search Tool). During the initial searches, a taxonomic mismatch was identified because the protein sequence was compared with a homologous sequence from a non-human primate. (no acabado)!!!
The WT CDS and the WT protein correspond to the human lysozyme gene (LYZ), which is located at 12q15 on chromosome 12 and has four exons. It is expressed in the stomach, salivary gland, intestine, and seven other tissues, and its product is named lysozyme C precursor. The mutant CDS and the mutant protein match the same gene and the same protein as the WT.

### The variant at the gene and protein levels
Aligning the mutant against the WT sequences revealed a single difference at each level (Table 1). The nucleotide at position 221 is the second base of codon 74 (nucleotides 220–222). The T>C substitution changes the codon from ATA to ACA, so the encoded amino acid changes from isoleucine to threonine. Because the amino acid changes and no stop codon is created, the variant is missense, neither synonymous nor nonsense. The sequence length is unchanged and the alignments contain no gaps, so there are no insertions or deletions and the reading frame is not altered.

Table 1. The disease-associated variant at the gene and protein levels.
| Level | WT | Mutant | Notation |
|---|---|---|---|
| CDS, position 221 | T | C | c.221T>C |
| Codon 74 | ATA | ACA | Second base substitution |
| Protein, position 74 | Ile (I) | Thr (T) | p.Ile74Thr |
| Side chain | Nonpolar, hydrophobic | Polar, hydrophilic | Change in amino acid properties |

### Conservation across species
The WT lysozyme CDS and proteins of human, dog, and giant panda were aligned. All three proteins have 148 residues and the protein alignment contains no gaps (Figure 1). At the protein level, 115 of 148 residues (77.7%) are identical in the three species and 33 positions are variable. The human protein differs from the dog and the giant panda at 29 positions each (80.4% identity), whereas the dog and the giant panda differ at only 10 positions (93.2%; Table 2).

| Pair                  | Protein identity | Codon identity | Nucleotide identity |
|-----------------------|------------------|---------------|---------------------|
| Human vs dog          | 80.4%            | 62.2%         | 83.9%               |
| Human vs giant panda  | 80.4%            | 64.2%         | 84.1%               |
| Dog vs giant panda    | 93.2%            | 82.4%         | 93.5%               |

The most conserved protein regions are residues 21–31 (FERCELARTLK) and 69–89 (STDYGIFQINSRYWCNDGKTP, 21 residues, the longest conserved block), together with segments 56–64, 110–118 (AVACAKRVV), and 123–131. All eight cysteines are conserved, as are the two catalytic residues, Glu53 and Asp71 (UniProt P61626). The most variable regions are the N-terminus, which includes the signal peptide (residues 3–20), and the segments 32–41, 96–109, and 132–145. For example, immediately after the conserved GKTP motif (position 90), human lysozyme has glycine whereas the dog and giant panda have arginine. The same pattern is seen at the CDS level, where the conserved nucleotide stretches (for example, c.61–93 and c.211–263) code for the conserved protein motifs.

Between human and dog, 56 of the 148 codons differ at the nucleotide level, but only 29 differ at the amino acid level. The other 27 codons carry only synonymous changes, most of them at the third codon position (46% of the 72 nucleotide differences, against 39% at the first position and 15% at the second). Consequently, the three species look more similar at the protein than at the codon level (Table 2).

Position 74. Ile74 is identical in the three species and lies inside the longest conserved block (residues 69–89).
## Discussion
[Discuss implications, compare with existing research, and highlight limitations.]
## Conclusions
[State the main conclusions and their significance.]
## Methods
[Provide technical details for reproducibility: Data Sources, Implementation, Statistical
Analysis.]
## Abbreviations
[List abbreviations used, e.g., AI: Artificial Intelligence.]
## Declarations
Availability of data and materials: [Statement on repository/access]
Authors' contributions: [Specify roles]
## References
1. Author A, Author B. Title. BMC Bioinformatics. Year;Vol:Pages
