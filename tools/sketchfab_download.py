"""Download CC BY dinosaur models from Sketchfab as .glb into models/.

Needs a Sketchfab API token (https://sketchfab.com/settings/password):
    SKETCHFAB_TOKEN=xxxx python tools/sketchfab_download.py [species ...]
With no species given, every entry in PICKS is downloaded. The zip is saved
under .raw/ and the glTF inside is packed to models/<species>.glb. If
gltf-transform is installed (npm i -g @gltf-transform/cli), textures are
converted to WebP like the existing models.
"""
import io, json, os, shutil, subprocess, sys, urllib.request, zipfile

# species -> Sketchfab uid (candidates from .thumbs/cands.json: CC Attribution, animated)
PICKS = {
    'triceratops':     '6b0695ecb40a40dabd4f118ee4b729cd',  # TRICERA - seth the yutyrannus, 9 anims
    'spinosaurus':     'c11709dbf9e3472f9533343f1f342564',  # Spinosaurus_animation - seirogan
    'allosaurus':      '8a0506931dec4191999423fc5d0b348c',  # Allosaurus skin 2 - seth the yutyrannus
    'parasaurolophus': 'ab7807cf205c42f08b16ee2f2fc0e32d',  # parasaurolophus_from_unity - dead tubby's, 5 anims
    'ankylosaurus':    '0c9978755f244457a566b258139affa4',  # Ankylosaurus from unity - dead tubby's, 6 anims
    'brachiosaurus':   'cf45b96559a4468b9487a657acc3d7a3',  # Branchiosaurus - kenchoo
    'diplodocus':      'b4d3a76625274284a56c4f9f872fcd2d',  # WWD diplodocus (animated) - seth the yutyrannus
    'iguanodon':       'bc5bf0d1284a4515ac7724fd138fd540',  # Dino Hunter Deadly Shores Iguanodon - SpikeDaBoi, 50 anims
    'gallimimus':      '3e0f606c92a748cebc4ea7031afdea8c',  # Dino Hunter Deadly Shores Gallimimus - PaPmont, 44 anims
    'coelophysis':     '701a8ae582fd4f83b3e8c8f3fbf870de',  # accurate dilophosaurus rig - Hhhhhh66 (stand-in), 4 anims
}
API = 'https://api.sketchfab.com/v3/models/'


def get(url, token=None):
    req = urllib.request.Request(url, headers={'Authorization': f'Token {token}'} if token else {})
    with urllib.request.urlopen(req) as r:
        return r.read()


def fetch(species, uid, token):
    info = json.loads(get(API + uid))
    lic = (info.get('license') or {}).get('label', '?')
    print(f'{species}: "{info["name"]}" by {info["user"]["displayName"]} [{lic}]')
    if 'CC Attribution' != lic:
        print('  skipped: license is not CC BY')
        return
    dl = json.loads(get(API + uid + '/download', token))
    raw = os.path.join('.raw', species)
    shutil.rmtree(raw, ignore_errors=True)
    zipfile.ZipFile(io.BytesIO(get(dl['gltf']['url']))).extractall(raw)
    src = next(os.path.join(d, f) for d, _, fs in os.walk(raw) for f in fs if f.endswith('.gltf'))
    out = os.path.join('models', species + '.glb')
    cmd = ['gltf-transform', 'webp', src, out] if shutil.which('gltf-transform') else ['npx', '-y', '@gltf-transform/cli', 'copy', src, out]
    subprocess.run(cmd, check=True)
    print(f'  -> {out} ({os.path.getsize(out) / 1e6:.1f} MB)  {info["viewerUrl"]}')


def main():
    token = os.environ.get('SKETCHFAB_TOKEN')
    if not token:
        sys.exit('Set SKETCHFAB_TOKEN to your Sketchfab API token.')
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    for sp in sys.argv[1:] or PICKS:
        try:
            fetch(sp, PICKS[sp], token)
        except Exception as e:
            print(f'{sp}: failed - {e}')


if __name__ == '__main__':
    main()
