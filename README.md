# **Hotel Booking Demand**

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
│   │   
│   └── processed/                 # Final datasets
│
├── src/                          # Source code
│   ├── data/                 # Scripts for data exploration and preparation
│   │
│   ├── models/               # Code for models        
│   │
│   └── evaluation.py         # Code for model evaluation
│
├── run_all/                    # Scripts to run full or partial pipelines          
│
├── notebooks/                     # Jupyter notebooks for EDA or visualization
│   └── dataset_description.ipynb   #Description of the several raw data
│
├── results/                       # Generated results like tables and figures
│   ├── tables/
│   ├── reports/
│   └── figures/
│
└── entry_point/                         