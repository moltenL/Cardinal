# Cardinal
Cardinal is a web server that serves data from the frc1678/server project to the frc1678/viewer project.

# Use
There are two main uses for Cardinal. Both involve serving data to the Viewer app. The most important data that is sent, is from the frc1678/server project and is current match and competition data. The second type of data is auto generated testing data.

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

# First test
![2021-09-15_23-59](https://user-images.githubusercontent.com/35516367/133566395-8b683eda-ba8e-4f1d-8362-dabdbd083461.png)

# Roadmap
#### 1. System architecture & framework decision
	- Decide what framework we will use
	- Decide on the architecture (framework dependent)

#### 2. Basic functioning system & initial tests
	- Run the system on every developer's computer and troubleshoot
	- Get automatic testing working with Github actions

#### 3. Automatic test data generator API
	- Fully generate data the view can use to test from this service
	- Serve test data for Viewer to easily pull using REST standards

#### 4. Serve current competition data <b>(Currently here)</b>
	- Pull data from Mongodb about the current competition
	- Setup vies to serve this data
	- Collect time deltas per user of when the last data was pulled
	- Setup database for time deltas
	- Create functionality to pull data that has been changed since last pull

#### 5. Discuss specifics of hosting, etc.
	- Where will we host this web server
		note: this isn't as time-sensitive as development

#### 6. Help frontend integrate this API into Viewer.
	- Create documentation on the API and it's proper use
	- Support the Viewer's developers in their implementation efforts

#### 7. Full systems test
	- Run the server with test data from scouts
	- Run this web server and pull data from it
	- Test Viewer and it's ability to pull data

