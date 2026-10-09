# Disease Project - Risk Assessment Matrix

Risk = Likelihood × Impact. Scale: 1–3. Levels: 1–2 Low, 3–5 Medium, 6–9 High.

> This Markdown file contains static values from the Excel workbook. Scores, levels, statements and heat-map counts do not update automatically when edited here.

## Summary

| Level | Number of risks |
| --- | --- |
| High risks | 5 |
| Medium risks | 7 |
| Low risks | 0 |
| Total risks | 12 |

## Risk Matrix

| ID | Risk | Work package | Related tasks | Owner | Likelihood (1-3) | Impact (1-3) | Score | Level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | the disease is not fully understood from only 3 papers | WP2 - Disease | T2.1 | All | 1 | 3 | 3 | Medium |
| R2 | the WT and mutant CDS files are not valid or their translation does not match the protein FASTA | WP3 - Gene | T3.1 | Juan David | 2 | 3 | 6 | High |
| R3 | the mutation is hard to locate in the CDS alignment (several differences, indels or ambiguous position) | WP3 - Gene | T3.2 | Juan David | 2 | 2 | 4 | Medium |
| R4 | the mutation barely changes the physicochemical properties, so the effect is hard to explain | WP4 - Protein | T4.2 | Junwei Lin | 2 | 2 | 4 | Medium |
| R5 | no suitable PDB structure exists for the WT or the mutant protein | WP5 - Structure | T5.1 | Marina | 3 | 2 | 6 | High |
| R6 | the modelled mutant structure has low quality and cannot be trusted | WP5 - Structure | T5.2 | Marina | 2 | 3 | 6 | High |
| R7 | the superposition shows very small or unclear differences around the mutation | WP5 - Structure | T5.3 | Marina | 2 | 2 | 4 | Medium |
| R8 | orthologs cannot be validated for the third species | WP6 - Species | T6.1 | Abril | 2 | 2 | 4 | Medium |
| R9 | the mutated position is not conserved or the alignment is poor around it | WP6 - Species | T6.2, T6.3 | Abril | 2 | 2 | 4 | Medium |
| R10 | the numbering and mutation name are inconsistent between CDS, protein, UniProt and PDB | WP7 - Integration | T4.1, T5.3, T7.1 | All | 3 | 3 | 9 | High |
| R11 | the results of the different levels do not agree and the causal chain is not supported | WP7 - Integration | T7.2 | Abril | 2 | 3 | 6 | High |
| R12 | the report is not finished or consistent in the last four days | WP8 - Report | T8.1, T8.2 | All | 2 | 2 | 4 | Medium |

## Risk Details

<details>
<summary>R1 — the disease is not fully understood from only 3 papers</summary>

**Why we have realized it**

the whole project depends on understanding the disease and we are limited to a maximum of 3 papers

**Contingency plan**

every member reads the papers, we cross-check key facts in UniProt/OMIM, and we ask the instructors if the causal chain is unclear

**Risk statement**

Our identified risk is the disease is not fully understood from only 3 papers, we have realized because the whole project depends on understanding the disease and we are limited to a maximum of 3 papers; our contingency plan consists of every member reads the papers, we cross-check key facts in UniProt/OMIM, and we ask the instructors if the causal chain is unclear.

</details>

<details>
<summary>R2 — the WT and mutant CDS files are not valid or their translation does not match the protein FASTA</summary>

**Why we have realized it**

every later analysis (gene, protein, structure, species) starts from these sequences

**Contingency plan**

we re-download the sequences from the original database, check ATG, stop codon and reading frame, and ask the instructors before continuing

**Risk statement**

Our identified risk is the WT and mutant CDS files are not valid or their translation does not match the protein FASTA, we have realized because every later analysis (gene, protein, structure, species) starts from these sequences; our contingency plan consists of we re-download the sequences from the original database, check ATG, stop codon and reading frame, and ask the instructors before continuing.

</details>

<details>
<summary>R3 — the mutation is hard to locate in the CDS alignment (several differences, indels or ambiguous position)</summary>

**Why we have realized it**

the WT and mutant sequences may differ in more than one position or use different numbering

**Contingency plan**

we use a second alignment tool, check the codon change manually, and compare the result with the protein alignment of WP4

**Risk statement**

Our identified risk is the mutation is hard to locate in the CDS alignment (several differences, indels or ambiguous position), we have realized because the WT and mutant sequences may differ in more than one position or use different numbering; our contingency plan consists of we use a second alignment tool, check the codon change manually, and compare the result with the protein alignment of WP4.

</details>

<details>
<summary>R4 — the mutation barely changes the physicochemical properties, so the effect is hard to explain</summary>

**Why we have realized it**

a single amino-acid change often gives very small differences in MW, pI, GRAVY or instability index

**Contingency plan**

we complement the table with the position of the change in the domains, a substitution matrix (e.g. BLOSUM62), conservation and the structural results

**Risk statement**

Our identified risk is the mutation barely changes the physicochemical properties, so the effect is hard to explain, we have realized because a single amino-acid change often gives very small differences in MW, pI, GRAVY or instability index; our contingency plan consists of we complement the table with the position of the change in the domains, a substitution matrix (e.g. BLOSUM62), conservation and the structural results.

</details>

<details>
<summary>R5 — no suitable PDB structure exists for the WT or the mutant protein</summary>

**Why we have realized it**

experimental structures that contain exactly this mutation are often not available

**Contingency plan**

we use the closest WT structure and build the mutant by in silico mutagenesis or homology modelling (e.g. SWISS-MODEL, AlphaFold)

**Risk statement**

Our identified risk is no suitable PDB structure exists for the WT or the mutant protein, we have realized because experimental structures that contain exactly this mutation are often not available; our contingency plan consists of we use the closest WT structure and build the mutant by in silico mutagenesis or homology modelling (e.g. SWISS-MODEL, AlphaFold).

</details>

<details>
<summary>R6 — the modelled mutant structure has low quality and cannot be trusted</summary>

**Why we have realized it**

obtaining the mutant structure is the most technical step of the structure analysis

**Contingency plan**

we run a basic quality check (e.g. pLDDT, Ramachandran), try a second modelling method, and describe the limits of the model in the report

**Risk statement**

Our identified risk is the modelled mutant structure has low quality and cannot be trusted, we have realized because obtaining the mutant structure is the most technical step of the structure analysis; our contingency plan consists of we run a basic quality check (e.g. pLDDT, Ramachandran), try a second modelling method, and describe the limits of the model in the report.

</details>

<details>
<summary>R7 — the superposition shows very small or unclear differences around the mutation</summary>

**Why we have realized it**

a single substitution usually produces local changes that are small compared with the whole protein

**Contingency plan**

we measure distances, contacts and hydrogen bonds around the mutation (not only the global RMSD) and describe also the absence of large changes

**Risk statement**

Our identified risk is the superposition shows very small or unclear differences around the mutation, we have realized because a single substitution usually produces local changes that are small compared with the whole protein; our contingency plan consists of we measure distances, contacts and hydrogen bonds around the mutation (not only the global RMSD) and describe also the absence of large changes.

</details>

<details>
<summary>R8 — orthologs cannot be validated for the third species</summary>

**Why we have realized it**

the third species is not selected yet and orthology must be confirmed in human, C. l. familiaris and the new species

**Contingency plan**

we prepare 2-3 alternative candidate species in advance and switch to the next one if the orthology cannot be confirmed

**Risk statement**

Our identified risk is orthologs cannot be validated for the third species, we have realized because the third species is not selected yet and orthology must be confirmed in human, C. l. familiaris and the new species; our contingency plan consists of we prepare 2-3 alternative candidate species in advance and switch to the next one if the orthology cannot be confirmed.

</details>

<details>
<summary>R9 — the mutated position is not conserved or the alignment is poor around it</summary>

**Why we have realized it**

the three species may be distant and the region of the mutation may be variable

**Contingency plan**

we test a second multiple alignment tool (e.g. MUSCLE, Clustal Omega), check nearby residues, and explain what it means for the interpretation

**Risk statement**

Our identified risk is the mutated position is not conserved or the alignment is poor around it, we have realized because the three species may be distant and the region of the mutation may be variable; our contingency plan consists of we test a second multiple alignment tool (e.g. MUSCLE, Clustal Omega), check nearby residues, and explain what it means for the interpretation.

</details>

<details>
<summary>R10 — the numbering and mutation name are inconsistent between CDS, protein, UniProt and PDB</summary>

**Why we have realized it**

each database and file can use a different numbering (signal peptides, isoforms, tags), so the same mutation may appear at different positions

**Contingency plan**

we define one reference sequence and numbering from the start, record every offset in the consistency checklist, and fix contradictions before writing the report

**Risk statement**

Our identified risk is the numbering and mutation name are inconsistent between CDS, protein, UniProt and PDB, we have realized because each database and file can use a different numbering (signal peptides, isoforms, tags), so the same mutation may appear at different positions; our contingency plan consists of we define one reference sequence and numbering from the start, record every offset in the consistency checklist, and fix contradictions before writing the report.

</details>

<details>
<summary>R11 — the results of the different levels do not agree and the causal chain is not supported</summary>

**Why we have realized it**

gene, protein, structure and species results are produced by different members and joined only at the end

**Contingency plan**

we compare the results at milestones M3 and M4, explain the differences honestly in the discussion, and answer the two research questions only with supported evidence

**Risk statement**

Our identified risk is the results of the different levels do not agree and the causal chain is not supported, we have realized because gene, protein, structure and species results are produced by different members and joined only at the end; our contingency plan consists of we compare the results at milestones M3 and M4, explain the differences honestly in the discussion, and answer the two research questions only with supported evidence.

</details>

<details>
<summary>R12 — the report is not finished or consistent in the last four days</summary>

**Why we have realized it**

the results sections, figures and references have to be written and unified between 16 and 19 October

**Contingency plan**

each owner starts writing their section during their analysis, we agree figure style and reference format in advance, and we keep one day for the final edit

**Risk statement**

Our identified risk is the report is not finished or consistent in the last four days, we have realized because the results sections, figures and references have to be written and unified between 16 and 19 October; our contingency plan consists of each owner starts writing their section during their analysis, we agree figure style and reference format in advance, and we keep one day for the final edit.

</details>

## Risk Heat Map (number of risks per cell)

Counts are the static results from the Risk Matrix above.

| Likelihood / Impact | 1 - Minor | 2 - Moderate | 3 - Severe |
| --- | --- | --- | --- |
| 3 - Very likely | 0 | 1 | 1 |
| 2 - Possible | 0 | 6 | 3 |
| 1 - Unlikely | 0 | 0 | 1 |

Risk levels by cell:

| Likelihood / Impact | 1 - Minor | 2 - Moderate | 3 - Severe |
| --- | --- | --- | --- |
| 3 - Very likely | Medium (3) | High (6) | High (9) |
| 2 - Possible | Low (2) | Medium (4) | High (6) |
| 1 - Unlikely | Low (1) | Low (2) | Medium (3) |

## Scoring scales

| Value | Likelihood | Impact |
| --- | --- | --- |
| 1 | Unlikely | Minor: small delay, easy to fix |
| 2 | Possible | Moderate: affects one task or deliverable |
| 3 | Very likely | Severe: affects several work packages or the final grade |

| Level | Score range |
| --- | --- |
| Low | 1-2 |
| Medium | 3-5 |
| High | 6-9 |
