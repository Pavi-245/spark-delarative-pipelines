# Imperative vs Declarative Pipelines in SDP (Reinsurance Context)

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
Here, the developer manually controls each step of the pipeline: reading, joining, aggregating, and writing.

Declarative Example (SDP)
python
from pyspark import pipelines as sdp

@sdp.materialized_view(name="claims_by_region")
def claims_by_region():
    return (
        spark.table("claims")
             .join(spark.table("policies"), "policy_id")
             .groupBy("region")
             .count()
    )
Here, the desired output is declared, and SDP automatically handles orchestration, retries, and dependencies.

Reinsurance Context
Imperative pipelines are useful for ad‑hoc actuarial analysis, where analysts want to quickly test assumptions or run one‑off calculations on claims and policies.

Declarative pipelines are ideal for production workflows, such as calculating regional claim aggregates for reinsurers.

Example: A reinsurer may need daily updates of claim counts by region to assess exposure.

Declarative style ensures the pipeline is scalable, maintainable, and fault‑tolerant without manual orchestration.

Key Takeaway
Use imperative style when you need fine‑grained control for exploratory work.

Use declarative style when building repeatable, production‑grade pipelines in the reinsurance domain.
