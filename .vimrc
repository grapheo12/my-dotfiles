set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'joshdick/onedark.vim'
Plugin 'neoclide/coc.nvim'

call vundle#end()
filetype plugin indent on

set number
set relativenumber
syntax on
colorscheme onedark
set tabstop=8
set softtabstop=4
set shiftwidth=4
set noexpandtab
