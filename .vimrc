" Glossary of useful vim commands
" http://tedlogan.com/techblog3.html

" tell vim how many columns a tab counts for
"set softtabstop=4

" shiftwidth to control how many columns text is indented with the 
" reindent operations (<< and >>) and automatic C-style indentation. 
set shiftwidth=8

" Do not set "expandtabs", 
" which expands tabs as spaces, as tabs will prevent you from properly formatting code.
set noexpandtab

" enable auto filetype detect
filetype on
set ff=unix

" Toggle the numbering or no numbering by pressing Ctrl-N-N 
" or type set nu!
nmap <C-N><C-N> :set invnumber <CR>
nmap <C-L><C-L> :set invlist <CR>
nmap <C-P><C-P> :set invpaste <CR>

nmap <F2> :w<CR><Esc>
" remove trailing spaces
nmap <F3> :%s/\S\zs\s\+$//g<CR><Esc>
" remove empty lines
nmap <F4> :%s/\s\+$//g<CR><Esc>
nmap <F5> :Tlist<Enter>

colors zellner
set modeline

" have syntax highlighting in terminals which can display colours:
syntax on

" display the current mode and partially-typed commands in the status line:
set showmode
set showcmd

" show matching brackets
set showmatch

" Highlighted Search
set hlsearch

" Show where the cursor is
set ruler




