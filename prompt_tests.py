trend_analysis_prompt = ChatPromptTemplate.from_template("""
You are a professional financial analyst. 
You will be provided with two json files. 
The first input, 'Income Statement,' contains the Income Statement of company 'A' for the past three years: year 1, year 2, and year 3.
The second input, 'Balance Sheet,' contains the Balance Sheet of company 'A' for the past two years: year 2 and year 3. 

<Task>:
You should identify noticeable time series changes in the financial statements, which may infer the future earnings of the company. 

<Example>:
trend analysis: The company’s revenues have shown a consistent upward trend over the past three years, growing from 16199.0 to 26142.0. This represents a significant increase in sales, indicating a strong market demand for the company’s products or services. However, the cost of goods sold has also increased substantially, from 4443.0 to 12602.0, which could potentially erode profit margins if not managed effectively. Despite this, the gross profit has increased, albeit at a slower pace, suggesting that the company has been able to maintain a degree of pricing power or cost efficiency.

<Inputs>:
Income Statement: 
{Income_Statement}

Balance Sheet:
{Balance_Sheet}
""")

ratio_analysis_prompt = ChatPromptTemplate.from_template("""
You are a professional financial analyst. 
You will be provided with two json files. 
The first input, 'Income Statement,' contains the Income Statement of company 'A' for the past three years: year 1, year 2, and year 3.
The second input, 'Balance Sheet,' contains the Balance Sheet of company 'A' for the past two years: year 2 and year 3. 

<Task>:
Your task is to compute key financial ratios that are useful in predicting future earnings. 
For each ratio, start by stating the formula, then perform the computation using the data provided. 
After computing the ratios, provide economic interpretations of the computed values.
You are not limited to a specific set of ratios. 
Consider operating efficiency, liquidity, and (or) leverage ratios, among others that you deem relevant.

<Example>:
ratio analysis: Operating margin for the current year (t) can be calculated as Operating Income After Depreciation / Sales (net), which equals 7065.0 / 26142.0, resulting in an operating margin of approximately 27.02%. This ratio indicates the percentage of each dollar of revenue that the company retains as operating income after accounting for the cost of goods sold and operating expenses. A higher operating margin is generally favorable as it suggests efficiency in managing costs and the ability to generate profit from sales. The efficiency of the company can be evaluated through the asset turnover ratio, calculated as Sales (net) / Total Asset, which equals 26142.0 / 346288.0, resulting in an asset turnover ratio of approximately 0.08. This ratio measures how efficiently the company uses its assets to generate sales, with a higher ratio indicating better efficiency. Comparing the operating margin of the current year with the previous year, there is a noticeable improvement from the previous year’s operating income after depreciation of 5391.0 and sales of 21325.0, which resulted in an operating margin of approximately 25.28%. This improvement suggests that the company has become more efficient in managing its operating expenses or has gained better pricing power. However, the asset turnover ratio has decreased from the previous year, indicating a relative decline in sales efficiency in utilizing assets. This mixed result of improved operating margin but decreased asset turnover ratio suggests careful monitoring of asset utilization and cost management is required.

<Inputs>:
Income Statement: 
{Income_Statement}

Balance Sheet:
{Balance_Sheet}

"""
)

prediction_prompt = ChatPromptTemplate.from_template("""
<Analyses>:
Trend Analysis of time-series financial statements:
{Trend_Analysis}
Ratio analysis based on financial statements:
{Ratio_Analysis}

<Task>:
Using a company's financial statements, trend analysis, and ratio analysis, you should find clues for predicting the company's future earnings. 
Then, you should make two kinds of prediction. 
- First, you should predict whether the EPS (Earnings per share) of this company in the subsequent period, year 4, will increase or decrease compared to last year's EPS (year 3). If it's increase, write 1, else if it's decrease, write 0. You also need to tell me the confidence score(0~1) in your answer. 
- Second, you should predict magnitude of earnings change(Large, moderate or small).

<Example>:
reason: The prediction of a ‘better’ EPS in the next year is primarily based on the observed revenue growth trend and the improvement in operating margin, which suggests that the company is effectively managing its operating expenses relative to its sales growth. However, the decrease in asset turnover ratio and the substantial increase in the cost of goods sold raise concerns about the efficiency of asset utilization and cost management. These factors introduce some uncertainty into the prediction, hence the moderate level of certainty. The expected change in EPS is considered ‘moderate’ because, while the company shows potential for improved profitability, there are underlying efficiency issues that could temper the magnitude of EPS growth.

Please generate your answer in the following template format, which consists of two analyses, one rationale, and three final predictions. Do not change the format.                                                                  
<Answer Template(max 1024 tokens)>:
1. <Trend Analysis>:max 700 tokens
2. <Ratio Analysis>:max 700 tokens
3. <Rationale for final prediction>: max 500 tokens
4. <Prediction>
- Confidence score for prediction:0 to 1 
- Magnitude of earnings change:large or moderate or small 
- EPS direction:0 or 1
""")