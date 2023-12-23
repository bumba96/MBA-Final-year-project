# MBA-Final-year-project
Empirical Results
In this Chapter, we present the empirical results making use of the data ob-
tained from Yahoo Finance [9] encompassing a 5-year period of daily adjusted
closing prices of the two flagship Indian stock market indices, namely, S&P
BSE SENSEX and NIFTY 50, spanning from October 17, 2018 to October
13, 2023. The former, commonly known as SENSEX, is a benchmark index of
30 of India’s largest and most liquid public companies. The companies that
make up the SENSEX (which was launched in 1986) are chosen from the
companies listed in the Bombay Stock Exchange (BSE) (operated by S&P)
and is float-adjusted as well as market capitalization-weighted. Similarly,
NIFTY 50 is a benchmark Indian stock market index that represents the
weighted average of 50 of the largest Indian companies listed on the National
Stock Exchange (NSE), and was launched in 1996. For the purposed of asset
management, these two indices play a vital role in a spectrum of areas such
as benchmarking fund portfolios, index-based derivatives and index funds.
Both the indices include companies from diverse sectors and hence is a good
representative of the state of Indian economy. However, the weightage given
to each sector may vary between the two indices and the base year, as well
20
as market representation for both the indices vary too.
After extracting the data for both the indices, it was meticulously orga-
nized in ascending chronological order, with the adjusted closing prices of
both indices recorded alongside their respective dates. To calculate the daily
returns, a straightforward approach utilizing simple historical returns was
employed, owing to its portfolio additive nature. This methodology aligns
with our goal of constructing a portfolio from the selected indices for further
analysis.
Now, to understand each of the methods associated with calculation of
VaR (discussed in Chapter 3), we have implemented the methods on this
5-year historical index data and created three separate models to calculate 1-
day, 5-day and 10-day VaR, with different confidence intervals. The software
used for this study is Google Colab notebooks. The programming language
used was Python, where we started off by importing the necessary libraries,
which include (for our study) “NumPy, Pandas, datetime, y finance, mat-
plotlib and SciPy”.
4.1 Historical Method
The historical approach for calculating VaR relies on past data to estimate
the potential loss which a portfolio may face within a certain confidence
level, over a specified time horizon. We have adopted the following steps to
implement this approach on our data set.
(A) Step 1: Time range of the data (5 years) was selected for both the
indices, SENSEX and NIFTY 50 and it was extracted from the Yahoo
Finance website into the Python notebook.
(B) Step 2: Calculation of daily simple returns was done for both the indices.
21
(C) Step 3: Weights were assigned to each index to create a portfolio of
investment. For our study, we have taken an equally weighted portfolio
of SENSEX and NIFTY 50.
(D) Step 4: Historical portfolio daily returns were calculated for the equally
weighted portfolio.
(E) Step 5: For a T -day VaR, we converted daily returns to T -day returns.
This can be done by summing up every T consecutive daily returns.
This gives us the total return over each T -day period.
(F) Step 6: Returns were sorted in ascending order (most negative to most
positive) and confidence interval (which is “1-minus-Significance level”)
was set.
(G) Step 7: VaR was calculated by taking the return from the sorted list
which represents the percentage significance level (1%, if confidence in-
terval is 99%) of returns above it.
Initially, we calculated 1-day VaR with 99% confidence interval from the
5-year historical daily returns data and the histogram distribution for the
same is shown below in Figure 4.1
Next, we calculated a series of VaR percentage values for different combi-
nations of time period and confidence interval and the results are tabulated
in Table 4.1.
4.2 Variance-Covariance Method
The Variance-Covariance method of calculating VaR is an approach that uses
the statistical measures of mean (expected return) and standard deviation
(volatility) of an investment’s returns to estimate the VaR. It assumes that
returns are normally distributed and uses the covariance matrix to account
for the correlation between different investments in a portfolio. For this
method, Step 1 to Step 5 remains same as discussed in historical approach,
which is followed by the enumerated subsequent steps.
(A) Step 6: We calculate the portfolio mean and standard deviation. For
mean or expected return calculation we take the average of all the daily
23
returns of the portfolio. To calculate standard deviation, we take the
square root of portfolio variance which in turn is calculated by the co-
variance matrix
(B) Step 7: We set up a confidence interval and calculate the VaR using the
formula:
V ar(X) = μ + zα(1 − α)σ,
μ is the portfolio expected return, (1 − α) is the significance level, zα
is the z-score corresponding to significance level and σ is the portfolio
standard deviation.

4.3 Monte-Carlo Method
The Monte-Carlo approach to calculating VaR involves using computer al-
gorithms to simulate a large number of random daily portfolio returns, then
calculating losses on the portfolio for each simulated return, and finally de-
termining the VaR as the worst percentage loss that will not be exceeded
with a certain confidence level. In this method also (like the earlier two
25
approaches) Step 1 to Step 5 remains same. Step 6 is same as the variance-
covariance approach as both are parametric methods and assumes the data
to be normally distributed. After going through these six steps, we follow
the next steps as enumerated below.
(A) Step 7: We create a large number of simulated portfolio returns (10,000
in our case) which follows a normal distribution based on three param-
eters:
(a) Random number between 0 and 1.
(b) Portfolio expected return of the historical data.
(c) Portfolio standard deviation of the historical data.
(B) Step 8: VaR was calculated by sorting these simulated returns (most
negative to most positive) and taking the return from the sorted list
which has significant level (confidence interval) percentage of returns
above it. 
Chapter 5
Conclusion and Future
Directions
The study begins by discussing the six main types of financial risks in asset
management and the evolution of banking regulations. Chapter 1 highlights
the formation of the Basel Committee on Banking Supervision to standard-
ize global banking regulations. Basel-I, introduced in 1988, was the first
global regulation for financial systems, addressing disparities in capital re-
quirements and enforcement practices. It introduced the Cooke Ratio, which
accounted for credit risk from both on-balance-sheet and off-balance-sheet
items. Banks were required to maintain capital equal to at least 8% of risk-
weighted assets, with specific requirements for Tier 1 and Tier 2 capital.
Basel-II, introduced in 1999, addressed shortcomings of Basel-I by incorpo-
rating counterparty credit risk and operational risk in capital requirements,
and emphasized supervisory review and market discipline. Basel-II.5, for-
mulated post the 2008 financial crisis, revised the calculation of market risk
capital. Basel-III, implemented from 2013 to 2019, introduced more stringent
regulations including management of liquidity risk, and specific requirements
for Tier 1 and Tier 2 capital. Basel-IV, initiated in 2023, aims to enhance
the credibility of banks and comparability of capital ratios globally. It re-
fines risk assessment, adjusts credit valuation and operational risk, restricts
the use of internal models, and emphasizes standardized methods. It also
introduces a Leverage Ratio buffer for globally significant banks.
Chapter 2 discusses some of the renowned measures of risk. They are stan-
dard deviation (or equivalently variance), semi-deviation, VaR and CVaR.
Standard deviation measures the volatility of returns and is used to maximize
expected returns for a given level of risk, or minimize risk for a given level
of expected returns. Semi-deviation, on the other hand, measures downside
risk, penalizing returns lower than the expected return but not those higher.
VaR is a measure of risk that quantifies potential losses over a specified time
horizon at a given confidence level. However, VaR does not account for
the extent of losses beyond the confidence level. ES or CVaR, on the other
hand, quantifies the expected loss if things get much worse beyond the VaR
paradigm, providing a more comprehensive measure of risk.
Chapter 3 discusses three methods for calculating VaR: the Historical
Method, the Variance Co-variance Method, and the Monte-Carlo Method.
The Historical Method uses historical returns to estimate VaR, while the
Variance Co-variance Method assumes asset returns are normally distributed
and uses variance (single asset) and covariance (multiple asset) of returns.
The Monte-Carlo Method, on the other hand, uses probability distributions
and random variables to estimate VaR.
Chapter 4 discusses the empirical results of applying the three methods
to calculate VaR on a 5-year historical data of Indian stock market indices,
Sensex and Nifty 50. The approach uses past data to estimate potential loss,
with steps including selection of data, calculation of daily simple returns,
assignment of weights to create a portfolio, calculation of historical portfolio
daily returns, conversion of daily returns to T -day returns, sorting of returns
in ascending order, and calculation of VaR.
5.1 Future Directions
Creating an Optimized Portfolio: The first step in our future scope involves
the creation of an optimized portfolio. This process will involve the use of
mathematical models and algorithms to adjust the assets in the portfolio in
such a way that the overall risk is minimized. The goal is to rearrange the
portfolio’s assets in a way that the potential for financial loss, as measured
by VaR, is as low as possible, while still achieving the desired return on
investment.
Calculating VaR of the Optimized Portfolio: Once the portfolio is op-
timized, the next step will be to calculate the VaR of this portfolio. This
will involve applying the methods discussed in Chapter 3 (Historical Method,
Variance Co-variance Method, and Monte-Carlo Method) to the optimized
portfolio. The aim is to estimate the potential loss that could occur in the op-
timized portfolio over a specific time frame, given normal market conditions.
This allows us to assess the riskiness of our portfolio and make necessary
adjustments if required.
Creating a Green Portfolio: The third step in our future scope involves
the creation of a green portfolio. This portfolio will consist of investments
in companies that are considered environmentally friendly or are contribut-
ing positively to environmental sustainability. The selection of assets for
this portfolio will involve careful analysis of the companies’ environmental
policies, practices, and impact.

Finding VaR of the Green Portfolio: The final step will be to calculate the
VaR of the green portfolio. Similar to the optimized portfolio, this will involve
applying the methods discussed in Chapter 3 to the green portfolio. The aim
is to estimate the potential loss that could occur in the green portfolio over a
specific time frame, providing a measure of the financial risk associated with
investing in environmentally friendly companies.



