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
