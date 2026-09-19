FROM python:3.12-slim
WORKDIR /app
ENV LOG_FILE=/app/logs/app.log
ENV THRESHOLD=3
ENV OUTPUT_FILE=/app/output/log_report.json
COPY log_analyser.py .
RUN useradd -m appuser
RUN mkdir -p /app/output && chown -R appuser:appuser /app/output
USER appuser
ENTRYPOINT ["python3", "log_analyser.py"]
#CMD ["--log-file", "/app/logs/app.log", "--threshold", "3", "--output", "/app/output/log_report.json"]
