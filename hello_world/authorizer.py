def lambda_handler(event, context):
    token = event["authorizationToken"]
    effect = "Deny"
    if token == "hoge":
        effect = "Allow"

    return {
        "principalId": "hello_world_authorizer",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": event["methodArn"],
                }
            ],
        },
        "context": {},
    }
