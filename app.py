import json
import boto3
import logging
from datetime import datetime

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

codepipeline = boto3.client('codepipeline')

PIPELINE_NAME = "MyPipeline"

def lambda_handler(event, context):

    start_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    logger.info("=" * 60)
    logger.info("AWS CI/CD AUTOMATION STARTED")
    logger.info("=" * 60)
    logger.info(f"Pipeline Name : {PIPELINE_NAME}")
    logger.info(f"Execution Time: {start_time}")
    logger.info(f"Request ID    : {context.aws_request_id}")

    try:
        response = codepipeline.start_pipeline_execution(
            name=PIPELINE_NAME
        )

        execution_id = response['pipelineExecutionId']

        logger.info("Pipeline Trigger Status : SUCCESS")
        logger.info(f"Execution ID            : {execution_id}")
        logger.info("Deployment workflow initiated successfully.")
        logger.info("=" * 60)

        return {
            "statusCode": 200,
            "message": "Pipeline execution started successfully",
            "pipeline": PIPELINE_NAME,
            "executionId": execution_id,
            "timestamp": start_time
        }

    except Exception as e:

        logger.error("Pipeline Trigger Status : FAILED")
        logger.error(f"Error Details: {str(e)}")

        return {
            "statusCode": 500,
            "message": "Pipeline execution failed",
            "error": str(e),
            "timestamp": start_time
        }
