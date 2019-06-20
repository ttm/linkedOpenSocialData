import datadotworld as d

td = intro_dataset = d.load_dataset('rfabbri/test1')

q = """SELECT * WHERE {?s ?p ?o}"""

q2 = """
PREFIX po: <http://purl.org/socialparticipation/po/>
SELECT ?s WHERE {?s a po:Participant}
"""

r = d.query('rfabbri/test1', q2, query_type='sparql')
