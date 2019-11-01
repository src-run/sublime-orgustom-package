
##
 # This file is part of the `src-run/sublime-orton-package` project.
 #
 # (c) Rob Frawley 2nd <rmf@src.run>
 #
 # For the full copyright and license information, please view the LICENSE.md
 # file that was distributed with this source code.
 ##

from .settings_base_helper import SettingsBaseHelper

class SettingUtilities(BaseSettingsHelper):

    CONTEXT_ROOT = "setting-root"
    CONTEXT_VIEW = "setting-view"

    def initSettingContexts(self, s_root, s_view = None):
        """Initialized the setting context(s) available for the given environment.

        Initialize the root context of the settings object.

        The root context object must implement the "settings()" method and can
        optionally offer a "view" property containing an object instance which
        also contains a "settings()" object.

        :param s_root: a root-level sublime text settings object instance
        :type s_root:  sublime.Settings
        :param s_view: a view-level sublime text settings object instance
        :type s_view:  sublime.Settings|None
        :return:       no value
        :rtype:        None
        """
 
        self._s_root = s_root;
        self._s_view = s_view;

    def settings(self, context):
        if self.CONTEXT_ROOT == context:
            return self.settingsRoot()

        if self.CONTEXT_VIEW == context:
            return self.settingsView()

        raise ValueError("Unrecognized settings object context: {}." % (str(context)))

    def settingsCheckValue(self, key, context = self.CONTEXT_ROOT):
        return self.settings(context).has(key)

    def settingsCheckRootValue(self, key):
        return self.settingsCheckValue(key, self.CONTEXT_ROOT)

    def settingsCheckViewValue(self, key):
        return self.settingsCheckValue(key, self.CONTEXT_VIEW)

    def settingsFetchValue(self, key, context = self.CONTEXT_ROOT):
        return self.settings(context).get(key) if self.settingsCheckValue(key, context) else None

    def settingsFetchRootValue(self, key):
        return self.settingsFetchValue(key, self.CONTEXT_ROOT);

    def settingsFetchViewValue(self, key):
        return self.settingsFetchValue(key, self.CONTEXT_VIEW);

    def settingsApplyValue(self, key, context = self.CONTEXT_ROOT):
        return self.settings(context).set(key, val)

    def settingsApplyRootValue(self, key, val):
        return self.settingsApplyValue(key, val, self.CONTEXT_ROOT);

    def settingsApplyViewValue(self, key, val):
        return self.settingsApplyValue(key, val, self.CONTEXT_VIEW);

    def settingsPurgeValue(self, key, context = self.CONTEXT_ROOT):
        return bool(self.settings(context).erase(key)) if self.settings(context).has(key) else False

    def settingsPurgeRootValue(self, key):
        return self.settingsPurgeValue(key, self.CONTEXT_ROOT)

    def settingsPurgeViewValue(self, key):
        return self.settingsPurgeValue(key, self.CONTEXT_VIEW)