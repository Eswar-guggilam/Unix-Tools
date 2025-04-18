
[![VIM](https://www.vim.org/images/vim_editor.gif)](https://www.vim.org/images/vim_editor.gif)

[![LinkedIn](https://img.shields.io/badge/linkedin-Eswar%20Guggilam%20linkedIn-blue)](https://www.linkedin.com/in/eswar-guggilam-tv/)
## Advanced Vim Editing: To Boost Your Productivity
Vim is a simple command line editor with better customisation. There are 3 modes in Vim editor 1. Normal mode, 2. Insert Mode and 3. Visual Mode makes it easier to edit.


## Modal Editing

- **Normal Mode:** The default mode for most commands.
    - ` h, j, k, l `: Move one character left, down, up, or right.
    - ` w, e, b `: Move to the beginning or end of the next or previous word.
    - ` 0, ^ `: Move to the beginning of the current line or the first non-whitespace character.
    - ` dd, yy/Y, pp/P `: Delete lines, Copy lines, Paste lines.
    - `D` : Delete from cursor to end of line
    - `x` : Delete character under cursor
    - `X` : Delete character before cursor
    - ` $ `: Move to the end of the current line.
    - ` gg `: Go to the first line.
    - ` shft + g (G)`: Go to the last line.
    - ` shft + zz `: Save and exit
    - `{number}G` : Go to specific line number. `620+shft+G`
    - ` Esc + u`, ` ctrl + r` : Unod, Redo
- **Screen Movement**
    - `ctrl+f` - Page down
    - `ctrl+b` - Page up
    - `ctrl+d` - Half page down
    - `ctrl+u` - Half page up
- **Jumps**
    - `ctrl+o` - Go to older position in jump list
    - `ctrl+i` - Go to newer position in jump list
    - `g;` - Go to older position in change list
    - `g,` - Go to newer position in change list
    - `:jumps` - List jump history
- **Insert Mode:** Enter this mode to insert text.
    - `i, a, o, O`: Insert before the cursor, after the cursor, a new line below, or a new line above.
- **Visual Mode:** Select text for various operations.
    - `v`: Character-wise selection.
    - `shft + v`: Line-wise selection.
    - `gv`: Go back to the previous selection.
    - `ctrl + alt + v`: Free form selection, that can effect multiple lines

## Mode Switching
- `i` - Enter insert mode before cursor
- `I` - Enter insert mode at beginning of line
- `a` - Enter insert mode after cursor
- `A` - Enter insert mode at end of line
- `o` - Open new line below and enter insert mode
- `O` - Open new line above and enter insert mode
- `Esc` - Exit current mode to normal mode
- `v` - Enter visual mode
- `V` - Enter visual line mode
- `ctrl+v` - Enter visual free form mode
  
**Motions and Operators**

- **Operators:** Commands that act on selected text or a motion.
    - `d`: Delete the selected text or the result of a motion.
    - `y`: Yank (copy) the selected text or the result of a motion.
    - `c`: Change the selected text or the result of a motion to insert mode.
    - `p`: Put (paste) the last yanked or deleted text.

## File Operations
- **Basic Operations**
    - `:w` - Write (save) file
    - `:w filename` - Write to filename
    - `:q` - Quit
    - `:q!` - Quit without saving
    - `:wq` or `:x` - Write and quit
    - `:saveas filename` - Save as filename

- **File Explorer (netrw)**
    - `:Explore` or `:E` - Open file explorer
    - `:Sexplore` - Open in horizontal split
    - `:Vexplore` - Open in vertical split
## Search and Replace

- **Basic Search:**
    - `/pattern`: Search forward for the pattern.
        - Ex: `/ws-var1`: to find ws-var in the program.
    - `/string1.*string2`: Search for the string, starting with 'string1' & ending with 'string2'.
        - Ex: `/ws.*out`: To find the string starting with 'ws' & ending with 'out' (Ex: ws-stmt-out-num) 
    - `?pattern`: Search backwards for the pattern.
        - Ex: ` ?ws-var`: to find ws-var from down.
    - `n`: Find the next match.
    - `N`: Find the previous match.
    - `*` - Search forward for word under cursor
    - `#` - Search backward for word under cursor
    - `g*` - Search forward for partial word under cursor
    - `g#` - Search backward for partial word under cursor

- **Replace:**
    - `:%s/old/new/g`: Replace all occurrences of "old" with "new" in the current file.
       - `%s/var/ws-var/g`: To replace all the var with ws-var.
    - `:5,11%s/var/ws-var/gci`: Replace according to your option from 5 to 11th line.
       - `4,21%s/var/ws-var/gci`: To replace all 'var' with 'ws-var' from 4 to 21 lines according to your options.

## Window Management and Tabs

- **Windows:**
    - `:split`: Split the current window horizontally.
    - `:vsplit`: Split the current window vertically.
    - `:close`: Close the current window.
- **Tabs:**
    - `:tabnew`: Open a new tab.
    - `:tabnext`: Go to the next tab.
    - `:tabprevious`: Go to the previous tab.
    - `:tabclose`: Close the current tab.
    - `Ctrl + ww`: Allows to navigate between the tabs.

- **Indent/Outdent:**

    - `>>`: Indent the current line or selected lines.
    - `<<`: Outdent the current line or selected lines.
- **Change case:**
    - `guu`: Change the current line to lowercase.
    - `gUU`: Change the current line to uppercase.
    - `~`: Change the case of the selection.
    - `:%s/.*/\L&/`: Converts all Upper to Lower cases.
    - `:%s/.*/\U&/`: Converts all Lower to Upper cases.


- **Note**
    - Please suggest new ideas for improving this document. Actively seeking contributions
