import bvbrc as bv

genome = bv.GenomeClient()

q = bv.query(
    bv.keyword("COMPL*TE"),
    select=["genome_id", "genome_name", "genome_status"],
    sort=["+genome_length"],
    limit=50
)

q = bv.query(
    bv.fld("genome_name") == "Mycobacterium",
    select=["genome_id", "genome_name"]
)

# res = genome.search(
#     genome.checkm_completeness > 99,
#     select=["genome_name", "checkm_completeness"],
#     limit=5,
#     return_format=bv.ReturnFormat.CSV,
#     genome_quality="Good"
# )

res = genome.submit_query(q)
df = res.to_polars()
print(df)



