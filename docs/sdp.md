# What is Spark Declarative Pipelines (SDP)?
Spark Declarative Pipelines (SDP) is a declarative framework for building reliable, maintainable, and testable data pipelines on Apache Spark.
Instead of focusing on:
	•	job ordering
	•	orchestration logic
	•	retries and failure handling
SDP allows you to focus on:
	•	what datasets should exist
	•	what transformations define those datasets
Spark automatically handles:
	•	execution orchestration
	•	dependency resolution
	•	compute management
	•	incremental processing
	•	error handling
	
This shift from execution‑first to intent‑first is exactly the philosophy Palantir Foundry has been built on for years.

## What SDP Supports
SDP is designed for both batch and streaming workloads, including:
	•	Cloud storage ingestion\ Amazon S3, Azure ADLS Gen2, Google Cloud Storage
	•	Message‑bus ingestion\ Apache Kafka, Amazon Kinesis, Google Pub/Sub, Azure EventHub
	•	Incremental batch and streaming transformations
These are the same primitives we commonly use in Palantir Foundry — but here they are expressed directly in Spark’s core programming model.






# SDP Examples in Reinsurance
## 1. Querying Tables Defined in Pipeline
```python
@sdp.materialized_view(name="claims")
def claims():
    return spark.read.csv("/mock/reinsurance/claims.csv", header=True)

@sdp.materialized_view(name="policies")
def policies():
    return spark.read.csv("/mock/reinsurance/policies.csv", header=True)

@sdp.materialized_view(name="claims_with_policy")
def claims_with_policy():
    return spark.table("claims").join(spark.table("policies"), "policy_id")
```
## 2. Creating Tables in a For Loop
```python
regions = ["APAC", "EMEA", "NA"]

for region in regions:
    @sdp.table(name=f"{region.lower()}_claims")
    def regional_claims(region_filter=region):
        return (
            spark.table("claims_with_policy")
                 .filter(f"region = '{region_filter}'")
        )
```
## 3. Creating Flows to Write to a Single Target
```python
# Create unified streaming table for global claims
sdp.create_streaming_table("global_claims")

@sdp.append_flow(target="global_claims")
def append_apac():
    return spark.readStream.table("apac_claims")

@sdp.append_flow(target="global_claims")
def append_emea():
    return spark.readStream.table("emea_claims")
```






