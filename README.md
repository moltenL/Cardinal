# Cardinal

# First test
![2021-09-15_23-59](https://user-images.githubusercontent.com/35516367/133566395-8b683eda-ba8e-4f1d-8362-dabdbd083461.png)

# Usage

## Test Data Generator
```
# Format
curl -X GET "http://127.0.0.1:8000/cardinal/api/generate/<schema_name>/?format=json" \
  -H "Authorization: Token abc"

# Example
curl -X GET "http://127.0.0.1:8000/cardinal/api/generate/calc_tba_team_schema/?format=json" \
  -H "Authorization: Token abc"

```
#### Output
```json
[
  {
    "auto_high_balls_percent_inner": 89.7359,
    "tele_high_balls_percent_inner": 16.1893,
    "climb_all_success_avg_time": 96.7847,
    "team_name": "rNvKwQbEoMBnA",
    "climb_percent_success": 46.9206,
    "climb_all_successes": 13,
    "climb_level_successes": 8,
    "park_successes": 16,
    "auto_line_successes": 42,
    "team_number": 4665
  }
]
```
