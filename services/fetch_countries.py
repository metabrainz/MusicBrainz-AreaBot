import lib.fetch_SPARQL as fq

CURRENT_COUNTRIES = """\
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>

SELECT ?country ?countryLabel ?iso_3166_1_code ?geonamesID
WHERE {
  {
    ?country wdt:P31 wd:Q3624078.
    OPTIONAL {
      ?country wdt:P297 ?iso_3166_1_code.
    }
    OPTIONAL {
      ?country wdt:P1566 ?geonamesID.
    }
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
"""

FORMER_COUNTRIES = """\
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>

SELECT ?country ?countryLabel ?iso_3166_3_code ?geonamesID
WHERE {
  {
    ?country wdt:P31 wd:Q3024240.
    OPTIONAL {
      ?country wdt:P773 ?iso_3166_3_code.
    }
    OPTIONAL {
      ?country wdt:P1566 ?geonamesID.
    }
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
"""

FORMER_AND_CURRENT_COUNTRIES = """\
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>

SELECT ?country ?countryLabel ?iso_3166_1_code ?iso_3166_3_code ?status ?geonamesID
WHERE {
  {
    ?country wdt:P31 wd:Q3624078.
    OPTIONAL {
      ?country wdt:P297 ?iso_3166_1_code.
    }
    OPTIONAL {
      ?country wdt:P1566 ?geonamesID.
    }
    BIND("Current" AS ?status)
  }
  UNION
  {
    ?country wdt:P31 wd:Q3024240.
    OPTIONAL {
      ?country wdt:P773 ?iso_3166_3_code.
    }
    OPTIONAL {
      ?country wdt:P1566 ?geonamesID.
    }
    BIND("Historical" AS ?status)
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}

"""


def main():
    # fq.fetch_and_store(FORMER_AND_CURRENT_COUNTRIES, "data/former_and_current_countries.csv")
    fq.fetch_and_store(CURRENT_COUNTRIES, "data/current_countries.csv")
    fq.fetch_and_store(FORMER_COUNTRIES, "data/former_countries.csv")


if __name__ == "__main__":
    main()
