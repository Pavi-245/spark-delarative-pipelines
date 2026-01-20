# Imperative vs Declarative Pipelines in SDP

## Conceptual Difference

| Approach       | Imperative | Declarative |
|----------------|------------|-------------|
| Style          | Step-by-step instructions | Define desired end state |
| Control        | Developer manages execution | SDP orchestrates automatically |
| Example        | Explicit Spark jobs | SDP pipeline spec + decorators |

---

## Imperative Example (Manual Spark Job)

```python
# Imperative: explicitly control ETL
claims = spark.read.csv("/data/reinsurance/claims.csv", header=True)
policies = spark.read.csv("/data/reinsurance/policies.csv", header=True)

joined = claims.join(policies, "policy_id")
aggregated = joined.groupBy("region").count()

aggregated.write.mode("overwrite").saveAsTable("claims_by_region")
