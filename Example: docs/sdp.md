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
