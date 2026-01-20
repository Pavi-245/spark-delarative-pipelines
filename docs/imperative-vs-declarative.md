# Imperative vs Declarative Programming in SDP

| Aspect | Imperative Approach | Declarative Approach |
|--------|---------------------|----------------------|
| **Focus** | Explicitly coding each step of data ingestion, transformation, and output | Defining desired tables/views and letting SDP orchestrate execution |
| **Control** | Developer manages orchestration, error handling, and dependencies | SDP automatically handles orchestration, retries, and dependencies |
| **Example** | `df = spark.read.csv(...); df.write.save(...)` | `@sdp.materialized_view def claims_mv(): return spark.table("claims")` |
| **Reinsurance Context** | Manually coding ingestion of claims, policies, and treaties | Declaring flows for claims, policies, and treaty exposures, SDP ensures consistency |
