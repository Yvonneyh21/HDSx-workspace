# Table 1 Audit Note

## Cohort

The analysis included adults aged 20–80 (inclusive). I used `filter(Age >= 20, Age <= 80)` to select the cohort, reducing the dataset from 105,626 to 57,137 rows.

## Missingness

I checked missing values for six variables: BMI, Age, IncomeGroup, Gender, Race, and Cycle before creating Table 1.

## Planted Issues

| Issue | Category | Why it matters | Corrected approach |
|---|---|---|---|
| Incorrect age filter | Correctness | `Age > 20` and `Age < 80` exclude participants aged exactly 20 or 80. | Use `filter(Age >= 20, Age <= 80)`. |
| Variance instead of SD | Correctness | `var()` calculates variance, not standard deviation. | Use `sd()` with `na.rm = TRUE`. |
| Absolute file path | Reproducibility | The local Windows path may not work in another environment. | Use a relative path within the repository. |
| Unsupported interpretation | Interpretation | Statistical significance and causation cannot be concluded from descriptive statistics alone. | Describe differences in mean BMI without claiming significance or causation. |
| Misleading data provenance | Stewardship | The comment incorrectly describes the classroom CSV as freshly downloaded NHANES data. | Identify the prepared classroom dataset and its source accurately. |

## AI-Use Check

ChatGPT helped me organize the R analysis and duble check the planted errors. I verified the cohort counts, missingness results, and Table 1 against the class examples. I also reviewed the starter code and corrected the audit explanations based on the course materials.