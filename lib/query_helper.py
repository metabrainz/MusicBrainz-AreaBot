def make_subdivision_query(division_identifier):
    """Returns a SPARQL query to fetch the subdivisions of a given division."""

    DIRECT_SUBDIVISION = """
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?subdivision ?subdivisionLabel
    WHERE {
    BIND(%s AS ?division)
    OPTIONAL {
        ?division wdt:P150 ?subdivision.
    }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    }
    """
    query = DIRECT_SUBDIVISION % division_identifier
    return query
