# WorkSafe Evidence Intelligence

**Reproducible Occupational Safety Analytics and Evidence-Informed Prevention Decision Support**

WorkSafe Evidence Intelligence (WEI) is a planned data science platform for analyzing occupational injury and incident data, exploring patterns in incident narratives, and presenting evidence-linked prevention control options for occupational health and safety professionals and researchers.

The project aims to bridge occupational safety practice, statistical analysis, data engineering, and transparent research methods.

> **Project status:** Product blueprint defined. Initial repository and data-feasibility work are being established. Analytical pipelines, machine learning models, the recommendation engine, and the dashboard are not yet implemented or validated.

## 1. Project Objectives

The long-term objective is to develop a reproducible and transparent platform that helps users explore occupational incident data and examine evidence relevant to workplace injury prevention.

Planned objectives include:

- Collecting and documenting suitable official occupational safety datasets.
- Establishing reproducible data ingestion, validation, and processing workflows.
- Performing exploratory and statistically appropriate analyses.
- Exploring incident narratives using text analysis and evaluated machine learning methods where the data support valid evaluation.
- Maintaining a structured registry of authoritative prevention guidance.
- Presenting source-linked prevention control options with applicability conditions, limitations, and review status.
- Providing an interactive interface for incident exploration, industry analysis, evidence review, and reporting.

These objectives define the intended product scope. Their implementation and validity will be assessed incrementally.

## 2. Planned Data Sources

The following official sources are candidates for the data-feasibility phase. Their available fields, coverage, definitions, access methods, reuse conditions, and suitability for specific research questions must be verified before analytical use.

| Source | Intended role | Official resource |
|---|---|---|
| OSHA Severe Injury Reports (SIR) | Incident-level exploration and narrative analysis | [OSHA SIR](https://www.osha.gov/severe-injury-reports) |
| OSHA Fatality Inspection Data | Separate exploration of fatality-related inspections | [OSHA Fatalities](https://www.osha.gov/fatalities) |
| OSHA Injury Tracking Application (ITA) data | Evaluation of available establishment-level injury and illness data | [OSHA ITA Data](https://www.osha.gov/itadata) |
| BLS Survey of Occupational Injuries and Illnesses (SOII) | Nonfatal occupational injury and illness estimates, counts, and rates | [BLS SOII Data](https://www.bls.gov/iif/nonfatal-injuries-and-illnesses-tables.htm) |
| BLS Census of Fatal Occupational Injuries (CFOI) | Analysis of fatal occupational injury statistics | [BLS CFOI Data](https://www.bls.gov/iif/fatal-injuries-tables.htm) |

The inclusion of a source in this list does not imply that it has already been downloaded, validated, or integrated into the platform.

Each source will be assessed separately. Differences in statistical definitions, reporting coverage, classification systems, and denominators must be documented before comparisons are made.

## 3. Planned Analytical Capabilities

### Data Engineering and Quality

- Source registration and retrieval metadata.
- Preservation of original source snapshots.
- Schema and data-type validation.
- Missing-value, duplicate, and domain checks.
- Documented normalization and transformation rules.
- Data dictionaries, validation reports, and reproducible processing.

### Exploratory and Statistical Analysis

- Incident frequency and distribution analysis.
- Temporal trend exploration.
- Analysis by available industry, event, injury, and geographic categories.
- Comparisons based on compatible definitions and appropriate denominators.
- Explicit documentation of uncertainty and data limitations.

Reported counts will not be presented as exposure-adjusted rates or as direct measures of the underlying risk of an individual workplace.

### Incident Narrative Intelligence

- Text cleaning and exploratory analysis.
- Investigation of available incident classification labels.
- Baseline NLP and machine learning experiments where appropriate.
- Evaluation with suitable metrics and independent test data.
- Error analysis, documentation of label provenance, and model limitations.

A machine learning model will not be treated as valid merely because it produces predictions. Its task, labels, evaluation design, and limitations must be established first.

### Evidence-Linked Prevention Controls

- A structured hazard taxonomy and control catalog.
- An evidence registry containing authoritative source links.
- Candidate control retrieval based on documented rules.
- Alignment with the hierarchy of controls.
- Applicability conditions, cautions, and verification methods.
- Explicit review status and human expert oversight.
- Abstention when evidence is insufficient for a responsible suggestion.

The system is intended to support professional judgment, not replace it.

### Interactive Application

The planned interface includes incident exploration, industry benchmarking, narrative analysis, prevention controls, evidence exploration, data-quality reporting, and methodological documentation.

The interface will be developed after the underlying data and analytical workflows have been established and tested.

## 4. Methodological and Safety Principles

The project follows these principles:

1. **Traceability:** Important results must be linked to their source data, analytical method, and relevant version.
2. **Reproducibility:** Processing and analysis should be repeatable using documented procedures.
3. **Source integrity:** Different datasets must not be combined without justified and documented harmonization.
4. **Statistical responsibility:** Counts, published rates, estimates, denominators, and uncertainty must be distinguished.
5. **Evaluation before deployment:** Models must be evaluated before being considered suitable for use.
6. **Evidence-linked controls:** Prevention control options must include relevant sources, applicability conditions, and limitations.
7. **Human oversight:** Safety-related suggestions require appropriate professional review.

Incident reports alone do not establish causality or provide a valid basis for predicting the probability of a future accident at a specific workplace or for a specific worker.

## 5. Planned Technical Architecture

The intended architecture is modular, with clear boundaries between data processing, analytical methods, evidence management, recommendation logic, and the user interface.

The planned technology stack includes:

- **Programming:** Python
- **Tabular analysis:** Pandas and NumPy
- **Analytical storage and querying:** Parquet and DuckDB, with SQLite where appropriate
- **Statistical and machine learning methods:** Suitable Python scientific libraries, including scikit-learn where appropriate
- **Visualization:** Plotly
- **Dashboard:** Streamlit
- **Quality assurance:** Automated tests, data validation, and reproducible workflows
- **Version control and collaboration:** Git and GitHub
- **Continuous integration:** GitHub Actions as the testing workflow matures

These technologies are planned choices, not a claim that the corresponding components have already been implemented.

## 6. Development Roadmap

Development will follow explicit stages and acceptance criteria rather than a fixed three-month deadline.

1. Establish the project scope and repository.
2. Evaluate source feasibility, schemas, coverage, and data-use conditions.
3. Build data ingestion and validation workflows.
4. Develop descriptive and statistical analyses.
5. Establish analytical data models and query workflows.
6. Evaluate suitable NLP and machine learning baselines.
7. Build the hazard taxonomy, control catalog, and evidence registry.
8. Develop the evidence-based recommendation engine.
9. Implement the interactive application.
10. Complete testing, security checks, documentation, expert review, and deployment.

Each stage must meet its acceptance criteria before dependent components are advanced.

## 7. Reproducibility and Data Governance

The project is intended to maintain clear separation between raw, intermediate, and analysis-ready data.

As the implementation develops, the repository will document:

- Source URLs and retrieval dates.
- Data coverage and known limitations.
- Schema versions and data dictionaries.
- Transformation and validation procedures.
- Code, data, and model or rule versions.
- Tests and quality-assurance results.

Raw datasets, private information, credentials, and other sensitive material must not be committed to the public repository. Data redistribution will be subject to the applicable terms of each source.

## 8. Current Status and Limitations

The project is currently in its initial setup and feasibility stage.

At this stage:

- The product scope and intended architecture have been defined.
- Data-source feasibility remains to be established.
- No analytical results are being claimed.
- No machine learning model has been validated for deployment.
- No prevention recommendation engine or operational dashboard is being presented as complete.

Project documentation will be updated as components are implemented, tested, and evaluated.

## 9. Intended Use and Disclaimer

WorkSafe Evidence Intelligence is intended as an analytical and research decision-support project.

It does not replace workplace-specific risk assessment, qualified HSE judgment, applicable legal requirements, or equipment manufacturers' instructions.

Prevention control options must be interpreted in their relevant operational, technical, and legal context. They must not be treated as guaranteed methods of reducing incidents.

## 10. Repository and Documentation

As the project matures, this repository will contain its implementation, configuration, data documentation, tests, methodology, and supporting reports.

Reproducible execution instructions and technical documentation will be added when the relevant components are available.

---

**Project:** WorkSafe Evidence Intelligence (WEI)  
**Domain:** Occupational Health and Safety · Data Science · Evidence-Informed Prevention  
**Status:** Initial setup and data-feasibility planning
