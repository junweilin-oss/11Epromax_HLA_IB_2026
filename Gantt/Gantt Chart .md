# Wild Type vs Mutant: understanding hereditary lysozyme amyloidosis

**Project members:** Juan David Ricaurte, Junwei Lin, Abril Cesar, Marina Cabredo  
**Institution:** UPC  
**Date:** 15.09.2026

## Gantt Chart


### WP1 – Project Setup & Planning

| Task ID | Task title | Owner | Start | End | Days | Real duration | Output | Predecessor | Definition of done |
|---|---|---|---|---|---|---|---|---|---|
| T1.1 | Create the Gantt Chart Template | Juan David | 15/09 | 15/09 | 1 | 15 sep-15 sep | Gantt chart template (.xlsx) | - | .xlsx document created with a templete of a general Gantt Chart. |
| T1.2 | Initialize GitHub repository | Junwei Lin | 17/09 | 17/09 | 1 | 17 sep-17 sep | GitHub repository shared with all members | - | Repo created and shared with the members |
| T1.3 | Repository structure | Abril | 17/09 | 17/09 | 1 | 17 sep-17 sep | Repository folder structure with .gitignore, README and report files | T1.2 | Creation of the Gantt, Status and Figures folders in the github repository. Creation of gitignore, readme and report documents. |
| T1.4 | Edit report document | Abril | 17/09 | 17/09 | 1 | 17 sep-17 sep | Report template following the journal format | T1.3 | The report document have the structure of the general format recommended of a magazine |
| T1.5 | Write readme document | Junwei Lin | 17/09 | 17/09 | 1 | 17 sep-17 sep | README document | T1.3 | The document explain what our project is about, why is important to research it and what questions are we gonna answer. |
| T1.6 | Complete the Gantt chart & risk matrix | Juan David & Abril | 22/09 | 08/10 | 13 |  | Completed Gantt chart and risk analysis | T1.1 | Gantt chart + risk analysis committed to repo. |
| M1 | **MILESTONE: Roles & planning approved** | — | 15/09 | 08/10 | 18 | — | — | T1.6 | All members are agree whit scope & plan |

### WP2 – Study the dessease and proteine

| Task ID | Task title | Owner | Start | End | Days | Real duration | Output | Predecessor | Definition of done |
|---|---|---|---|---|---|---|---|---|---|
| T2.1 | Research papers about the desease | All | 01/10 | 04/10 | 4 | 1 oct- 5 oct | Reference list with short notes on the selected papers (max. 3) | - | The group have recolected as maximum 3 papers that allows to understand what is the disesasse about |
| T2.2 | Define analysis folders | Junwei Lin | 04/10 | 04/10 | 1 | 8 oct- 8oct | Documented Git workflow and analysis folder structure | T2.1 | folders data/, gene/, protein/, structure/, species/ created.|
| T2.3 | Define roles | All | 05/10 | 05/10 | 1 | 05 oct- 05 oct | Role assignment table | T2.2 | Each member is clear about their role in the project |
| M2 | **MILESTONE: Disease understood & workflow ready** | — | 01/10 | 05/10 | 5 | 01-08 oct | — | T2.3 | Papers read and folders created in repo |

### WP3 – Gene level analysis

| Task ID | Task title | Owner | Start | End | Days | Real duration | Output | Predecessor | Definition of done |
|---|---|---|---|---|---|---|---|---|---|
| T3.1 | Identify the WT gene with BLASTn (NCBI) | Juan David | 09/10 | 12/10 | 2 |  | Gene identification record (gene, chromosome, locus, accession) | T2.3 | Gene, chromosome, locus and curated RefSeq accession (NM_) of the WT CDS recorded; exons and tissues of expression noted from the NCBI Gene page. |
| T3.2 | Search the mutant CDS with BLASTn and align WT vs mutant CDS | Juan David | 13/10 | 13/10 | 1 |  | CDS alignment and mutation description in c. notation (position, type, effect) | T3.1 | Mutant matches the same gene; mutation located and written in c. notation, with its type (substitution, insertion or deletion) and effect (synonymous, missense, nonsense or frameshift); numbering shared with the team. |
| T3.3 | Summarize gene-level results (figure + summary) | Juan David | 14/10 | 14/10 | 1 |  | Gene-level figure and summary text | T3.2 | Alignment figure and short summary committed to gene/ in the repo. |

### WP4 – Protein level analysis

| Task ID | Task title | Owner | Start | End | Days | Real duration | Output | Predecessor | Definition of done |
|---|---|---|---|---|---|---|---|---|---|
| T4.1 | Identify the WT protein with BLASTp and align WT vs mutant protein | Junwei Lin | 09/10 | 12/10 | 2 |  | Protein identification record and WT vs mutant protein alignment | T2.3 | Protein name, gene and curated RefSeq accession (NP_) recorded; amino-acid change written in p. notation and consistent with the gene-level result of T3.2. |
| T4.2 | Compare WT and mutant amino acids and locate the change in UniProt features | Junwei Lin | 13/10 | 13/10 | 1 |  | Table comparing WT and mutant amino acids, with the change located in UniProt features | T4.1 | Table comparing size, charge and polarity of both amino acids, plus the position of the change relative to domains and known variants (UniProt: Family & Domains, Variant viewer). |
| T4.3 | Summarize protein-level results | Junwei Lin | 14/10 | 14/10 | 1 |  | Protein-level figure and summary text | T4.2 | Figure and short summary committed to protein/ in the repo. |
| M3 | **MILESTONE: Sequence-level analyses done** | — | 09/10 | 14/10 | 5 | — | — | T4.3 & T3.3 | Gene and protein results committed and consistent with each other |

### WP5 – Structure analysis

| Task ID | Task title | Owner | Start | End | Days | Real duration | Output | Predecessor | Definition of done |
|---|---|---|---|---|---|---|---|---|---|
| T5.1 | Find PDB structures from the UniProt ID and choose the best one | Marina | 09/10 | 12/10 | 2 |  | Homolog FASTA files and accession record for the assigned species | T2.3 | BLASTn and BLASTp restricted to the assigned species; correct gene checked; species, gene and accessions recorded and FASTA files saved in species/. |
| T5.2 | Download and inspect the chosen structure | Marina | 13/10 | 13/10 | 1 |  | Homolog FASTA files and accession record for the third species | T5.1 | Third species chosen by the group;species, gene and accessions recorded and FASTA files saved in species/. |
| T5.3 | Superimpose WT vs mutant and describe diferences | Marina | 14/10 | 14/10 | 1 |  | CDS and protein alignments of the three species | T5.2 | Two alignments (CDS and protein) of human, assigned species and third species run and saved in species/. |
| T5.4 | Structural figures and summary | Marina | 15/10 | 15/10 | 1 |  | Structural figures and summary text | T5.3 | Figures and short summary committed to structure/ in the repo. |

### WP6 – Cross-species comparison

| Task ID | Task title | Owner | Start | End | Days | Real duration | Output | Predecessor | Definition of done |
|---|---|---|---|---|---|---|---|---|---|
| T6.1 | Find the homologs (CDS and protein) in the assigned species | Abril | 09/10 | 12/10 | 2 |  | Selected species and validated ortholog list | T2.3 | Third species chosen; orthologs confirmed for human, C. l. familiaris and the third species. |
| T6.2 | Choose a third species and find its homologs (CDS and protein) | Abril | 13/10 | 13/10 | 1 |  | Ortholog FASTA file and multiple alignment | T6.1 | Single FASTA with the three proteins and alignment file committed to species/. |
| T6.3 | Align the three CDS and the three proteins with the BLAST alignment tool | Abril | 13/10 | 13/10 | 1 |  |  |  |  |
| T6.4 | Check conservation of the mutated position and summarize | Abril | 14/10 | 14/10 | 1 |  | Conservation figure and summary text | T6.2 | Conservation of the mutated position described, with a figure and short summary in species/. |
| M4 | **MILESTONE: Structure & cross-species analyses done** | — | 09/10 | 15/10 | 6 | — | — | T6.4 & T5.4 | Structure and species results committed to repo |

### WP7 – Biological integration

| Task ID | Task title | Owner | Start | End | Days | Real duration | Output | Predecessor | Definition of done |
|---|---|---|---|---|---|---|---|---|---|
| T7.1 | Check numbering and results are consistent across levels | Abril | 15/10 | 15/10 | 1 |  | Consistency checklist (mutation name and numbering) | T6.4, T5.4, T4.3 & T3.3 | Same mutation name, position and numbering in all analyses; contradictions listed and resolved. |
| T7.2 | Build causal chain, answer the two research questions and write the discussion | Abril | 15/10 | 15/10 | 1 |  | Discussion section and summary figure | T7.1 | Discussion section and summary figure committed to report/; both research questions answered explicitly. |
| M5 | **MILESTONE: Integration & report draft complete** | — | 15/10 | 15/10 | 1 | — | — | T7.2 | Discussion written and all sections present in the report |

### WP8 – Report & final submission

| Task ID | Task title | Owner | Start | End | Days | Real duration | Output | Predecessor | Definition of done |
|---|---|---|---|---|---|---|---|---|---|
| T8.1 | Write each member's methods and results in the report | All | 16/10 | 19/10 | 2 |  | Methods and Results sections drafted in the report | T7.2 | BLAST and databases described in Methods with the parameters used; findings in Results; FASTA files listed in Declarations; each part committed to the repo. |
| T8.2 | Edit report and figures (style, numbering, references) | Marina | 16/10 | 19/10 | 2 |  | Edited report with unified style, captions and references | T8.1 | Unified style, numbered figures with captions and complete references. |
| T8.3 | Final repository check and submission | Junwei Lin | 19/10 | 20/10 | 2 |  | Final repository version submitted on main | T8.2 | README updated, repo reproducible and clean, final version on main and submitted. |
| M6 | **MILESTONE: Final submission** | — | 16/10 | 20/10 | 4 | — | — | T8.3 | Repository submitted |
