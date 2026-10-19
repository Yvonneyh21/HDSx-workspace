
def summarize_bmi(data):
    """Summarize BMI by income group and gender."""

    clean_data = data.dropna(
        subset=["BMI", "IncomeGroup", "Gender"]
    )

    summary = (
        clean_data
        .groupby(["IncomeGroup", "Gender"])["BMI"]
        .agg(["count", "mean", "std"])
        .reset_index()
    )

    return summary
