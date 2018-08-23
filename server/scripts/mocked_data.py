import uuid
import random
import json
from typing import List

BITMAP_TYPES = [
    {'type': 'png',
     'bpp': 8},
    {'type': 'jpg',
     'bpp': 2},
    {'type': 'dds',
     'bpp': 4},
]

NAME_THEMES = ['generic', 'winterlands', 'territories', 'wetlands']

BITMAP_CHANNELS = ['RGB', 'ARGB', 'RGBA']
BITMAP_SIZE = [128, 256, 512, 1024, 2048, 4096]
BITMAP_NAME_MATERIAL = ['metal', 'wood', 'cloth', 'plastic', 'glass', 'composite']
BITMAP_NAME_OBJECT = ['windows', 'door', 'wall', 'floor', 'roof', 'weapon', 'tool']
MESH_EXTENSIONS = ['obj', 'fbx']
MESH_CLASS = ['prop', 'env', 'char']
MESH_DESCRIPTOR = ['chair', 'table', 'statue', 'door', 'window', 'pants']
BOOL = [True, False]


class Tag:

    def __init__(self, id: int, name: str, color: str):
        self.id = id
        self.name = name
        self.color = color


BITMAP_TAGS = [
    Tag(id=0, name='texture2d', color='ff9900'),
    Tag(id=1, name='texture3d', color='99ff00'),
    Tag(id=2, name='tiling', color='99ff00'),
    Tag(id=3, name='rock', color='99ff00'),
    Tag(id=4, name='wood', color='99ff00')
]

MESH_TAGS = [
    Tag(id=5, name='mesh3d', color='99ff00'),
    Tag(id=6, name='mesh2d', color='99ff00'),
    Tag(id=7, name='chair', color='99ff00'),
    Tag(id=8, name='table', color='99ff00'),
    Tag(id=9, name='statue', color='99ff00')
]

CATEGORY_TAGS = [
    Tag(id=10, name='character', color='99ff00'),
    Tag(id=11, name='terrain', color='99ff00'),
    Tag(id=12, name='prop', color='99ff00')

]


def get_rnd_tags(min: int, max: int, tags: List[Tag]) -> List[str]:
    if min == max:
        num_tags = min
    else:
        num_tags = random.randrange(min, max + 1)

    random_tags: List[str] = list()

    while len(random_tags) < num_tags:
        tag: Tag = random.choice(tags)
        if tag.name not in random_tags:
            random_tags.append(tag.name)

    return random_tags


def get_bitmap_description(asset):
    metadata = asset.get('metadata')
    return f'{metadata.get("res_x")} x {metadata.get("res_y")} {metadata.get("channels")} @ {metadata.get("bpp")}bpp'


def get_mesh_description(asset):
    metadata = asset.get('metadata')
    return f'{metadata.get("drawcalls")} drawcall(s) {metadata.get("vertices")} vertices {metadata.get("lods")} LOD(s)'


def get_asset_name(list_a: List[str], list_b: List[str], list_c: List[str]):
    return '_'.join(
        [random.choice(list_a),
         random.choice(list_b),
         random.choice(list_c),
         str(random.randrange(100, 1000))])


def get_bitmap():
    tex_type = random.choice(BITMAP_TYPES)
    tex_res = random.choice(BITMAP_SIZE)
    tex_channels = random.choice(BITMAP_CHANNELS)
    num_channels = len(tex_channels)
    size = tex_res * tex_res * num_channels * tex_type.get('bpp')

    bitmap = {
        'id': str(uuid.uuid4()),
        'thumb': 'thumb.png',
        'name': get_asset_name(NAME_THEMES, BITMAP_NAME_MATERIAL, BITMAP_NAME_OBJECT),
        'type': 'bitmap',
        'extension': tex_type.get('extension'),
        'tags': get_rnd_tags(1, 3, BITMAP_TAGS) + get_rnd_tags(0, 2, CATEGORY_TAGS),
        'metadata': {
            'size_bytes': size,
            'res_x': tex_res,
            'res_y': tex_res,
            'channels': tex_channels,
            'bpp': tex_type.get('bpp'),
            'mip_maps': random.choice(BOOL)
        }
    }

    bitmap['description'] = get_bitmap_description(bitmap)

    return bitmap


def get_mesh():
    extension = random.choice(MESH_EXTENSIONS)
    vertices = random.randrange(2 ** 10, 2 ** 16)
    uv_channels = random.randrange(1, 4)
    size = vertices * 8 * uv_channels
    drawcalls = random.randrange(1, 5)

    mesh = {
        'id': str(uuid.uuid4()),
        'thumb': 'thumb.png',
        'name': get_asset_name(NAME_THEMES, MESH_CLASS, MESH_DESCRIPTOR),
        'type': 'mesh',
        'extension': extension,
        'tags': get_rnd_tags(1, 3, MESH_TAGS) + get_rnd_tags(0, 2, CATEGORY_TAGS),
        'metadata': {
            'vertices': vertices,
            'uv_channels': uv_channels,
            'size_bytes': size,
            'lods': random.randrange(1, 5),
            'drawcalls': drawcalls
        }
    }

    mesh['description'] = get_mesh_description(mesh)

    return mesh


if __name__ == '__main__':

    # print(get_rnd_tags(1, 3, MESH_TAGS))
    textures = (get_bitmap() for x in range(300))
    meshes = (get_mesh() for x in range(300))

    with open('assets.json', 'w') as f:
        json.dump(list(textures) + list(meshes), f)
