---
linkTitle: "Documentation"
title: "Home"
description: "Welcome to the documentation for Mario & Luigi: Bowser’s Inside Story!"
next: 'getting-started'
cascade:
  type: docs
---

> [!IMPORTANT]
> Most of the content on this site is only applicable to the original NDS version of the game!
> The 3DS remake, *Mario & Luigi: Bowser's Inside Story + Bowser Jr.'s Journey,* is much less understood,
> but will hopefully be documented soon enough.

Welcome to the documentation for *Mario & Luigi: Bowser's Inside Story* (BIS, known in Japan as *マリオ&ルイージRPG3!!!/Mario & Luigi RPG 3!!!)!*
New to modding this game? Then check out:
{{< cards >}}
    {{< card link="getting-started" title="Getting started" icon="document-text" >}}
{{< /cards >}}

## Tools & Libraries
### Tools
* **[Spritoglobin](https://github.com/MnL-Modding/Spritoglobin)** \[[Releases](https://github.com/MnL-Modding/Spritoglobin/releases)\] --- Sprite viewer. Currently only supports the US and EU versions. Editing support is being worked on.
* **[QtMnL](https://github.com/MnL-Modding/QtMnL)** \[[Releases](https://github.com/MnL-Modding/QtMnL/releases)\] (pronounced "cute emm-'n'-ell") --- GUI editor, built using Python and `mnllib.py`. Currently only supports editing `FEvent` scripts, but will hopefully support more soon.
* **[`mnlscript.py`](https://github.com/MnL-Modding/mnlscript.py)** --- Compiler and decompiler for the *Mario & Luigi* scripting language from and to Python, built using `mnllib.py`. Once again currently only supports `FEvent` scripts, but will hopefully support the rest soon.
### Libraries
* **`mnllib`** --- Library for the *Mario & Luigi* games. Provides things like classes with serializers and deserializers, as well as an implementation of the compression algorithm used by the game. Most development is done on the Python version.
    * **[`mnllib.py`](https://github.com/MnL-Modding/mnllib.py)** --- Pure Python implementation.
    * **[`mnllib.rs`](https://github.com/MnL-Modding/mnllib.rs)** --- Rust implementation. Currently only contains compression and decompression.

## Useful links
* [Google Drive](https://drive.google.com/drive/folders/1tVT5e3FYjqoBaatpglisQF4WcgfiS-DL) with extra documentation. Currently contains documentation for the text code and special characters, as well as a backup for the script commands documentation.
* Script commands documentation. Currently in raw TXT format, built by [`bisdocs.py`](https://github.com/MnL-Modding/BIS-docs/blob/main/cutscene_code/bisdocs.py):
    * [`FEvent` script commands documentation](scripting/fevent_commands.txt).
* [Notes](scripting/notes.txt) left behind by the developers in the footers of the scripts, in Japanese. Currently only notes within `FEvent` and Battle scripts are dumped. Automatically scraped by [`dump_notes.py`](https://github.com/MnL-Modding/BIS-docs/blob/main/cutscene_code/dump_notes.py).
