from services import fetch_countries, fetch_subdivisions
from lib.utils import measure_execution_time


@measure_execution_time
def main():
    # 1. Fetch countries
    fetch_countries.main()
    fetch_subdivisions.main()


if __name__ == "__main__":
    main()
