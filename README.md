# VTEX IO Snippets

A collection of **71 snippets** for [VTEX IO](https://developers.vtex.com/) store theme development. Supports **Helix**, **Neovim**, **Vim**, and **VS Code**.

> **Note:** This collection is a work in progress. Contributions are welcome.

## Install

### Helix

Requires [scls](https://github.com/estin/simple-completion-language-server) for external snippet support.

Add to your `languages.toml` (typically `~/.config/helix/languages.toml`):

```toml
[[language]]
name = "jsonc"
language-servers = ["scls", "vscode-json-language-server"]
```

Add to your `external-snippets.toml` (typically `~/.config/helix/external-snippets.toml`):

```toml
[[sources]]
name = "vtexio-snippets"
git = "https://github.com/erickferreir4/vtexio-snippets.git"

[[sources.paths]]
scope = ["jsonc"]
path = "snippets.json"
```

Then run:

```bash
simple-completion-language-server fetch-external-snippets
simple-completion-language-server validate-snippets
```

### Neovim / Vim

```lua
-- Packer
use "erickferreir4/vtexio-snippets"

-- lazy.nvim
{ "erickferreir4/vtexio-snippets" }

-- vim-plug
Plug 'erickferreir4/vtexio-snippets'

-- coc.nvim
CocInstall https://github.com/erickferreir4/vtexio-snippets@master
```

### VS Code

This package is not yet on the VS Code Marketplace. Install it locally:

1. Clone the repo into `~/.vscode/extensions/vtexio-snippets/`
2. Restart VS Code

Alternatively, copy the individual snippet files from `snippets/` into your `.vscode/` directory as `.code-snippets` files.

## Usage

Type a prefix and press Tab to expand into a full VTEX IO block configuration. Use Tab to jump between placeholders (`$1`, `$2`, etc.).

| Input       | Expands to                         |
|-------------|------------------------------------|
| `rich`      | `rich-text` block with props       |
| `flexc`     | `flex-layout.col` block            |
| `flexr`     | `flex-layout.row` block            |
| `prsp`      | `product-selling-price` block      |
| `stacl`     | `stack-layout` block               |
| `slidlg`    | `slider-layout-group` block        |

## Project Structure

```
snippets/
  Layout-Apps/         (10 files)
  Basic-components/    (17 files)
  Store-components/    (12 files)
snippets.json         (all 71 snippets in a single file)
package.json          (VS Code extension manifest)
```

## Snippets

### Layout Apps

| Prefix    | Snippet                   |
|-----------|---------------------------|
| `flexr`   | Flex Layout Row           |
| `flexc`   | Flex Layout Column        |
| `flexrc`  | Flex Col into Flex Row    |
| `flexcr`  | Flex Row into Flex Col    |
| `condlp`  | Condition Layout Product  |
| `condls`  | Condition Layout Search   |
| `condlpb` | Condition Layout Binding  |
| `discl`   | Disclosure Layout         |
| `disclg`  | Disclosure Layout Group   |
| `resd`    | Responsive Desktop        |
| `restt`   | Responsive Tablet         |
| `restp`   | Responsive Phone          |
| `overl`   | Overlay Layout            |
| `modl`    | Modal Layout              |
| `stacl`   | Stack Layout              |
| `slidl`   | Slider Layout             |
| `slidlg`  | Slider Layout Group       |
| `sticl`   | Sticky Layout             |
| `tabl`    | Tab Layout                |

### Basic Components

| Prefix    | Snippet                      |
|-----------|------------------------------|
| `rich`    | Rich Text                    |
| `autoc`   | Autocomplete Result List     |
| `addc`    | Add To Cart Button           |
| `banns`   | Banner Search                |
| `brec`    | Breadcrumb                   |
| `brecs`   | Breadcrumb Search            |
| `foot`    | Footer                       |
| `headr`   | Header                       |
| `login`   | Login                        |
| `loginc`  | Login Content                |
| `menup`   | Menu Props                   |
| `menuc`   | Menu Children                |
| `menus`   | Menu Submenu                 |
| `highlf`  | Product Highlights Filter    |
| `highls`  | Product Highlights Simple    |
| `highlw`  | Product Highlights Wrapper   |
| `minic`   | Minicart v2                  |
| `prsp`    | Product Selling Price        |
| `prlp`    | Product List Price           |
| `prspp`   | Product Spot Price           |
| `prip`    | Product Installments Price   |
| `prilp`   | Product Installments List    |
| `prilip`  | Product Installments Item    |
| `prps`    | Product Price Savings        |
| `prpsps`  | Product Spot Price Savings   |
| `prlpr`   | Product List Price Range     |
| `prspr`   | Product Selling Price Range  |
| `prsn`    | Product Seller Name          |
| `prpsu`   | Product Price Suspense       |
| `prqy`    | Product Quantity             |
| `prspeg`  | Product Specifications Group |
| `prsu`    | Product Summary Self         |
| `prsubu`  | Product Summary Buy Button   |
| `prsui`   | Product Summary Image        |
| `searb`   | Search Bar                   |
| `searl`   | Search Result Layout         |
| `filn`    | Filter Navigator             |
| `stors`   | Store Search                 |
| `searlc`  | Search Result Custom         |
| `lisci`   | Store Image                  |

### Store Components

| Prefix  | Snippet              |
|---------|----------------------|
| `infc`  | Info Card            |
| `img`   | Image                |
| `backt` | Back To Top Button   |
| `log`   | Logo                 |
| `notb`  | Notification Bar     |
| `prbr`  | Product Brand        |
| `prds`  | Product Description  |
| `prims` | Product Images       |
| `prna`  | Product Name         |
| `shar`  | Share                |
| `ships` | Shipping Simulator   |
| `skus`  | Sku Selector         |

## Contributing

Missing a block? Open an [issue](https://github.com/erickferreir4/vtexio-snippets/issues) or submit a PR. Snippet files use the [FriendlySnippets](https://github.com/rafamadriz/friendly-snippets) format.

## License

[MIT](https://github.com/erickferreir4/vtexio-snippets/blob/master/LICENSE.md) &copy; 2022
