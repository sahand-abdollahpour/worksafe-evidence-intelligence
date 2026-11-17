
# Data Notes: OSHA Severe Injury Reports (SIR)

Working notes on the raw data snapshot used in this project. Each entry records what was checked and what was found, so that later decisions can be traced. Counts below were produced by the code in `src/inspect_raw_archive.py`.

## 1. Source and snapshot

| Item | Value |
|---|---|
| Source | OSHA Severe Injury Reports, <https://www.osha.gov/severe-injury-reports> |
| Archive | `January2015toNovember2025.zip` (16,224,511 bytes) |
| Contents | one CSV, `January2015toNovember2025.csv` (57,403,269 bytes) |
| Rows x columns | 105,996 x 28 |
| Event date range | 2015-01-01 to 2025-11-30 |
| Downloaded on | `TODO: YYYY-MM-DD` |
| SHA-256 of the ZIP | `TODO: output of Get-FileHash -Algorithm SHA256` |

The raw files are kept locally in `data/raw/` and are not committed to Git.

## 2. What the data covers

According to OSHA, the reports cover severe injuries (amputation, in-patient hospitalization, or loss of an eye) that employers must report since 1 January 2015 under 29 CFR 1904.39, and represent incidents under federal OSHA jurisdiction. Work-related fatalities are not part of this dataset.

## 3. Loading rules

- `Primary NAICS`, `Inspection` and `Zip` are read as strings. Without this, pandas reads them in mixed types (`DtypeWarning`) and drops the leading zero of ZIP codes (`07424` becomes `7424.0`).
- `EventDate` is parsed with the explicit format `%m/%d/%Y`. All 105,996 values parse without errors.
- Missing values: `Primary NAICS` 2, `Zip` 24, `Inspection` 70,526.

## 4. Record keys

- `UPA` is unique and is used as the record key.
- `ID` is **not** unique: 10 rows share an `ID` value, in 5 pairs. Within each pair the records differ in `UPA`, state and event date, so they are separate incidents, not duplicates. All affected IDs begin with `201501` and all events are in January 2015. No rows are removed.

## 5. Text cleaning

Leading, trailing and repeated spaces made identical categories count as different values. After trimming and collapsing whitespace, the number of distinct values changed as follows:

| Column | Before | After |
|---|---|---|
| `EventTitle` | 649 | 568 |
| `NatureTitle` | 349 | 303 |
| `Part of Body Title` | 275 | 211 |
| `SourceTitle` | 1,957 | 1,714 |
| `Secondary Source Title` | 1,662 | 1,493 |
| `Employer` | 71,454 | 70,572 |

## 6. `FederalState`

| Value | Rows |
|---|---|
| 1 | 103,504 |
| 0 | 2,492 |

- The column splits **states**, not rows: no state has both values.
- The 22 jurisdictions with value `0` (Alaska, Arizona, California, Hawaii, Indiana, Iowa, Kentucky, Maryland, Michigan, Minnesota, Nevada, New Mexico, North Carolina, Oregon, Puerto Rico, South Carolina, Tennessee, Utah, Vermont, Virginia, Washington, Wyoming) match OSHA's published list of the 22 State Plans that cover both private and public workplaces.
- The meaning of the column is not defined in the OSHA documentation found so far. Reading it as a state-plan indicator is therefore a working hypothesis, and it is unclear why these records appear in a federal-jurisdiction dataset.
- Consequence: report counts are **not comparable across states** (for example California has 539 records, Texas 17,491). Analyses should be run on all rows and, as a check, on `FederalState == 1` only.

## 7. Other observations

- `Hospitalized` and `Amputation` count workers per report (values above 1 occur), they are not 0/1 flags.
- 2025 covers only January to November and must not be compared with full years.

## 8. Open items

- Check the consistency of the event labels (`Event` code vs `EventTitle`). Preliminary check: 476 distinct codes, many mapping to more than one title, and many with very few records. To be re-verified in code before any classification work.
- Confirm the definition of `FederalState` (OSHA documentation or OSHA contact).
- Review the 66 repeated narratives.