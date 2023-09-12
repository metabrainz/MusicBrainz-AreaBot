from services import fetch_countries
from lib.utils import measure_execution_time


@measure_execution_time
def main():
    # 1. Fetch countries
    fetch_countries.main()


if __name__ == "__main__":
    main()
