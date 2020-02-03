'''
Qtile Config by Shubham Mishra(@grapheo12)
'''
import os
import subprocess
from libqtile import layout
from libqtile import hook
from libqtile import bar, widget
from libqtile.command import lazy
from libqtile.config import Key
from libqtile.config import Group
from libqtile.config import Screen
from libqtile.config import Drag, Click
from libqtile.dgroups import simple_key_binder

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

if __name__ in ['config', '__main__']:
    #Set mod key and terminal and wmname
    wmname = 'LG3D'
    mod = 'mod4'
    myTerm = 'termite'

    #Set layouts
    layouts = [
            layout.xmonad.MonadTall(),
            layout.max.Max(),
            layout.matrix.Matrix()
            ]
    
    #Set groups
    groups = [
            Group("Web"),
            Group("Code"),
            Group("Files"),
            Group("GFX"),
            Group("Misc")
            ]

    #Set screens
    screens = [
            Screen(bottom=bar.Bar([
                widget.GroupBox(),
                widget.WindowTabs(),
                widget.Pacman(),
                widget.Notify(),
                widget.Battery(),
                widget.Clock(format="%H:%M:%S"),
                widget.Sep(
                        linewidth = 0,
                        padding = 5,
                        ),
               widget.Systray(
                        padding = 5
                        ),


                ], 30))
            ]


    #Set keybindings
    keys = [
            Key([mod], 'm',
                lazy.spawn('rofi -combi-modi window,drun,ssh -theme solarized -font "hack 10" -show combi')
                ),
            Key([mod], 'w',
                lazy.spawn('firefox')
                ),
            Key([mod], 'f',
                lazy.spawn('pcmanfm')
                ),
            Key([mod, 'shift'], 'Return',
                lazy.spawn("termite")
                ),
            Key([mod], 'q',
                lazy.window.kill()
                ),
            Key([mod], 'c',
                lazy.layout.next()
                ),
            Key([mod], 'Right',
                lazy.screen.next_group()
                ),
            Key([mod], 'Left',
                lazy.screen.prev_group()
                ),
            Key([mod], 'space',
                lazy.next_layout()
                ),
            Key([mod], 'Up',
                lazy.window.toggle_fullscreen()
                ),
            Key([mod], 'Down',
                lazy.window.toggle_floating()
                ),
            Key([mod, 'shift'], '1',
                lazy.window.togroup("Web")
                ),
            Key([mod, 'shift'], '2',
                lazy.window.togroup("Code")
                ),
            Key([mod, 'shift'], '3',
                lazy.window.togroup("Files")
                ),
            Key([mod, 'shift'], '4',
                lazy.window.togroup("GFX")
                ),
            Key([mod, 'shift'], '5',
                lazy.window.togroup("Misc")
                ),
            Key([mod, 'shift'], 'equal',
                lazy.layout.increase_ratio()
                ),
            Key([mod], 'minus',
                lazy.layout.decrease_ratio()
                ),
            Key([mod, 'control'], 'r',
                lazy.restart()
                ),
            Key([mod, 'control'], 'l',
                lazy.shutdown()
                ),

            ]
    dgroups_key_binder = simple_key_binder(mod)

    mouse = [Drag([mod], "Button1", lazy.window.set_position_floating(),      # Move floating windows
                 start=lazy.window.get_position()),
            Drag([mod], "Button3", lazy.window.set_size_floating(),          # Resize floating windows
                 start=lazy.window.get_size()),
            Click([mod, "shift"], "Button1", lazy.window.bring_to_front())]  # Bring floating window to front


