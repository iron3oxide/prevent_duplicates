app_name = "prevent_duplicates"
app_title = "Prevent Duplicates"
app_publisher = "iron3oxide"
app_description = "Helps you find documents with similar content to the one you\'re about to save. You decide which fields are relevant and which degree of similarity is acceptable."
app_email = "hello@iron3oxi.de"
app_license = "gpl-3.0"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "prevent_duplicates",
# 		"logo": "/assets/prevent_duplicates/logo.png",
# 		"title": "Prevent Duplicates",
# 		"route": "/prevent_duplicates",
# 		"has_permission": "prevent_duplicates.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/prevent_duplicates/css/prevent_duplicates.css"
# app_include_js = "/assets/prevent_duplicates/js/prevent_duplicates.js"

# include js, css files in header of web template
# web_include_css = "/assets/prevent_duplicates/css/prevent_duplicates.css"
# web_include_js = "/assets/prevent_duplicates/js/prevent_duplicates.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "prevent_duplicates/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "prevent_duplicates/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "prevent_duplicates.utils.jinja_methods",
# 	"filters": "prevent_duplicates.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "prevent_duplicates.install.before_install"
# after_install = "prevent_duplicates.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "prevent_duplicates.uninstall.before_uninstall"
# after_uninstall = "prevent_duplicates.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "prevent_duplicates.utils.before_app_install"
# after_app_install = "prevent_duplicates.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "prevent_duplicates.utils.before_app_uninstall"
# after_app_uninstall = "prevent_duplicates.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "prevent_duplicates.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"prevent_duplicates.tasks.all"
# 	],
# 	"daily": [
# 		"prevent_duplicates.tasks.daily"
# 	],
# 	"hourly": [
# 		"prevent_duplicates.tasks.hourly"
# 	],
# 	"weekly": [
# 		"prevent_duplicates.tasks.weekly"
# 	],
# 	"monthly": [
# 		"prevent_duplicates.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "prevent_duplicates.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "prevent_duplicates.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "prevent_duplicates.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "prevent_duplicates.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["prevent_duplicates.utils.before_request"]
# after_request = ["prevent_duplicates.utils.after_request"]

# Job Events
# ----------
# before_job = ["prevent_duplicates.utils.before_job"]
# after_job = ["prevent_duplicates.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"prevent_duplicates.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

