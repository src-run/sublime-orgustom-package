
##
 # This file is part of the `src-run/sublime-orton-package` project.
 #
 # (c) Rob Frawley 2nd <rmf@src.run>
 #
 # For the full copyright and license information, please view the LICENSE.md
 # file that was distributed with this source code.
 ##

class SettingsBaseHelper(object):

    CONTEXT_ROOT = "settings-obj-context:root"
    CONTEXT_VIEW = "settings-obj-context:view"

    def initializeSettingContexts(self, settings_root, settings_view = None):
        """Initialized the setting context(s) available in current environment.

        This method must be invoked with a root settings object context (and an
        optional view settings object context) prior to calling any of the other
        helper methods defined by this class (as well as any classes inheriting
        from it) to initialize the properties required for any of these helpers
        to function.

        :param settings_root: a root-level sublime text settings object instance
        :type settings_root: sublime.Settings
        :param settings_view: a view-level sublime text settings object instance
        :type settings_view: sublime.Settings|none
        :return: no value
        :rtype: none
        """
 
        self.settings_root = settings_root;
        self.settings_view = settings_view;

    def _settingsContextSanitize(self, settings, context):
        """Sanitize passed settings object or throw value error with context.

        :param settings: a sublime text settings object
        :type settings: sublime.Settings|none
        :param context: the settings context name requested
        :type context: string
        :return: the sanitize sublime text settings object
        :rtype: sublime.Settings
        """

        if None == settings:
            raise AttributeError('Unavailable settings object context "{}" in "{}".' % (
                str(context), self.__class__.__name__)
            )

        return settings

    def _settingsContext(self, context):
        """Returns the settings object for the requested context.

        This method returns a settings object matching the settings context type
        requested via the only argument. Use any of the static class variables
        matching "self.CONTEXT_*" to populate the context argument. An exception
        will be thrown if any invalid context is requested.

        :param context: the settings context name to resolve
        :type context: string
        :return: a sublime text settings object instance
        :rtype: sublime.Settings
        """

        switch(context):
            case self.CONTEXT_ROOT:
                return self._settingsContextSanitize(self.settings_root, context)

            case self.CONTEXT_VIEW:
                return self._settingsContextSanitize(self.settings_view, context)

            default:
                raise ValueError('Unrecognized settings object context "{}" in "{}".' % (
                    str(context), self.__class__.__name__)
                )
