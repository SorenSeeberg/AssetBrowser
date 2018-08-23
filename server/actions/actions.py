from typing import Tuple
from server.tables_assets import Asset, Texture, TextureFormat, AssetTexture
from server import paths
from mr_database import MrDatabase
from mr_database import DatabaseConnection
from mr_database import ConType
from mr_database import Records


class AssetTypeId:

    texture = 1
    mesh = 2
    material = 3


def get_textures(db: MrDatabase, asset_condition: str= "") -> Tuple[Records, Records, Records]:

    with DatabaseConnection(db, ConType.batch):
        assets: Records = get_assets_textures(db, asset_condition)
        # textures: Records = assets.select_join_records(db, Texture)
        textures: Records = Records([asset.select_join_record(db, Texture) for asset in assets])
        texture_formats: Records = db.select_records(TextureFormat)

    return assets, textures, texture_formats


def get_assets_all(db: MrDatabase, condition: str="") -> Records:
    return __get_assets__(db, asset_type_id=-1, condition=condition)


def get_assets_textures(db: MrDatabase, condition: str="") -> Records:
    return __get_assets__(db, asset_type_id=AssetTypeId.texture, condition=condition)


def get_assets_mesh(db: MrDatabase, condition: str = "") -> Records:
    return __get_assets__(db, asset_type_id=AssetTypeId.mesh, condition=condition)


def get_assets_material(db: MrDatabase, condition: str = "") -> Records:
    return __get_assets__(db, asset_type_id=AssetTypeId.material, condition=condition)


def __get_assets__(db: MrDatabase, asset_type_id: int=-1, condition: str="", fetch_join_tables: bool=False) -> Records:

    # db = MrDatabase(paths.ASSET_DATABASE_PATH)

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


if __name__ == '__main__':

    db = MrDatabase(paths.ASSET_DATABASE_PATH)

    with DatabaseConnection(db, ConType.batch):
        textures = get_textures()
