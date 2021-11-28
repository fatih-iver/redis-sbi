# Redis-Sbi

In other words, Redis Slack Bot Interface. 
Helps you interact with Redis over Slack.

This bot is specifically designed to be deployed as AWS Lambda Function.

There are 3 steps to have this Bot working:

1 - Create Docker Image  
2 - Create AWS Lambda Function  
3 - Create Slack App

Learn how to complete these step from [here](https://medium.com/@fiver6/lets-write-a-redis-slack-bot-deploy-it-as-aws-lambda-function-3c1bf8bfc0df).


## Usage

From anywhere in Slack, run redis-cli commands without specifying host, port, and password.

```bash
/redis-sbi <redis-command>
```

### Example Usages

```bash
/redis-sbi PING
/redis-sbi INFO
/redis-sbi SET test-key test-value
/redis-sbi GET test-key
/redis-sbi --scan --pattern test*
/redis-sbi DEL test-key
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
