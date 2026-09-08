---
name: Excel KPI Dashboard Builder
description: Use this skill when the user asks to analyze Excel or CSV sales data, define KPI calculations, design a sales dashboard, or create Streamlit dashboard code.
---

# Excel KPI Dashboard Builder

## Purpose

Help create reliable Excel-based sales KPI analysis and dashboard designs for GM sales operations.

Use this skill when the user asks to:

- Analyze Excel or CSV sales data
- Create a sales KPI dashboard
- Define KPI calculations
- Design charts or dashboard sections
- Generate Streamlit dashboard code
- Improve an existing Excel or Streamlit dashboard
- Review sales, production, inventory, or allowance data

Do not use this skill for unrelated topics.

## Important principles

- Do not invent numbers, columns, dates, or business rules.
- First inspect the available files, worksheets, columns, and data types.
- Clearly identify missing, duplicated, or inconsistent data.
- Separate actual values from assumptions.
- Explain KPI formulas in simple language.
- Use the latest available data only when the source data contains a clear date field.
- If the data is insufficient, explain what is missing before calculating the KPI.

## Standard workflow

### Step 1: Inspect the data

Identify:

- File name
- Worksheet names
- Number of rows and columns
- Column names
- Date columns
- Key dimensions such as market, brand, model, dealer, channel, and period
- Numeric columns such as sales, production, inventory, and allowance
- Missing values and duplicate rows

### Step 2: Validate the data

Check for:

- Missing required columns
- Incorrect date formats
- Duplicate records
- Blank or invalid numeric values
- Inconsistent market or model names
- Different units or currencies
- Inconsistent monthly or weekly definitions

Report validation issues before presenting conclusions.

### Step 3: Define the KPI logic

For each KPI, show:

1. KPI name
2. Business meaning
3. Formula
4. Required columns
5. Filter conditions
6. Data limitations

Possible KPIs include:

- Total sales
- Sales by market
- Sales by brand
- Sales by model
- Monthly sales trend
- Year-over-year growth
- Month-over-month growth
- Inventory
- Inventory days
- Production volume
- Sales allowance
- Target achievement
- Mix percentage

### Step 4: Design the dashboard

Use the following structure unless the user requests a different format:

1. Executive summary
2. KPI cards
3. Monthly trend chart
4. Market or region comparison
5. Brand and model performance
6. Inventory and production view
7. Allowance or incentive view
8. Detail table
9. Data quality notes

### Step 5: Explain the result

Start with:

- Three key findings
- Important risks or data limitations
- Recommended next actions

Use tables when they make the result easier to understand.

### Step 6: Generate code when requested

When the user asks for Streamlit code:

- Use the existing app.py as a reference when available.
- Keep the code modular and easy to maintain.
- Include file upload functionality for Excel and CSV files.
- Include worksheet selection for Excel files.
- Add filters for date, market, brand, model, and dealer when those columns exist.
- Show clear error messages when required columns are missing.
- Do not claim that the application was executed or deployed unless execution was actually confirmed.
- Keep business rules separate from chart and layout code.

## Standard response format

Use this format for analysis:

### Data Summary

- File:
- Worksheets:
- Rows:
- Columns:
- Date range:

### Data Quality

| Check | Result | Action |
|---|---|---|
| Required columns |  |  |
| Missing values |  |  |
| Duplicate rows |  |  |
| Date format |  |  |

### KPI Summary

| KPI | Value | Formula | Limitation |
|---|---:|---|---|
|  |  |  |  |

### Key Findings

1. 
2. 
3. 

### Recommended Actions

1. 
2. 
3. 
