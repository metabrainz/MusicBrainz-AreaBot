import lib.fetch_SPARQL as fq

SUBDIVISIONS = """
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?country ?countryLabel ?division ?divisionLabel ?geonamesID ?iso_3166_2_code
WHERE {
  ?country wdt:P31 wd:Q3624078.   # Sovereign states
  OPTIONAL {
    ?country wdt:P150 ?division.  # Administrative division of the country
    OPTIONAL {
      ?division wdt:P1566 ?geonamesID.  # Geonames ID for the division
    }
    OPTIONAL {
      ?division wdt:P300 ?iso_3166_2_code # ISO 3166 2 code for the division
    }
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
"""


def main():
    fq.fetch_and_store(SUBDIVISIONS, "data/subdivisions.csv")


if __name__ == "__main__":
    main()
