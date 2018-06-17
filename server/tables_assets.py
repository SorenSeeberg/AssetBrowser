from mr_database import MrDatabase
from mr_database import Table
from mr_database import Column
from mr_database import DataTypes


""" ASSET """


class AssetType(Table):

    id = Column(DataTypes.integer, pk=True)
    name = Column(DataTypes.varchar(24))


class Asset(Table):
    id = Column(DataTypes.integer, pk=True)
    name = Column(DataTypes.varchar(60))
    assetTypeid = Column(DataTypes.integer, fk=(AssetType, 'id'), default=1)


""" ASSET - TEXTURE """


class TextureFormat(Table):

    id = Column(DataTypes.integer, pk=True)
    name = Column(DataTypes.char(3))


class Texture(Table):

    id = Column(DataTypes.integer, pk=True)
    format = Column(DataTypes.integer, fk=(TextureFormat, 'id'), default=1)
    resolutionX = Column(DataTypes.smallint, default=1024)
    resolutionY = Column(DataTypes.smallint, default=1024)


class AssetTexture(Table):
    id = Column(DataTypes.integer, pk=True)
    assetId = Column(DataTypes.integer, fk=(Asset, 'id'), default=1)
    textureId = Column(DataTypes.integer, fk=(Texture, 'id'), default=1)


""" ASSET - MESH """


class Mesh(Table):
    id = Column(DataTypes.integer, pk=True)
    assetId = Column(DataTypes.integer, fk=(AssetType, 'id'), default=1)


class AssetsMesh(Table):
    id = Column(DataTypes.integer, pk=True)
    assetId = Column(DataTypes.integer, fk=(Asset, 'id'), default=1)
    model3dId = Column(DataTypes.integer, fk=(Mesh, 'id'), default=1)


""" TAGS """


class TagGroup(Table):

    id = Column(DataTypes.integer, pk=True)
    name = Column(DataTypes.varchar(60))
    color = Column(DataTypes.char(6))


class Tag(Table):

    id = Column(DataTypes.integer, pk=True)
    groupId = Column(DataTypes.integer, fk=(TagGroup, 'id'), default=1)
    name = Column(DataTypes.varchar(60))
    color = Column(DataTypes.char(8))


class AssetTag(Table):
    """Junction Table: Asset & Yag"""

    id = Column(DataTypes.integer, pk=True)
    assetId = Column(DataTypes.integer, fk=(Asset, 'id'))
    tagId = Column(DataTypes.integer, fk=(Tag, 'id'))


if __name__ == '__main__':
    db = MrDatabase('table_test.db')
    db.create_table(AssetType)
    db.create_table(Asset)

    db.create_table(TextureFormat)
    db.create_table(Texture)
    db.create_table(AssetTexture)

    db.create_table(Mesh)
    db.create_table(AssetsMesh)

    db.create_table(TagGroup)

    default_tag_group = TagGroup()
    default_tag_group.name = "Default Tags"
    default_tag_group.color = "FFFFFF"

    db.insert_record(default_tag_group)
    db.create_table(Tag)
    db.create_table(AssetTag)
