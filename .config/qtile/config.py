import os
import subprocess

from time import time
from pathlib import Path

from libqtile import bar, layout, widget, hook

# qtile on arch requires python-psutil to show the memory or cpu
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy


def screenshot(save=True, copy=True):
    def f(qtile):
        path = Path.home() / "Pictures"
        path /= f"screenshot_{str(int(time() * 100))}.png"
        shot = subprocess.run(["maim", "--select", "|"], stdout=subprocess.PIPE)

        if save:
            with open(path, "wb") as sc:
                sc.write(shot.stdout)

        if copy:
            subprocess.run(
                ["xclip", "-selection", "clipboard", "-t", "image/png"],
                input=shot.stdout,
            )

    return f


mod = "mod4"
terminal = "alacritty"
homePath = str(Path.home())

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "x", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "o", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key(
        [mod],
        "o",
        # lazy.spawn("rofi -show drun", shell=True),
        lazy.spawn("rofi -show drun"),
        # lazy.spawn("rofi -show combi -mode -combi-modes 'drun,run'"),
        desc="Spawn a command using a prompt widget",
    ),
    Key([mod], "a", lazy.spawn("pavucontrol"), desc="Spawn a volume control"),
    Key([mod], "w", lazy.spawn("firefox"), desc="Spawn firefox"),
    # Key([mod], "f", lazy.spawn("pcmanfm"), desc="Spawn file manager"),
    Key(
        [mod, "shift"],
        "e",
        # lazy.spawn("i3lock --color='#000000'"),
        lazy.spawn(homePath + "/.local/bin/powermenu"),
        desc="Spawn a prompt to show lock and shutdown options.",
    ),
    #    Key(
    #        [mod, "shift"],
    #        "p",
    #        lazy.function(screenshot()),
    #    ),
    Key([mod, "shift"], "m", lazy.hide_show_bar(), desc="Toggle top bar"),
    Key(
        [mod, "control"],
        "1",
        lazy.to_screen(0),
        desc="Keyboard focus to monitor 1 (left most)",
    ),
    Key(
        [mod, "control"],
        "2",
        lazy.to_screen(1),
        desc="Keyboard focus to monitor 2 (center)",
    ),
    Key(
        [mod, "control"],
        "3",
        lazy.to_screen(2),
        desc="Keyboard focus to monitor 3 (right most)",
    ),
]

groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(toggle=True),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus="#555555",
        border_width=2,
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        border_focus="#555555",
        border_width=2,
        ratio=0.6,
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(linewidth=0, padding=5),
                widget.Image(
                    # filename="~/.config/qtile/images/phoenix_logo.jpg",
                    filename="~/.config/qtile/images/ying_yang_32.png",
                    scale="False",
                    mouse_callbacks={
                        "Button1": lambda: os.system("rofi -show drun"),
                        # "Button1": lambda: qtile.cmd_spawn("rofi -show drun"),
                        # "Button1": lambda: lazy.spawn("rofi -show drun"),
                    },
                ),
                # widget.CurrentLayout(),
                # widget.AGroupBox(),
                widget.Sep(linewidth=0, padding=5),
                widget.GroupBox(
                    highlight_method="block",
                    rounded=False,
                    toggle=True,
                    inactive="#AAAAAA",
                    active="#FFFFFF",
                    # active"#000000",
                    # this_current_screen_border="#49a4f8",  # default color #215578
                    this_current_screen_border="34b35b",
                ),
                # widget.Prompt(),
                widget.Sep(linewidth=0, padding=10),
                # Hacky solution to hide the window name without shifting the elements on the right to the left
                widget.WindowName(foreground="#000000", background="#000000"),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.CurrentLayout(),
                widget.Sep(linewidth=0, padding=10),
                widget.CPU(
                    format="cpu: {load_percent}%",
                    update_interval=5.0,
                ),
                widget.Sep(linewidth=0, padding=10),
                widget.Memory(
                    measure_mem="G",
                    update_interval=5.0,
                ),
                # widget.Net(),
                widget.Sep(linewidth=0, padding=10),
                widget.Battery(
                    format=" {percent:2.0%} {char}",
                    charge_char="ac",
                    discharge_char="dc",
                    update_interval=5.0,
                ),
                widget.Sep(linewidth=0, padding=10),
                widget.TextBox(font="FontAwesome", text=""),
                widget.Clock(format="%a %b %d   %H:%M "),
                widget.Systray(),
                widget.Sep(linewidth=0, padding=5),
                # widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="qjackctl"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


@hook.subscribe.startup_once
def autostart():
    filePath = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([filePath])


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
