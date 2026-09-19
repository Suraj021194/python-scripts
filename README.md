# Log Analyser

A Python script that parses application logs, counts log levels, and alerts on repeated error messages.

## Features
- Counts INFO, WARN, and ERROR log lines
- Tracks frequency of each unique error message
- Alerts when an error repeats at or above a configurable threshold
- Outputs a JSON summary report

## Usage (local)
```bash
python3 log_analyser.py --log-file /path/to/log --threshold 3 --output report.json
```

## Arguments
Each setting can be set via a CLI flag or an environment variable:

| Setting     | CLI flag       | Env var       | Default                       |
|-------------|----------------|---------------|--------------------------------|
| Log file    | `--log-file`   | `LOG_FILE`    | `/app/logs/app.log`           |
| Threshold   | `--threshold`  | `THRESHOLD`   | `3`                            |
| Output file | `--output`     | `OUTPUT_FILE` | `/app/output/log_report.json` |

## Usage (Docker)
```bash
docker build -t log-analyser .

docker run \
  -v /path/to/logs:/app/logs \
  -v /path/to/output:/app/output \
  log-analyser
```

Override any setting at runtime without rebuilding:
```bash
docker run -e THRESHOLD=1 -v ~/logs:/app/logs -v ~/output:/app/output log-analyser
```

The container runs as a non-root user (`appuser`). If a bind-mounted host folder 
is owned by a different UID, you may need to `chown` it to match.

## CI/CD
Every push to `main` triggers `.github/workflows/docker-publish.yml`, which builds 
this image and pushes it to Docker Hub, tagged with the commit SHA:

```bash
docker pull suraj0294/log-analyser:<commit-sha>
```

See it live: [hub.docker.com/r/suraj0294/log-analyser](https://hub.docker.com/r/suraj0294/log-analyser)