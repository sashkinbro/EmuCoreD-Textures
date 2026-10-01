# EmuCoreD-Textures

Nintendo 3DS texture pack catalog for [EmuCoreD](https://github.com/sashkinbro/EmuCoreD).

Azahar loads replacement textures from `load/textures/<title id>/` inside the
emulator data folder. Packs use PNG, DDS, or KTX images and an optional
`texture_replacements.json` manifest.

## Layout

- `textures.json` - the catalog consumed by the app
- `schemas/texture-catalog.schema.json` - catalog schema
- `scripts/` - validation helpers

## Status

The catalog is being populated. Redistributable packs are mirrored in this
repository; entries without redistribution permission link to their authors'
downloads. The catalog credits the original sources.

No game data is distributed here. Nintendo 3DS is a trademark of Nintendo.
