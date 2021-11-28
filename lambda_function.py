import subprocess
import os

from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler


def respond_to_slack_within_3_seconds(body, ack):
    ack(f"Accepted command: {body['command']} {body['text']}", response_type="in_channel")


def redis_sbi(respond, body):
    print(f"Started processing request: {body}")
    redis_host = os.getenv(f"REDIS_HOST", "localhost")
    redis_port = os.getenv(f"REDIS_PORT", "6379")
    redis_password = os.getenv("REDIS_PASSWORD", None)
    redis_command = body["text"]
    output = subprocess.getoutput(f"redis-cli --no-auth-warning -c -h {redis_host} -p {redis_port}"
                                  f"{' -a ' + redis_password if redis_password else ''} {redis_command}")
    respond(f" > {output}", response_type="in_channel")
    print(f"Finished processing request: {body}")


app = App(process_before_response=True)
app.command("/redis-sbi")(ack=respond_to_slack_within_3_seconds, lazy=[redis_sbi])


def lambda_handler(event, context):
    return SlackRequestHandler(app=app).handle(event, context)


if __name__ == "__main__":
    app.start()
