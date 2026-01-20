# examples/claims_pipeline.py
# Demonstration of querying tables and joining claims with policies
# in a reinsurance context using Spark Declarative Pipelines (SDP).

from pyspark import pipelines as sdp
from pyspark.sql import SparkSession

# Initialize Spark session (normally handled by Palantir SDP runtime)
spark = SparkSession.builder.appName("ClaimsPipeline").getOrCreate()

# Define a streaming table for raw claims ingestion
@sdp.table
def claims_stream():
    return (spark.readStream.format("kafka")
            .option("kafka.bootstrap.servers", "localhost:9092")
            .option("subscribe", "claims_topic")
            .load())

# Define a materialized view for policy data
@sdp.materialized_view
def policies_mv():
    return (spark.read.format("csv")
            .option("header", True)
            .load("/data/reinsurance/policies.csv"))

# Join claims with policies to enrich claims with policy details
@sdp.materialized_view
def claims_with_policies():
    return (spark.table("claims_stream")
            .join(spark.table("policies_mv"), "policy_id")
            .select("policy_id", "claim_id", "loss_amount", "claim_date", "policy_holder"))
