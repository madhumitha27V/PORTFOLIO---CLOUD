# Portfolio Website - AWS Serverless Deployment

A serverless portfolio website deployed on AWS using Lambda, API Gateway, and DynamoDB with EmailJS integration for contact form functionality.

## 🏗️ Architecture

- **AWS Lambda**: Python 3.14 serverless function serving HTML pages
- **API Gateway**: REST API with GET and POST endpoints
- **DynamoDB**: NoSQL database (Madhu_Table) storing contact form submissions
- **EmailJS**: Client-side email service sending form submissions to cloud091327@gmail.com

## 📁 Project Structure

```
CLOUD PROJECT/
├── lambda_function.py    # Main Lambda handler
├── contactus.html        # Portfolio homepage with all sections
├── success.html          # Form submission success page
└── README.md            # This file
```

## ✨ Features

- **Responsive Design**: Mobile-friendly sidebar navigation
- **Left Sidebar Navigation**: Profile section with avatar and social links
- **Portfolio Sections**:
  - Hero/Home
  - Skills (C, Python, Java, HTML, CSS, React.js, Node.js, MongoDB, Git, Data Structures, Algorithms, IoT)
  - Projects (4 featured projects with GitHub links)
  - Achievements (5 cards)
  - Education (B.E., HSC, SSLC)
  - Certifications (4 certifications)
  - Contact Form
- **EmailJS Integration**: Real-time email notifications
- **DynamoDB Storage**: Backup of all form submissions
- **Smooth Animations**: Gradient effects, hover transitions, shimmer animations

## 🚀 Deployment Steps

### 1. Create DynamoDB Table
```
Table Name: Madhu_Table
Primary Key: email (String)
```

### 2. Prepare Lambda Function
1. Zip all 3 files together:
   - `lambda_function.py`
   - `contactus.html`
   - `success.html`
2. Ensure files are at root level of ZIP (not in a subfolder)

### 3. Create Lambda Function
1. Go to AWS Lambda Console
2. Create new function (Python 3.14 runtime)
3. Upload the ZIP file
4. Set Handler: `lambda_function.lambda_handler`
5. Set Timeout: 10 seconds
6. Add IAM permissions:
   - `AmazonDynamoDBFullAccess`
   - `CloudWatchLogsFullAccess`

### 4. Create API Gateway
1. Create REST API
2. Create resource: `/`
3. Add methods:
   - **GET**: Returns portfolio HTML
   - **POST**: Processes form and saves to DynamoDB
4. Enable **Lambda Proxy Integration** for both methods
5. Enable CORS
6. Deploy API to stage (e.g., "Madh")

### 5. EmailJS Configuration
- **Service ID**: `service_stz6sqk`
- **Template ID**: `template_e4lcqsq`
- **Public Key**: `oQmPVgRLxfOwSIaj0`
- **Recipient Email**: cloud091327@gmail.com

## 🔗 API Endpoints

- **Invoke URL**: `https://eb9anw7oq6.execute-api.us-east-1.amazonaws.com/Madh/`
- **GET** `/`: Displays portfolio website
- **POST** `/`: Submits contact form (though EmailJS handles this client-side)

## 📝 Form Fields

The contact form collects:
- **name**: Full name of the visitor
- **email**: Email address for responses
- **message**: Message content

## 🛠️ Technologies Used

- **Backend**: Python 3.14, AWS Lambda, Boto3
- **Database**: Amazon DynamoDB (PartiQL)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Email**: EmailJS SDK
- **Icons**: Font Awesome 6.5.0
- **API**: AWS API Gateway (REST)
- **Monitoring**: AWS CloudWatch Logs

## 💰 AWS Free Tier Usage

All services used stay within AWS Free Tier limits:
- ✅ Lambda: 1M requests/month
- ✅ API Gateway: 1M API calls/month (12 months)
- ✅ DynamoDB: 25GB storage
- ✅ CloudWatch: 5GB logs/month

## 🧪 Testing

1. Open the API Gateway URL in browser
2. Navigate through all sections using sidebar
3. Fill out the contact form
4. Submit and verify:
   - Email received at cloud091327@gmail.com
   - Success page displays
   - Data stored in DynamoDB Madhu_Table

## 📧 Contact

- **Email**: cloud091327@gmail.com
- **Portfolio Owner**: Madhumitha V
- **Institution**: Kongu Engineering College
- **Program**: Electrical & Electronics Engineering

## 📄 License

Personal portfolio project - All rights reserved.

---

**Last Updated**: December 2025  
**Deployment Status**: Active on AWS Lambda  
**API Gateway Stage**: Madhumitha
