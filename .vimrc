" Glossary of useful vim commands
" http://tedlogan.com/techblog3.html

" **** start of the tabs section ****
" shiftwidth to control how many columns text is indented with the 
" reindent operations (<< and >>) and automatic C-style indentation. 
set shiftwidth=4
set ts=4
set sts=4
set shiftwidth=4
" expandtab replaces tabs with spaces, PEP8 recommends spaces instead of tabs 
set expandtab
" **** end of tabs ****

set autoindent
set smartindent
set smarttab
set cindent

" automatically indent the braces
inoremap {<CR> {<CR>}<C-o>O

" enable auto filetype detect
filetype on
set ff=unix

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

" use the mouse in vim
set mouse=a


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

