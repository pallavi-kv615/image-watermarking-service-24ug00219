import boto3
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

s3 = boto3.client("s3")


def lambda_handler(event, context):

    # Get bucket name and uploaded file name
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    # Process only images inside input folder
    if not key.startswith("input/"):
        return {
            "statusCode": 200,
            "body": "File is not in input folder"
        }

    # Get image from S3
    response = s3.get_object(
        Bucket=bucket,
        Key=key
    )

    image_data = response["Body"].read()

    # Open image
    image = Image.open(BytesIO(image_data))

    # Create drawing object
    draw = ImageDraw.Draw(image)

    # Watermark text
    watermark_text = "Pallavi KV - 24UG00219"

    # Image size
    width, height = image.size

    # Large, readable font
    font = ImageFont.load_default(size=48)

    # Get text size
    bbox = draw.textbbox(
        (0, 0),
        watermark_text,
        font=font
    )

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Position watermark at top-left
    margin = 30
    position = (margin, margin)

    # Add watermark with dark outline
    draw.text(
        position,
        watermark_text,
        font=font,
        fill="white",
        stroke_width=3,
        stroke_fill="black"
    )

    # Save image temporarily
    output_buffer = BytesIO()

    image.save(
        output_buffer,
        format="JPEG"
    )

    output_buffer.seek(0)

    # Create output filename
    filename = key.split("/")[-1]
    output_key = "output/watermarked_" + filename

    # Upload watermarked image to S3
    s3.put_object(
        Bucket=bucket,
        Key=output_key,
        Body=output_buffer,
        ContentType="image/jpeg"
    )

    return {
        "statusCode": 200,
        "body": "Watermark added successfully"
    }