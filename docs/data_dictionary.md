# M5 Data Dictionary

This document describes the datasets and columns used in the Retail Demand Forecasting & Inventory Intelligence Platform.
## 1. calendar.csv

The calendar dataset maps M5 day identifiers to actual dates and contains calendar events and SNAP information.

| Column | Data Type | Description |
|---|---|---|
| date | date | Actual calendar date |
| wm_yr_wk | integer | Walmart year-week identifier |
| weekday | string | Name of the day of the week |
| wday | integer | Numeric day-of-week identifier |
| month | integer | Month number |
| year | integer | Calendar year |
| d | string | M5 sequential day identifier, such as d_1 |
| event_name_1 | string | Name of the primary event or holiday, if present |
| event_type_1 | string | Type of the primary event, such as Cultural, National, Religious, or Sporting |
| event_name_2 | string | Name of a second event occurring on the same date, if present |
| event_type_2 | string | Type of the second event, if present |
| snap_CA | integer | Indicates whether SNAP purchasing is active in California |
| snap_TX | integer | Indicates whether SNAP purchasing is active in Texas |
| snap_WI | integer | Indicates whether SNAP purchasing is active in Wisconsin |

### Profiling Summary

- Rows: 1,969
- Columns: 14
- Date range: 2011-01-29 to 2016-06-19
- Unique weeks: 282
- Unique weekdays: 7
- Years represented: 2011–2016
- Primary event names: 30
- Primary event types: 4
- `event_name_1` and `event_type_1` contain 1,807 null values.
- `event_name_2` and `event_type_2` contain 1,964 null values.
- All other columns contain no null values.

- ## 2. sales_train_validation.csv

The sales dataset contains historical daily unit sales for each item and store combination.

| Column | Data Type | Description |
|---|---|---|
| id | string | Unique identifier for an item-store sales series |
| item_id | string | Unique product identifier |
| dept_id | string | Department the item belongs to |
| cat_id | string | Product category |
| store_id | string | Store identifier |
| state_id | string | State where the store is located |
| d_1 to d_1913 | integer | Daily unit sales for each sequential M5 day |

### Profiling Summary

- Rows: 30,490
- Columns: 1,919
- Identifier columns: 6
- Daily sales columns: 1,913
- First sales day: d_1 (2011-01-29)
- Last sales day: d_1913 (2016-04-24)
- Unique items: 3,049
- Unique departments: 7
- Unique categories: 3
- Unique stores: 10
- Unique states: 3
- Categories: FOODS, HOBBIES, HOUSEHOLD
- States: CA, TX, WI
- Minimum daily unit sales: 0
- Maximum daily unit sales: 763
- No null values were found in the dataset.


## 3. sell_prices.csv

The sell prices dataset contains weekly selling prices for items at each store.

| Column | Data Type | Description |
|---|---|---|
| store_id | string | Store identifier |
| item_id | string | Unique product identifier |
| wm_yr_wk | integer | Walmart year-week identifier used to connect prices with the calendar |
| sell_price | double | Selling price of the item for the specified store and week |

### Profiling Summary

- Rows: 6,841,121
- Columns: 4
- Unique stores: 10
- Unique items: 3,049
- Unique weeks: 282
- Date range: 2011-01-29 to 2016-06-19
- Minimum selling price: $0.01
- Maximum selling price: $107.32
- No null values were found in any of the four columns.
