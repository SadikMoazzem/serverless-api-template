import json

def lambda_handler(event, context):
    '''
    function that gets called when the lambda is called
    :param event:
    :param context:
    :return: Dict
    '''
    print('-------------Lambda Called')

    print('response')
    print({
        'statusCode': 200,
        'body': json.dumps(event),
    })
    print('-------------Lambda Ended Successfully')
    return {
        'statusCode': 200,
        'body': json.dumps(event),
    }

if __name__=='__main__':
    # Example Event sent by AWS API Gateway
    event = {
        "resource": "/test-endpoint",
        "path": "/test-endpoint",
        "httpMethod": "GET",
        "headers": None,
        "multiValueHeaders": None,
        "queryStringParameters": {
            "hey": "1"
        },
        "multiValueQueryStringParameters": None,
        "pathParameters": None,
        "stageVariables": None,
        "requestContext": {
            "resourceId": "ovtm1s",
            "resourcePath": "/get-masjids",
            "httpMethod": "GET",
            "extendedRequestId": "WvIQYF_ZLPEFu2w=",
            "requestTime": "28/Nov/2020:21:00:24 +0000",
            "path": "/get-masjids",
            "accountId": "026290566452",
            "protocol": "HTTP/1.1",
            "stage": "test-invoke-stage",
            "domainPrefix": "testPrefix",
            "requestTimeEpoch": 1606597224748,
            "requestId": "20faacc1-aebd-4b4b-953a-dee89be01152",
            "identity": {
            "cognitoIdentityPoolId": None,
            "cognitoIdentityId": None,
            "apiKey": "test-invoke-api-key",
            "principalOrgId": None,
            "cognitoAuthenticationType": None,
            "userArn": "arn:aws:iam::026290566452:root",
            "apiKeyId": "test-invoke-api-key-id",
            "userAgent": "aws-internal/3 aws-sdk-java/1.11.864 Linux/4.9.217-0.3.ac.206.84.332.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.262-b10 java/1.8.0_262 vendor/Oracle_Corporation",
            "accountId": "026290566452",
            "caller": "026290566452",
            "sourceIp": "test-invoke-source-ip",
            "accessKey": "ASIAQMHYKGU2EDB2Y5FU",
            "cognitoAuthenticationProvider": None,
            "user": "026290566452"
            },
            "domainName": "testPrefix.testDomainName",
            "apiId": "wvbfqjk3oc"
        },
        "body": None,
        "isBase64Encoded": False
    }

    lambda_handler(event, None)
