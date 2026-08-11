import argparse, json, logging, sys, os

parser=argparse.ArgumentParser()
parser.add_argument("--log-file", default="/tmp/app.log")
parser.add_argument("--threshold", default=3, type=int)
parser.add_argument("--output", default="/tmp/log_report.json")

args=parser.parse_args()



logging.basicConfig(
    filename="/tmp/log_analyser.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logging.info("Log Analyser started")
print(f"Analyzing: {args.log_file}, threshold={args.threshold}, output={args.output}")

# layer 2 plan

info_count=0
warn_count=0
error_count=0
error_message={}
with open(args.log_file, "r") as f:
    for i in f:
        if "ERROR" in i:
            word=i.split()
            message=" ".join(word[3:])
            if message not in error_message:
                error_message[message] = 1
            else:
                error_message[message] += 1
            error_count=error_count+1
        elif "WARN" in i:
            warn_count=warn_count+1
        elif "INFO" in i:
            info_count=info_count+1
        else:
            print("Nothing matching")
print(f"Number of Error:{error_count}, Number of warning count: {warn_count} and Number of INfo: {info_count}")            
print(error_message)

for message, count in error_message.items():
    if count >= args.threshold:
        logging.error(f"ALERT: '{message}' occured {count} times")
        print(f"Alert: '{message}' occured {count} times")
    else:
        print(f"No alert needed for that '{message}' ({count} times)")

report = {
    "info_count": info_count,
    "warn_count": warn_count,
    "error_count": error_count,
    "error_message": error_message,
    "threshold": args.threshold
}

with open(args.output, "w") as f:
    json.dump(report, f, indent=4)

print(f"Confirmation: final report is {args.output} ")