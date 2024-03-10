from geocoders.geocoder import Geocoder
import api
from api import API
import pandas as pd
import pathlib

file_path = pathlib.Path(__file__).resolve().parent / "data" / "sample_data.csv"
df = pd.read_csv(file_path)


# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        area = API.get_area(area_id)
        result = [area.name]
        while area.parent_id is not None:
            area = API.get_area(area.parent_id)
            result.append(area.name)
        result = result[::-1]
        return ', '.join(result)
geocoder = SimpleQueryGeocoder()
result = geocoder._apply_geocoding("88")
print(result)