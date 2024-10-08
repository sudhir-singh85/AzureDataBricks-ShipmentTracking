# Databricks notebook source
from datetime import datetime, timedelta

date = datetime.strptime('2024-01-01', '%Y-%m-%d').date()
end_date = datetime.strptime('2026-01-01', '%Y-%m-%d').date()

while date < end_date:
    date_key = int(date.strftime('%Y%m%d'))
    year = date.year
    month = date.month
    day = date.day
    
    spark.sql(f"""
        INSERT INTO gold.dim_date (DateKey, Date, Year, Month, Day)
        VALUES ({date_key}, '{date}', {year}, {month}, {day})
    """)
    
    date += timedelta(days=1)
