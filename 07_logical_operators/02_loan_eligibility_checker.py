# 🔺 Level 2 — Logic Challenge
# "The Loan Eligibility Checker"

# Taking user input
age = int(input("Enter age: "))
monthly_income = float(input("Enter monthly income: "))
credit_score = float(input("Enter credit score: "))

eligible_age = age >= 21
eligible_monthly_income = monthly_income >= 25000
eligible_credit_score = credit_score >= 700
eligible_credit_score_relaxed = credit_score >= 600
high_income = monthly_income > 50000
reason = ""
status = ""


if high_income and eligible_credit_score_relaxed and eligible_age:
    status = "✅ Loan Approved"
    reason = "High income applicant with acceptable credit score."
elif eligible_age and eligible_credit_score and eligible_monthly_income:
    status = "✅ Loan Approved"
    reason = "standard approval"
elif not eligible_age:
    status = "❌ Not Eligible"
    reason = "too young"
elif not eligible_monthly_income:
    status = "❌ Not Eligible "
    reason = "insufficient income"
else:
    status = "❌ Not Eligible "
    reason = "credit score too low"

print(f"{status}")
print(f"Reason: {reason}")