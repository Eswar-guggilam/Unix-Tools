## Advanced Vim Editing: To Boost Your Productivity
Vim is a simple command line editor with better customisation. There are 3 modes in Vim editor 1. Normal mode, 2. Insert Mode and 3. Visual Mode makes it easier to edit.


**1. Modal Editing**

- **Normal Mode:** The default mode for most commands.
    - ` h, j, k, l `: Move one character left, down, up, or right.
    - ` w, e, b `: Move to the beginning or end of the next or previous word.
    - ` 0, ^ `: Move to the beginning of the current line or the first non-whitespace character.
    - ` $ `: Move to the end of the current line.
    - ` gg `: Go to the first line.
    - ` shft + g (G)`: Go to the last line.
    - ` shft + zz `: Save and exit
- **Insert Mode:** Enter this mode to insert text.
    - `i, a, o, O`: Insert before the cursor, after the cursor, a new line below, or a new line above.
- **Visual Mode:** Select text for various operations.
    - `v`: Character-wise selection.
    - `shft + v`: Line-wise selection.
    - `gv`: Go back to the previous selection.

**2. Motions and Operators**

- **Operators:** Commands that act on selected text or a motion.
    - `d`: Delete the selected text or the result of a motion.
    - `y`: Yank (copy) the selected text or the result of a motion.
    - `c`: Change the selected text or the result of a motion to insert mode.
    - `p`: Put (paste) the last yanked or deleted text.

**4. Search and Replace**

- **Basic Search:**
    - `/pattern`: Search forward for the pattern.
        - Ex: `/ws-var1`: to find ws-var in the program.     
    - `?pattern`: Search backwards for the pattern.
        - Ex: ` ?ws-var`: to find ws-var from down.
    - `n`: Find the next match.
    - `N`: Find the previous match.
- **Advanced Search:**
    - `\<`: Match the beginning of a word.
    - `\>`: Match the end of a word.
    - `\+`: Match one or more occurrences.
    - `\*`: Match zero or more occurrences.
- **Replace:**
    - `:%s/old/new/g`: Replace all occurrences of "old" with "new" in the current file.
       - `%s/var/ws-var/g`: To replace all the var with ws-var.
    - `:5,11%s/var/ws-var/gci`: Replace according to your option from 5 to 11th line.
       - `4,21%s/var/ws-var/gci`: To replace all 'var' with 'ws-var' from 4 to 21 lines according to your options.

**5. Window Management and Tabs**

- **Windows:**
    - `:split`: Split the current window horizontally.
    - `:vsplit`: Split the current window vertically.
    - `:close`: Close the current window.
- **Tabs:**
    - `:tabnew`: Open a new tab.
    - `:tabnext`: Go to the next tab.
    - `:tabprevious`: Go to the previous tab.
    - `:tabclose`: Close the current tab.

- **Indent/Outdent:**

    - `>>`: Indent the current line or selected lines.
    - `<<`: Outdent the current line or selected lines.
- **Change case:**
    - `guu`: Change the current line to lowercase.
    - `gUU`: Change the current line to uppercase.
    - `~`: Change the case of the selection.
    - `:%s/.*/\L&/`: Converts all Upper to Lower cases.
    - `:%s/.*/\U&/`: Converts all Lower to Upper cases.
