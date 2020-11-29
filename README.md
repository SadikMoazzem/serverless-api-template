# Serverless API Template

This is a Template for AWS Lambdas with AWS Gateway
Created by @SadikMoazzem

## Testing locally

Create venv
Set ENV vars
```
$env:[ENV NAME] = ''
```

Run Each lambda separately

```
python {lambda_dir}/lambda_function.py
```

## Deploying to AWS

*AWS CLI needs to be configured for this to work
This can be run in the root to deploy all or in individual Dir

```
bash deploy.sh
```