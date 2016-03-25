# Malpractice claims analysis (1991-2012)
A product of _HappyData_ initiative

-----

## Data source: 
NPDB (National Practitioner Data Bank) Medical Malpractice dataset, US Department of Health and Human Services

Downloaded via Engima:
https://app.enigma.io/table/us.gov.hhs.npdb.report-ful


## Code:
https://github.com/HappyDataOrg/health-malpractice

## Code and data details
Data file used in the analysis is `data/enigma-us.gov.hhs.npdb.report-full.csv`. 
Python code is in `notebooks\Malpractice.ipynb`: it contains data selection, cleansing, aggregation, analysis and visualizations.

Note that the code uses a helper library module.

## Findings:
   * [Visual analysis](https://public.tableau.com/profile/michael.kishelev#!/vizhome/MalpracticeClaims_1991-2011/MalpTrendsstory) - posted at Tableau Public
   
   * Payment totals have gone up from 1992-2004, then peaked and decreased in later years
   * A few states dominate the payment cases on all metrics, partly because of large population but also lack of caps on punitive damages. For example, NY, IL, MA and PA clearly stand out, while CA and TX are proportionately lower (as compared to their populations), as they place a 250,000 cap on non-economic damages.
   * Over time, there seems to be a notable increase in non-payment resolutions, such as license suspension and probation for medical professionals

## Notes and further questions:
   * No attempt has been made to verify the data quality and check against other sources. For example, some individual payments appear very large, which can be verified against news sources and court filings
   
   * Available data does not break down by specialty (e.g. OB/gyn), so only high-level detail is avaialble by title (MD, OD, DDS, etc)
   
   * It would be informative to correlate patterns to changes in malpractice premiums. Data may be available in Apr 2016.
   
## References:
   * [NPDB - who reports what](http://www.npdb.hrsa.gov/hcorg/whatYouMustReportToTheDataBank.jsp#reportableActions)

   * [NPDB guidebook](http://www.npdb.hrsa.gov/resources/aboutGuidebooks.jsp?page=EOverview.jsp#collapseTwo)

   * [Damages caps by state](http://www.nolo.com/legal-encyclopedia/state-state-medical-malpractice-damages-caps.html)
   