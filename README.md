# shell-slovio
Bash/zsh translator and word-of-the-day in slovio.

What is slovio? It's a constructed language made to be best understood by the maximum number of speakers of slavic languages.

# Installation
1. git clone git@github.com:vladiibine/shell-slovio.git ~/.local/share/shell-slovio
2. alias slovio='python ~/.local/share/shell-slovio/slovio.py'

# Usage
$ slovio I like pie  

slovio: no entry found for I

slovio: like: lub-it, podob-ju, podob-uo, takak

slovio: pie: pirog, tort, kolacx


$ slovio -r lubit

slovio reverse: lubit: cherish, enjoy, fancy, have fun, like
