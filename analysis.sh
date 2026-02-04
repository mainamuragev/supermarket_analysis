#!/bin/bash
# analysis.sh — supermarket stakeholder queries

echo "Apples purchased with cash:"
awk -F',' 'NR>1 && tolower($6) ~ /apple/ && tolower($10)=="cash" {sum+=$4} END {print sum}' supermarket_transactions.csv

echo "Cash amount spent on apples:"
awk -F',' 'NR>1 && tolower($6) ~ /apple/ && tolower($10)=="cash" {sum+=$8} END {print sum}' supermarket_transactions.csv

echo "Non-member spend at Bakershire:"
awk -F',' 'NR>1 && tolower($9) ~ /bakershire/ && tolower($12) ~ /non-member/ {sum+=$8} END {print sum}' supermarket_transactions.csv
