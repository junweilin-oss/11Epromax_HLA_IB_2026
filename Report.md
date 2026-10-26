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

<img width="3080" height="1689" alt="image" src="https://github.com/user-attachments/assets/d0935b08-0089-46c8-b466-7ab38ee572fc" />
Figure 1. Alignment of the lysozyme protein sequences of human, dog, and giant panda. Conserved regions and position 74 (Ile in the three species) are marked.

### Structural comparison of human and dog lysozyme

The structures of human WT and dog lysozyme were compared using the superposition provided in the LYZ conservation report of the course (Introduction to Bioinformatics 2026). The global RMSD was 1.54 Å. Both proteins share the same fold: human WT has helices at residues 23–32, 43–53, 98–103, 108–117, and 128–134 and short β-strands at 19–21, 56–58, 60–64, 69–73, and 77–79, whereas the dog has helices at 22–32, 42–54, 99–103, 107–119, and 122–134 and shorter strands at 61–62, 71–72, and 77–78. At 103 of the 129 aligned positions (80%), both proteins have the same secondary structure class.

The local backbone displacement (distance between corresponding α-carbons after superposition) averaged 1.07 Å (Figure 2). The largest values appear in loops (residues 65–68 and 88–91) and at the C-terminus (140–148), reaching 6.25 Å at position 65. At position 74 the displacement is only 0.449 Å, well below the average.

(figure 2) no echa!!!

Figure 2. Local backbone displacement (α-carbon distance, in Å) between human WT and dog lysozyme after structural superposition. Position 74 is shown in red and the dashed line marks the global RMSD (1.54 Å).

## Discussion
The wild-type and mutant sequences of human LYZ differ at a single nucleotide, c.221T>C, which changes codon 74 from ATA to ACA and produces the missense variant p.Ile74Thr. The sequence length is the same and the alignments have no gaps, so the reading frame is not altered and the protein keeps its 148 residues. The mutant matches the same gene and protein as the WT, so the change is a point variant inside LYZ, in agreement with the description of hereditary lysozyme amyloidosis as a disease caused by LYZ variants, among which Ile56Thr (Ile74Thr in the precursor) has been reported (Pepys 1993; Sattianayagam 2012).

Human, dog, and giant panda share 77.7% of their residues, and the dog and the giant panda are more similar to each other (93.2%) than to the human protein (80.4%). All eight cysteines and the two catalytic residues (Glu53 and Asp71) are conserved, whereas the N-terminus, which includes the signal peptide, and several segments (32–41, 96–109, and 132–145) are variable. Between human and dog, 56 codons differ at the nucleotide level but only 29 at the amino acid level, which suggests that changes that alter the amino acid are less tolerated than synonymous ones. Ile74 is identical in the three species and lies inside the longest conserved block (residues 69–89), the same block that contains Asp71, so a change at this position is more likely to matter than a change in a variable region.

Human and dog lysozyme share the same fold, with a global RMSD of 1.54 Å and the same secondary structure class at 103 of 129 aligned positions (80%). The largest local displacements are in loops and at the C-terminus (up to 6.25 Å at position 65), but loops are flexible, so a high displacement there does not mean that the structures are different. At position 74 the human–dog displacement is only 0.449 Å, well below the average (1.07 Å). Therefore, the sequence differences between human and dog (29 of 148 positions) do not break the fold, and conservation of the structure does not require identical sequences.

The Ile74Thr variant replaces isoleucine (aliphatic, neutral, large) by threonine (polar uncharged, neutral, medium). The charge does not change, but the side chain becomes polar and smaller. The backbone moves very little, with a local displacement of 0.225 Å at the variant and a global WT–mutant RMSD of 0.253 Å, lower than the human–dog values (0.449 Å at the same position and 1.54 Å globally). The variant therefore does not distort the backbone, and its effect is probably chemical: a hydrophobic side chain is lost at a conserved position, which can change the interactions with the neighbouring residues. How this leads to the deposition of amyloid cannot be answered with our data.

This study has some limitations. The structural analysis is based on the superposition provided in the course report and on a single ortholog (dog), we did not model the structures ourselves, and we did not calculate the stability of the protein or the interactions of the residue. A small backbone displacement does not rule out consequences for folding or for the interactions of the protein, because changes can be structural, chemical, or both. Finally, our conclusions come from computational analyses only and were not tested experimentally.

## Conclusions
The disease-associated variant is a single nucleotide substitution (c.221T>C) that changes codon 74 from ATA to ACA and causes the missense change p.Ile74Thr (Ile56Thr in the mature protein) in the LYZ gene. The mutant matches the same gene and protein as the WT, there are no insertions or deletions, and the reading frame is not altered.

The comparison of human, dog, and giant panda shows that Ile74 is conserved in the three species and lies inside the longest conserved block of the protein (residues 69–89). The human protein shares 80.4% identity with the dog and the giant panda, and all eight cysteines and the two catalytic residues are conserved.

Human and dog lysozyme have very similar structures (global RMSD 1.54 Å), and the biggest differences are in flexible loops. The variant replaces a conserved hydrophobic residue (Ile) by a polar and smaller one (Thr) but moves the backbone very little (0.225 Å locally and 0.253 Å globally). Therefore, the effect of the variant is probably chemical rather than structural.

Regarding the two questions of the project, (i) the molecular basis of the disease seems to be a chemical change at a conserved position, with no distortion of the backbone, and (ii) the comparison across species shows that this position and its surrounding block are conserved, which suggests that they are important for the function of lysozyme. Further work could include calculations of protein stability, the analysis of other variants such as Trp64Arg or Asp67His, and the comparison with more orthologs.

## Methods
**Data sources**
We used the CDS and protein FASTA files of human WT lysozyme, human mutant lysozyme, dog (Canis lupus familiaris), and giant panda (Ailuropoda melanoleuca), stored in the project repository (GitHub, 11Epromax_HLA_IB_2026). 

**Gene and protein identification.**
The WT CDS and protein were identified with BLAST (NCBI) similarity searches, and the best hits were checked to confirm that the species of the match was the correct one. The gene name, the chromosomal location, the number of exons, and the tissues of expression were taken from the record of the identified gene (Gene ID 4069).

**Variant analysis.**
The mutant sequences were aligned against the WT sequences with BLAST ("Align two or more sequences"), using the WT as the reference, to find the differences at the nucleotide and amino acid levels. The variant was named with the c. (coding DNA) and p. (protein) notation. The codon affected was identified by counting the nucleotides from the start codon, and the variant was classified as synonymous, missense, or nonsense according to its effect on the codon. Because the human protein is a precursor with an 18-residue signal peptide, the position in the mature protein was calculated as the precursor position minus 18 (74 − 18 = 56). The precursor numbering is used throughout the report.

**Conservation across species. **
The CDS and protein sequences of human, dog, and giant panda were aligned with BLAST, using the WT as the reference, to find the differences at the nucleotide and amino acid levels. Identity was calculated as the fraction of identical positions in the alignment, at the protein, codon, and nucleotide levels, for each pair of species. Conserved and variable regions were identified by looking at the positions that were identical or different in the three species. The positions of the catalytic residues and of the cysteines were checked against UniProt (P61626). For the comparison of the human and dog CDS, the synonymous and non-synonymous codon changes and the position of each nucleotide change in the codon were counted.

**Structural analysis. **
The structures of human WT, human mutant, and dog lysozyme were compared using the superposition provided in the LYZ conservation report of the course (Introduction to Bioinformatics 2026). In this report, the structures are superposed and the corresponding residues are aligned. From the report we took the global RMSD, the secondary structure class at each aligned position (α-helix, β-strand, or loop/other), the local backbone displacement (distance between corresponding backbone α-carbons after superposition), and the physicochemical properties of the amino acids (group, charge, and size). Positions without structural data (gaps or unavailable) were not included in the percentages. The local displacement at each position was read from the report and averaged over the aligned positions. For the variant, we took from the report the local backbone displacement at position 74 and the global RMSD between the WT and mutant structures, and we compared them with the human–dog values at the same position. The structural views of the superposition (backbone-displacement coloring, human versus ortholog coloring, and WT versus mutant) come from the same report.

**Reproducibility.**
The sequence files and the results of the analyses are stored in the project repository, so all steps can be repeated.

## Abbreviations
CDS: coding DNA sequence
BLAST: Basic Local Alignment Search Tool
EC: Enzyme Commission number
HLA: hereditary lysozyme amyloidosis
LYZ: lysozyme gene
RMSD: root-mean-square deviation
WT: wild type

## Declarations
Availability of data and materials: The sequence files and the analyses are available in the project repository (GitHub, 11Epromax_HLA_IB_2026). The structural data come from the LYZ conservation report of the course (Introduction to Bioinformatics 2026).
Authors' contributions: Junwei.L  Bioinformatics undergraduate student  GitHub Repository Manager, Structural level: PDB and modelling
Juan.D    Bioinformatics undergraduate student  Gantt and Genetic-level analyzer
Abril     Bioinformatics undergraduate student  Comparison across species (human, C. l. familiaris, and a third species)
Marina    Bioinformatics undergraduate student  Protein level: sequence, properties, domains, conservation

## References
Granel B, Valleix S, Serratrice J, Chérin P, Texeira A, Disdier P, et al. Lysozyme amyloidosis: report of 4 cases and a review of the literature. PubMed PMID: 16523055.
Introduction to Bioinformatics 2026. LYZ conservation report (LYZ_conservation_11DP-E.html). UPC. 
National Library of Medicine.
Pepys MB, Hawkins PN, Booth DR, Vigushin DM, Tennent GA, Soutar AK, et al. Human lysozyme gene mutations cause hereditary systemic amyloidosis. Nature. 1993;362:553–7.
Sattianayagam PT, et al. Hereditary lysozyme amyloidosis – phenotypic heterogeneity and the role of solid organ transplantation. J Intern Med. 2012;272:36–44.
UniProt Consortium. P61626 (LYSC_HUMAN), lysozyme C. https://www.uniprot.org/uniprotkb/P61626.
https://panelapp.genomicsengland.co.uk/panels/502/gene/LYZ/
https://flybase.org/reports/FBhh0000350.html
https://cloud-clone.com/items/B193.html
