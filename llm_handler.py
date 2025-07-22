def convert_question_to_sql(question: str) -> str:
    q = question.lower()
    if "total sales" in q:
        return "SELECT SUM(total_sales) FROM total_sales;"
    elif "roas" in q:
        return "SELECT SUM(ad_sales) / SUM(ad_spend) FROM ad_sales;"
    elif "highest cpc" in q:
        return "SELECT item_id, MAX(ad_spend * 1.0 / clicks) AS cpc FROM ad_sales;"
    else:
        return "SELECT 'Sorry, I did not understand the question.';"
