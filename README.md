# unicef-assignment
ANC4 &amp; SBA Coverage Analysis

# Positions Applied For

 Learning and Skills Data Analyst Consultant :Req.#581598  
 Household Survey Data Analyst Consultant :Req#581656  
 Administrative Data Analyst :Req#581696  
 Microdata Harmonization Consultant :Req#581699

 This project aims at calculating Population Weighted Coverage where the key concepts used are:
-Automation: Modular pipeline with reusable code such that scripts are executed sequentially in clean order.
-Antenatal care 4+ visits:percentage of women (aged 15-49 years) attended at least four times during pregnancy by any provider.
Skilled birth attendant:percentage of deliveries attended by skilled health personnel.
-Group-based comparison: Compares coverage across “On-track” and “Off-track” country groups.

# Project Structure

anc4-sba-coverage-analysis/
├── data/
│   ├── outputs/              # Output CSVs and results from the analysis
│   │   └── coverage_summary.csv
│   ├── processed/            # Cleaned datasets after preparation steps
│   └── raw/                  # Raw input data files (CSV, Excel, etc.)
│
├── notebooks/                # Modular notebooks for each pipeline stage
│   ├── data_preparation.ipynb       # Loads raw data, extracts ISO codes
│   ├── data_cleaning_exploration.ipynb  # Cleans datasets, harmonizes schema
│   ├── merge_and_analysis.ipynb     # Merges data and computes weighted coverage
│   └── generate_report.ipynb        # Generates an HTML report with plot
│
├── report/
│   └── coverage_report.html  # Final HTML report with visualizations
│
├── templates/
│   └── report_template.html  # HTML template used for report generation
│
├── run_project.py            # Main script to automate full pipeline
├── user_profile.py           # Reusable utility functions
├── requirements.txt          # List of required Python dependencies
├── .gitignore
└── README.md

# Project Execution Steps:
PREREQUISITES: Python 3.7 or higher needs to be installed
RUN: pip install -r requirements.txt
RUN: pip install ipykernel (Ensure your Jupyter kernel is properly installed and available)
RUN: python -m ipykernel install --user
Validate Jupyter Kernel RUN: jupyter kernelspec list
RUN: python run_project.py


# Folder Description:

# 1)Notebooks:
Contains modular Jupyter notebooks representing each step of the pipeline: data preparation, cleaning, analysis, and reporting. Each notebook is designed to be reusable, independently executable, and aligned with a clean project structure.

A)data_preparation.ipynb: Loads raw datasets (ANC4, SBA, tracking status, and population estimates), extracts and standardizes ISO3 country codes. Filters data to retain only countries present across all datasets and saves the cleaned subsets to data/processed/

B)data_cleaning_exploration.ipynb: Performs data quality checks on the cleaned datasets by identifying missing values and duplicates. Ensures all required fields for population-weighted analysis are intact, allowing safe progression to analysis steps.

C)merge_and_analysis.ipynb:This notebook merges filtered indicator data with birth projections and U5MR track status. It selects the most recent ANC4 and SBA values (2018–2022) per country and merges them with 2022 birth estimates. Countries are grouped into "On-track" or "Off-track" based on U5MR classification. Population-weighted averages for ANC4 and SBA are then computed per group and saved for reporting.

D)generate_report.ipynb:generate_report.ipynb:This notebook generates an HTML report by plotting population-weighted ANC4 and SBA coverage by group.
It embeds both the summary table and the bar chart into a pre-defined HTML template and the final report is saved in the report/ directory for easy sharing or publishing.

# 2)data/ directory: 
Organizes all datasets used in this project.
-raw/ contains the original input files sourced from (1) UNICEF Global Data Repository at the country level for 2018–2022, (2) UN World Population Prospects 2022 (WPP2022) for population projections, and (3) an Excel file for under-five mortality classifications used to group countries as on-track or off-track.

-processed/ includes cleaned datasets with standardized ISO3 codes, filtered for countries common across all data sources.

-outputs/ holds final results i.e population-weighted ANC4 and SBA coverage summaries.

All datasets are harmonized to ensure consistent country coverage and indicator formatting throughout the pipeline.

# 3)report/
Contains the final rendered HTML output generated from the analysis pipeline.
The file coverage_report.html presents the population weighted coverage results in a visual,shareable format.This folder acts as the destination for final reports ready for stakeholders.

# 4)templates/
This folder stores the reusable HTML template (report_template.html) used to generate the final report.The template includes placeholders for embedding the coverage data table and the seaborn-generated plot.It is designed for automation of reporting in a structured and consistent layout.

# 5)requirements.txt:
 It provides a list of all required Python packages for setting up the environment.This step ensures reproducbility across collaborators.

# 6)user_profile.py: 
This script helps us to code run smoothly on any system.It does this by managing all the important folder paths(raw data, processed files, reports,and templates are stored) in one place using smart relative paths.This way we do not have to hard-code the file paths. Function called load_file()is created which knows how to open both CSV and Excel files. 

# 7)run_project.py: 
It runs the Whole Project in one go.We do not have to open and run each notebook one by one, run_project.py takes care of everything in the right order i.e from loading the raw data, cleaning it, doing the analysis, and finally creating the HTML report.
Command : python run_project.py 
It executes all notebooks in order,saves processed datasets to data/processed/,
outputs the final summary and chart to data/outputs/, generates the HTML report and saves it to the report/ folder.