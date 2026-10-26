# Visual Audit Note

## Plot Question

How does mean BMI vary by income group across NHANES survey cycles in the prepared classroom dataset?

## Issues Checked

| Issue | Category | Why it matters | Correction |
|---|---|---|---|
| The original y-axis only shows BMI values from 24 to 28. | Design | A narrow axis can make small BMI differences look much larger. | Use a clearly labelled BMI axis. The revised plot uses a zoomed scale to show small differences, and this choice is explained in the caption. |
| The original title says low income drives obesity. | Interpretation | Descriptive data cannot prove that income causes obesity. | Use a neutral title describing mean BMI by income group. |
| The original plot only shows two NHANES cycles. | Correctness | Two data points cannot show what happened in the cycles between them. | Include the available cycles with sufficient observations and avoid unsupported trend claims. |
| The subtitle specifies adults aged 20–80, but the original code does not filter by age. | Correctness | The population described may not match the data used. | Filter the data to participants aged 20–80. |
| Missing values, survey weighting, and group sizes are not explained. | Bias / Aggregation | Readers may assume all records were included and the results represent the US population. | Disclose missing values, describe the analysis as unweighted, and exclude groups with fewer than 30 observations. |

## Final Caption

This figure shows unweighted mean BMI (kg/m²) by income group across NHANES cycles for adults aged 20–80 in the prepared NHANES classroom dataset. Records with missing BMI, Age, IncomeGroup, or Cycle were excluded, along with income-by-cycle groups with fewer than 30 observations. The BMI axis is zoomed to show small differences, which may make them appear larger; these descriptive results do not establish causation or provide nationally representative estimates.

## AI-Use Check

ChatGPT helped me check the problems i found in the original plot, and helped me generate the explaination to a more acdemic way. Copilot helped check and explain the errors in code. I checked the issues against the provided R code, the generated plot. 