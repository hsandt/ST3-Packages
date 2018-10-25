import sublime, sublime_plugin

class bookmarkWatcher(sublime_plugin.EventListener):
    def on_activated_async(self, view):
        sublime.active_window().run_command("sublime_bookmark", {"type": "mark_buffer" } )
        sublime.active_window().run_command("sublime_bookmark", {"type": "move_bookmarks" } )


    def on_modified_async(self, view):
        sublime.active_window().run_command("sublime_bookmark", {"type": "move_bookmarks" } )


    def on_deactivated_async(self, view):
        sublime.active_window().run_command("sublime_bookmark", {"type": "mark_buffer" } )
        sublime.active_window().run_command("sublime_bookmark", {"type": "move_bookmarks" } )

    #must be no close, not on pre close. on pre-close,the view still exists
    def on_close(self, view):
        # it may break the plugin to comment this, but that's a hot fix to avoid very long
        # on_close event (see Profile Events command). This plugin is unmaintained anyway, but bookmarks may be useful.
        pass
        # sublime.active_window().run_command("sublime_bookmark", {"type": "update_temporary" } )

    def on_pre_save_async(self, view):
        pass
        #sublime.run_command("sublime_bookmark", {"type": "save_data" } )
