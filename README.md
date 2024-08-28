### Prepare For Deployment

1. `pip3 install -t dependencies -r requirements.txt`
Install all dependencies into 'dependencies' folder. 

2. `(cd dependencies; zip ../aws_lambda_artifact.zip -r .; cd ..)`
Zip dependencies folder into 'aws_lambda_artifact.zip'.

3. `zip aws_lambda_artifact.zip -u main.py api.py sicumon/*`
Add additional files to zip archive. 