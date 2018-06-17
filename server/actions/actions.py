from server.tables_assets import Asset, Texture, TextureFormat
from server import paths
from mr_database import MrDatabase
from mr_database import Records


class AssetTypeId:

    texture = 1
    mesh = 2
    material = 3


def get_assets_all(condition: str="") -> Records:
    return __get_assets__(asset_type_id=-1, condition=condition)


def get_assets_textures(condition: str="") -> Records:
    return __get_assets__(asset_type_id=AssetTypeId.texture, condition=condition)


def get_assets_mesh(condition: str = "") -> Records:
    return __get_assets__(asset_type_id=AssetTypeId.mesh, condition=condition)


def get_assets_material(condition: str = "") -> Records:
    return __get_assets__(asset_type_id=AssetTypeId.material, condition=condition)


def __get_assets__(asset_type_id: int=-1, condition: str="", fetch_join_tables: bool=False) -> Records:

    db = MrDatabase(paths.ASSET_DATABASE_PATH)

    conditions = list()

    if asset_type_id != -1:
        conditions.append(f'assetTypeId = {asset_type_id}')

    if condition:
        conditions.append(condition)

    condition = ' AND '.join(conditions)

    if fetch_join_tables:
        records: Records = db.select_records(Asset, condition)
        [record.fetch_join_tables() for record in records]
        return records
    else:
        return db.select_records(Asset, condition)
