# Image Watermarking Service - 24UG00219

## Project Description

This project is a serverless Image Watermarking Service built using AWS Lambda and Amazon S3.

The function automatically adds a watermark containing the student name and Student ID to an image uploaded to the input folder in Amazon S3.

## Technologies Used

- Python
- AWS Lambda
- Amazon S3
- Pillow (Python Imaging Library)

## How It Works

1. An image is uploaded to the `input/` folder of the S3 bucket.
2. The S3 event automatically triggers the AWS Lambda function.
3. Lambda downloads the uploaded image.
4. Pillow adds the watermark:
   `Pallavi KV - 24UG00219`
5. The watermarked image is saved in the `output/` folder.
6. The output image can be accessed using a public S3 URL.

## S3 Bucket

Bucket name:

`pallavi-watermark-24ug00219`

Folders:

- `input/` - Contains the original images.
- `output/` - Contains the watermarked images.

## Student Details

**Student ID:** 24UG00219

**Assignment:** 9 - Image Watermarking Service

## Output

The final watermarked image is available here:

https://pallavi-watermark-24ug00219.s3.ap-south-1.amazonaws.com/output/watermarked_image1.jpg
