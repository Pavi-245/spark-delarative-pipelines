# SDP Examples in Reinsurance

This page contains **Python code snippets** showing how to use SDP in Palantir for reinsurance pipelines.

---

## 1. Querying Tables Defined in Pipeline
```python
@sdp.materialized_view
def claims_with_policies():
    return (spark.table("claims_stream")
            .join(spark.table("policies_mv"), "policy_id")
            .select("policy_id", "claim_id", "loss_amount"))
for region in ["US", "EU", "APAC"]:
    @sdp.table(name=f"{region.lower()}_treaty_exposures")
    def regional_treaty_exposures(region_filter=region):
        return spark.table("treaty_exposures").filter(f"region = '{region_filter}'")
sdp.create_streaming_table("claims_consolidated")

@sdp.append_flow(target="claims_consolidated")
def append_domestic_claims():
    return spark.readStream.table("claims_domestic")

@sdp.append_flow(target="claims_consolidated")
def append_international_claims():
    return spark.readStream.table("claims_international")

---

## 📝 Step 4: Python Example Files (`examples/`)

### `examples/claims_pipeline.py`
```python
from pyspark import pipelines as sdp

@sdp.table
def claims_stream():
    return spark.readStream.table("claims_raw")

@sdp.materialized_view
def policies_mv():
    return spark.read.csv("/data/reinsurance/policies.csv", header=True)

@sdp.materialized_view
def claims_with_policies():
    return (spark.table("claims_stream")
            .join(spark.table("policies_mv"), "policy_id"))
