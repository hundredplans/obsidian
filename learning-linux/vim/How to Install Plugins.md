Go into your [[init.vim]] file and type this
```vim
call plug#begin()
Plug 'plugin_path'
call plug#end()
```
Then type :PlugInstall into the [[command-line-mode]], don't remove after from [[init.vim]] after install

If you want to install only specific Plugins do a space seperated list
- *:PlugInstall plugin_name1 plugin_name2*