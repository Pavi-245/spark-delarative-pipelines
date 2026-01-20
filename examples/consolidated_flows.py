sdp.create_streaming_table("claims_consolidated")

@sdp.append_flow(target="claims_consolidated")
def append_domestic_claims():
    return spark.readStream.table("claims_domestic")

@sdp.append_flow(target="claims_consolidated")
def append_international_claims():
    return spark.readStream.table("claims_international")
