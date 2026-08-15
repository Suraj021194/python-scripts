# Log Analyser

A Python script that parses application logs, counts log levels, and alerts on repeated error messages.

## Features
- Counts INFO, WARN, and ERROR log lines
- Tracks frequency of each unique error message
- Alerts when an error repeats at or above a configurable threshold
- Outputs a JSON summary report

## Usage
```bash
python3 log_analyser.py --log-file /path/to/log --threshold 3 --output report.json
```

## Arguments
- `--log-file` : path to the log file to analyze (default: /tmp/app.log)
- `--threshold` : number of repeats before alerting (default: 3)
- `--output` : path to write the JSON report (default: /tmp/log_report.json)