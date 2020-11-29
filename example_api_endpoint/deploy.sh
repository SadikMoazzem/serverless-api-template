echo --------Deploying GET MASJIDS /get-masjids
python3 -m pip install --target ./package -r ./requirements.txt -q
cd package
cd ..
mkdir lambda
cp get_masjids/lambda_function.py lambda/
cp -r package/. lambda/
cd lambda
zip -q -r my-deployment-package.zip *
aws lambda update-function-code --function-name mylocalmasjid-getMasjids --zip-file fileb://./my-deployment-package.zip
rm -r my-deployment-package.zip
cd ../
rm -r package
rm -r lambda
echo --------SUCCESS