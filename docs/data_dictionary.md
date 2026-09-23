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
| event_type_1 | string | Type of the primary event |
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
- All other columns contain no null values.## 1. calendar.csv

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
| event_type_1 | string | Type of the primary event |
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
- All other columns contain no null values.## 1. calendar.csv

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
| event_type_1 | string | Type of the primary event |
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
