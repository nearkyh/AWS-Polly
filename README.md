# How to use Amazon Polly


## 1. Join AWS
To create an AWS account
1. Open https://aws.amazon.com and select [Create an AWS Account].
2. Follow the online instructions.


## 2. Create IAM user
To create an administrator user and log in to the console
1. Create an admin user named adminuser in your AWS account. For instructions, See [Creating Users and Administrators Groups for the First Time](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).
2. Users can log in to the AWS Management console using specific URLs. For more information, See [How to log in to your account in the User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_how-users-sign-in.html).


## 3. Getting Started with the AWS CLI
AWS Command Line Interface Configuration
- `virtualenv env --python=python3.5`
- `source env/bin/activate`
- `pip install awscli`

Configuring the AWS Command Line Interface
- `aws configure`
```bash
AWS Access Key ID [None]: YOUR-AWS-ACCESS-KEY-ID
AWS Secret Access Key [None]: YOUR-AWS-SECRET-ACCESS-KEY
Default region name [None]: 
Default output format [None]: 
```


## 4. Testing aws-polly 
Install Dependencies
- `pip install boto3`

Run
- `python example.py`
```bash
msg >> 'Enter text'
return output_aws_polly.mp3 file
```


## 5. Available Voices
If you want to change the language, change the name_id variable in [example.py](https://github.com/yonghankim/aws-polly/blob/master/example.py).
- [`Voice List`](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html)
