# **Hotel Booking Demand

## **Folder structure**

```text
protein-ligand-interaction-dataset-pipeline
│
├── README.md                     # Project overview
├── .gitignore                    # Files/folders to ignore in git
├── requirements.txt              # Python dependencies
├── environment.yml               # Conda environment
│
├── data/                         # Project data
│   ├── raw/                      # Original, unmodified data
│   │   ├── column_roles.csv/             
│   │   ├── COURSE_RELEASE_FILES_README.txt/       
│   │   ├── DATASET_MANIFEST.yml/     
│   │   ├── hotel_bookings_course_release_v1.csv/ 
│   │   ├── SHA256SUMS.txt/ 
│   │   ├── subsample_indices_v1_n30000_seed12345.txt/ 
│   │   └── referencePaper/ 
│   │
│   ├── interim/                  # Intermediate outputs from pipeline steps
│   │   ├── split_cif_chains/
│   │   ├── fasta_sequences/
│   │   ├── filtered_datasets/    # Filtered CSV/XLSX outputs
│   │   └── interaction_details_csv_cif/
│   │
│   └── processed/
│       ├── binary_interactions_csv/
│       ├── esm_embeddings/                # Final ML-ready datasets
│       └── mordred_descriptors/
│
├── src/                          # Source code
│   ├── pipeline/                 # Stepwise scripts organized by pipeline steps
│   │   ├── 01_pdb_download/
│   │   ├── 02_cif_protein_chain_and_ligand_extraction/
│   │   ├── 03_filtering/
│   │   ├── 04_expand_filter_merge_ligand_data/
│   │   ├── 05_filter_cif_fasta_by_ligands/
│   │   ├── 06_interaction/
│   │   ├── 07_embeddings_ESM2/
│   │   ├── uniprot_mappings/
│   │   ├── covalent_bonds/
│   │   └── binding_affinity/
│   │
│   ├── features/                    # Code for embeddings/descriptors
│   │   ├── esm_embeddings.py
│   │   └── mordred_descriptors.py                 
│   │
│   └── config.py                 # Global configuration and parameters
│
├── pipelines/                    # Scripts to run full or partial pipelines
│   ├── run_dataset_pipeline.py
│   ├── run_embedding_pipeline.py
│   └── run_full_pipeline.py                  
│
├── models/                       # Saved ML models (future work)
│
├── notebooks/                     # Jupyter notebooks for EDA or visualization
│   ├── exploratory_analysis.ipynb
│   └── dataset_statistics.ipynb
│
├── results/                       # Generated results like tables and figures
│   ├── tables/
│   └── figures/
│
├── tests/                         # Unit or integration tests (optional)
│
└── docs/                          # Additional documentation
    ├── pipeline_overview.md
    ├── dataset_description.md
    └── methodology.md
```