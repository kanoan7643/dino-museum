# 中生代恐龍館

用 three.js 製作的互動 3D 恐龍介紹網頁，單一 HTML 檔，不需建置。

- 15 種中生代恐龍；13 種使用 Sketchfab 動畫模型，腔骨龍與板龍依骨骼比例程序化生成
- 動作：站立、走路、跑步、休息、進食、吼叫（Web Audio 合成叫聲）
- 語音解說：瀏覽器內建語音合成，可選配音、語速、音調
- 地質年代軸、體長比較、人類比例尺

## 使用

直接用瀏覽器開啟 `index.html`，或啟用 GitHub Pages。自然語音在 Microsoft Edge 效果最好。

## 說明

體型、速度與年代為常見學術估計；皮膚顏色與叫聲屬推測。

## 3D 模型來源（CC BY 4.0）

| 物種 | 模型 | 作者 |
|------|------|------|
| 暴龍 | [Animated Tyrannosaurus Rex Dinosaur Running Loop](https://sketchfab.com/3d-models/animated-tyrannosaurus-rex-dinosaur-running-loop-38007d947ae74dea83988cb0b08ee053) | LasquetiSpice |
| 迅猛龍 | [PBR Velociraptor (Animated)](https://sketchfab.com/3d-models/pbr-velociraptor-animated-8f1744af7b0847a2aabe3df90be802f0) | Ferocious Industries |
| 劍龍 | [PBR Stegasaurus (Animated)](https://sketchfab.com/3d-models/pbr-stegasaurus-animated-ec254ea1554941fe8a131f62db0faf3d) | Ferocious Industries |
| 厚頭龍 | [PBR Pachycephalasaurus (Animated)](https://sketchfab.com/3d-models/pbr-pachycephalasaurus-animated-6eea5cee4afa4730bf75c6329a43e56d) | Ferocious Industries |
| 三角龍 | [TRICERA](https://sketchfab.com/3d-models/tricera-6b0695ecb40a40dabd4f118ee4b729cd) | seth the yutyrannus |
| 棘龍 | [Spinosaurus_animation](https://sketchfab.com/3d-models/spinosaurus-animation-c11709dbf9e3472f9533343f1f342564) | seirogan |
| 異特龍 | [Allosaurus skin 2](https://sketchfab.com/3d-models/allosaurus-skin-2-8a0506931dec4191999423fc5d0b348c) | seth the yutyrannus |
| 副櫛龍 | [parasaurolophus_from_unity](https://sketchfab.com/3d-models/parasaurolophus-from-unity-ab7807cf205c42f08b16ee2f2fc0e32d) | dead tubby's |
| 甲龍 | [Ankylosaurus from unity](https://sketchfab.com/3d-models/ankylosaurus-from-unity-0c9978755f244457a566b258139affa4) | dead tubby's |
| 腕龍 | [Branchiosaurus](https://sketchfab.com/3d-models/branchiosaurus-cf45b96559a4468b9487a657acc3d7a3) | kenchoo |
| 梁龍 | [WWD diplodocus (animated)](https://sketchfab.com/3d-models/wwd-diplodocus-animated-b4d3a76625274284a56c4f9f872fcd2d) | seth the yutyrannus |
| 禽龍 | [Dino Hunter Deadly Shores Iguanodon](https://sketchfab.com/3d-models/dino-hunter-deadly-shores-iguanodon-bc5bf0d1284a4515ac7724fd138fd540) | SpikeDaBoi |
| 似雞龍 | [Dino Hunter Deadly Shores Gallimimus](https://sketchfab.com/3d-models/dino-hunter-deadly-shores-gallimimus-3e0f606c92a748cebc4ea7031afdea8c) | PaPmont |

模型由 GitHub Actions（`.github/workflows/sketchfab.yml`）執行 `tools/sketchfab_download.py` 下載，需要儲存庫 secret `SKETCHFAB_TOKEN`。

授權：[Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/)。修改：貼圖轉為 WebP 以縮小檔案（gltf-transform）；異特龍模型加上色調。
