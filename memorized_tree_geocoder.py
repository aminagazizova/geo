from __future__ import annotations
from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data
        self.__dict_data = {}
        self._extend_dict(self.__data)

    def _extend_dict(self, tree_areas: list[TreeNode], parent_str: str = ''):
        for node in tree_areas:
            address = f'{parent_str}, {node.name}' if parent_str else node.name
            self.__dict_data[node.id] = address
            self._extend_dict(node.areas, address)

    def _apply_geocoding(self, area_id: int) -> str:
        return self.__dict_data.get(str(area_id))
geocoder = MemorizedTreeGeocoder()
result = geocoder._apply_geocoding("88")
print(result)