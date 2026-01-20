regions = ["US", "EU", "APAC"]

for region in regions:
    @sdp.table(name=f"{region.lower()}_treaty_exposures")
    def regional_treaty_exposures(region_filter=region):
        return spark.table("treaty_exposures").filter(f"region = '{region_filter}'")
