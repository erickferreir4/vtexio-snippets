# VTEX IO Snippets

A collection of **71 snippets** for VTEX IO store theme development in JSONC format.

> **Note:** This collection is a work in progress. Many VTEX IO blocks are still missing and will be added over time. Contributions are welcome.

## Install

Add to your Neovim / Vim plugin manager:

```lua
-- Packer
use "erickferreir4/vtexio-snippets"

-- Plug
Plug 'erickferreir4/vtexio-snippets'

-- coc.nvim
CocInstall https://github.com/erickferreir4/vtexio-snippets@master
```

For VS Code, copy the files from `snippets/jsonc/` into your `.vscode/` directory.

> **Note:** This package is not yet available as a plugin in the VS Code Marketplace.

## Usage

Each snippet expands to a block configuration with `$1`, `${1:name}` placeholders. Type the prefix and press Tab.

```
rich + Tab  →  rich-text block with props
flexc + Tab →  flex-layout.col block
prsp + Tab  →  product-selling-price block
```

## Project Structure

```
snippets/
  jsonc/
    Layout-Apps/       (10 files)
    Basic-components/  (17 files)
    Store-components/  (12 files)
snippets.md           (quick reference)
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

## License

[MIT](https://github.com/erickferreir4/vtexio-snippets/blob/master/LICENSE.md) &copy; 2022
