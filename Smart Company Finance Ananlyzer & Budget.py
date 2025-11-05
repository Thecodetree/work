# Smart Company Finance Ananlyzer & Budget Planner

import pandas as pd

class CompanyFinance:
    def __init__(Self, revenue, operating_expenses, debt, investment_goal_percent):
        self.revenue = revenue
        self.operating_expenses = operating_expenses
        self.debt = debt
        self.investment_goal_percent = investment_goal_percent

    def calculate_profit(self):
        return max(self.revenue - self.operating_expenses, 0)

    def financial_health_score(self):
        profit = self.calculate_profit()
        debt_ratio = self.debt / max(self.revenue, 1)
        profit_margin = profit / max(self.revenue, 1)
        score = (profit_margin * 60 + (1 - debt_ratio) * 40)
        return round(max(0, min(score, 100)), 2)

    def plan_investment_budget(self):
        profit = self.calculate_profit()
        health_score = self.financial_health_score()
        adjustment_factor = 1 + (health_score - 50) / 200
        planned_investment = profit * self.investment_goal_percent * adjustment_factor
        return round(planned_investment, 2)

    def calculate_employee_cost(self, num_employees, avg_salary, benefits_percent=0.25):
        total_cost = num_employees * avg_salary * (1 + benefits_percent)
        return round(total_cost, 2)

    def recommendations(self, health_score, profit, debt_ration, investment, employee cost, num_employees):
        suggestions = []

        if profit <= 0:
            suggestions.append("The company is operating at or near a loss - cut expenses immediately.")
        elif health_score > 80:
            suggestions.append("The Company is financially strong - consider increasing investment for growth.")
        elif 50 < health_score <= 80:
            suggestions.append("Stable perfirmance - maintain current investment theory and monitor trends.")
        else:
            suggestions.append("Company has below average financial health - focus on reducing costs and debt.")

        if debt_ratio > 0.4:
            suggestions.append('High debt ratio detected - consider refinancing or debt reduction.')
        elif debt_ratio < 0.1:
            suggestions.append("Maintain current staffing levels until profits increase.")

        if investment < 0.05 * profit:
            suggestions.append("")
        elif investment > 0.3 * profit:
            suggestions.append("Investment level is high - ensure ROI projections justify spending.")

        return " | ".join(suggestions)

    def summary(self, num_employess, avg_salary):
        profit = self.calculate_profit()
        health_score = self.financial_health_score()
        planned_investment = self.plan_investment_budget()
        planned_investment = self.plan_investment_budget()
        emloyee_cost = self.calculate_employee_cost(num_empployees, avg_salary)
        debt_ratio = self.debt / max(self.revenue, 1)

        return {
            "Revenue": self.revenue,
            "Operating Expenses": self.operating_expenses,
            "Debt": self.debt
            "profit": profit,
            "Financial_Health_Score": health_score,
            "Debt_Ratio": round(debt_ratio, 2),
            "Planned_Investment": planned_investment,
            "Yearly_Employee_Cost": employee_cost,
            "Recommendations": self.recommendations(health_score, profit, debt_ratio, Planned_investment, emloyee_cost, num_employees)}

    #Function to process the file and generate summaries

    def process_financial_file(file_path, num_employees, Avg_salary):
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            df = pd.read_csv(file_path)
        else:
            raise ValueError("Unsupported file format. Please use .csv or xlsx")

        results = []

        for _, row in df.iterrows():
            company = company_finance(
                revenue=row["Revenue"],
                operating_expenses=row["Operating_Expenses"],
                debt=row["Debt"],
                investment_goal_percent=row["Investment_Goal_Percent"])
                summary = company.summary(num_employees, avg_salary)
                results.append(summary)

        results_df = pd.DataFrame(results)
        print("\n---- Smart Company Financial Summary ----\n")
        print(results_df.to_string(index=False))
        print(results.df)

# Example of Use case

if __name__ "__main__":
    file_path = "company_finances.csv"
    num_employees = 45
    avg_salary = 60000

    results = process_financial_file(file_path, num_employees, avg_salary)

    results.to_csv("Financial_summary_with_recommendations.csv", index=False)
    print("\nResults saved to 'financial_summary_with_recommendations.csv'")